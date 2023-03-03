def geneatoors(n):
    i=0
    while n>i:
        yield n
        n=n-1

for i in geneatoors(int(input())):
    print(i)