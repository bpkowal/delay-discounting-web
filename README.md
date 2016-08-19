#delay-discounting-web
A web.py python based adaptive algorithm for collecting indifference points at a magnitude of $10

not currently configured for deployment in public url but can be run locally on web browser

Dependencies 
>> If you are new to Python try starting here...https://bootstrap.pypa.io/get-pip.py 
  1. Install pip from http://pypi.python.org/pypi/pip
  2. Use ... python -m pip install "--packages you need--"
  a. distribute from http://pypi.python.org/pypi/distribute
  b. nose from http://pypi.python.org/pypi/nose/
  c. virtualenv from http://pypi.python.org/pypi/virtualenv
  d. lpthw.web ...this is just a fork of web.py made by the
    author of Learn Python the Hard Way
  3. Use ....[Environment]::SetEnvironmentVariable("Path", 
    "$env:Path;C:\Python27\Scripts", "User") 



if running through Terminal (MAC) execute by entering the following commands after download of skeleton
  1. export PYTHONPATH=$PYTHONPATH:.
  2. python bin/apple.py
then opening web browser (Safari) and navagating to  http://localhost:8080/

if running in PowerShell or Cmd (PC) execute by entering the following commands after downlaod of skeleton
  1. $env:PYTHONPATH = "$env:PYTHONPATH;." (works on Powershell) or 
    I hacked this together set PYTHONPATH=%PYTHONPAT%;C:\location of dir (works on Cmd)
  2. python bin/apple.py
then opening web browser (Chrome) and navagating to  http://localhost:8080/

user data are saved to test.txt in main/setup to run one participant at a time with no ID
test.txt will not close if user does not complete program and may cause subsiquent errors following first run

ctrl-c is used to terminate program

test folder is for running nosetests...
