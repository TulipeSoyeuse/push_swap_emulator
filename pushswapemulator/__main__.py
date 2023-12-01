import argparse
import random
from collections import deque
from subprocess import PIPE, run
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

parser.add_argument(
    "--it",
    action="store_true",
    help="iteractive mode, create stack and let you experiment,\n\
    all pushswap cmd are available plus 'reset' who reset the stack at his original value",
)
parser.add_argument(
    "--check",
    nargs="*",
    help="pass a list of operations to the program, quit at the end of the list",
)
parser.add_argument(
    "stack",
    nargs="*",
    type=int,
    help="""list of integers to be imputed as stack,
                    if only one number is given, it will be used as the borne for a range of number""",
)
parser.add_argument(
    "--pipe",
    action="store_true",
    help="pass your pushswap result in the stdin of this program",
)
parser.add_argument(
    "--exec",
    nargs=1,
    type=str,
    help="use this flag to input your C executable directly to the program",
)
parser.add_argument("--test", action="store_true")

args = parser.parse_args()

if len(args.stack) > 1:
    swapper = Swapper(args.stack)
else:
    stack = list(range(0, args.stack[0]))
    random.shuffle(stack)
    swapper = Swapper(stack)

if args.test :
    cmd = [str(i) for i in swapper.stack_a]
    cmd.insert(0,"")
    print(f"{args.exec[0]} ", " ".join(cmd))
    res = run(cmd, executable=args.exec[0], capture_output=True, text=True, timeout=40)
    print(res.stdout)
    exit(0)

swapper.display_env("")

if args.exec:
    cmd = [str(i) for i in swapper.stack_a]
    cmd.insert(0,"")
    res = run(cmd, executable=args.exec[0], capture_output=True, text=True)
    cmds = res.stdout.split("\n")
    for cmd_out in cmds:
        swapper.parse_input(cmd_out)
        resolution(swapper, cmd_out)

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
    cmds = stdin.read().split("\n")[:-1]
    for cmd in cmds:
        swapper.parse_input(cmd)
        resolution(swapper, cmd)
