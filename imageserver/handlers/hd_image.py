# coding=utf-8
import tornado.web
import json
import base64
from io import BytesIO
from tornado.log import app_log as imagelog
import matplotlib.pyplot as plt


class ImageHandler(tornado.web.RequestHandler):
    def get(self):
        xdata = self.get_arguments("xdata")
        ydata = self.get_arguments("ydata")
        if len(xdata) != len(ydata):
            return self.write(json.dumps({"err_code": 1, "msg": "x y length not the same"}))
        # print(f"{xdata} {ydata}")
        # print(xdata)
        # print(ydata)
        ydata = [float(i) for i in ydata]
        plt.plot(xdata, ydata, marker='o')
        plt.rcParams['font.sans-serif'] = ['WenQuanYi Zen Hei Mono']
        plt.gcf().subplots_adjust(bottom=0.2)
        plt.xticks(rotation=75, fontsize=12)
        if len(xdata) < 5:
            plt.xlim(0, 5)
        figfile = BytesIO()
        # filename = "xy_{}.png".format(self.request.request_time())
        # print(filename)
        plt.savefig(figfile, dpi=600, format="png")
        figdata_png = base64.b64encode(figfile.getvalue()).decode()
        # figfile.close()
        plt.cla()
        plt.close()
        # print(len(figdata_png))
        imagelog.info("{} \n{} \nimgb64 len:{}".format(xdata, ydata, len(figdata_png)))
        return self.write(json.dumps({"err_code": 0, "img": figdata_png}))
