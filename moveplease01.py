#!/usr/bin/env python3


import shutil

import os

os.chdir('/home/student/mycode/ceph_storage/')

shutil.move('raynor.obj', '/home/student/mycode/')

xname = input('What is the new name for kerrigan.obj? ')

shutil.move('kerrigan.obj', xname)


