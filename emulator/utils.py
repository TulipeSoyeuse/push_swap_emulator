def check_valid_input(stack: list):
    if len(set(stack)) != len(stack):
        raise ValueError("your stack have duplicate !")
