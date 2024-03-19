#!/usr/bin/python3
from __future__ import print_function
import sys

def magic_calculation(a, b):

    """Match bytecode provided by Holberton School."""

    from magic_calculation_102 import add, sub

    if a < b:
        c = add(a, b)

        for i in range(4, 6):
            c = add(c, i)
        return (c)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
    else:
        return res
