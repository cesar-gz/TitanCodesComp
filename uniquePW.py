"""
As a security measure, our company needs to update the passwords for all 100 employees. 
Your task is to generate 100 unique passwords that meet the following criteria:

14 characters exactly in length
At least one uppercase letter
At least one lowercase letter
At least one digit
At least one special character from the set (!@#$%^&)
Access the validation site here and submit the passwords, one per line.

Only 100 passwords are required, no more, no less
"""

import random

asciiLowercase = 'abcdefghijklmnopqrstuvwxyz'
asciiUppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
specialChars = '!@#$%^&'

def inputChar():

    char = ""

    randomNumber = random.randint(1,4)

    if(randomNumber == 1):
        randNum = random.randint(0,25)
        char = asciiLowercase[randNum]
        return char

    if(randomNumber == 2):
        randNum = random.randint(0,25)
        char = asciiUppercase[randNum]
        return char
    
    if(randomNumber == 3):
        randNum = random.randint(0,9)
        char = digits[randNum]
        return char
    
    if(randomNumber == 4):
        randNum = random.randint(0,6)
        char = specialChars[randNum]
        return char
    

passwordList = []

for x in range(100):
    character = ""
    randNum = random.randint(0,25)
    chars = asciiLowercase[randNum]
    character += chars
    randNum = random.randint(0,25)
    chars = asciiUppercase[randNum]
    character += chars
    randNum = random.randint(0,9)
    chars = digits[randNum]
    character += chars
    randNum = random.randint(0,6)
    chars = specialChars[randNum]
    character += chars
    for y in range(10):
        character += inputChar()
    passwordList.append(character)  

f = open("submission.txt", "w")

for word in passwordList:
    print(word)
    f.write(word + "\n")

f.close()