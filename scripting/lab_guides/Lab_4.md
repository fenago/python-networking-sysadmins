<img align="right" src="./logo.png">

Lab 4. Automating Regular Administrative Activities
----------------------------------------------------------------



In this lab, we will cover the following topics:


-   Accepting input by redirection, pipe, and input files
-   Handling passwords at runtime in scripts
-   Executing external commands and getting their output
-   Prompting for a password during runtime and validation
-   Reading configuration files
-   Adding logging and warning code to scripts
-   Putting limits on CPU and memory usage
-   Launching a web browser
-   Using the `os` module for handling directory and files
-   Making backups (with `rsync`)



Accepting input by redirection, pipe, and input files
-----------------------------------------------------------------------


For accepting input by redirection, we use
`stdin`. `pipe` is another form of redirection. This concept means providing the output of one program as the input to another
program. We can accept input by external files as well as by using
Python.



### Input by redirection



`stdin` and `stdout` are objects created by the `os` module. We\'re going to write
a script in which we will use
`stdin` and `stdout`.

Create a script called `redirection.py` and write the
following code in it:


```
import sys

class Redirection(object):
    def __init__(self, in_obj, out_obj):
        self.input = in_obj
        self.output = out_obj
    def read_line(self):
        res = self.input.readline()
        self.output.write(res)
        return res

if __name__ == '__main__':
    if not sys.stdin.isatty():
        sys.stdin = Redirection(in_obj=sys.stdin, out_obj=sys.stdout)

    a = input('Enter a string: ')
    b = input('Enter another string: ')
    print ('Entered strings are: ', repr(a), 'and', repr(b))
```

Run the preceding program as follows:


```
$ python3 redirection.py
```

We will receive the following output:


```
Output:
Enter a string: hello
Enter another string: python
Entered strings are:  'hello' and 'python'
```

Whenever the program runs in an interactive session, `stdin`
is the keyboard input and `stdout` is the user\'s Terminal.
The `input()` function is used to take input from the user, and `print()` is the
way to write on the Terminal
(`stdout`).

 


### Input by pipe



Pipe is another form of redirection. This technique is used to pass information from one program to another. The `|` symbol denotes pipe. By using
the pipe technique, we can use more than two commands in such a way that
the output of one command acts as input to the next command.

Now, we are going to see how we can accept an input using pipe. For
that, first we\'ll write a simple script that returns a
`floor` division. Create a script called
`accept_by_pipe.py` and write the following code in it:


```
import sys

for n in sys.stdin:
    print ( int(n.strip())//2 )
```

Run the script and you will get the following output:


```
$ echo 15 | python3 accept_by_pipe.py
Output:
7
```

In the preceding script, `stdin` is a keyboard input. We are
performing a `floor` division on the number we enter at
runtime. The floor division returns only the integer part of the
quotient. When we run the program, we pass `15` followed by
the pipe `|` symbol, and then our script name. So, we are
providing `15` as input to our script. So the floor division
is performed and we get the output as `7`.

We can pass multiple input to our script. So, in the following
execution, we have passed multiple input values as `15`,
`45`, and `20.` For handling multiple input values,
we have written a `for` loop in our script. So, it will first
take the input as `15`, followed by `45`, and then
`20.` The output will be printed on a new line for each input,
as we have written `\n` between the input value. To enable
this interpretation of a backslash, we passed the `-e` flag:


```
$ echo -e '15\n45\n20' | python3 accept_by_pipe.py
Output:
7
22
10
```

After running this, we got floor divisions
for `15`, `45` and `20` as `7`,
`22`, and `10`, respectively, on new lines.



### Input by input file



In this section, we are going to learn about
how we can take input from an input file.
Taking  input from an input file is easier in Python. We are going to
look at an example for this. But first, we are going to create a simple
text file called `sample.txt` and we\'ll write the following
code in it:

`Sample.txt`:


```
Hello World
Hello Python
```

Now, create a script called `accept_by_input_file.py` and
write the following code in it:


```
i = open('sample.txt','r')
o = open('sample_output.txt','w')

a = i.read()
o.write(a)
```

Run the program and you will get the following output:


```
$ python3 accept_by_input_file.py
$ cat sample_output.txt
Hello World
Hello Python
```


Handling passwords at runtime in scripts
----------------------------------------------------------



In this section, we will look at a simple example for handling passwords in script. We will
create a script
called `handling_password.py` and write the following content
in it:


