# coding=utf-8

import os
import re

print os.listdir('.')

pic_names = os.listdir('.')
for pic in pic_names:
    if re.split("\.",pic)[-1] == "bmp":
        print pic
        new_name = pic.replace('ȥȥȥȥ','')
        os.rename(pic,new_name)
