a = input()

upp = 0
low = 0

for i in range(len(a)) :
    if a[i] >= 'a' and a[i] <= 'z' :
        low += 1
    else :
        upp += 1

print(upp, low)