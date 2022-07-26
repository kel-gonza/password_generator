from easy_read import easy_to_read
from easy_func import easy_to_say
from all_characters import all_characters

print("Welcome to Password Generator!")
print("Just input the amount of characters you want in the password and the type of options you want for that password\n")
print("There are three types of options: 'easy to read', 'easy to say' and 'all characters'.")
print("\n*Easy to read*: will give you a password that has no numbers or special characters.")
print("\n*Easy to say*: will not give you ambiguous characters like, 'i','L','l','0', or 'O'")
print("\n*All characters*: will include all letters, numbers, and special characters.")
print("\nEnjoy!\n")

while True:
    # added an try except else, for the ValueError when the user doesn't put an input
    try:
        password_length = int(
            input("How long do you want your password to be? "))
    except ValueError:
        print("Error. Please enter a valid number.")
        continue
    else:
        break

while True:
    # added a loop so the input won't stop when the user doesn't pick the right option
    what_kind_pass = input("Pick the type of options you want for the password: \
        \n'easy to read', 'easy to say', or 'all characters' options)\n ")

    if what_kind_pass != 'easy to read' and what_kind_pass != 'easy to say' and what_kind_pass != 'all characters':
        print("please, type one of the choices above.")
        continue
    else:
        break

# by comparing the password length it will show how strong the password is
# will also do by 'password length' is how long the password should be and how many
# characters it will go inside the list

while True:

    if what_kind_pass == 'easy to read':
        # this will lead to the easy_to_read functions
        read = easy_to_read(what_kind_pass, password_length)
        print(f"This is your password: {read}")
        break

    elif what_kind_pass == 'easy to say':
        # this will lead to the easy to say functions
        say = easy_to_say(what_kind_pass, password_length)
        print(f"This is your password: {say}")
        break

    elif what_kind_pass == 'all characters':
        # this will lead to the all character functions
        all = all_characters(what_kind_pass, password_length)
        print(f"This is your password: {all}")
        break

if password_length <= 6:
    print("Weak password.")
elif password_length <= 10:
    print("Medium strength password.")
elif password_length >= 11:
    print("Strong password.")
