<img align="right" src="./logo.png">

Lab 14. Working with Apache and Other Log Files
------------------------------------------------------------



In this lab, you are going to learn about log files. You will learn
how to parse log files. You will also learn why you need to write
exceptions in your programs. The different ways to parse different files
are also important. You will also learn about `ErrorLog` and
`AccessLog`. Finally, you will learn about how to parse other
log files.

In this lab, you will learn the following:


-   Parsing complex log files
-   The need for exceptions
-   Tricks for parsing different files
-   Error log
-   Access log
-   Parsing other log files


Parsing complex log files
--------------------------------------------

Before moving on to an example of log parsing or changing configurations
in a log file, first we have to understand what we have got in a typical
log file. According to that we have to decide, we will learn how to
manipulate or get the information from it. We can also look for common
terms in the log file so that we can use those common terms to fetch
data.


Let\'s create a `read_apache_log.py`script and write the
following content in it:


```
def read_apache_log(logfile):
            with open(logfile) as f:
                        log_obj = f.read()
                        print(log_obj)

if __name__ == '__main__':
            read_apache_log("access.log")
```

Run the script and you will get the output as follows:


```
student@ubuntu:~$ python3 read_apache_log.py
Output:
64.242.88.10 - - [07/Mar/2004:16:05:49 -0800] "GET /twiki/bin/edit/Main/Double_bounce_sender?topicparent=Main.ConfigurationVariables HTTP/1.1" 401 12846
64.242.88.10 - - [07/Mar/2004:16:06:51 -0800] "GET /twiki/bin/rdiff/TWiki/NewUserTemplate?rev1=1.3&rev2=1.2 HTTP/1.1" 200 4523
64.242.88.10 - - [07/Mar/2004:16:10:02 -0800] "GET /mailman/listinfo/hsdivision HTTP/1.1" 200 6291
64.242.88.10 - - [07/Mar/2004:16:11:58 -0800] "GET /twiki/bin/view/TWiki/WikiSyntax HTTP/1.1" 200 7352
64.242.88.10 - - [07/Mar/2004:16:20:55 -0800] "GET /twiki/bin/view/Main/DCCAndPostFix HTTP/1.1" 200 5253
64.242.88.10 - - [07/Mar/2004:16:23:12 -0800] "GET /twiki/bin/oops/TWiki/AppendixFileSystem?template=oopsmore&param1=1.12&param2=1.12 HTTP/1.1" 200 11382
64.242.88.10 - - [07/Mar/2004:16:24:16 -0800] "GET /twiki/bin/view/Main/PeterThoeny HTTP/1.1" 200 4924
64.242.88.10 - - [07/Mar/2004:16:29:16 -0800] "GET /twiki/bin/edit/Main/Header_checks?topicparent=Main.ConfigurationVariables HTTP/1.1" 401 12851
64.242.88.10 - - [07/Mar/2004:16:30:29 -0800] "GET /twiki/bin/attach/Main/OfficeLocations HTTP/1.1" 401 12851
64.242.88.10 - - [07/Mar/2004:16:31:48 -0800] "GET /twiki/bin/view/TWiki/WebTopicEditTemplate HTTP/1.1" 200 3732
64.242.88.10 - - [07/Mar/2004:16:32:50 -0800] "GET /twiki/bin/view/Main/WebChanges HTTP/1.1" 200 40520
64.242.88.10 - - [07/Mar/2004:16:33:53 -0800] "GET /twiki/bin/edit/Main/Smtpd_etrn_restrictions?topicparent=Main.ConfigurationVariables HTTP/1.1" 401 12851
64.242.88.10 - - [07/Mar/2004:16:35:19 -0800] "GET /mailman/listinfo/business HTTP/1.1" 200 6379
…..
```

In the preceding example, we created
one `read_apache_log`function to read Apache log files. Within
that, we opened a log file and then printed the log entries in it. After
defining the `read_apache_log()` function, we called it in the
main function with the Apache log file\'s name. In our case, the Apache
log file is named `access.log`**.**

After reading log entries in the `access.log` file, now we are
going to parse the IP addresses from the log file. For that, create
a `parse_ip_address.py`script and write the following content
in it:


