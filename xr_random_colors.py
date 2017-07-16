#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import choice
from shutil import copyfile
from sys import argv
import subprocess
import os.path
from os import listdir

HOME = os.path.expanduser("~")
XR_FILE = os.path.join(HOME, '.Xresources')
COPIED_FILE = os.path.join(HOME, '.Xresources.bak')

try:
    if argv[1]:
        SCHEMES_DIR = os.path.join(HOME, '.urxvt_colors_js_css')
except IndexError:
    SCHEMES_DIR = os.path.join(HOME, '.urxvt_colors')


if not os.path.isfile(COPIED_FILE):
    copyfile(XR_FILE, COPIED_FILE)

schemes = listdir(SCHEMES_DIR)
scheme = choice(schemes)
scheme_path = os.path.join(SCHEMES_DIR,  scheme)
print(scheme_path)

with open(XR_FILE, 'r+') as Xresources, \
        open(scheme_path, 'r') as scheme_file:
    Xread = Xresources.readlines()
    Xread = [l.rstrip() for l in Xread]
    txt = ('!!! COLOR SCHEME !!!')
    split_point = Xread.index(txt)
    configs = [x for (i, x) in enumerate(Xread) if i < split_point]
    scheme_read = scheme_file.readlines()
    scheme_read = [l.rstrip() for l in scheme_read]
    Xresources.seek(0)
    Xresources.truncate()
    first = '\n'.join(configs)
    midpoint = '\n' + txt + '\n'
    last = '\n'.join(scheme_read)
    Xresources.write(first + midpoint + last)


subprocess.call(['xrdb', XR_FILE])
