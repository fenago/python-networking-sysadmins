<img align="right" src="./logo.png">

Lab 12. Remote Monitoring of Hosts Over Telnet and SSH
-------------------------------------------------------------------



In this lab, you will learn how to carry out basic configurations on
a server with Telnet and SSH configured. We will begin by using the
Telnet module, after which we will implement the same configurations
using the preferred method: SSH using different modules in Python. You
will also learn about how `telnetlib`, `subprocess`,
`fabric`, `Netmiko`, and `paramiko`
modules work. For this lab, you must have a basic knowledge of
networking.

In this lab, we will cover the following topics:


-   The `telnetlib()` module
-   The `subprocess.Popen()` module
-   SSH using fabric module
-   SSH using Paramiko library
-   SSH using Netmiko library



The telnetlib() module
-----------------------------------------



In this section, we are going to learn about the Telnet
protocol and then we will do Telnet
operations using the `telnetlib` module over a remote server.

Telnet is a network protocol that allows a user to communicate with
remote servers. It is mostly used by network administrators to remotely
access and manage devices. To access the device, run the Telnet command
with the IP address or hostname of a remote server in your Terminal.

 

Telnet uses TCP on the default port number `23`. To use
Telnet, make sure it is installed on your system. If not, run the
following command to install it:


```
$ sudo apt-get install telnetd
```

To run Telnet using the simple Terminal, you just have to enter the
following command:


```
$ telnet ip_address_of_your_remote_server
```

Python has the `telnetlib` module to perform Telnet functions
through Python scripts. Before telnetting your remote device or router,
make sure they are configured properly and, if not, you can do basic
configuration by using the following command in the router\'s Terminal:


```
configure terminal
enable password 'set_Your_password_to_access_router'
username 'set_username' password 'set_password_for_remote_access'
line vty 0 4 
login local 
transport input all 
interface f0/0 
ip add 'set_ip_address_to_the_router' 'put_subnet_mask'
no shut 
end 
show ip interface brief
```

Now, let\'s see the example of Telnetting a remote device. For that,
create a `telnet_example.py`script and write following content
in it:


```
import telnetlib
import getpass
import sys

HOST_IP = "your host ip address"
host_user = input("Enter your telnet username: ")
password = getpass.getpass()

t = telnetlib.Telnet(HOST_IP)
t.read_until(b"Username:")
t.write(host_user.encode("ascii") + b"\n")
if password:
    t.read_until(b"Password:")
    t.write(password.encode("ascii") + b"\n")

t.write(b"enable\n")
t.write(b"enter_remote_device_password\n") #password of your remote device
t.write(b"conf t\n")
t.write(b"int loop 1\n")
t.write(b"ip add 10.1.1.1 255.255.255.255\n")
t.write(b"int loop 2\n")
t.write(b"ip add 20.2.2.2 255.255.255.255\n")
t.write(b"end\n")
t.write(b"exit\n")
print(t.read_all().decode("ascii") )
```

Run the script and you will get the output as follows:


```
student@ubuntu:~$ python3 telnet_example.py
Output:
Enter your telnet username: student
Password:


server>enable
Password:
server#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
server(config)#int loop 1
server(config-if)#ip add 10.1.1.1 255.255.255.255
server(config-if)#int loop 23
server(config-if)#ip add 20.2.2.2 255.255.255.255
server(config-if)#end
server#exit
```

In the preceding example, we accessed and configured a Cisco router
using the `telnetlib` module. In this script, first, we took
the username and password from the user to initialize the Telnet
connection with a remote device. When the connection was established, we
did further configuration on the remote device. After telnetting, we
will be able to access a remote server or device. But there is one very
important disadvantage of this Telnet protocol, and that is all the
data, including usernames and passwords is sent over a network in a text
manner, which may cause a security risk. Because of that, nowadays
Telnet is rarely used and has been replaced by a very secure
protocol named Secure Shell, known as SSH.



### SSH



SSH is a network protocol and is used to
manage a device or servers through remote access. SSH uses public key
encryption for security purposes. The important difference between
Telnet and SSH is that SSH uses encryption, which means that all data
transmitted over a network is protected from unauthorized real-time
interception.

 

User who accesses a remote server or device must install an SSH client.
Install SSH by running the following command in your Terminal:


```
$ sudo apt install ssh
```

