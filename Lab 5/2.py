import re
text1 = input()
text2 = re.findall('^a(b{2,3})')
print(text2)