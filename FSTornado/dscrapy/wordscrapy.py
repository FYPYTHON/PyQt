# coding=utf-8
import requests
from bs4 import BeautifulSoup
import time
# url = 'http://5b0988e595225.cdn.sohucs.com/images/20190731/ae05a73bf4644d3a8a8184a09750709b.jpeg'
#
# a = requests.get(url)
# fname = url.split('/')[-1]
# print(a.content)
# print(a.encoding)
# with open("F:/" + fname, 'wb') as f:
#     f.write(a.content)

root_url = "https://www.sohu.com/a/330649978_799053"


def ge_all_url():
    html = requests.get(root_url)
    soup = BeautifulSoup(html.text, 'lxml')
    image_url = soup.find_all("img")

    urls = []
    for img in image_url:
        iurl = img.get("src")
        if iurl.endswith(".jpeg"):
            urls.append(iurl)
            # print(img.get("src"))
    print(len(urls))
    save_to_picture(urls)


def save_to_picture(urls):
    path = "F:/image/word/"
    for url in urls:
        picture = requests.get(url)
        fname = url.split('/')[-1]
        with open(path + fname, 'wb') as f:
            f.write(picture.content)
            print("save ", fname)
        time.sleep(1)


if __name__ == '__main__':
    ge_all_url()



