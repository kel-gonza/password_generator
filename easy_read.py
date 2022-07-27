import random
from variables import lower_letters, upper_letter

characters = []
alphabet = list(lower_letters + upper_letter)


def easy_to_read(what_kind_pass, password_length):
    # easy to say function gives a password that has no numbers and no special
    # characters
    for letters in range(password_length):
        characters.append(random.choice(alphabet))
    random.shuffle(characters)
    password = ''.join(characters)
    return password
