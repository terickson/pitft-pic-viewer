
import argparse
from subprocess import call
parser = argparse.ArgumentParser(description='update google calendar')
parser.add_argument('--picFolder', dest='picFolder', required=True, type=str, help="Get the folder that the pictures will be coming from.")
parser.add_argument('--sleepTime', dest='sleepTime', required=True, type=int, help="Get the time to sleep between pictures.")
args = parser.parse_args()
picFolder = args.picFolder
sleepTime = args.sleepTime
viewCommand = '/usr/bin/fbi -T 2 -noverbose -a -t ' + str(sleepTime) + ' -u -d /dev/fb1 `find ' + picFolder + ' -iname "*.png" -o -iname "*.jpg"`'


def main():
    call([viewCommand], shell=True)
    while True:
        pass


if __name__ == '__main__':
    main()
