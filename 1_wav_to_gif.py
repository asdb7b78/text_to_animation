import os

print('Name of .wav file:')
name = input()
os.system('./rhubarb -o tmp.txt ' + name + '.wav')
os.system('python3 make_gif.py '+name+' < tmp.txt')
os.system('rm tmp.txt')
