# coding=utf-8

import matplotlib.pyplot as plt
import os

def show_jj_data(jid):
    x = []
    y = []
    with open("data/{}.txt".format(jid), 'r') as f:
        lines = f.readlines()
        for line in lines:
            x1, y1, p1 = line.strip(" ").split(" ")

            x.append(x1)
            y.append(float(y1))
    x.reverse()
    y.reverse()
    # nlen = len(x)
    # print(nlen)
    # pos = nlen // 2
    # pos = nlen
    # plt.plot(x[nlen - pos:], y[nlen - pos :])
    plt.plot(x, y)
    plt.savefig(r"image/{}.png".format(jid))
    # plt.show()
    plt.close()


def do_gene_png():
    all_file = os.listdir("data")
    for file in all_file:
        jid = os.path.splitext(file)[0]
        print(jid)
        show_jj_data(jid)


if __name__ == '__main__':
    do_gene_png()
    # show_jj_data("001415")