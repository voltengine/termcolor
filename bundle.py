#!/bin/python

# Copies that awful BSD-3-Clause to build directory

import sys, os, shutil

src = os.path.normpath(os.path.join(os.path.dirname(__file__), 'LICENSE'))
dst = os.path.normpath(os.path.join(sys.argv[1], 'licenses', 'termcolor.txt'))

print('Copying license to "' + os.path.abspath(dst) + '"...')

os.makedirs(os.path.dirname(dst), exist_ok=True)
shutil.copyfile(src, dst)
