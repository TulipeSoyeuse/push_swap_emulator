from colorama import Fore


def check_valid_input(stack: list):
    if len(set(stack)) != len(stack):
        raise ValueError("your stack have duplicate !")


def resolution(swapper, cmd=None):
    swapper.display_env(cmd)
    if swapper.is_solved():
        print(
            Fore.GREEN + "-" * 9 + " " + f"STACK SORTED : {swapper.moves} move used",
            Fore.GREEN + "-" * 9,
        )
        exit(0)
