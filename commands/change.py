from utils.decorator import input_error

@input_error
def change_contact(args, contacts):
    if len(args) != 2:
        raise ValueError
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return f"Contact {name} updated."
    raise KeyError