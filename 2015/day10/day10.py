# --- Day 10: Elves Look, Elves Say ---
# Today, the Elves are playing a game called look-and-say. They take turns making sequences by reading aloud the previous sequence and using that reading as the next sequence. For example, 211 is read as "one two, two ones", which becomes 1221 (1 2, 2 1s).

# Look-and-say sequences are generated iteratively, using the previous value as input for the next step. For each step, take the previous value, and replace each run of digits (like 111) with the number of digits (3) followed by the digit itself (1).

# For example:

# 1 becomes 11 (1 copy of digit 1).
# 11 becomes 21 (2 copies of digit 1).
# 21 becomes 1211 (one 2 followed by one 1).
# 1211 becomes 111221 (one 1, one 2, and two 1s).
# 111221 becomes 312211 (three 1s, two 2s, and one 1).
# Starting with the digits in your puzzle input, apply this process 40 times. What is the length of the result?

import re
starter = "1113122113"
def morph(string: str) -> str:

    strings = []

    newString = None
    char = None
    for i in range(len(string)):
        if newString is None:
            char = string[i]
            newString = string[i]
            continue
        if char == string[i]:
            newString += string[i]
        else:
            strings.append(newString)
            newString = string[i]
            char = string[i]

    strings.append(newString)

    newString = ""
    for string in strings:
        newString += str(len(string)) + string[0]

    return newString

string = starter
for i in range(40):
    string = morph(string)
print("40 times = ", len(string))

string = starter
for i in range(50):
    string = morph(string)
print("50 times = ", len(string))



        




