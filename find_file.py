import os
import string
import platform

# platform independent system wide search for a file using os walk
# Linux find - find / -iname host.conf

req_file = input("Enter the file name to find: ")

# get platform
platform_type = platform.system()

def get_win_drives():
# / is the root for linux but there is not equivalent in windows
# path = "/"
# need a way to identify all drives in Windows
# i.e. path = "C:\\Users\\xorci\\Documents"
# Get all valid drives in Windows and store in a list
  win_drives = []
  pos_drive_names = string.ascii_uppercase
  for drive_ltr in pos_drive_names:
    if os.path.exists(f'{drive_ltr}:\\'):
      win_drives.append(f'{drive_ltr}:\\')
  print(win_drives)
  return win_drives

def search(path):
  for p, d, f in list(os.walk(path)):
    for file in f:
      if req_file in file:
        print(os.path.join(p, file))

if platform_type == 'Windows':
  for drive in get_win_drives():
    search(f'{drive}Users\\xorci\\Documents')
else:
  search('/')

