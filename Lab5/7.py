import re

def textt(text):
    h=''
    d=re.sub('_',' ',text)
    d=d.title()
    d=re.sub(' ','',d)
    return d

text=input()

print(textt(text))