import re

text1 = input()
text2 = re.findall('[a-z]+_[a-z]+$',text1)

print(text2)  