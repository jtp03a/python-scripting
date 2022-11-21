import os

# current working dir
print(os.getcwd())

# change dir
# os.chdir("C:\Python")
# print(os.getcwd())

# list dir
files1 = os.listdir(os.getcwd())
# For windows have to provide \\ to avoid escape chars
files2 = os.listdir("C:\\Python\\test\\os")
# or
files3 = os.listdir(r"C:\\Python\\test\\os")
print(files2)
print(files3)

# create dirs
# os.chdir("C:\Python")
# os.mkdir("test2")
# os.makedirs("test2/test/test/test")
# cannot use if folder already created, must specify exist_ok=True

# remove dirs
# os.rmdir("test2")

# Path methods
current_dir = os.getcwd()
file1 = "text1.txt"
combined = os.path.join(current_dir, file1)
print(combined)
print(os.path.exists(combined))
print(os.path.isfile(combined))
print(os.path.isdir(combined))

# Statistics
print(os.stat(combined).st_size)

# Environment Variables
path = os.environ.get("PATH")
print(path)
print(os.getlogin())

# os walk
