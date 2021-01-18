#!/usr/bin/env python3

import gdb
import os
import tempfile
import random
import string

"""
print `msg` if `debug` is True
"""
def log(msg, debug=False):
    if debug:
        print(f'[*] {msg}')

"""
execute given `cmd` and return output
"""
def exc(cmd, debug=False):
    log(f'executing: `{cmd}`', debug)
    output = gdb.execute(cmd, to_string=True)
    return output

"""
continue and return output
"""
def cont(debug=False):
    return exc('c', debug)

"""
break on `symbol` and continue if `c` is True
if `c` is True then return output
"""
def bs(symbol, c=False, debug=False):
    log(f'breaking on symbol {symbol}', debug)
    exc(f'b {symbol}', debug)
    if c: # continue
        return cont(debug)

"""
break at `addr` and continue if `c` is True
if `c` is True then return output
"""
def ba(addr, c=False, debug=False):
    log(f'breaking at address {addr}', debug)
    exc(f'b *{addr}', debug)
    if c: # continue
        return cont(debug)

"""
file `filename`
"""
def f(filename, debug=False):
    log(f'file on {filename}', debug)
    exc(f'file {filename}', debug)

"""
return random string of `size` chars
"""
def getRandomString(size):
    charset = string.ascii_letters + string.digits
    return ''.join(random.choices(charset, k=size))

"""
return entry point of binary `filename`
"""
def getEntry(filename, debug=False):
    log(f'getting {filename} entry point', debug)
    size = 6
    tmpfilename = './gdbpython_tempfile_' + getRandomString(size)
    log(f'created temporary file {tmpfilename}', debug)
    mycmd = f"readelf -h {filename} | grep 'Entry point' | tr -s ' ' | cut -d ' ' -f 5"
    os.system(f'{mycmd} > {tmpfilename}')
    entry = open(tmpfilename, 'r').read()[:-1]
    os.system(f'rm -f {tmpfilename}')
    log(f'removed temporary file {tmpfilename}', debug)
    log(f'{filename} entry point = {entry}', debug)
    return entry

"""
make `filename` the currently debugged file and break at its entry point
if `entry` is provided then it breaks at `entry` instead
"""
def init(filename, entry=None, debug=False):
    f(filename, debug)
    if entry == None:
        entry = getEntry(filename, debug)
    ba(entry, False, debug)

"""
run with `stdin` or `args`
"""
def run(stdin=None, stdin_cmd=None, args=[], debug=False):
    if stdin:
        log(f'running with `r < {stdin}`', debug)
        exc(f'r < {stdin}', debug)
    elif stdin_cmd:
        log(f'running with `r < <({stdin_cmd})`', debug)
        exc(f'r < <({stdin_cmd})', debug)
    elif args:
        strargs = ' '.join(args)
        log(f'running with `r {strargs}`', debug)
        exc(f'r {strargs}', debug)

"""
return output of printing given symbol
"""
def get(symbol, debug=False):
    log(f'printing {symbol}', debug)
    return exc(f'p ${symbol}', debug)
