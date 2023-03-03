def generattors(n):
    for i in range(n):  
        if i%3==0 and i%4==0:
            yield i


for i in generattors(int(input())):
    print(i)