```
import sys
import paramiko
import time

ip_address = "192.168.2.106"
username = "student"
password = "training"
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.load_system_host_keys()
ssh_client.connect(hostname=ip_address,\
                                    username=username, password=password)
print ("Successful connection", ip_address)
ssh_client.invoke_shell()
remote_connection = ssh_client.exec_command('cd Desktop; mkdir work\n')
remote_connection = ssh_client.exec_command('mkdir test_folder\n')
#print( remote_connection.read() )
ssh_client.close
```

Run the preceding script and you will receive the following output:


```
$ python3 handling_password.py

Output:
Successful connection 192.168.2.106
```

In the preceding script, we used the `paramiko` module.
The `paramiko` module is a Python implementation of
`ssh` that provides client-server functionality.

Install `paramiko` as follows:


```
pip3 install paramiko
```

In the preceding script, we are remotely
connecting to the host, `192.168.2.106`. We have
provided the host\'s username and password in
our script.

After running this script, on the `192.168.2.106` desktop, you
will find a `work` folder and `test_folder` can be
found in the `home/` directory of `192.168.2.106`.



Executing external commands and getting their output
----------------------------------------------------------------------



In this section, we are going to learn about
Python\'s subprocess module. Using `subprocess`, it\'s easy to
spawn new processes and get their return
code, execute external commands, and start new applications.

We are going to see how we can execute external commands and get their
output in Python by using the `subprocess` module. We will
create a script called `execute_external_commands.py` and
write the following code in it:


```
import subprocess
subprocess.call(["touch", "sample.txt"])
subprocess.call(["ls"])
print("Sample file created")
subprocess.call(["rm", "sample.txt"])
```


```
subprocess.call(["ls"])
print("Sample file deleted")
```

Run the program and you will get the following output:


```
$ python3 execute_external_commands.py
Output:
1.py     accept_by_pipe.py      sample_output.txt       sample.txt
accept_by_input_file.py         execute_external_commands.py         output.txt        sample.py
Sample.txt file created
1.py     accept_by_input_file.py         accept_by_pipe.py execute_external_commands.py  output.txt            sample_output.txt       sample.py
Sample.txt file deleted
```



Capturing output using the subprocess module
--------------------------------------------------------------



In this section, we are going to learn about how we can capture output. We will pass `PIPE` for
the `stdout` argument to capture the output. Write a script
called `capture_output.py` and write
the following code in it:


```
import subprocess
res = subprocess.run(['ls', '-1'], stdout=subprocess.PIPE,)
print('returncode:', res.returncode)
print(' {} bytes in stdout:\n{}'.format(len(res.stdout), res.stdout.decode('utf-8')))
```

Execute the script as follows:


```
student@ubuntu:~$ python3 capture_output.py
```

On execution, we will receive the following output:


```
Output:
returncode: 0
191 bytes in stdout:
1.py
accept_by_input_file.py
accept_by_pipe.py
execute_external_commands.py
getpass_example.py
ouput.txt
output.txt
password_prompt_again.py
sample_output.txt
sample.py
capture_output.py
```

In the preceding script, we imported the subprocess module of Python,
which helps in capturing the output. The subprocess module is used for
creating new processes. It also helps in connecting input/output pipes
and getting return code. `subprocess.run()` will run the
command passed as an argument. `Returncode` will be the exit
status of your child process. In the output, if you get return code as
`0`, it indicates it ran successfully.



Prompting for passwords during runtime and validation
-----------------------------------------------------------------------



In this section, we are going learn about
the `getpass module` to handle passwords at runtime. The `getpass()` module in Python
prompts the user to enter a password without echoing. The
`getpass` module is used to handle the password prompt
whenever programs interact with a user through the Terminal.

We are going to see some examples of how to use the `getpass`
module:


1.  Create a script called `no_prompt.py` and write the
    following code in it:

```
import getpass
try:
            p = getpass.getpass()
except Exception as error:
            print('ERROR', error)
else:
            print('Password entered:', p)
```

In this script, a prompt is not provided for the user. So, by default,
it is set to the `Password` prompt.

Run the script as follows:


```
$ python3 no_prompt.py
Output :
Password:
Password entered: abcd
```

 

 

 

 


2.  We will provide a prompt for entering a password. So, create a
    script callled `with_prompt.py` and write the following
    code in it:

```
import getpass
try:
            p = getpass.getpass("Enter your password: ")
except Exception as error:
            print('ERROR', error)
else:
            print('Password entered:', p)
```

Now, we have written a script that provides a prompt for a password. Run
the program as follows:


```
$ python3 with_prompt.py
Output:
Enter your password:
Password entered: abcd
```

