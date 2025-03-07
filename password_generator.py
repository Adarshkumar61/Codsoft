import random
import string

def password(length):
    randompass = string.ascii_letters + string.digits
    if length < 4:
        print("Password length should atleast 4")
        return None
    password = "".join(random.choice(randompass) for i in range(length))
    return password
length = int(input("Enter the password length you want: "))
print("Random generated password is: ", password(length))
    