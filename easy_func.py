import random
from variables import lower_letters, upper_letter

characters = []
letters = list(lower_letters + upper_letter)


def easy_to_say(what_kind_pass, password_length):
    # easy to say function gives a password that has no numbers and no special
    # characters
    for letters in range(password_length):
        characters.append(random.choice(letters))
    random.shuffle(characters)
    password = ''.join(characters)
    return password
