# used to execute operating system commands
# The return from os.system() stored in a variable is only 0 for success and 1 for fail, not the actual return text of the comamnd

import subprocess

# basic commands
# sp = subprocess.Popen(cmd, shell=True/False, stdout=subprocess.PIPE, stderr=subprocess.PIPE) - add universal_newlines=True to get string instead of byte
# rc = sp.wait() - will store success status, 0 success, 1 fail
# out, err=sp.communicate()

# Shell security consideration - from python3 docs - Unlike some other popen functions, this implementation will never implicitly call a system shell. This means that all characters, including shell metacharacters, can safely be passed to child processes. If the shell is invoked explicitly, via shell=True, it is the application’s responsibility to ensure that all whitespace and metacharacters are quoted appropriately to avoid shell injection vulnerabilities. On some platforms, it is possible to use shlex.quote() for this escaping.

# shell = True - cmd is passed as a string
# shell = False - cmd is passed as a list, doesnt work on Env variables

# ex. cmd='ls -lrt' -> Shell True
# ex. cmd=['ls', 'lrt'] or cmd.split() -> Shell False

# For Windows
# Maybe problems with shell false, try shell true

# examples
# cmd = 'bash --version'
cmd = 'java -version'
# cmd='ls -lrt'

sp = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
# sp = subprocess.Popen(cmd.split(), shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
rc = sp.wait()
out, err = sp.communicate()

print(rc) # 0 - Success
if rc == 0:
  if bool(out) == True:    
    for line in out.splitlines():
      # for bash version
      # if "version" in line and "release" in line:
      #   print(line.split()[3].split("(")[0])
      print(line)
  if bool(out) == False:
    if bool(err) == True:
      print(err)
else:
  print(f' Error: {err}')

# Above example tests for a special case in which the java version is being output as an error and not as output