Here, we have provided the `Enter your password` prompt for
the user.

Now, we will write a script where if we enter a wrong password, it will
just print a simple message but it will not prompt again to enter a
correct password.


3.  Write a script called `getpass_example.py` and write the
    following code in it:

```
import getpass
passwd = getpass.getpass(prompt='Enter your password: ')
if passwd.lower() == '#pythonworld':
            print('Welcome!!')
else:
            print('The password entered is incorrect!!')
```

Run the program as follows (here we are entering a correct password,
that is, `#pythonworld`):


```
$ python3 getpass_example.py
Output:
Enter your password:
Welcome!!
```

Now, we will enter a wrong password and will check what message we
receive:


```
$ python3 getpass_example.py
Output:
Enter your password:
The password entered is incorrect!!
```

 

 

 

 

 

 

Here, we have written a script that never asks again to enter a password
if we write a wrong password.

Now, we will write a script that will ask to enter the correct password
again when we provide a wrong password. To get the login name of the
user, `getuser()` is used. The `getuser()` function
will return the system logged-in user. Create a script
called `password_prompt_again.py` and write the following code
in it:


```
import getpass
user_name = getpass.getuser()
print ("User Name : %s" % user_name)
while True:
            passwd = getpass.getpass("Enter your Password : ")
            if passwd == '#pythonworld':
                        print ("Welcome!!!")
                        break
            else:
                        print ("The password you entered is incorrect.")
```

Run the program and you will get the
following output:


```
student@ubuntu:~$ python3 password_prompt_again.py
User Name : student
Enter your Password :
The password you entered is incorrect.
Enter your Password :
Welcome!!!
```



Reading configuration files
---------------------------------------------



In this section, we are going learn about
the `configparser` module of Python. By using
the `configparser` module, you can manage user-editable
configuration files for the application.

The common use of these configuration files is that users or system
administrators can edit the files using a simple text editor to set
application defaults and then the application will read and, parse them
and act based on the contents written in them.

To read a configuration file, `configparser` has
the `read()` method. Now, we will write a simple script named
`read_config_file.py`. Before that, create a `.ini`
file named `read_simple.ini` and write the following content
in it: `read_simple.ini`


```
[bug_tracker]
url =https://www.nbcnews.com/
```

Create `read_config_file.py` and enter the following content
in it:


```
from configparser import ConfigParser
p = ConfigParser()
p.read('read_simple.ini')
print(p.get('bug_tracker', 'url'))
```

Run `read_config_file.py` and you will get the following
output:


```
$ python3 read_config_file.py

Output:
https://www.nbcnews.com/
```

The `read()` method accepts more than one filename. Whenever
each filename gets scanned and if that file exists, then it will be
opened and read. Now, we will write a script for reading more than one
filename. Create a script called `read_many_config_file.py`
and write the following code in it:


```
from configparser import ConfigParser
import glob

p = ConfigParser()
files = ['hello.ini', 'bye.ini', 'read_simple.ini', 'welcome.ini']
files_found = p.read(files)
files_missing = set(files) - set(files_found)
print('Files found:  ', sorted(files_found))
print('Files missing:  ', sorted(files_missing))
```

Run the preceding script and you will get the following output:


```
$ python3 read_many_config_file.py

Output
Files found:   ['read_simple.ini']
Files missing:   ['bye.ini', 'hello.ini', 'welcome.ini']
```

In the preceding example, we used the `configparser` module of
Python, which helps in managing configuration files. First, we created a
list named `files`. The `read()` function will read
the configuration files. In the example, we created a variable
called  `files_found`, which will store the names of the
configuration files present in your directory. Next, we created
another variable
called `files_missing`, which will return filenames that
aren\'t in your directory. And, lastly, we are printing the file names
that are present and missing.



Adding logging and warning code to scripts
------------------------------------------------------------



In this section, we will learn about the
logging and warnings modules of Python. The
logging module will keep a track of events occurring within a program.
The warnings module warns the programmers about the changes made in the
language as well as the libraries.

Now, we are going to see a simple logging example. We will write a
script called `logging_example.py` and write the following
code in it:


```
import logging
LOG_FILENAME = 'log.txt'
logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG,)
logging.debug('This message should go to the log file')
with open(LOG_FILENAME, 'rt') as f:
            prg = f.read()
print('FILE:')
print(prg)
```

Run the program as follows::


```
$ python3 logging_example.py

Output:
FILE:
DEBUG:root: This message should go to the log file
```

Check `hello.py` and you see the debug message printed in that
script:


