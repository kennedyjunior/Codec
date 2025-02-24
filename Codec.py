# Codec by Kennedy Junior
# If you liked this project, give it a ⭐ on GitHub!
# github.com/kennedyjunior

letras = "abcdefghijklmnopqrstuvwxyz"

def caesar_cipher(text, shift, encrypt=True):
    result = ""
    for char in text:
        if char.lower() in letras:
            shift_amount = shift if encrypt else -shift
            new_char = letras[(letras.index(char.lower()) + shift_amount) % 26]
            result += new_char.upper() if char.isupper() else new_char
        else:
            result += char 
    return result

print("What do you want?")
print("Press 1 for encrypt or 2 for decrypt")

try:
    choice = int(input())  # Converte para inteiro
    if choice == 1:
        print("----Encrypt mode----")
        message = input("Enter your message: ")
        shift = int(input("Enter shift value: "))
        print("Encrypted message:", caesar_cipher(message, shift, encrypt=True))
    elif choice == 2:
        print("----Decrypt mode----")
        message = input("Enter your encrypted message: ")
        shift = int(input("Enter shift value: "))
        print("Decrypted message:", caesar_cipher(message, shift, encrypt=False))
    else:
        print("Invalid option, please try again.")
        exit()
except ValueError:
    print("Invalid input. Please enter a valid number.")
    exit()