import os
import glob
import shutil
import time

# path to Big Bubba usb horn (Fuck Yeah!!)
usb_path = glob.glob('/media/bigbubba/*')

# Source folder of mp3 files
source_dir = '/home/projects/Horns/Starwars'

# Destination () of course it's the Big Bubba Fuck Yeah!)
dest_dir = '/media/bigbubba/'

# Mount usb as the usb stick and check that it exists
def usbMount():
    from subprocess import check_call
    check_call(['mount', '/dev/sdb1','/media/bigbubba'])
    time.sleep(.1)

# Delete all the files.
def emptyBubba():
    for f in usb_path:
        os.remove(f)
        print(usb_path)
    time.sleep(.1)

# Copy all files to the usb stick.
def copyToBubba():
    for filename in glob.glob(os.path.join(source_dir, '*.*')):
        shutil.copy(filename, dest_dir)
    time.sleep(.1)

usbMount()
emptyBubba()
copyToBubba()



