import argparse
from collections import deque
from sys import argv



from emulator.swapper import Swapper

parser = argparse.ArgumentParser(
    description="""
this programme replicate the functionning of the push_swap checker, or sort a stack
base on a list of command.
Can be lauch on interactive mode for more fun."""
)

parser.add_argument("--it", action="store_true")
parser.add_argument("--check", nargs="*")
parser.add_argument("stack", nargs="*", type=int)

Swapper
