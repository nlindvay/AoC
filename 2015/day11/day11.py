# --- Day 11: Corporate Policy ---
# Santa's previous password expired, and he needs help choosing a new one.

# To help him remember his new password after the old one expires, Santa has devised a method of coming up with a password based on the previous one. Corporate policy dictates that passwords must be exactly eight lowercase letters (for security reasons), so he finds his new password by incrementing his old password string repeatedly until it is valid.

# Incrementing is just like counting with numbers: xx, xy, xz, ya, yb, and so on. Increase the rightmost letter one step; if it was z, it wraps around to a, and repeat with the next letter to the left until one doesn't wrap around.

# Unfortunately for Santa, a new Security-Elf recently started, and he has imposed some additional password requirements:

# Passwords must include one increasing straight of at least three letters, like abc, bcd, cde, and so on, up to xyz. They cannot skip letters; abd doesn't count.
# Passwords may not contain the letters i, o, or l, as these letters can be mistaken for other characters and are therefore confusing.
# Passwords must contain at least two different, non-overlapping pairs of letters, like aa, bb, or zz.
# For example:

# hijklmmn meets the first requirement (because it contains the straight hij) but fails the second requirement requirement (because it contains i and l).
# abbceffg meets the third requirement (because it repeats bb and ff) but fails the first requirement.
# abbcegjk fails the third requirement, because it only has one double letter (bb).
# The next password after abcdefgh is abcdffaa.
# The next password after ghijklmn is ghjaabcc, because you eventually skip all the passwords that start with ghi..., since i is not allowed.
# Given Santa's current password (your puzzle input), what should his next password be?

# Your puzzle input is cqjxjnds.

import re

def incr(c):
    if c == 'z':
        return 'a'
    return chr(ord(c) + 1)

s = "cqjxjnds"
p = list(s)

for i in range(2):
    valid = False
    while not valid:

        idx = len(p)-1
        
        r1 = False # one straight 'abc' or 'efg'
        r2 = False # no 'i', 'o', or 'l'
        r3 = False # 2 diff. non-overlapping pairs 'xx' 'bb'

        if p[idx] == z:
            for i in range(len(p)):
                if idx-i != idx:
                    if p[idx-i+1] == z:
                        p[idx-i] = incr(p[idx-i])
                    else:
                        break
        p[idx] = incr(p[idx])

        for i in range(len(p) - 2):
            # check r1: one straight 'abc' or 'efg'
            if ord(p[i])+1 == ord(p[i+1]) and ord(p[i])+2 == ord(p[i+2]):
                r1 = True

        f = "".join(p)

        # check r2: no 'i', 'o', or 'l'
        if re.search("i|o|l", f) is None:
            r2 = True

        # check r3: 2 diff. non-overlapping pairs 'xx' 'bb'
        m =  re.findall("(a{2}|b{2}|c{2}|d{2}|e{2}|f{2}|g{2}|h{2}|i{2}|j{2}|k{2}|l{2}|m{2}|n{2}|o{2}|p{2}|q{2}|r{2}|s{2}|t{2}|u{2}|v{2}|w{2}|x{2}|y{2}|z{2})", f)
        if m is not None and len(m) == 2:
            r3 = True

        if r1 and r2 and r3:
            valid = True

    print(''.join(p))