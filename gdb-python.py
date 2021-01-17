#!/usr/bin/env python3

import gdb
from subprocess import Popen, PIPE

"""
print `msg` if `debug` is True
"""
def log(debug=False, msg):
    if debug:
        print(f'[*] {msg}')

"""
continue
"""
def cont(debug=False):
    log(debug, 'continue')
    output = gdb.execute('c', to_string)
    return output

