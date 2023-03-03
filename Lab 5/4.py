import re

text1 = input()
text2 = re.findall('^[A-Z]+[a-z]+$',text1)

print(*text2)