Also, on a remote server where the user wants to communicate, an SSH
server must be installed and running. SSH uses the TCP protocol and
works on port number `22` by default.

You can run the `ssh` command through the Terminal as follows:


```
$ ssh host_name@host_ip_address
```

Now, you will learn to do SSH by using different modules in Python, such
as subprocess, fabric, Netmiko, and Paramiko. Now, we will see those
modules one by one.



The subprocess.Popen() module
------------------------------------------------



The `Popen` class handles the process creation and management.
By using this module, developers can handle less common cases. The child
program execution will be done in a new process. To execute a child
program on Unix/Linux, the class will use the `os.execvp()`
function. To execute a child program in
Windows, the class will use the `CreateProcess()` function.

Now, let\'s see some useful arguments of `subprocess.Popen()`:


```
class subprocess.Popen(args, bufsize=0, executable=None, stdin=None, stdout=None,
                                    stderr=None, preexec_fn=None, close_fds=False, shell=False,
                                    cwd=None, env=None, universal_newlines=False,
              startupinfo=None, creationflags=0)
```

Let\'s look at each argument:


-   `args`:** **It can be a sequence of program
    arguments or a single string. If `args` is a sequence, the
    first item in args is executed. If args is a string, it recommends
    to pass args as a sequence.
-   `shell`: The shell argument is by default set to
    `False` and it specifies whether to use shell for
    execution of the program. If shell is `True`, it
    recommends to pass args as a string. In Linux, if
    `shell=True`, the shell defaults to `/bin/sh`.
    If `args` is a string, the string specifies the command to
    execute through the shell.
-   `bufsize`: If `bufsize` is `0` (by
    default, it is `0`), it means unbuffered and if
    `bufsize` is `1`, it means line buffered. If
    `bufsize` is any other positive value, use a buffer of the
    given size. If `bufsize` is any other negative value, it
    means fully buffered.
-   `executable`: It specifies that the replacement program to
    be executed. 
-   `stdin`, `stdout`, and `stderr`: These
    arguments define the standard input, standard output, and standard
    error respectively. 
-   `preexec_fn`:** **This is set to a callable
    object and will be called just before the child is executed in the
    child process.
-   `close_fds`:** **In Linux, if
    `close_fds` is true, all file descriptors except
    `0`, `1`, and `2` will be closed
    before the child process is executed. In Windows, if
    `close_fds` is `true` then the child process
    will inherit no handles. 
-   `env`:** **If the value is not
    `None`, then mapping will define environment variables for
    new process.
-   `universal_newlines`:** **If the value is
    `True` then `stdout` and `stderr` will
    be opened as text files in newlines mode.
:::

Now, we are going to see an example of `subprocess.Popen()`.
For that, create a `ssh_using_sub.py` script and write the
following content in it:


```
import subprocess
import sys

HOST="your host username@host ip"
COMMAND= "ls"

ssh_obj = subprocess.Popen(["ssh", "%s" % HOST, COMMAND],
 shell=False,
 stdout=subprocess.PIPE,
 stderr=subprocess.PIPE)

result = ssh_obj.stdout.readlines()
if result == []:
 err = ssh_obj.stderr.readlines()
 print(sys.stderr, "ERROR: %s" % err)
else:
 print(result)
```

Run the script and you will get the output as follows:


```
student@ubuntu:~$ python3 ssh_using_sub.py
Output :
student@192.168.0.106's password:
[b'Desktop\n', b'Documents\n', b'Downloads\n', b'examples.desktop\n', b'Music\n', b'Pictures\n', b'Public\n', b'sample.py\n', b'spark\n', b'spark-2.3.1-bin-hadoop2.7\n', b'spark-2.3.1-bin-hadoop2.7.tgz\n', b'ssh\n', b'Templates\n', b'test_folder\n', b'test.txt\n', b'Untitled1.ipynb\n', b'Untitled.ipynb\n', b'Videos\n', b'work\n']
```

In the preceding example, first, we imported the subprocess module, then
we defined the host address where you want to establish the SSH
connection. After that, we gave one simple command that executed over
the remote device. After all this was set up, we put this information in
the `subprocess.Popen()` function. This function executed the
arguments defined inside that function to create a connection with the
remote device. After the SSH connection was established, our defined
command was executed and provided the result. Then we printed the result
of SSH on the Terminal, as shown in the output.



