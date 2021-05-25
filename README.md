# gdbpython

Author: *Ewaël*

This script contains some useful functions when it comes to Python scripting in `gdb`. I was bored to copy them again and again when doing reversing challenges so I decided to create a little wrapper containing all of them.

This repo is public because I feel like there are not that many ressources about Python scripting in `gdb`. This was written for my personnal usage and environnement when doing reverse engineering challenges so do not expect it to work flowlessly at any time.

Please note that this should **NEVER** be run as `root` as I create and delete a temporary file when getting the binary entry point. Even if the filename is randomized the risk is useless.

Of course this will always be a work in progress as I will add features and fix the code directly and only on the `master` branch because I'm lazy. Thus again do not expect it to work at any time, I'm just sharing this because I'm pretty sure it could help someone one day.

## Usage

You can either copy the functions that interest you manually and import the `gdb` module to keep the verbose interface during execution, or import this module directly:

```python
import gdbpython
import gdbpython as g
from gdbpython import *
```

You must add this repository to your `PYTHONPATH` to import the module:

```bash
export PYTHONPATH=$PYTHONPATH:/path/to/gdb-python
```

The followings packages are required to enjoy every functions of the script:

```
readelf
gdb
```

I **HIGHLY** suggest to use it with [gef](https://github.com/hugsy/gef). Not only because it is an insanely powerful tool but also because some commands as [PIE](https://en.wikipedia.org/wiki/Position-independent_code) breakpoints will not work in vanilla `gdb`. The following Python3 libraries are also required:

```
gdb
os
tempfile
random
string
```

Then you can use your script like this:

```
gdb -q -x script.py
```

## Documentation

Still in progress. See comments above functions until it's done.
