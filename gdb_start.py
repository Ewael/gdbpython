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
        exc(f'r {strargs} < <(python3 -c "print(\'{stdin}\')")')
    elif stdin:
        exc(f'r < <(python3 -c "print(\'{stdin}\')")')
    elif stdin_file:
        exc(f'r < {stdin_file}')
    elif stdin_cmd:
        exc(f'r < <({stdin_cmd})')
    elif args:
        strargs = ' '.join(args)
        exc(f'r {strargs}')
    else:
        exc('r')
