
def solve(numheads, numlegs):
    ch = 0
    rab = 0
    if(numheads < numlegs) :
        rab = (numlegs - 2 * numheads) / 2
        ch = numheads - rab
    return [int(ch), int(rab)]

print(solve(35, 94))
