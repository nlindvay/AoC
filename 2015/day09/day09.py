# --- Day 9: All in a Single Night ---
# Every year, Santa manages to deliver all of his presents in a single night.

# This year, however, he has some new locations to visit; his elves have provided him the distances between every pair of locations. He can start and end at any two (different) locations he wants, but he must visit each location exactly once. What is the shortest distance he can travel to achieve this?

# For example, given the following distances:

# London to Dublin = 464
# London to Belfast = 518
# Dublin to Belfast = 141
# The possible routes are therefore:

# Dublin -> London -> Belfast = 982
# London -> Dublin -> Belfast = 605
# London -> Belfast -> Dublin = 659
# Dublin -> Belfast -> London = 659
# Belfast -> Dublin -> London = 605
# Belfast -> London -> Dublin = 982
# The shortest of these is London -> Dublin -> Belfast = 605, and so the answer is 605 in this example.

# What is the distance of the shortest route?
import re
import itertools

rules = []
cities = []
with(open("2015\day09\input.txt", "r")) as F:
    while True:
        line = F.readline().replace("\n", "")
        if not line:
            break
        split = line.split(" ")
        split.pop(3)
        split.pop(1)
        rules.append(split[0] + " " + split[1] + " " +split[2])
        rules.append(split[1] + " " + split[0] + " " + split[2])

        for string in split:
            if re.match("[a-zA-Z]+", string):
                if not cities.__contains__(string):
                    cities.append(string)
    
    shortestDist = None
    furthestDist = None
    for perm in itertools.permutations(cities):  

        dist = 0
        for i in range(len(perm)-1):
            for rule in rules:
                split = rule.split(" ")
                if re.match(perm[i], split[0]) and re.match(perm[i+1], split[1]):
                    dist += int(split[2])
                    
        if shortestDist is None:
            shortestDist = dist
        elif dist < shortestDist: 
            shortestDist = dist

        if furthestDist is None:
            furthestDist = dist
        elif dist > furthestDist: 
            furthestDist = dist
        
    print("part 1 answer: ", shortestDist)
    print("part 2 answer: ", furthestDist)

#     --- Part Two ---
# The next year, just to show off, Santa decides to take the route with the longest distance instead.

# He can still start and end at any two (different) locations he wants, and he still must visit each location exactly once.

# For example, given the distances above, the longest route would be 982 via (for example) Dublin -> London -> Belfast.

# What is the distance of the longest route?

# Although it hasn't changed, you can still get
   

