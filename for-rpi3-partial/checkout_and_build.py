#!/usr/bin/python

import os
import sys

team = [2, 3, 4, 5, 6, 7, 8, 10, 11]

for n in team:
    print('cd team dir: ' + str(n))
    os.system('cd ' + './osfall2019-team' + str(n) + ' ; ' + 'git checkout proj2' + ' ; ' + './build-rpi3-arm64.sh')
    print('build done!')
