import random
from variables import lower_letters, upper_letter

characters = []
alphabet = list(lower_letters + upper_letter)


def easy_to_read(what_kind_pass, password_length):
    """This functions gives a password that has no numbers and no
    special characters

    Args:
        what_kind_pass (string): it leads to this function
        password_length (integer): will tell how many characters the user 
        wants for the password

    Returns:
        string: gives the full password based on the length and the type of password
    """

    for letters in range(password_length):
        characters.append(random.choice(alphabet))
    random.shuffle(characters)
    password = ''.join(characters)
    return password
