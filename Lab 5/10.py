import re
def snake(text):
    str = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', str).lower()

text=input()

print(snake(text))