```
import re
from collections import Counter

r_e = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
with open("access.log") as f:
            print("Reading Apache log file")
            Apache_log = f.read()
            get_ip = re.findall(r_e,Apache_log)
            no_of_ip = Counter(get_ip)
            for k, v in no_of_ip.items():
                        print("Available IP Address in log file " + "=> " + str(k) + " " + "Count "  + "=> " + str(v))
```

Run the script and you will get the output as follows:


```
student@ubuntu:~/work/Lab_15$ python3 parse_ip_address.py


Output:
Reading Apache log file
Available IP Address in log file => 127.0.0.1 Count => 1259
……
```


### Analyzing exceptions



In this section, we are going to understand
analyzing exceptions. Every exception that occurs must be handled. Your
log files should also contain few exceptions. If you are getting similar
types of exceptions a number of times, then your program has some issue
and you should make the necessary changes as soon as possible.

Consider the following example:


```
f = open('logfile', 'r')
print(f.read())
f.close()
```

After running the program, you get the output as follows:


```
Traceback (most recent call last):
  File "sample.py", line 1, in <module>
    f = open('logfile', 'r')
FileNotFoundError: [Errno 2] No such file or directory: 'logfile'
```

In this example, we are trying to read a file that is not present in our
directory and as a result it shows an error. So, from the error we can
analyze what kind of solution we have to provide. To handle such a case,
we can use an exception handling technique. So, let\'s see an example of
handling errors using an exception handling technique.

Consider the following example:


```
try:
    f = open('logfile', 'r')
    print(f.read())
    f.close()
except:
    print("file not found. Please check whether the file is present in your directory or not.")
```

After running the program, you get the output as follows:


```
file not found. Please check whether the file is present in your directory or not.
```


Parsing other log files
------------------------------------------



There are also different log files available
within our system, including Apache log. In our Linux distribution, the
log files are in the `/var/log/` folder within the root
filesystem as shown here:


![](./images/7f26ec0b-2ec6-45f8-9657-7a7db7bcb751.png)


In the preceding screenshot, we can easily see the different types of
log files (for instance, authentication log file `auth.log`,
system log file `syslog`, and dpkg log `dpkg.log`)
available for different operations entries. As we perform operations on
Apache log files, as shown previously, we can also perform the same kind
of operations on local log files. Let\'s see an example for parsing one
of the log files from before. Create
a `simple_log.py`script and write the following content in it:


```
f=open('/var/log/dpkg.log','r')

lines = f.readlines()
for line in lines:
            kern_log = line.split()
            print(kern_log)
f.close()
```

Run the script as follows:


```
student@ubuntu:~$ python3 simple_log.py
```


Like reading the log file, we can also perform various operations
on it, just like we are going to perform some operations now. Now, we
are going to access content in the kernel log file through indexing. It
is possible because of the `split` function, as it splits all
the information in the file as a different iteration. So, let\'s see an
example of such a condition. Create a `simple_log1.py` script
and put the following script in it:


```
f=open('/var/log/dpkg.log','r')

lines = f.readlines()
for line in lines:
            kern_log = line.split()[1:3]
            print(kern_log)
```

Run the script and you will get the following output:


```
student@ubuntu:~$ python3 simple_log1.py
```


Summary
--------------------------



In this lab, you learned about how to work with different types of
log files. You also learned about parsing complex log files and the need
for exceptions while handling these files. The tricks for parsing log
files will help in performing the parsing smoothly. You also learned
about `ErrorLog` and `AccessLog`.

In the next lab, you are going to learn about SOAP and REST
communication.



Questions
----------------------------


1.  What is the difference between runtime and compile time exceptions
    in Python?
2.  What are regular expressions?
3.  Explore the Linux commands `head`, `tail`,
    `cat`, and `awk`.
4.  Write a Python program to append the contents of one file to another
    file.
5.  Write a Python program to read the contents of a file in reverse
    order.
6.  What would be the output of the following expressions?
    a.  `re.search(r'C\Wke', 'C@ke').group()`
    b.  `re.search(r'Co+kie', 'Cooookie').group()`
    c.  `re.match(r'<.*?>', '<h1>TITLE</h1>').group()`
    

