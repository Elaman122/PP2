import re

text1 = input() # cdab
text2 = re.search('^a.+b\Z',text1)

print(text2)