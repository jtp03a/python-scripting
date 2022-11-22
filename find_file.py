import os

# platform independent system wide search for a file using os walk
# Linux find - find / -iname host.conf

req_file = input("Enter the file name to find: ")

# works for linux but not windows
# path = "/"

path = "C:\\Users\\xorci\\Documents"

for p, d, f in list(os.walk(path)):
  print(p, d, f)
  for file in f:
    if req_file in file:
      print(os.path.join(p, file))

