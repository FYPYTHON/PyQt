#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/19 9:55
# @Author  : 1823218990@qq.com
# @File    : hd_predict.py
# @Software: PyCharm

from tornado.web import authenticated
from tornado.log import app_log as weblog
from common.global_func import get_user_info, DATE_FORMAT
from handlers.basehd import BaseHandler, check_token
from handlers.view.hd_jijin import strtime_check
from database.tbl_jijin import TblJijin
from datetime import datetime, timedelta
from pandas import DataFrame
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM
import json


def get_gid_all_data(self, jid, days):
    two_weeks_before = datetime.now() + timedelta(days=-days)
    str_date = two_weeks_before.strftime(DATE_FORMAT)
    result = self.mysqldb().query(TblJijin.jdate, TblJijin.jvalue).filter(TblJijin.jid == jid
                                                                          , TblJijin.jdate >= str_date).order_by(
        TblJijin.jdate.asc()
    ).all()
    jdata = dict()
    jdate = []
    jvalue = []
    for res in result:
        jdate.append(res.jdate)
        jvalue.append(res.jvalue)
    jdata["jdate"] = jdate
    jdata["jvalue"] = jvalue
    # jdata["jmax"] = max(jvalue) if jvalue else 0
    # jdata["jmin"] = min(jvalue) if jvalue else 0
    return jdate, jvalue


def predict_jj(df, dataset, predict_index, cycles):
    train = dataset[0:predict_index, :]
    valid = dataset[predict_index:, :]

    # 将数据集转换为x_train和y_train
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(dataset)

    x_train, y_train = [], []
    for i in range(cycles, len(train)):
        x_train.append(scaled_data[i - cycles:i, 0])
        y_train.append(scaled_data[i, 0])
    x_train, y_train = np.array(x_train), np.array(y_train)

    x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))

    # 创建和拟合LSTM网络
    model = Sequential()
    model.add(LSTM(units=50, return_sequences=True, input_shape=(x_train.shape[1], 1)))
    model.add(LSTM(units=50))
    model.add(Dense(1))

    model.compile(loss='mean_squared_error', optimizer='adam')
    model.fit(x_train, y_train, epochs=1, batch_size=1, verbose=2)

    # 使用过去值来预测246个值
    inputs = df[len(df) - len(valid) - cycles:].values
    inputs = inputs.reshape(-1, 1)
    inputs = scaler.transform(inputs)

    X_test = []
    for i in range(cycles, inputs.shape[0]):
        X_test.append(inputs[i - cycles:i, 0])
    X_test = np.array(X_test)

    X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
    closing_price = model.predict(X_test)
    closing_price = scaler.inverse_transform(closing_price)
    return closing_price.tolist()


class AppJijinPredict(BaseHandler):
    @check_token
    def get(self):
        jid = self.get_argument("jid", None)
        days = int(self.get_argument("days", "14"))
        pdate = self.get_argument("jdate", None)

        if not strtime_check(self, pdate):
            return self.write(json.dumps({"error_code": 1, "msg": u"date日期格式错误"}))
        jdate, jvalue = get_gid_all_data(self, jid, days)
        if len(jdate) != len(jvalue):
            weblog.error("date:{} value:{} length not the same".format(len(jdate), len(jvalue)))
            return self.write(json.dumps({"error_code": 1, "msg": u"数据获取错误"}))
        if len(jdate) > 10:
            df = DataFrame({"Date": jdate, "Value": jvalue})
            df.drop('Date', axis=1, inplace=True)
            dataset = df.values
            # ---
            if pdate in jdate:
                predict_index = jdate.index(pdate)
            else:
                predict_index = -1
            try:
                data = predict_jj(df, dataset, predict_index, 5)
            except Exception as e:
                weblog.error("{}".format(e))
                return self.write(json.dumps({"error_code": 1, "msg": u"预测失败", "data": [], "jdate": jdate, "jvalue": jvalue}))
            weblog.info("ok")
            return self.write(json.dumps({"error_code": 0, "msg": "ok", "data": data, "jdate": jdate, "jvalue": jvalue}))
        else:
            weblog.error("length:{} too short please select again".format(len(jdate)))
            return self.write(json.dumps({"error_code": 1, "msg": u"数据量不足, 请加大选择范围"}))
        pass


if __name__ == "__main__":
    pass