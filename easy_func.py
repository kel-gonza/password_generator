import random
from variables import lower_letters, upper_letter, symbols, numbers

characters = []

ambiguous = list(lower_letters + upper_letter + symbols + numbers)

# remove ambiguous letters
ambiguous.remove('i')
ambiguous.remove('I')
ambiguous.remove('l')
ambiguous.remove('0')
ambiguous.remove('L')
ambiguous.remove('O')
ambiguous.remove('|')


def easy_to_say(what_kind_pass, password_length):
    """this function will give no ambiguous characters like:
    i, I, l, L, 0, O, |

    Args:
        what_kind_pass (string): it leads to this function
        password_length (integer): will tell how many characters the user 
    wants for the password

    Returns:
        string: gives the full password based on the length and the type of password
    """

    for letters in range(password_length):
        characters.append(random.choice(ambiguous))
    random.shuffle(characters)
    password = ''.join(characters)
    return password
