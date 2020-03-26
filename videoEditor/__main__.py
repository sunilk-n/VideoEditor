import os
import sys
import argparse

from moviepy.editor import *

def editVideo(videoFile, start=0, end=60):
    videoClip = VideoFileClip(videoFile)
    editVideoClip = videoClip.subclip(start, end)
    return editVideoClip

def getArguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-i", "--input",
        help="Input movie file",
        required=True
    )
    parser.add_argument(
        "-s", "--start", type=int,
        help="Start time in seconds",
        required=False
    )
    parser.add_argument(
        "-e", "--end", type=int,
        help="End time in seconds",
        required=False
    )
    parser.add_argument(
        "-o", "--output",
        default="D:/Youtube videos/outFiles",
        help="Set output path to save the mp4 file",
        required=False
    )

    args = parser.parse_args(sys.argv)
    return args


def main():
    args = getArguments()

    defaultInPath = "D:/Youtube videos/inFiles"
    start = 0
    if args.start:
        start = args.start
    if args.end:
        end = args.end
    else:
        end = start + 60
    
    inputPath = args.input
    if not os.path.exists(inputPath):
        inputPath = os.path.join(defaultInPath, inputPath)
        if not os.path.exists(inputPath):
            print("Sorry, The file path mentioned doesn't exists")
            sys.exit()
    outputFile = os.path.join(args.output, os.path.basename(inputPath).split('.')[0]+".mp4")
    eVideo = editVideo(inputPath, start=start, end=end)
    eVideo.write_videofile(outputFile, codec='libx264')
    

if __name__ == "__main__":
    main()
    
