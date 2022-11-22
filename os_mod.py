import os

# os.sep - find out the path seperator for the current os / \
print(os.sep)

# current working dir
print(os.getcwd())

# change dir
# os.chdir("C:\Python")
# print(os.getcwd())

# list dir
files1 = os.listdir(os.getcwd())
print(files1)
# For windows paths have to provide \\ to avoid hitting special chars like \n and \t
# files2 = os.listdir("C:\\Python\\test\\os")
# or
# files3 = os.listdir(r"C:\\Python\\test\\os")
# print(files2)
# print(files3)

# create dirs
# os.chdir("C:\Python")
# os.mkdir("test2")
# os.makedirs("test2/test/test/test")
# cannot use if folder already created, must specify exist_ok=True

# remove dirs
# os.rmdir("test2")

# remove and remove dirs (recursively)
# os.removedirs("test2/test/test/test")
# os.rename(src, dest)

# Path methods
current_dir = os.getcwd()
fake_path = '/home/jpeterson/node_projects/python-scripting/test'
file1 = "text1.txt"
combined = os.path.join(current_dir, file1)
print(combined)
print(os.path.exists(combined))
print(os.path.isfile(combined))
print(os.path.isdir(combined))

# basename
print(f'Basename: {os.path.basename(current_dir)}')
# Dir Name
print(f'Dirname: {os.path.dirname(current_dir)}')

# Split
print(os.path.split(current_dir))

# exists
print(os.path.exists(current_dir))
print(os.path.exists(fake_path))

# Statistics
print(os.stat(combined).st_size)

# Environment Variables
# path = os.environ.get("PATH")
# print(path)
# print(os.getlogin())

# os.getuid()
# os.getpid()

# os walk - used to generate directory and file names in a directory tree by walking
# os walk will always generate a list of tuples
# First value in the tuple is the path of the directory
# Second value in the tuple is the list of sub folders in that directory
# Second value in the tuple is the list of files in the folder
# next tuple in the list of tuples is the same for the next sub directory

test_path = "/home/jpeterson/node_projects/python-scripting"

print(list(os.walk(test_path))[-2:])

for path, directories, files in list(os.walk(test_path))[-2:]:    
  print(path) #the path
  if len(directories) > 0: #only print the directory list if there are actually sub dirs
    print(directories) #the folders in the path
  print(files) #the files in the path
  for file in files:
    print(os.path.join(path, file)) #get the complete path for each file



