#!/usr/bin/env python3

import gdb

'''
execute the given command
return output
'''
def exc(cmd: str) -> str:
    output = gdb.execute(cmd, to_string=True)
    return output

'''
return context()
'''
def context() -> str:
    return exc('context')

'''
return output of `p symbol` with the given symbol
'''
def get(symbol: str) -> str:
    return exc(f'p ${symbol}')

'''
set follow-fork-mode with the given mode:
    - child
    - parent
'''
def setFork(mode: str) -> None:
    exc(f'set follow-fork-mode {mode}')
