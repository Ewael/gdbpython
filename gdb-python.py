#!/usr/bin/env python3

import gdb
from subprocess import Popen, PIPE

"""
print `msg` if `debug` is True
"""
def log(debug=False, msg):
    if debug:
        print(f'[*] {msg}')


