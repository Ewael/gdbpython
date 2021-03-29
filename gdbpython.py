#!/usr/bin/env python3

import gdb
import os
import tempfile
import random
import string

def exc(cmd):
    output = gdb.execute(cmd, to_string=True)
    return output

def context():
    return exc('context')

def cont():
    return exc('c')

def bs(symbol):
    exc(f'b {symbol}')

def ba(addr):
    exc(f'b *{addr}')

def f(filename=False):
    exc(f'file {filename}')

def getRandomString(size):
    charset = string.ascii_letters + string.digits
    return ''.join(random.choices(charset, k=size))

def getEntry(filename):
    size = 6
    tmpfilename = './gdbpython_tempfile_' + getRandomString(size)
    mycmd = f"readelf -h {filename} | grep 'Entry point' | tr -s ' ' | cut -d ' ' -f 5"
    os.system(f'{mycmd} > {tmpfilename}')
    entry = open(tmpfilename, 'r').read()[:-1]
    os.system(f'rm -f {tmpfilename}')
    return entry

def init(filename, entry=None):
    f(filename)
    if not entry:
        entry = getEntry(filename)
    ba(entry)

def run(stdin=None, stdin_cmd=None, args=[]):
    if stdin:
        exc(f'r < {stdin}')
    elif stdin_cmd:
        exc(f'r < <({stdin_cmd})')
    elif args:
        strargs = ' '.join(args)
        exc(f'r {strargs}')
    else:
        exc('r')

def get(symbol=False):
    return exc(f'p ${symbol}')

def tb(addr):
    exc(f'tb *{addr}')

def tbc(addr):
    tb(addr)
    cont()
