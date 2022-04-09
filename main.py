import random


def password_generator(n):
    """Return a password of nth character"""
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "@#&(!)-$€%§+=?<>"
    total = lowercase + uppercase + numbers + symbols
    password = ""
    for _ in range(n):
        password += random.choice(total)
    return password


if __name__ == "__main__":
    length = int(input("Enter the length of your password : "))
    pwd = password_generator(length)
    print(pwd)
