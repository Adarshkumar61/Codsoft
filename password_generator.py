import random
import string

def random_pass(length): 
    if length < 4: 
        return "password length should atleast 4 digits.."
    char = string.ascii_letters + string.digits
    # use combination of char letter and and many
    password = " ".join(random.choice(char) for i in range(length))
    return password

while True:
    try:
        length = int(input("Enter your password length: "))
        break
    except ValueError:
        print("invalid input..")
        
password = random_pass(length)
print("Generated password: ", password)    
print("Thanku for using our program.😊")
    