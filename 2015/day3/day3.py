# --- Day 3: Perfectly Spherical Houses in a Vacuum ---
# Santa is delivering presents to an infinite two-dimensional grid of houses.

# He begins by delivering a present to the house at his starting location, and then an elf at the North Pole calls him via radio and tells him where to move next. Moves are always exactly one house to the north (^), south (v), east (>), or west (<). After each move, he delivers another present to the house at his new location.

# However, the elf back at the north pole has had a little too much eggnog, and so his directions are a little off, and Santa ends up visiting some houses more than once. How many houses receive at least one present?

# For example:

# > delivers presents to 2 houses: one at the starting location, and one to the east.
# ^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
# ^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.

nodes = {}

root = (0,0)

curr = root

nodes[root] = 1

with(open("2015\day3\day3_input.txt", "r")) as F:

    while(True):
        move = F.read(1)
        if not move:
            break
        
        if move == "^":
            nxt = (curr[0], curr[1] + 1)
        if move == "v":
            nxt = (curr[0], curr[1] - 1)
        if move == "<":
            nxt = (curr[0] - 1, curr[1])
        if move == ">":
            nxt = (curr[0] + 1, curr[1])

        if nodes.__contains__(nxt):
            nodes[nxt] += 1
        else:  
            nodes[nxt] =  1

        curr = nxt
    
    print(nodes.__len__())

#     --- Part Two ---
# The next year, to speed up the process, Santa creates a robot version of himself, Robo-Santa, to deliver presents with him.

# Santa and Robo-Santa start at the same location (delivering two presents to the same starting house), then take turns moving 
# based on instructions from the elf, who is eggnoggedly reading from the same script as the previous year.

# This year, how many houses receive at least one present?

# For example:

# ^v delivers presents to 3 houses, because Santa goes north, and then Robo-Santa goes south.
# ^>v< now delivers presents to 3 houses, and Santa and Robo-Santa end up back where they started.
# ^v^v^v^v^v now delivers presents to 11 houses, with Santa going one direction and Robo-Santa going the other.
        
nodes = {}

root = (0,0)

s_curr = root
r_curr = root

nodes[root] = 1

with(open("2015\day3\day3_input.txt", "r")) as F:
    while(True):
        moves = F.read(2)
        if not moves:
            break

        s_move = moves[0]

        if s_move == "^":
            s_nxt = (s_curr[0], s_curr[1] + 1)
        if s_move == "v":
            s_nxt = (s_curr[0], s_curr[1] - 1)
        if s_move == "<":
            s_nxt = (s_curr[0] - 1, s_curr[1])
        if s_move == ">":
            s_nxt = (s_curr[0] + 1, s_curr[1])

        if nodes.__contains__(s_nxt):
            nodes[s_nxt] += 1
        else:  
            nodes[s_nxt] =  1
        
        s_curr = s_nxt

        r_move = moves[1]

        if r_move == "^":
            r_nxt = (r_curr[0], r_curr[1] + 1)
        if r_move == "v":
            r_nxt = (r_curr[0], r_curr[1] - 1)
        if r_move == "<":
            r_nxt = (r_curr[0] - 1, r_curr[1])
        if r_move == ">":
            r_nxt = (r_curr[0] + 1, r_curr[1])

        if nodes.__contains__(r_nxt):
            nodes[r_nxt] += 1
        else:  
            nodes[r_nxt] =  1

        r_curr = r_nxt

    
    print(nodes.__len__())

 



