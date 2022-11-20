import os

f = open('random.dic', 'r')
lines = f.readlines()

for line in lines:
    os.system("./program " + line)