```
$ cat log.txt

Output:
DEBUG:root: This message should go to the log file
```

Now, we will write a script called `logging_warnings_codes.py`
and write the following code in it:


```
import logging
import warnings
logging.basicConfig(level=logging.INFO,)
warnings.warn('This warning is not sent to the logs')
logging.captureWarnings(True)
warnings.warn('This warning is sent to the logs')
```

Run the script as
follows:


```
$ python3 logging_warnings_codes.py

Output:
logging_warnings_codes.py:6: UserWarning: This warning is not sent to the logs
    warnings.warn('This warning is not sent to the logs')
WARNING:py.warnings:logging_warnings_codes.py:10: UserWarning: This warning is sent to the logs
    warnings.warn('This warning is sent to the logs')
```


### Generating warnings



`warn()` is used to generate the
warnings. Now, we will see a simple example of generating warnings.
Write a script called `generate_warnings.py` and write a
following code in it:


```
import warnings
warnings.simplefilter('error', UserWarning)
print('Before')
warnings.warn('Write your warning message here')
print('After')
```

Run the script as follows:


```
$ python3 generate_warnings.py

Output:
Before:
Traceback (most recent call last):
  File "generate_warnings.py", line 6, in <module>
    warnings.warn('Write your warning message here')
UserWarning: Write your warning message here
```

In the preceding script, we passed a warning message through
`warn()`. We used a simple filter so that your warning will
get treated as an error and that error will get solved accordingly by
the programmer.



Putting limits on CPU and memory usage
--------------------------------------------------------



In this section, we will learn about how we
can limit CPU and memory usage. First, we
will write a script for putting a limit on CPU usage. Create a script
called `put_cpu_limit.py` and write the following code in it:


```
import resource
import sys
import signal
import time
def time_expired(n, stack):
            print('EXPIRED :', time.ctime())
            raise SystemExit('(time ran out)')
signal.signal(signal.SIGXCPU, time_expired)
# Adjust the CPU time limit
soft, hard = resource.getrlimit(resource.RLIMIT_CPU)
print('Soft limit starts as  :', soft)
resource.setrlimit(resource.RLIMIT_CPU, (10, hard))
soft, hard = resource.getrlimit(resource.RLIMIT_CPU)
print('Soft limit changed to :', soft)
print()
# Consume some CPU time in a pointless exercise
print('Starting:', time.ctime())
for i in range(200000):
            for i in range(200000):
                        v = i * i
# We should never make it this far
print('Exiting :', time.ctime())
```

Run the preceding script as follows:


```
$ python3 put_cpu_limit.py

Output:
Soft limit starts as  : -1
Soft limit changed to : 10
Starting: Thu Sep  6 16:13:20 2018
EXPIRED : Thu Sep  6 16:13:31 2018
(time ran out)
```

In the preceding script, we used
`setrlimit()` to limit the CPU usage. So, in our script, we
have set the limit to 10 seconds.



Launching webbrowser
--------------------------------------



In this section, we will learn about
the `webbrowser` module of Python. This module has functions
to open URLs in browser applications. We will see a simple example.
Create a script called `open_web.py` and write the following
code in it:


```
import webbrowser
webbrowser.open('https://www.nbcnews.com/')
```

Run the script as follows:


```
$ python3 open_web.py

Output:
Url mentioned in open() will be opened in your browser.
webbrowser – Command line interface
```

You can also use the `webbrowser` module of Python through the
command line and can use all of it. To use `webbrowser`
through the command line, run the following command:


```
$ python3 -m webbrowser -n https://www.google.com/
```

Here, <https://www.google.com/> will be opened in the browser window.
You can use the following two options:


-   `-n`: Open a new window
-   `-t`: Open a new tab


Using the os module for handling directory and files
----------------------------------------------------------------------



In this section, we will learn about
the `os` module of Python. Python\'s `os` module
helps in achieving operating system tasks. We
need to import the `os` module if we want to perform
operating system tasks.

We will look at some examples related to handlingfiles and directories.

 



### Creating and deleting the directory



In this section, we are going to create a
script where we will see what functions we
can use for working with the directories on
your filesystem, which will include creating,
listing, and removing the content. Create a script
called  `os_dir_example.py` and write the following code in
it:


```
import os
directory_name = 'abcd'
print('Creating', directory_name)
os.makedirs(directory_name)
file_name = os.path.join(directory_name, 'sample_example.txt')
print('Creating', file_name)
with open(file_name, 'wt') as f:
            f.write('sample example file')
print('Cleaning up')
os.unlink(file_name)
os.rmdir(directory_name)       # Will delete the directory
```

