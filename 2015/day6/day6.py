# --- Day 6: Probably a Fire Hazard ---
# Because your neighbors keep defeating you in the holiday house decorating contest year after year, you've decided to deploy one million lights in a 1000x1000 grid.

# Furthermore, because you've been especially nice this year, Santa has mailed you instructions on how to display the ideal lighting configuration.

# Lights in your grid are numbered from 0 to 999 in each direction; the lights at each corner are at 0,0, 0,999, 999,999, and 999,0. The instructions include whether to turn on, turn off, or toggle various inclusive ranges given as coordinate pairs. Each coordinate pair represents opposite corners of a rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore refers to 9 lights in a 3x3 square. The lights all start turned off.

# To defeat your neighbors this year, all you have to do is set up your lights by doing the instructions Santa sent you in order.

# For example:

# turn on 0,0 through 999,999 would turn on (or leave on) every light.
# toggle 0,0 through 999,0 would toggle the first line of 1000 lights, turning off the ones that were on, and turning on the ones that were off.
# turn off 499,499 through 500,500 would turn off (or leave off) the middle four lights.
# After following the instructions, how many lights are lit?

import re as regex

dim = 1000
grid = [[0] * dim for i in range(dim)]
lit = 0

with(open("2015\day6\day6_input.txt", "r")) as F:
    while(True):
        line = F.readline().replace("\n","")
        if not line:
            break

        coordinates = regex.findall("[0-9]+[,][0-9]+", line) 
        coord1 = coordinates[0].split(",")
        coord2 = coordinates[1].split(",")
        x1= int(coord1[0])
        x2 = int(coord2[0])
        y1 = int(coord1[1])
        y2 = int(coord2[1])

        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                if line.__contains__("turn on"):
                    grid[i][j] = 1
                elif line.__contains__("turn off"):
                    grid[i][j] = 0
                elif line.__contains__("toggle"):
                    if grid[i][j] == 1:
                        grid[i][j] = 0
                    elif grid[i][j] == 0:
                        grid[i][j] = 1

for i in range(dim):
    for j in range(dim):
        if grid[i][j] == 1:
                lit += 1

print("part 1 answer: ", lit)

# --- Part Two ---
# You just finish implementing your winning light pattern when you realize you mistranslated Santa's message from Ancient Nordic Elvish.

# The light grid you bought actually has individual brightness controls; each light can have a brightness of zero or more. The lights all start at zero.

# The phrase turn on actually means that you should increase the brightness of those lights by 1.

# The phrase turn off actually means that you should decrease the brightness of those lights by 1, to a minimum of zero.

# The phrase toggle actually means that you should increase the brightness of those lights by 2.

# What is the total brightness of all lights combined after following Santa's instructions?

# For example:

# turn on 0,0 through 0,0 would increase the total brightness by 1.
# toggle 0,0 through 999,999 would increase the total brightness by 2000000.

dim = 1000
grid = [[0] * dim for i in range(dim)]
brightness = 0

with(open("2015\day6\day6_input.txt", "r")) as F:
    while(True):
        line = F.readline().replace("\n","")
        if not line:
            break

        coordinates = regex.findall("[0-9]+[,][0-9]+", line) 
        coord1 = coordinates[0].split(",")
        coord2 = coordinates[1].split(",")
        x1= int(coord1[0])
        x2 = int(coord2[0])
        y1 = int(coord1[1])
        y2 = int(coord2[1])

        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                if line.__contains__("turn on"):
                    grid[i][j] += 1
                elif line.__contains__("turn off"):
                    if grid[i][j] > 0:
                        grid[i][j] += -1
                elif line.__contains__("toggle"):
                    grid[i][j] += 2
               

for i in range(dim):
    for j in range(dim):
        brightness += grid[i][j]

print("part 2 answer: ", brightness)