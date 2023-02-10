num = input().split(' ')

def prime():
    cnt = 0
    pr = []
    for i in range(0, len(num)):
        for j in range(1, int(num[i]) + 1):
            if(int(num[i]) % j == 0):
                cnt+=1
        if(cnt == 2):
            pr.append(num[i])
        cnt = 0
    return pr

print(prime())
