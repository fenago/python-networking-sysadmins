<img align="right" src="./logo.png">

Lab 5. Handling Files, Directories, and Data
---------------------------------------------------------



In this lab, you will learn about the following:


-   Using the `os` module to work with directories
-   Copying, moving, renaming, and deleting data
-   Working with paths, directories, and files
-   Comparing data
-   Merging data
-   Pattern matching files and directories
-   Metadata: data about data
-   Compressing and restoring
-   Using a `tarfile` module to create TAR archives
-   Using a `tarfile` module to examine the contents of TAR
    files



Using the os module to work with directories
--------------------------------------------------------------


**Get the working directory**

To start working with directories, first, we will get the name of our current working
directory. The `os` module has
a `getcwd()` function, using which we can get the current
working directory. Start the `python3` console and enter the
following commands to get the directory name:


```
$ python3
Python 3.6.5 (default, Apr  1 2018, 05:46:30) 
[GCC 7.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import os
>>> os.getcwd()
'/home/jovyan'
>> 
```


**Changing the directory**


Using the `os` module, we can change the current working directory.
For that, the `os` module has the
`chdir()` function, for example:


```
>>> os.chdir('/home/jovyan/work')
>>> print(os.getcwd())
/home/jovyan/work
>>> 
```


**Listing files and directories**


Listing the directory contents is easy in
Python. We are going to use the `os` module that has a
function named `listdir()`, which will return the names of
files and directories from your working
directory:


```
>>> os.listdir()
['Public', 'python_learning', '.ICEauthority', '.python_history', 'work', '.bashrc', 'Pictures', '.gnupg', '.cache', '.bash_logout', '.sudo_as_admin_successful', '.bash_history', '.config', '.viminfo', 'Desktop', 'Documents', 'examples.desktop', 'Videos', '.ssh', 'Templates', '.profile', 'dir', '.pam_environment', 'Downloads', '.local', '.dbus', 'Music', '.mozilla']
>>> 
```


**Renaming a directory**



The `os` module in Python has a `rename()` function
that helps in changing the name of the
directory:


```
>>> os.rename('work', 'work1')
>>> os.listdir()
['Public', 'work1', 'python_learning', '.ICEauthority', '.python_history', '.bashrc', 'Pictures', '.gnupg', '.cache', '.bash_logout', '.sudo_as_admin_successful', '.bash_history', '.config', '.viminfo', 'Desktop', 'Documents', 'examples.desktop', 'Videos', '.ssh', 'Templates', '.profile', 'dir', '.pam_environment', 'Downloads', '.local', '.dbus', 'Music', '.mozilla']
>> 
```



Copying, moving, renaming, and deleting data
--------------------------------------------------------------



**Copying the data**



In this section, we will see how we can copy
files using the `shutil` module. For that, first, we will
create a `hello.py` file and write some text in it.

`hello.py`:


```
print ("")
print ("Hello World\n")
print ("Hello Python\n")
```

 


Now, we will write the code for copying into the
`shutil_copy_example.py` script. Write the following content
in it:


```
import shutil
import os
shutil.copy('hello.py', 'welcome.py')
print("Copy Successful")
```

Run the script as follows:


```
$ python3 shutil_copy_example.py

Output:
Copy Successful
```

Check the presence of the `welcome.py` script and you will
find the contents of `hello.py` are copied successfully in
`welcome.py`.


**Moving the data**



Here, we will see how we can move the data.
We will use `shutil.move()` for this
purpose. `shutil.move(source, destination)` will move the file
from source to destination. Now, we will create
a `shutil_move_example.py` script and write the following
content in it:


```
import shutil
shutil.move('/home/jovyan/work/python-networking-sysadmins/sample.txt', '/home/jovyan/Desktop/.')
```

Run the script as follows:


```
$ python3 shutil_move_example.py
```




### Renaming data



