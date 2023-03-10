import os

path=r'C:\Users\Rober\OneDrive\Рабочий стол\benzema.txt'

if os.path.exists(path):
    print(os.path.basename(path))
    print("---------")
    print(os.path.dirname(path))