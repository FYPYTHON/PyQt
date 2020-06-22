# coding=utf-8
from common.common_base import running_time
from common.common_base import print_file_lineno
RETRY = 3

import inspect


def printLineFileFunc():
    from datetime import datetime
    dd = print_file_lineno()
    print(datetime.now(), dd)


@running_time
def main():
    n_retry = 0
    while n_retry < RETRY:
        pass
        n_retry += 1
    print("over")


if __name__ == '__main__':
    main()
    printLineFileFunc()
    pass
