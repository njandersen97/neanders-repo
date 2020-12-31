#!/user/bin/env python

import os
import argparse

x = os.urandom(9)

def tohex(v):
    ov = v
    if isinstance(v, str):
        ov = ord(v)
    ov = hex(ov)[2:]
    if len(ov) == 1:
        ov="0"+ov
    return ov

parser = argparse.ArgumentParser(description='Generate a cryptographically suitable random hex key of given length.')
parser.add_argument('-l', '--length', required=True, type=int, help='The key length (in bits); it will be floored to a byte boundary.')
args = parser.parse_args()

x = os.urandom(int(args.length / 8))

h = "".join([tohex(c) for c in x])

print(h)