In the previous section, we learned how we
can use `shutil.move()` to move files from source to
destination. Using `shutil.move()`, files can be renamed.
Create a `shutil_rename_example.py` script and write the
following content in it:


```
import shutil
shutil.move('hello.py', 'hello_renamed.py')
```

Run the script as follows:


```
$ python3 shutil_rename_example.py
```

Output:

Now, check that your filename will be
renamed `hello_renamed.py`.


### Deleting data


Now, create a `os_remove_file_directory.py` script and write
the following content in it:


```
import os
os.remove('sample.txt')
print("File removed successfully")
os.rmdir('work1')
print("Directory removed successfully")
```

Run the script as follows:


```
$ python3 os_remove_file_directory.py

Output:
File removed successfully
Directory removed successfully
```



Working with paths
------------------------------------



Now, we are going to learn about `os.path()`. It is used for
path manipulations. In this section, we will look at some of the functions that the `os` module offers for
pathnames.

Start the `python3` console:


```
student@ubuntu:~$ python3
Python 3.6.6 (default, Sep 12 2018, 18:26:19)
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>
```



```
>>> import os
>>> os.path.abspath('sample.txt')
'/home/jovyan/work/python-networking-sysadmins/sample.txt'
```


```
>>> os.path.dirname('/home/jovyan/work/python-networking-sysadmins/sample.txt')
'/home/jovyan/work'
```


```
>>> os.path.basename('/home/jovyan/work/python-networking-sysadmins/sample.txt')
'sample.txt'
```



```
>>> os.path.exists('/home/jovyan/work/python-networking-sysadmins/sample.txt')
True
```


```
>>> os.path.getsize('/home/jovyan/work/python-networking-sysadmins/sample.txt')
39
```




```
>>> os.path.isfile('/home/jovyan/work/python-networking-sysadmins/sample.txt')
True
```




```
>>> os.path.isdir('/home/jovyan/work/python-networking-sysadmins/sample.txt')
False
```


Comparing data
--------------------------------


We will study an example of comparing data using pandas. Initially, we
will create two `csv` files: `student1.csv` and
`student2.csv`. We will compare the data of these two
`csv` files and in output it should return the comparison.
Create two `csv` files as follows:

Create the `student1.csv` file content as follows:


```
Id,Name,Gender,Age,Address
101,John,Male,20,New York
102,Mary,Female,18,London
103,Aditya,Male,22,Mumbai
104,Leo,Male,22,Chicago
105,Sam,Male,21,Paris
106,Tina,Female,23,Sydney
```

Create the `student2.csv` file content as follows:


```
Id,Name,Gender,Age,Address
101,John,Male,21,New York
102,Mary,Female,20,London
103,Aditya,Male,22,Mumbai
104,Leo,Male,23,Chicago
105,Sam,Male,21,Paris
106,Tina,Female,23,Sydney
```

Now, we will create a `compare_data.py` script and write the
following content in it:


```
import pandas as pd
df1 = pd.read_csv("student1.csv")
df2 = pd.read_csv("student2.csv")
s1 = set([ tuple(values) for values in df1.values.tolist()])
s2 = set([ tuple(values) for values in df2.values.tolist()])
s1.symmetric_difference(s2)
print (pd.DataFrame(list(s1.difference(s2))), '\n')
print (pd.DataFrame(list(s2.difference(s1))), '\n')
```

Run the script as follows:


```
$ python3 compare_data.py

Output:
     0     1       2   3         4
0  102  Mary  Female  18    London
1  104   Leo    Male  22   Chicago
2  101  John    Male  20  New York


     0     1       2   3         4
0  101  John    Male  21  New York
1  104   Leo    Male  23   Chicago
2  102  Mary  Female  20    London
```



Exercise: Merging data
----------------------

Now, create a `merge_data_exercise.py` or notebook script and write the code to merge `student1.csv` and `student2.csv`.


Run the script as follows:

```
$ python3 merge_data_exercise.py

```


