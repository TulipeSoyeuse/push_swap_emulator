from .utils import *
from collections import deque
from colorama import Fore, init

init(autoreset=True)

class Swapper:
    def __init__(self, stack: list):
        """replicateur of the swap push function
        Args:
            stack (list): args from the commande line
        """
        check_valid_input(stack)
        self.stack_a = deque(stack)
        self.stack_b = deque()
        self.ref = stack
        self.moves = 0
        self.len = len(stack)

    def is_solved(self):
        return (sorted(self.ref) == list(self.stack_a))

    def sa(self):
        if len(self.stack_a) < 2:
            return
        a = self.stack_a.popleft()
        b = self.stack_a.popleft()
        self.stack_a.appendleft(a)
        self.stack_a.appendleft(b)
        self.moves += 1

    def sb(self):
        if len(self.stack_b) < 2:
            return
        a = self.stack_b.popleft()
        b = self.stack_b.popleft()
        self.stack_b.appendleft(a)
        self.stack_b.appendleft(b)
        self.moves += 1

    def pa(self):
        if len(self.stack_b) > 0:
            a = self.stack_b.popleft()
            self.stack_a.appendleft(a)
            self.moves += 1

    def pb(self):
        if len(self.stack_a) > 0:
            a = self.stack_a.popleft()
            self.stack_b.appendleft(a)
            self.moves += 1

    def ra(self):
        a = self.stack_a.popleft()
        self.stack_a.append(a)
        self.moves += 1

    def rb(self):
        self.stack_b.rotate()
        self.moves += 1

    def rra(self):
        self.stack_a.rotate()
        self.moves += 1

    def rrb(self):
        a = self.stack_b.pop()
        self.stack_b.appendleft(a)
        self.moves += 1

    def parse_input(self, input_):
        match input_ :
            case "sa" :
                self.sa()
            case "sb":
                self.sb()
            case "ss":
                self.sa()
                self.sb()
            case "pa":
                self.pa()
            case "pb":
                self.pb()
            case "ra":
                self.ra()
            case "rb":
                self.rb()
            case "rr":
                self.ra()
                self.rb()
            case "rra":
                self.rra()
            case "rrb":
                self.rrb()
            case "rrr":
                self.rra()
                self.rrb()
            case _:
                return f"{input_}:  unrecognized input"

    def display_env(self, cmd: str):
        print(Fore.RED + "-" * 9,Fore.RED + "ENV",Fore.RED + "-" * 9)
        print(f"command : {cmd}")
        print()
        print(" _                  _")
        for i in range(self.len):
            print(f"|{self.stack_a[i] if len(self.stack_a) > i else ' '}|\
                |{self.stack_b[i] if len(self.stack_b) > i else ' '}|")
        print("|_|                |_|")
        print(Fore.RED + f"MOVES:{self.moves}")
