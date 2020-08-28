#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/28 11:11
# @Author  : 1823218990@qq.com
# @File    : getmore.py
# @Software: PyCharm

import requests
import re
from bs4 import BeautifulSoup
cookies = {'login': 'false'}
url = 'https://so.gushiwen.org/shiwenv_444df93c9bdf.aspx'
# url = 'https://so.gushiwen.org/shiwenv_ad6f7cfa10c2.aspx'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'}

def get_describe_detail(url):
    # -- 翻译
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'lxml')
    fanyihtml = soup.find('a', {'href': re.compile("javascript:fanyiShow")})
    p_default = soup.find_all("p")[1:6]
    if fanyihtml is not None:
        fanyi_url = 'https://so.gushiwen.org/nocdn/ajaxfanyi.aspx?id='
        fy_id = fanyihtml.get("href").split(",")[1][1:-1]
        moreurl_fy = fanyi_url + fy_id
        moretxt_fy = requests.get(moreurl_fy, headers=headers, cookies=cookies).text
        soup_fy = BeautifulSoup(moretxt_fy, 'lxml')
        p_detail = soup_fy.find_all("p")
        # print("fy:", len(p_detail))
        # print(moreurl_fy)
        # print(p_detail, moreurl_fy)
        describe = ""
        for item in p_detail:
            zs = item.text
            if zs.startswith(u"参考资料") or zs.startswith(u"本节内容"):
                continue
            try:
                describe += zs[0:2] + "：\n" + zs[2:] + "\n"
            except:
                describe += zs + "\n"
        # zs = p_detail[1].text
        # yw = p_detail[0].text
        # describe = zs[0:2] + "：\n" + zs[2:] + "\n"
        # describe += yw[0:2] + "：\n" + yw[2:] + "\n"
    else:
        zs = p_default[1].text
        yw = p_default[0].text
        describe = zs[0:2] + "：\n" + zs[2:] + "\n"
        describe += yw[0:2] + "：\n" + yw[2:] + "\n"
        describe += p_default[2].text + "\n"
        describe += p_default[3].text + "\n"
    # -- 赏析
    htmltxt = requests.get(url).text
    soup = BeautifulSoup(htmltxt, 'lxml')
    shangxihtml = soup.find('a', {'href': re.compile("javascript:shangxiShow")})
    if shangxihtml is not None:
        shangxi_url = 'https://so.gushiwen.org/nocdn/ajaxshangxi.aspx?id='
        sx_id = shangxihtml.get("href").split(",")[1][1:-1]
        moreurl_sx = shangxi_url + sx_id
        moretxt_sx = requests.get(moreurl_sx, headers=headers, cookies=cookies).text
        soup_sx = BeautifulSoup(moretxt_sx, 'lxml')
        sx_detail = soup_sx.find_all("p")
        # print(sx_detail, moreurl_sx)

        if len(sx_detail) == 1 and sx_detail[0].text.startswith(u"未登录"):
            describe += p_default[2].text + "\n"
            describe += p_default[3].text + "\n"
        else:
            for item in sx_detail:
                if item.text is None or item.text.startswith(u"参考资料") or item.text.startswith(u"本节内容"):
                    continue
                describe += item.text + "\n"
    else:
        describe += p_default[2].text + "\n"
        describe += p_default[3].text + "\n"

    describe = describe.replace(u"\u3000", u'    ')
    # print(describe)
    # print('-----' * 10)
    return describe


if __name__ == '__main__':
    url = 'https://m.gushiwen.org/shiwenv_45c396367f59.aspx'
    describe = get_describe_detail(url)
    print(describe)
