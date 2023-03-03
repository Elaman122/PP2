import re

def textt(text):
    h=''
    text=re.split("[A-Z]",text)

    return text


print(textt('abcAabc'))