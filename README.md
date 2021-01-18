# gdbpython

Author: *Ewaël*

This script contains some useful functions when it comes to *Python* scripting in `gdb`. I was bored to copy them again and again when doing reversing challenges so I decided to create a little wrapper containing all of them.

This repo is public because I feel like there are not that many ressources about scripting in `gdb`. This was written for my personnal usage and environnement so do not expect it to work flowlessly if using it as such. Also note that this should **NEVER** be run as `root` as I create and delete a temporary file when getting the binary entry point.

Of course this will always be a work in progress as I will add features and fix the code directly and only on the `master` branch because I'm lazy. Thus again do not expect it to work at any time, I'm just sharing this because I'm pretty sure it could help someone one day.

## Usage

You can either copy the functions that interest you manually and import the `gdb` module to keep the verbose interface of `peda` during execution, or import this module directly:

```python
import gdbpython as g
```

You must also add this repository to your `PYTHONPATH` if you try to import the module:

```
export PYTHONPATH=$PYTHONPATH:/path/to/gdb-python
```

The followings packages are required to enjoy every functions of the script:

```
readelf
gdb
```

I **HIGHLY** suggest to use it with [peda](https://github.com/longld/peda). Not only because it is an insanely powerful tool but also because I do not even know if this works in a *vanilla* `gdb`.

The followings *Python* 3 libraries are also required:

```
gdb
os
tempfile
random
string
```

Then you can use your script in `gdb` this way:

```
gdb -q -x script.py
```

## TODO

* *typing* (see [doc](https://docs.python.org/3/library/typing.html))
* cleaner code + clearer doc
* better functions names
