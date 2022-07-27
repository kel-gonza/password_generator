import random
from variables import lower_letters, upper_letter, symbols, numbers

characters = []
all = list(lower_letters + upper_letter + symbols + numbers)


def all_characters(what_kind_pass, password_length):
    # this function will use all characters like special characters, numbers,
    # upper and lowercase letters
    for letters in range(password_length):
        characters.append(random.choice(all))
    random.shuffle(characters)
    password = ''.join(characters)
    return password
