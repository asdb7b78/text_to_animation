import imageio as io
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--duration', action='store',default='0.4', type=float, help='the duration of every image in gif')
parser.add_argument('-f', '--folder', action='store',default='Lip', help='the image folder name in "PNG"')
parser.add_argument('-n', '--name', action='store',default='output', help='the .wav file name')
args = parser.parse_args()

img_name = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
img = []

folder = args.folder
for n in img_name:
    img.append(io.imread('./Png/'+folder+'/'+n+'.png'))

Phonetic = []
while True:
    try:
        i = input().split('\t')
        Phonetic.append([i[0], i[1]])
    except EOFError:
        break

for i in range(0, len(Phonetic)-1):
    Phonetic[i][0] = float(Phonetic[i+1][0]) - float(Phonetic[i][0])
Phonetic.pop(len(Phonetic)-1)

d = args.duration
gif = []
for i in Phonetic:
    i[0] = int((float(i[0]) + d/2)//d)
    for j in range(0, i[0]):
        if i[1] == 'X' or i[1] == 'A':
            gif.append(img[0])
        elif i[1] == 'B':
            gif.append(img[1])
        elif i[1] == 'C':
            gif.append(img[2])
        elif i[1] == 'D':
            gif.append(img[3])
        elif i[1] == 'E':
            gif.append(img[4])
        elif i[1] == 'F':
            gif.append(img[5])
        elif i[1] == 'G':
            gif.append(img[6])
        elif i[1] == 'H':
            gif.append(img[7])

io.mimsave(args.name+'.gif', gif, duration = d)
