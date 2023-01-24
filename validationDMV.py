"""
It's my first day at my new job at the DMV, and my boss is having me look through
a list of license plates to see which are valid in our state and which aren't. Can you help me out?

I know the format for license plates in California is 1 digit followed by 3 uppercase letters 
followed by 3 more digits. For example, 1ABC234 is valid, whereas ABC1234 isn't. The list has 600 license plates, 
which is way too many for me to go through by hand! Some of these aren't even 7 characters, so they're definitely not right...

Can you look through all of them, and for each one, put a T if it's valid, and an F if it isn't? 
For example, if the list had 5 plates where the first 3 are valid and the last 2 aren't, you could tell me TTTFF. Thanks a ton!
"""

textFile = []

def processFile():
    with open("plates.txt", "r") as platesFile:
        for line in platesFile:
            line = line.strip("\n")
            textFile.append(line)

processFile()

answer = ""
size = len(textFile)

for x in range(size):
    line = textFile[x]

    # check if there are atleast 7 characters per license plate, no more, no less
    if len(line) > 7 or len(line) < 7:
        answer += "F"
        continue

    if line[0].isdigit() == True:
        if line[1].isalpha() == True:
            if line[2].isalpha() == True:
                if line[3].isalpha() == True:
                    if line[4].isdigit() == True:
                        if line[5].isdigit() == True:
                            if line[6].isdigit() == True:
                                answer += "T"
                                continue
                            else:
                                answer += "F"
                                continue
                        else:
                            answer += "F"
                            continue
                    else:
                        answer += "F"
                        continue
                else:
                    answer += "F"
                    continue
            else:
                answer += "F"
                continue
        else:
            answer += "F"
            continue
    else:
        answer += "F"
        continue

print(answer)
print(len(answer))
    
    
