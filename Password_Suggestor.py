import random

def password_generator(chars_for_password):
    chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
    '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
    '@', '>', '<', '?', '_', '-', '=', '+', '!', '$', '%', '^', '&', '*', 
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    char_num = chars_for_password
    password_raw = []

    for x in range(char_num):
        letter = random.choice(chars)
        password_raw.append(letter)

    def convert_to_str(array):
        password = ""
        return (password.join(array))

    return (convert_to_str(password_raw))

passwords_to_generate = int(input("How many passwords would you like to generate? "))
chars_num = int(input("Number of chars in your password: "))

for y in range(passwords_to_generate):
    print(str(y + 1) + ": " + password_generator(chars_num))
