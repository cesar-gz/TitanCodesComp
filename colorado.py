"""
The Colorado Department of Motor Vehicles is extremely jealous by the new license plate validator developed by the California DMV. 
In order to thoroughly test their own validator, they require a comprehensive list of all possible Colorado license plates. 
The format of a Colorado license plate is as follows:

ABC-123

Where ABC represents any combination of letters from A-Z, and 123 represents any combination of digits from 0-9. 
An example of a valid Colorado license plate is DMG-562.

To generate this list, we have written a program that generates all possible combinations of letters and digits and organizes
them into the desired format. Display the total number of license plates generated and show an organizer your code and output.

"""

import random

asciiUppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'

passwordList = []

counter = 0

print("beginning license plate generation . . .")

while counter < 10000:
    character = ""
    randNum = random.randint(0,25)
    chars = asciiUppercase[randNum]
    character += chars
    randNum = random.randint(0,25)
    chars = asciiUppercase[randNum]
    character += chars
    randNum = random.randint(0,25)
    chars = asciiUppercase[randNum]
    character += chars
    character += "-"
    randNum = random.randint(0,9)
    chars = digits[randNum]
    character += chars
    randNum = random.randint(0,9)
    chars = digits[randNum]
    character += chars
    randNum = random.randint(0,9)
    chars = digits[randNum]
    character += chars
    if character in passwordList:
        counter += 1
        continue
    else:
        passwordList.append(character)
        if counter == 100 or 500 or 1000 or 2000 or 3000 or 4000 or 5000 or 6000 or 7000 or 8000 or 9000:
            print(character)

print(len(passwordList))
#for word in passwordList:
#    print(word)
