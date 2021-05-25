#!/usr/bin/env python3

from main import *

'''
continue and return context
'''
def cont() -> str:
    return exc('c')

'''
break at given symbol
'''
def bs(symbol: str) -> None:
    exc(f'b {symbol}')

'''
break at given address
'''
def ba(addr: int) -> None:
    exc(f'b *{addr}')

'''
hardware breakpoint at given address
'''
def hba(addr: int) -> None:
    exc(f'hb *{addr}')

'''
temporary breakpoint at given address
'''
def tb(addr: int) -> None:
    exc(f'tbreak *{addr}')

'''
temporary breakpoint at given address and continue
-> useful to set up mutliple bp and comment the useless ones
'''
def tbc(addr: int) -> None:
    tb(addr)
    cont()

'''
pie breakpoint at given offset from base address
'''
def pba(offset: int) -> None:
    exc(f'pie breakpoint *{hex(offset)}')

'''
pie breakpoint at given offset from base address and continue
'''
def pbc(offset: int) -> None:
    pba(offset)
    cont()
