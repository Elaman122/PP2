import re

text = input()

x = re.sub(r"(\w)([A-Z])", r"\1 \2", text)

print(x)