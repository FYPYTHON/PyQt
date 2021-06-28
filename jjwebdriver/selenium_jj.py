# coding=utf-8
"""
http://chromedriver.storage.googleapis.com/index.html
"""
import platform
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from datetime import datetime
from time import sleep
from logging import FileHandler, getLogger, Formatter

logger = getLogger()
fileloghandler = FileHandler(filename="selenium_jj.log")
fmt=Formatter('[%(levelname)s] %(asctime)s %(filename)s [line:%(lineno)d] %(message)s')
fileloghandler.setFormatter(fmt)

logger.addHandler(fileloghandler)

if platform.system() == "Windows":
    dr = webdriver.Chrome("D:\workSpace\chromedriver91_win32\chromedriver.exe")
else:
    logger.error("not windows env can not run this function.")
    exit(0)


def get_info(tab_element: WebElement, jid: str):

    trs = tab_element.find_elements_by_tag_name("tr")
    logger.info(trs)
    logger.info("----")
    jj_file = open("{}.txt".format(jid), mode="a+")
    for tr in trs:
        print(tr.text)
        data_text = tr.text
        if len(data_text.split(" ")) >= 6:
            dlist = data_text.split(" ")
            jdate, jvalue, jper = dlist[0], dlist[1], dlist[3]
        else:
            dlist = data_text.split(" ")
            jdate, jvalue, jper = dlist[0], dlist[1], dlist[2]
        jj_file.write("{} {} {}\n".format(jdate, jvalue, jper[:-1]))
    jj_file.close()


def selenium_jj_main(jid):
    url = "http://fundf10.eastmoney.com/jjjz_{}.html".format(jid)
    # dr.maximize_window()
    dr.get(url)
    sleep(1)
    # get table info
    table_div = dr.find_element_by_id("jztable").find_element_by_tag_name("tbody")
    get_info(table_div, jid)

    pagebar = dr.find_element_by_id("pagebar")
    logger.info(pagebar.text)
    try:
        count = 0
        while True:
            if count > 10:
                break
            nextlabel = pagebar.find_element_by_xpath("//*[contains(text(), '下一页')]")
            logger.info(nextlabel.text)
            if nextlabel.get_attribute("class") == "end":
                logger.info("go end...")
                break
            else:
                nextlabel.click()
            sleep(3)
            # get table info
            table_div = dr.find_element_by_id("jztable").find_element_by_tag_name("tbody")
            get_info(table_div, jid)
            count += 1
            # ll = pagebar.find_elements_by_tag_name("label")
            # for l in ll:
            #     print(l.text)
            #     if l.text == "下一页":
            #         print("click...")
            #         l.click()
    except Exception as e:
        logger.error("{}".format(e))
        dr.close()
        dr.quit()

    # print(nextlabel)
    # if nextlabel.get_attribute("class") == "end":
    #     print("go end")


def get_search_jid():
    jids = []
    with open("jsearch.txt") as f:
        lines = f.readlines()
        for line in lines:
            jids.append(line.split(" ")[0])
    return jids


def start_webdriver():
    # jid = "002190"
    jids = get_search_jid()
    for jid in jids:
        print(jid)
        selenium_jj_main(jid)
        dr.refresh()
        logger.info("{} end.".format(jid))
    dr.close()
    logger.info("start webdriver end.")

if __name__ == '__main__':
    try:
        start_webdriver()
    except Exception as e:
        logger.error("{}".format(e))



