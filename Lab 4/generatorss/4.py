def generatoors(n,k):
    for i in range(n,k):  
        yield i**2


for i in generatoors(int(input()),int(input())):
    print(i)