SSH using fabric module
------------------------------------------



Fabric is a Python library as well as a command-line tool[]{#id326167680
.indexterm} for the use of SSH. It is used for system administration and
application deployment over the network. We can also execute shell
commands over SSH.

To use fabric module, first you have to install it using the
following command:


```
$ pip3 install fabric3
```

Now, we will see an example. Create a `fabfile.py`script and
write the following content in it:


```
from fabric.api import *

env.hosts=["host_name@host_ip"]
env.password='your password'

def dir():
    run('mkdir fabric')
    print('Directory named fabric has been created on your host network')

def diskspace():
    run('df')
```

 

 

Run the script and you will get the output as follows:


```
student@ubuntu:~$ fab dir
Output:
[student@192.168.0.106] Executing task 'dir'
[student@192.168.0.106] run: mkdir fabric

Done.
Disconnecting from 192.168.0.106... done.
```

In the preceding example, first, we imported the `fabric.api`
module, then we set the hostname and password to get connected with the
host network. After that, we set different task to perform over SSH.
Therefore, to execute our program instead of the Python3
`fabfile.py`, we used the `fab` utility
(`fab dir`), and after that we stated that the required tasks
should be performed from our `fabfile.py`.  In our case, we
performed the `dir` task, which creates a directory with the
name `'fabric'` on your remote network. You can add your
specific task in your Python file. It can be executed using the
`fab` utility of the fabric module.



SSH using the Paramiko library
-------------------------------------------------



Paramiko is a library that implements the SSHv2 protocol for secure
connections to remote devices. Paramiko is a pure Python interface
around SSH.

Before using Paramiko, make sure you have installed it properly on
your system. If it is not installed, you can
install it by running the following command
in your Terminal:


```
$ sudo pip3 install paramiko
```

Now, we will see an example of using `paramiko`. For this
`paramiko` connection, we are using a Cisco device. Paramiko
supports both password-based and  key-pair based authentication for a
secure connection with the server. In our script, we are using
password-based authentication, which means we check for a password and,
if available, authentication is attempted using plain username/password
authentication. Before we are going to do SSH to your remote device or
multi-layer router, make sure they are configured properly and, if not,
you can do basic configuration by using the following command in a
multi-layer router Terminal:


```
configure t
ip domain-name cciepython.com
crypto key generate rsa
How many bits in the modulus [512]: 1024
interface range f0/0 - 1
switchport mode access
switchport access vlan 1
no shut
int vlan 1
ip add 'set_ip_address_to_the_router' 'put_subnet_mask'
no shut
exit
enable password 'set_Your_password_to_access_router'
username 'set_username' password 'set_password_for_remote_access'
username 'username' privilege 15
line vty 0 4
login local
transport input all
end
```

Now, create a `pmiko.py`script and write the following content
in it:


```
import paramiko
import time

ip_address = "host_ip_address"
usr = "host_username"
pwd = "host_password"

c = paramiko.SSHClient()
c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
c.connect(hostname=ip_address,username=usr,password=pwd)

print("SSH connection is successfully established with ", ip_address)

rc = c.invoke_shell()
for n in range (2,6):
    print("Creating VLAN " + str(n))
    rc.send("vlan database\n")
    rc.send("vlan " + str(n) +  "\n")
    rc.send("exit\n")
    time.sleep(0.5)

time.sleep(1)
output = rc.recv(65535)
print(output)
c.close
```

Run the script and you will get the output as follows:


```
student@ubuntu:~$ python3 pmiko.py
Output:
SSH connection is successfuly established with  192.168.0.70
Creating VLAN 2
Creating VLAN 3
Creating VLAN 4
Creating VLAN 5
```

In the preceding example, first, we imported the `paramiko`
module, then we defined the SSH credentials required to connect the
remote device. After providing credentials, we created an instance
`'c'` of `paramiko.SSHclient()`, which is the
primary client used to establish connections with the remote device and
execute commands or operations. The creation of an `SSHClient`
object allows us to establish remote connections using the
`.connect()` function. Then, we set the policy
`paramiko` connection because, by
default, `paramiko.SSHclient` sets the SSH policy in reject
policy state. That causes the policy to reject any SSH connection
without any validation. In our script, we are neglecting this
possibility of SSH connection drop by using
the `AutoAddPolicy()` function that automatically adds the
server\'s host key without prompting it. We can use this policy for
testing purposes only, but this is not a good option in a production
environment because of security purpose.

