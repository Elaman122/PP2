def generaator(dad):
    for i in range(dad):
        yield i**2


for i in generaator(int(input())):
    print(i)