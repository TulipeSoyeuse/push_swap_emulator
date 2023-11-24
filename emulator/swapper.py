from utils import *
from collections import deque

class Swapper:
    def __init__(self, stack: list):
        """replicateur of the swap push function
        Args:
            stack (list): args from the commande line
        """
        check_valid_input(stack)
        self.stack_a = deque(stack, maxlen=len(stack))
        self.stack_b = deque(maxlen=len(stack))
        self.ref = stack

    def is_solved(self):
        return (sorted(self.ref) == list(self.stack_a))
