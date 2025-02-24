# Codec by Kennedy Junior
# If you liked this project, give it a ⭐ on GitHub!
# github.com/kennedyjunior

letras = ("abcdefghijklmnopqrstuvwxyz")
print("What do you want?")
print("Press 1 for encrypt or 2 for decrypt")

try:
    choice = int(input())  # Converte para inteiro
    if choice == 1:
        print("----Encrypt mode----")
    elif choice == 2:
        print("----Decrypt mode----")
    else:
        print("Invalid option, please try again.")
except ValueError:
    print("Invalid input. Please enter 1 or 2.")
    


     