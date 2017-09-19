
import os
from time import sleep
import argparse
from subprocess import call
parser = argparse.ArgumentParser(description='update google calendar')
parser.add_argument('--picFolder', dest='picFolder', required=True, type=str, help="Get the folder that the pictures will be coming from.")
parser.add_argument('--sleepTime', dest='sleepTime', required=True, type=int, help="Get the time to sleep between pictures.")
args = parser.parse_args()
picFolder = args.picFolder
sleepTime = args.sleepTime
viewCommand = '/usr/bin/fbi -T 2 -d /dev/fb1 -noverbose -a '


def main():
    while True:
        dirList = os.listdir(picFolder)
        dirList.sort()
        for filename in dirList:
            if filename.endswith('.png') or filename.endswith('.jpg'):
                command = viewCommand + picFolder + '/' + filename
                call([command], shell=True)
                sleep(sleepTime)
            else:
                continue


if __name__ == '__main__':
    main()