When an SSH connection is established, you can[]{#id326166977
.indexterm} do any configuration or operation that you want on
your device. Here, we created a few virtual
LANs on a remote device. After creating VLANs, we just closed the
connection.



SSH using the Netmiko library
------------------------------------------------



In this section, we will learn about Netmiko. The Netmiko library is an
advanced version of Paramiko. It is a `multi_vendor` library
that is based on Paramiko. Netmiko simplifies SSH connection to a
network device and takes particular operation on the device. Before
going doing SSH to your remote device or multi-layer router, make sure
they are configured properly and, if not, you can[]{#id326062929
.indexterm} do basic configuration by command mentioned in the Paramiko
section.

Now, let\'s see an example. Create a `nmiko.py`script and
write the following code in it:


```
from netmiko import ConnectHandler

remote_device={
    'device_type': 'cisco_ios',
    'ip':  'your remote_device ip address',
    'username': 'username',
    'password': 'password',
}

remote_connection = ConnectHandler(**remote_device)
#net_connect.find_prompt()

for n in range (2,6):
      print("Creating VLAN " + str(n))
      commands = ['exit','vlan database','vlan ' + str(n), 'exit']
      output = remote_connection.send_config_set(commands)
      print(output)

command = remote_connection.send_command('show vlan-switch brief')
print(command)
```

Run the script and you will get the output as follows:


```
student@ubuntu:~$ python3 nmiko.py
Output:
Creating VLAN 2
config term
Enter configuration commands, one per line.  End with CNTL/Z.
server(config)#exit
server #vlan database
server (vlan)#vlan 2
VLAN 2 modified:
server (vlan)#exit
APPLY completed.
Exiting....
server #
..
..
..
..
switch#
Creating VLAN 5
config term
Enter configuration commands, one per line.  End with CNTL/Z.
server (config)#exit
server #vlan database
server (vlan)#vlan 5
VLAN 5 modified:
server (vlan)#exit
APPLY completed.
Exiting....
VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Fa0/0, Fa0/1, Fa0/2, Fa0/3, Fa0/4, Fa0/5, Fa0/6, Fa0/7, Fa0/8, Fa0/9, Fa0/10, Fa0/11, Fa0/12, Fa0/13, Fa0/14, Fa0/15
2    VLAN0002                         active   
3    VLAN0003                         active   
4    VLAN0004                         active   
5    VLAN0005                         active   
1002 fddi-default                    active   
1003 token-ring-default         active   
1004 fddinet-default               active   
1005 trnet-default                    active
```

In the preceding example, we use Netmiko library to do SSH, instead of
Paramiko. In this script, first, we imported `ConnectHandler`
from the Netmiko library, which we used to establish an SSH connection
to the remote network devices by passing in the device dictionary. In
our case, that dictionary is `remote_device`. After the
connection is established, we executed configuration commands to create
a number of virtual LANs using the `send_config_set()`
function.

When we use this type (`.send_config_set()`) of function to
pass commands on a remote device, it automatically sets our device in
configuration mode. After sending configuration commands, we also passed
a simple command to get the information about the configured device.



Summary
--------------------------



In this lab, you learned about Telnet and SSH. You also learned the
different Python modules such as telnetlib, subprocess, fabric, Netmiko,
and Paramiko, using which we perform Telnet and SSH. SSH uses the public
key encryption for security purposes and is more secure than Telnet. 

In the next lab, we will use various Python libraries, with which
you can make graphical user interfaces.



Questions
----------------------------




1.  What is client-server architecture?
2.  How do you run operating-specific commands in Python code?
3.  What is the difference between LAN and VLAN?
4.  What will the output of the following code be?

```
   List = [‘a’, ‘b’, ‘c’, ‘d’, ‘e’]
   Print(list [10:])
```


5.  Write a Python program to display a calendar (hint: use
    the `calendar` module).
6.  Write a Python program to count the number of lines in a text file.


Further reading
----------------------------------




-   Paramiko documentation: <https://github.com/paramiko/paramiko> 
-   Fabric documentation: <http://www.fabfile.org/>
