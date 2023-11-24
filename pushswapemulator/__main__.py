import argparse
from collections import deque
from sys import argv, stdin

from colorama import Fore

from .swapper import Swapper
from .utils import resolution

parser = argparse.ArgumentParser(
    description="""
this programme replicate the functionning of the push_swap checker, or sort a stack
base on a list of command.
Can be lauch on interactive mode for more fun."""
)

parser.add_argument("--it", action="store_true")
parser.add_argument("--check", nargs="*")
parser.add_argument("stack", nargs="*", type=int)
parser.add_argument("--pipe", action="store_true")

args = parser.parse_args()
swapper = Swapper(args.stack)
swapper.display_env("")
if args.it and (args.check or args.pipe):
    print("it and check/pipe command are imcompatible")
    exit(1)

if args.it:
    while not swapper.is_solved():
        cmd = input("cmd :")
        swapper.parse_input(cmd)
        resolution(swapper, cmd)

if args.check:
    for cmd in args.check:
        swapper.parse_input(cmd)
        resolution(swapper, cmd)

if args.pipe:
    cmds = stdin.read().split('\n')[:-1]
    for cmd in cmds:
        swapper.parse_input(cmd)
        resolution(swapper)
