# --- Day 7: Some Assembly Required ---
# This year, Santa brought little Bobby Tables a set of wires and bitwise logic gates! Unfortunately, 
# little Bobby is a little under the recommended age range, and he needs help assembling the circuit.

# Each wire has an identifier (some lowercase letters) and can carry a 16-bit signal (a number from 0 to 65535). 
# A signal is provided to each wire by a gate, another wire, or some specific value. 
# Each wire can only get a signal from one source, but can provide its signal to multiple destinations. 
# A gate provides no signal until all of its inputs have a signal.

# The included instructions booklet describes how to connect the parts together: x AND y -> z means to connect wires x and y 
# to an AND gate, and then connect its output to wire z.

# For example:

# 123 -> x means that the signal 123 is provided to wire x.
# x AND y -> z means that the bitwise AND of wire x and wire y is provided to wire z.
# p LSHIFT 2 -> q means that the value from wire p is left-shifted by 2 and then provided to wire q.
# NOT e -> f means that the bitwise complement of the value from wire e is provided to wire f.
# Other possible gates include OR (bitwise OR) and RSHIFT (right-shift). If, for some reason, you'd like to emulate the circuit instead, 
# almost all programming languages (for example, C, JavaScript, or Python) provide operators for these gates.

# For example, here is a simple circuit:

# 123 -> x
# 456 -> y
# x AND y -> d
# x OR y -> e
# x LSHIFT 2 -> f
# y RSHIFT 2 -> g
# NOT x -> h
# NOT y -> i
# After it is run, these are the signals on the wires:

# d: 72
# e: 507
# f: 492
# g: 114
# h: 65412
# i: 65079
# x: 123
# y: 456
# In little Bobby's kit's instructions booklet (provided as your puzzle input), what signal is ultimately provided to wire a?
import re

lines = []
wires = {}

def addWire(var1, var2) -> True:
    if gate == "LSHIFT":
        wires[destination] = var1 << var2
    elif gate == "RSHIFT":
        wires[destination] = var1 >> var2
    elif gate == "AND":
        wires[destination] = var1 & var2
    elif gate == "OR":
        wires[destination] = var1 | var2
    else:
        return False
    return True

#read in the file
with(open("2015\day7\day7_input.txt", "r")) as F:
    while True:
        line = F.readline().replace("\n", "")
        if not line:
            break
        lines.append(line.split(" "))

while lines.__len__() != 0:
    indices = []
    for i in range(lines.__len__()):
        split = list.copy(lines[i])
        destination = split.pop()

        if destination == 'b':
            wires[destination] = 956
            indices.append(lines[i])

        else:
            split.pop()
            addedWire = False
            if split.__len__() == 3:
                var1 = split[0]
                gate = split[1]
                var2 = split[2]

                if re.match("[0-9]+",var1) and re.match("[0-9]+", var2):
                    addedWire = addWire(int(var1), int(var2))
              
                elif re.match("[a-z]+", var1) and re.match("[a-z]+", var2):
                    if wires.__contains__(var1) and wires.__contains__(var2):
                        addedWire = addWire(wires[var1], wires[var2])
                   
                elif re.match("[a-z]+", var1) and re.match("[0-9]+", var2):
                    if wires.__contains__(var1):
                        addedWire = addWire(wires[var1], int(var2))
                     
                elif re.match("[0-9]+", var1) and re.match("[a-z]+", var2):
                    if wires.__contains__(var2):
                        addedWire = addWire(int(var1), wires[var2])
                   
            if split.__len__() == 2:
                gate = split[0]
                var1 = split[1]
                if wires.__contains__(var1):
                    addedWire = True
                    wires[destination] = ~wires[var1]

            if split.__len__() == 1:
                var1 = split[0]
                if re.match("[0-9]+", var1):
                    wires[destination] = int(var1)
                    addedWire = True
                elif re.match("[a-z]+", var1):
                    if wires.__contains__(var1):
                        wires[destination] = wires[var1]
                        addedWire = True
            
            if addedWire == True:
                indices.append(lines[i])
                print("added wire from line: ".format(i), lines[i])
            

    for ind in indices:
        lines.remove(ind)

print(wires['a'])
