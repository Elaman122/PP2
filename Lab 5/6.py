import re

text1 = input()
text2 = re.sub('[ ,.]', ':', text1)
print(text2)