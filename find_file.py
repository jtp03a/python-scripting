import os
import string

# platform independent system wide search for a file using os walk
# Linux find - find / -iname host.conf

req_file = input("Enter the file name to find: ")

# works for linux because / is the root but there is not equivalent in windows
# path = "/"
# need a way to identify all drives in Windows
# i.e. path = "C:\\Users\\xorci\\Documents"
pos_drive_names = string.ascii_letters
for drive_ltr in pos_drive_names:
  if os.path.exists(f'{drive_ltr}:\\')
    print(f'{drive_ltr}:\\')

for p, d, f in list(os.walk(path)):
  print(p, d, f)
  for file in f:
    if req_file in file:
      print(os.path.join(p, file))

