import os
import argparse
from subprocess import call, check_output
from time import sleep


def get_pid(name):
    return check_output(["pidof", name])


def check_pid(pid):
    """ Check For the existence of a unix pid. """
    try:
        os.kill(pid, 0)
    except OSError:
        return False
    else:
        return True


parser = argparse.ArgumentParser(description='update google calendar')
parser.add_argument('--picFolder', dest='picFolder', required=True, type=str, help="Get the folder that the pictures will be coming from.")
parser.add_argument('--sleepTime', dest='sleepTime', required=True, type=int, help="Get the time to sleep between pictures.")
args = parser.parse_args()
picFolder = args.picFolder
sleepTime = args.sleepTime
viewCommand = '/usr/bin/fbi -T 2 -noverbose -a -t ' + str(sleepTime) + ' -u -d /dev/fb1 `/usr/bin/find ' + picFolder + ' -iname "*.png" -o -iname "*.jpg"`'


def main():
    while True:
        call([viewCommand], shell=True)
        sleep(1)
        pid = get_pid("fbi")
        while True:
            if not check_pid(pid):
                break


if __name__ == '__main__':
    main()
