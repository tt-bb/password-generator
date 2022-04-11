import random
import clipboard


def get_length_password():
    print("Enter the length of your password")
    print("(* Recommended length : more than 16 characters)")
    length = input("> ")
    while not length.strip().isdigit() or int(length) <= 0:
        length = input("Enter the length of your password : ")
    length = int(length.strip())

    return length


def get_complexity_password():
    print("What family of characters do you want ?")
    print("(* Recommended : Alphanumeric and symbols)")
    print("\t1. Uppercase only")
    print("\t2. Lowercase only")
    print("\t3. Numbers only")
    print("\t4. Alphanumeric only")
    print("\t5. Symbols only")
    print("\t6. Alphanumeric and symbols")

    character = input("> ")
    while not character.strip().isdigit() or int(character) not in range(1, 7):
        character = input("Enter the number of the family : ")
    character = int(character.strip())

    return character


def password_generator(n, family):
    """Return a password of nth character"""
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"
    alphanumeric = uppercase + lowercase + numbers
    symbols = "@#&(!)-$€%§+=?<>"
    total = uppercase + lowercase + numbers + symbols
    password = ""

    if family == 1:
        for _ in range(n):
            password += random.choice(uppercase)
        return password

    elif family == 2:
        for _ in range(n):
            password += random.choice(lowercase)
        return password

    elif family == 3:
        for _ in range(n):
            password += random.choice(numbers)
        return password

    elif family == 4:
        for _ in range(n):
            password += random.choice(alphanumeric)
        return password

    elif family == 5:
        for _ in range(n):
            password += random.choice(symbols)
        return password

    elif family == 6:
        for _ in range(n):
            password += random.choice(total)
        return password


if __name__ == "__main__":

    print("~~~ PASSWORD GENERATOR ~~~\n")

    # Get the length of the password
    length_password = get_length_password()
    print()
    # Get the complexity of the password
    complexity = get_complexity_password()
    # Get the password
    pwd = password_generator(length_password, complexity)
    print()
    print(f"Your password : {pwd}")
    clipboard.copy(pwd)
    print("Your password is now copied in your clipboard")
