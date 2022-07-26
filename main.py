import random

characters = []

print('Welcome to Password Generator!')
print('Please input the type of password you want.')

password_length = int(input("How long do you want your password to be? "))
what_kind_pass = input(
    "Pick the type of options you want for the password. ('easy to read', 'easy to say', or 'all character' options) ")

# by comparing the password length it will show how strong the password is
# will also do by 'password length' is how long the password should be and how many
# characters it will go inside the list

if password_length <= 6:
    print("weak password.")
elif password_length <= 10:
    print("Medium strength password.")
elif password_length >= 11:
    print("Strong password.")

while True:
    # this leads to the correct path that the user chooses
    if what_kind_pass == 'easy to read':
        # this will lead to the easy_to_read functions
        pass
    elif what_kind_pass == 'easy to say':
        # this will elad to the easy to say functions
        pass
    elif what_kind_pass == 'all character':
        # this will lead to the all character functions
        pass
