import random
from variables import lower_letters, upper_letter, symbols, numbers

characters = []
all = list(lower_letters + upper_letter + symbols + numbers)


def all_characters(what_kind_pass, password_length):
    """function would usee all characters like special characters, numbers
    lower case, and upper case letters

    Args:
        what_kind_pass (string): it leads to this function
        password_length (integer): will tell how many characters the user 
    wants for the password

    Returns:
        string: gives the full password based on the length and the type of password
    """

    for letters in range(password_length):
        characters.append(random.choice(all))
    random.shuffle(characters)
    password = ''.join(characters)
    return password
