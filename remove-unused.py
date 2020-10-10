#!/usr/bin/python

import os
import shutil
import re

with open('folder_list.txt') as f:
    folder_path = join(set(re.findall("[a-zA-Z\-\.'/]+", f.read())))
    shutil.rmtree(folder_path)
