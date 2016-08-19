#delay-discounting-web
A web.py python based adaptive algorithm for collecting indifference points at a magnitude of $10

--not currently configured for deployment in public url but can be run locally on web browser--

DEPENDENCIES 
If you are new to Python try starting here...https://bootstrap.pypa.io/get-pip.py 
  1. Install pip from http://pypi.python.org/pypi/pip
  2. Use ... python -m pip install "--packages you need--"
  3.  distribute from http://pypi.python.org/pypi/distribute
  4.  nose from http://pypi.python.org/pypi/nose/
  5.  virtualenv from http://pypi.python.org/pypi/virtualenv
  6.  lpthw.web ...this is just a fork of web.py made by the author of Learn Python the Hard Way
  7.  Use ....[Environment]::SetEnvironmentVariable("Path","$env:Path;C:\Python27\Scripts", "User") 


If running through Terminal (MAC) execute by entering the following commands after download of skeleton
  1. export PYTHONPATH=$PYTHONPATH:.
  2. python bin/apple.py
then opening web browser (Safari) and navagating to  http://localhost:8080/

If running in PowerShell or Cmd (PC) execute by entering the following commands after downlaod of skeleton
  1. $env:PYTHONPATH = "$env:PYTHONPATH;." (works on Powershell) or set PYTHONPATH=%PYTHONPAT%;C:\location of dir (works on Cmd)
  2. python bin/apple.py
then opening web browser (Chrome) and navagating to  http://localhost:8080/

user data are saved to test.txt in main/setup to run one participant at a time with no ID
test.txt will not close if user does not complete program and may cause subsiquent errors following first run

ctrl-c is used to terminate program

test folder is for running nosetests...
