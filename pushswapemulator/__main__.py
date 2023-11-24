import argparse
from collections import deque
from sys import argv

from colorama import Fore

from .swapper import Swapper

parser = argparse.ArgumentParser(
    description="""
this programme replicate the functionning of the push_swap checker, or sort a stack
base on a list of command.
Can be lauch on interactive mode for more fun."""
)

parser.add_argument("--it", action="store_true")
parser.add_argument("--check", nargs="*")
parser.add_argument("stack", nargs="*", type=int)

args = parser.parse_args()
swapper = Swapper(args.stack)
swapper.display_env("")
if args.it and args.check:
    print("it and check command are imcompatible")
    exit(1)

if args.it:
    while not swapper.is_solved():
        cmd = input("cmd :")
        swapper.parse_input(cmd)
        swapper.display_env(cmd)
        if swapper.is_solved():
            print(
                Fore.GREEN + "-" * 9 + " " + f"STACK SORTED : {swapper.moves} move used",
            Fore.GREEN + "-" * 9)
            exit(0)

if args.check:
    for i in args.check:
        swapper.parse_input(i)
        swapper.display_env(i)
        if swapper.is_solved():
            print(
                Fore.GREEN + "-" * 9 + " " + f"STACK SORTED : {swapper.moves} move used",
            Fore.GREEN + "-" * 9)
            exit(0)
