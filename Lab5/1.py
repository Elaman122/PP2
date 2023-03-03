import re

text = input()
tx = re.search("^a.b*$",text)

print(tx)