Run the script as follows:


```
$ python3 os_dir_example.py

Output:
Creating abcd
Creating abcd/sample_example.txt
Cleaning up
```

When you create a directory using `mkdir()`, all of the parent
directories must be already created. But, when you create a directory
with `makedirs()` , it will create any directory, which is
mentioned in a path that doesn\'t exist. `unlink()` will
remove the file path and `rmdir()` will remove the directory
path.


### Examining the content of a filesystem



In this section, we will list all of the content of a directory using `listdir()`. Create a script
called `list_dir.py` and write the following code in it:


```
import os
import sys
print(sorted(os.listdir(sys.argv[1])))
```

 

Run the script as follows:


```
$ python3 list_dir.py /home/student/

['.ICEauthority', '.bash_history', '.bash_logout', '.bashrc', '.cache', '.config', '.gnupg', '.local', '.mozilla', '.pam_environment', '.profile', '.python_history', '.ssh', '.sudo_as_admin_successful', '.viminfo', '1.sh', '1.sh.x', '1.sh.x.c', 'Desktop', 'Documents', 'Downloads', 'Music', 'Pictures', 'Public', 'Templates', 'Videos', 'examples.desktop', 'execute_external_commands.py', 'log.txt', 'numbers.txt', 'python_learning', 'work']
```

So, by using `listdir()`, you can list of all the content of
the folder.



Making backups (with rsync)
---------------------------------------------



This is the most important work system
administrators have to do. In this section,
we will learn about making backups using `rsync`.
The `rsync` command is used for copying files and directories
locally, as well as remotely, and performing data backups using
`rsync.` For that, we are going write a script
called `take_backup.py` and write the following code in it:


```
import os
import shutil
import time
from sh import rsync
def check_dir(os_dir):
            if not os.path.exists(os_dir):
                        print (os_dir, "does not exist.")
                        exit(1)
def ask_for_confirm():
            ans = input("Do you want to Continue? yes/no\n")
            global con_exit
            if ans == 'yes':
                        con_exit = 0
                        return con_exit
            elif ans == "no":
                        con_exit = 1
                        return con_exit
            else:1
                        print ("Answer with yes or no.")
                        ask_for_confirm()
def delete_files(ending):
            for r, d, f in os.walk(backup_dir):
                        for files in f:
                                    if files.endswith("." + ending):
                                                os.remove(os.path.join(r, files))

backup_dir = input("Enter directory to backup\n")   # Enter directory name
check_dir(backup_dir)
print (backup_dir, "saved.")
time.sleep(3)
backup_to_dir= input("Where to backup?\n")
check_dir(backup_to_dir)
print ("Doing the backup now!")
ask_for_confirm()
if con_exit == 1:
            print ("Aborting the backup process!")
            exit(1)
rsync("-auhv", "--delete", "--exclude=lost+found", "--exclude=/sys", "--exclude=/tmp", "--exclude=/proc",
"--exclude=/mnt", "--exclude=/dev", "--exclude=/backup", backup_dir, backup_to_dir)
```

Run the script as follows:


```
student@ubuntu:~/work$ python3 take_backup.py

Output :
Enter directory to backup
/home/student/work
/home/student/work saved.
Where to backup?
/home/student/Desktop
Doing the backup now!
Do you want to Continue? yes/no
yes
```

Now, check `Desktop/directory` and you will see
your work folder in that directory. There are
a few options used with the `rsync` command, namely the
following:


-   `-a`: Archive
-   `-u`: Update
-   `-h`: Human-readable format
-   `-v`: Verbose
-   `--delete`: Deletes extraneous files from the receiving
    side
-   `--exclude`: Exclude rule



Summary
-------------------------



In this lab, we learned about how we can automate regular
administration tasks. We learned about accepting input by various
techniques, prompting for passwords at runtime, executing external
commands, reading configuration files, adding warnings in your script,
launching `webbrowser` through the script as well as the
command line, using the `os` module to handle files and
directories, and making backups.

In the next lab, you will learn more about the `os` module
and handling data. Also, you will learn about the `tarfile`
module and how you can use it.



Questions
---------------------------




1.  How to use `readline` module?
2.  What are the Linux commands used for reading, creating the new file,
    deletion of the file, list the file in current directory?
3.  To run the Linux/windows commands in python which packages are
    available?
4.  How to read, or set new values in configuration `ini` file
5.  List the libraries available for finding the `cpu` usage?
6.  List the different methods to accept the input from the user?
7.  What is the difference between sort and sorted?
