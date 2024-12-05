from utils.decorator import input_error

@input_error
def show_phone(args, contacts):
    if len(args) != 1:
        raise ValueError
    name = args[0]
    if name in contacts:
        return f"{name}: {contacts[name]}"
    raise KeyError