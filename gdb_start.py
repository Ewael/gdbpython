#!/usr/bin/env python3

from gdb_main import *
from gdb_utils import *
from gdb_breakpoints import *

import os
import tempfile

'''
define given path as the binary to debug
'''
def f(filename: str) -> None:
    exc(f'file {filename}')

'''
set up everything to start debugging on the given binary
- define it as the current debugged procosss
- break on its entry point
    |-> if no entry point is given, get it with `readelf`
'''
def init(filename: str, entry: int=None) -> None:
    f(filename)
    if not entry:
        entry = getEntry(filename)
    ba(entry)

'''
run the debugged binary with ONE of the following args
- stdin         = pipe with `< <(python3 -c 'print(...)')`
- stdin_cmd     = pipe with `< <(cmd)`
- stdin_file    = pipe file
- args          = run with args
'''
def run(stdin: str=None,
        stdin_cmd: str=None,
        stdin_file: str=None,
        args: list=[]
        ) -> None:

    if stdin and args:
        strargs = ' '.join(args)
        exc(f'run {strargs} < <(python3 -c "print(\'{stdin}\')")')
    elif stdin:
        exc(f'run < <(python3 -c "print(\'{stdin}\')")')
    elif stdin_file:
        exc(f'run < {stdin_file}')
    elif stdin_cmd:
        exc(f'run < <({stdin_cmd})')
    elif args:
        strargs = ' '.join(args)
        exc(f'run {strargs}')
    else:
        exc('run')

'''
remote debugging, very useful with qemu for kernel / weird archs debugging:
- `qemu-system-i386 -s -S -kernel ./binary -monitor stdio`
- `qemu-arm -L /usr/arm-linux-gnueabihf -g 1234 ./binary`
'''
def remote(binary: str=None, host: str='localhost', port: int=1234):
    if binary: # if binary name is provided then give it to gdb
        f(filename)
    exc(f'target remote {host}:{port}')

'''
attach to running process
'''
def attach(pid: int):
    exc(f'attach {pid}')
