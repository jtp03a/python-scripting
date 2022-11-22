import platform
import getpass
# used to gather information about the system

# Print os type
print(platform.system())
# python version
print(platform.python_version())
print(platform.python_version_tuple())

print(platform.machine())
print(platform.release())
print(platform.node())
print(platform.uname())

# getpass - propts the user for a password without echoing. Secure way to handle password prompts where programs interact with users via the terminal
# getuser - function displays the login name of the user, checks env variables logname, user, lname, unsername in order and returns the value of the first non-empty string

print(getpass.getpass())
print(getpass.getuser())