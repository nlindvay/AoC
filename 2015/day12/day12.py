# --- Day 12: JSAbacusFramework.io ---
# Santa's Accounting-Elves need help balancing the books after a recent order. Unfortunately, their accounting software uses a peculiar storage format. That's where you come in.

# They have a JSON document which contains a variety of things: arrays ([1,2,3]), objects ({"a":1, "b":2}), numbers, and strings. Your first job is to simply find all of the numbers throughout the document and add them together.

# For example:

# [1,2,3] and {"a":2,"b":4} both have a sum of 6.
# [[[3]]] and {"a":{"b":4},"c":-1} both have a sum of 3.
# {"a":[-1,1]} and [-1,{"a":1}] both have a sum of 0.
# [] and {} both have a sum of 0.
# You will not encounter any strings containing numbers.

# What is the sum of all numbers in the document?
import re
import json
sum = 0
with(open("2015\day12\input.json", "r")) as F:
    while True:
        line = F.readline()
        if not line:
            break
        
        m = re.findall("[0-9]+|-[0-9]+", line)

        for n in m:
            sum += int(n)
print(sum)


def traverse() -> int :
    b'g'
    return 1

# Opening JSON file 
with open('2015\day12\input.json') as json_file: 
    data: dict = json.load(json_file) 
  
    # Print the type of data variable 
    for key in data.keys():
        if type(data[key]) is dict:
            print(key,type(data[key]), end="\n")
            print(type(data[key]))

         








