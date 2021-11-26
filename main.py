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
    parser.add_argument('-S', '--size', action='store_true', help='Resize the gif.')
    parser.add_argument('-H', '--height', action='store_true', help='Scale up the gif by height.')
    parser.add_argument('-P', '--pos', action='store_true', help='Set gif position, default = (0, 0).')
    args = parser.parse_args()
    
    tta.text_to_animation(args.pptx, args.page, args.name, args.folder, args.duration, args.pos, args.size, args.height)
