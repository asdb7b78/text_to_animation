import sys
import os
import argparse
from pptx import Presentation
from pptx.util import Inches

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('pptx', action='store', help='Pptx file.')
    parser.add_argument('page', action='store',type=int, help='Page number.')
    parser.add_argument('-s', '--sound', action='store', help='Wav or mp3 file.')
    parser.add_argument('-g', '--gif', action='store', help='Gif file.')
    args = parser.parse_args()
    
    prs = Presentation(args.pptx)
    if args.gif != None:
        prs.slides[args.page-1].shapes.add_movie(args.gif, Inches(0), Inches(0), Inches(2), Inches(2))
    if args.sound != None:
        prs.slides[args.page-1].shapes.add_movie(args.sound, Inches(0), Inches(0), Inches(2), Inches(2))

    prs.save("python_ppt.pptx")
