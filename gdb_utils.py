#!/usr/bin/env python3

import os
import string
import random

'''
return a random string of the given size
'''
def getRandomString(size: int) -> str:
    charset = string.ascii_letters + string.digits
    return ''.join(random.choices(charset, k=size))

'''
return a default charset
'''
def getCharset() -> str:
    return string.ascii_letters + string.digits + "@*{}+=$%^][() _-.?!"

'''
return the entry point address of the given binary
note: this creates a temporary file in the current working directory
'''
def getEntry(filename: str) -> int:
    size = 6
    tmpfilename = './gdbpython_tempfile_' + getRandomString(size)

    # the actual command to parse `readelf` output
    mycmd = f"readelf -h {filename}"
    mycmd += "| grep 'Entry point'"
    mycmd += "| tr -s ' '"
    mycmd += "| cut -d ' ' -f 5"

    os.system(f'{mycmd} > {tmpfilename}')
    entry = open(tmpfilename, 'r').read()[:-1]
    os.system(f'rm -f {tmpfilename}')
    return entry
