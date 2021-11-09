import imageio as io
import sys
img_name = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
img = []
for n in img_name:
    img.append(io.imread('./Png/'+ n +'.png'))

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

gif = []
for i in Phonetic:
    i[0] = int((float(i[0]) + 0.02)//0.04)
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
args = sys.argv[1:]
io.mimsave(args[0]+'.gif', gif, duration = 0.04)
