import time

n = int(input("Sample Input:\n"))

millisec = int(input())

root = pow(n, 0.5) 

print("Sample Output:")

time.sleep(millisec / 1000)

print("Square root of", n, "after", millisec, "is", root)