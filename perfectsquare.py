"""
The goal of this challenge (and category) is to create ASCII drawings with various levels of sophistication.

For the first one, the goal is to generate an NxN ASCII square. The only requirements are:

The corners are made of *

The rest of it is not an *
"""

answer = input("How long should each side be?")

answer = int(answer)

if answer == 2:
    print("**")
    print("**")

else:
    print("*" + "-"*answer + "*")

    for x in range(answer-2):
        print("-"*(answer+2))

    print("*" + "-"*answer + "*")
