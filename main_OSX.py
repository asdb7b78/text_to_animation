import os
import argparse
import text_to_animation as tta

#讀檔 -> 指定哪一頁 -> 轉換文字 -> 插入gif -> 插入聲音
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('pptx', action='store', help='Pptx name')
    parser.add_argument('page', action='store', default='0', type=int, help='Page number')
    parser.add_argument('-n', '--name', action='store', default='output', help="Name of .wav and .gif")
    parser.add_argument('-f', '--folder', action='store',default='Lip', help='Folder name in "PNG"')
    parser.add_argument('-d', '--duration', action='store',default='0.2', type=float, help='Gif duration of each image, default=0.2')
    parser.add_argument('--size', action='store_true', help='Resize the gif.')
    parser.add_argument('--height', action='store_true', help='Resize the gif by height.')
    parser.add_argument('--pos', action='store_true', help='Set gif position, default = (0, 0).')
    args = parser.parse_args()
    
    text = tta.pptx_to_text(args.pptx, args.page)

    tta.text_to_speech(text, args.name+'.wav')
    
    os.system("./rhubarb " + args.name + ".wav -o mouth.txt")
    
    tta.make_gif(args.folder, args.name + '.gif', dur=args.duration, mouth_path='mouth.txt')
    
    pos = [0, 0]
    size = False
    h = False
    if args.pos:
        print('Input new pos X Y in one line:')
        pos = input().split(' ')
        pos[0] = int(pos[0])
        pos[1] = int(pos[1])
    if args.size:
        print('Input new width and height in one line:')
        size = input().split(' ')
        size[0] = int(size[0])
        size[1] = int(size[1])
        if args.height:
            print("Can't resize with height simultaneously.")
    elif args.height: 
        print('Input new height:')
        h = int(input())

    prs = tta.insert_to_pptx(args.pptx, args.page, gif_path=args.name+'.gif', sound_path=args.name+'.wav', pos=pos, size=size, height=h)

    tta.save_pptx(prs, path='new_'+args.pptx)
