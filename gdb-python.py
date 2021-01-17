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

"""
break on `symbol` and continue if `c` is True
if `c` is True then return output
"""
def bs(symbol, c=False, debug=False):
    log(debug, f'breaking on symbol {symbol}')
    gdb.execute(f'b {symbol}')
    if c:
        return cont(debug)

"""
break at `addr` and continue if `c` is True
if `c` is True then return output
"""
def ba(addr, c=False, debug=False):
    log(debug, f'breaking at address {addr}')
    gdb.execute(f'b *{addr}')
    if c:
        return cont(debug)

"""
file `filename`
"""
def f(filename, debug=False):
    log(debug, f'file on {filename}')
    gdb.execute(f'file {filename}')

"""
return entry point of binary `filename`
"""
def getEntry(filename, debug=False):
    log(debug, f'getting {filename} entry point')
    cmd_readelf = Popen(('readelf', '-h'),
                    stdout=PIPE)
    cmd_grep = Popen(('grep', 'Entry point'),
                    stdin=cmd_readelf.stdout,
                    stdout=PIPE)
    cmd_tr = Popen(('tr', '-s', ' '),
                    stdin=cmd_grep.stdout,
                    stdout=PIPE)
    cmd_cut = Popen(('cut', '-d', ' ', '-f', '5'),
                    stdin=cmd_tr.stdout)
    entry = cmd_cut.stdout
    log(debug, f'{filename} entry point = {entry}')
    return entry

"""
make `filename` the currently debugged file and break at its entry point
if `entry` is provided then it breaks at `entry` instead
"""
def init(filename, entry=None, debug=False):
    if entry == None:
        entry = getEntry(filename, debug)
    f(filename, debug)
    ba(entry, c=False, debug)

"""
run with `stdin` or `args`
"""
def run(stdin=None, stdin_cmd=None, args=[], debug=False):
    if stdin:
        log(debug, f'running with `r < {stdin}`')
        gdb.execute(f'r < {stdin}')
    elif stdin_cmd:
        log(debug, f'running with `r < <({stdin_cmd})`')
        gdb.execute(f'r < <({stdin_cmd})')
    elif args:
        strargs = ' '.join(args)
        log(debug, f'running with `r {strargs}`')
        gdb.execute(f'r {strargs}')
