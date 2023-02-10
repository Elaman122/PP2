from itertools import permutations
def per(s):
    l = list(permutations(s))
    for i in l:
        print(i)

per('abc')