**Hint:** Use pandas **concat** function to complete the exercise. Solution is present in `merge_data.py`. 


Pattern matching files and directories
--------------------------------------------------------



Now, we will look at an example. First, create a
`pattern_match.py`script and write the following content in
it:


```
import glob
file_match = glob.glob('*.txt')
print(file_match)
file_match = glob.glob('[0-9].txt')
print(file_match)
file_match = glob.glob('**/*.txt', recursive=True)
print(file_match)
file_match = glob.glob('**/', recursive=True)
print(file_match)
```

Run the script as follows:


```
$ python3 pattern_match.py

Output:
['file1.txt', 'filea.txt', 'fileb.txt', 'file2.txt', '2.txt', '1.txt', 'file.txt']
['2.txt', '1.txt']
['file1.txt', 'filea.txt', 'fileb.txt', 'file2.txt', '2.txt', '1.txt', 'file.txt', 'dir1/3.txt', 'dir1/4.txt']
['dir1/']
```



Compressing and restoring
-------------------------------------------



In this section, we are going to learn about the
`make_archive()` function of the `shutil` module,
which will compress an entire directory. For
that, we are going to write a `compress_a_directory.py` script
and write the following content in it:


```
import shutil
shutil.make_archive('work', 'zip', 'work/')
```

Run the script as follows:


```
$ python3 compress_a_directory.py
```


Now, to restore the data from the compressed
file, we are going to use the `unpack_archive()` function from
the `shutil` module. Create
an `unzip_a_directory.py` script and write the following
content in it:


```
import shutil
shutil.unpack_archive('work1.zip')
```

Run the script as follows:


```
$ python3 unzip_a_directory.py
```

Now, check your directory. You will get all the contents after unzipping
the directory.



Using the tarfile module to create TAR archives
-----------------------------------------------------------------


Now, create a `tarfile_example.py` script and write the following content in
it:


```
import tarfile
tar_file = tarfile.open("work.tar.gz", "w:gz")
for name in ["welcome.py", "hello.py", "hello.txt", "sample.txt", "sample1.txt"]:
            tar_file.add(name)
tar_file.close()
```

Run the script as follows:


```
$ python3 tarfile_example.py
```

Now, check your present working directory; you will see
`work.tar.gz` has been created.



Exercise: Using a tarfile module to examine the contents of TAR files
-----------------------------------------------------------------------------


Now, create a `examine_tar_file_content_exercise.py` or notebook script and write the code to examine the contents of TAR files.



Run the script as follows:


```
$ python3 examine_tar_file_content_exercise.py


```


**Hint:** Use tarfile function **getnames** to complete the exercise. Solution is present in `examine_tar_file_content.py`. 


Summary
-------------------------


In this lab, we learned about Python scripts for handling files and
directories. We also learned how to use the `os` module to
work with directories. We learned how to copy, move, rename, and delete
files and directories. We also learned about the pandas module in
Python, which is used in comparing and merging data. We learned about
creating tar files and reading the contents of tar files using
the `tarfile` module. We also did pattern matching while
searching files and directories.

In the next lab, we will learn about `tar` archives and
ZIP creations.



Questions
---------------------------



1.  How to deal with different path regardless of different OS (Windows,
    Llinux)?
2.  What are different arguments available for `print()` in
    python?
3.  What is the use of `dir()` keyword in python?
4.  What is dataframe, series in `pandas` ?
5.  What is list comprehension?
6.  Can we do set comprehension and dictionary comprehension? If yes
    how?
7.  How to print first/last `N` rows using pandas dataframe?
8.  Write a program using list comprehension for printing the odd
    numbers
9.  What is the type of `sys.argv`?
10. a\) set
11. b\) list
12. c\) tuple
13. d\) string


Exercises
---------

1) Concat student1.csv and student2.csv using pandas library.
2) Examine the contents of TAR files using tarfile module

