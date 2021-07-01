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
        sma1 = self.get_arguments("sma1")
        sma2 = self.get_arguments("sma2")
        pos = self.get_arguments("position")
        
        imagelog.info("{}".format(len(ydata)))
        mutli = False
        if pos:
              mutli = True
        if len(xdata) != len(ydata) and not mutli:
            return self.write(json.dumps({"err_code": 1, "msg": "x y length not the same"}))
        # print(f"{xdata} {ydata}")
        # print(xdata)
        # print(ydata)
        ydata = [float(i) for i in ydata]
        if mutli:
            sma1 = [float(i) for i in sma1]
            sma2 = [float(i) for i in sma2]
            pos = [int(i) for i in pos]
            sma_data = [ydata, sma1, sma2, pos]
            plt.plot(xdata, *sma_data, marker='o')
        else:
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
