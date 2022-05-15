import string
import random

# Generator will use the following methods:
# 
# string.digits
# string.ascii_lowercase
# string.ascii_uppercase
# string.punctuation

def main():
    possibleChars = string.digits + string.ascii_lowercase + string.ascii_uppercase + string.punctuation
    possibleNoPuncuation = string.digits + string.ascii_lowercase + string.ascii_uppercase

    length = int(input(f"Please enter how long you want the password to be: "))

    password = ""
    passwordNoPunctuation = ""

    while(0 != length):
        password += possibleChars[random.randint(0,len(possibleChars)-1)]
        passwordNoPunctuation += possibleNoPuncuation[random.randint(0,len(possibleNoPuncuation)-1)]
        length -= 1

    print(f"Generated Password is: {password}")
    print(f"Generated Password without punctuation is: {passwordNoPunctuation}")

if __name__ == "__main__":
    main()