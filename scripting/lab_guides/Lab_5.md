<img align="right" src="./logo.png">

Lab 5. Handling Files, Directories, and Data
---------------------------------------------------------



The system administrator performs tasks such as handling various files,
directories, and data. In this lab, we will learn about the
`os` module. The `os` module provides the
functionality to interact with the operating system. Python programmers
can easily use this `os` module for performing file and
directory operations. The `os` module provides tools for
programmers that deal with files, paths, directories, and data.

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
shutil.move('/home/jovyan/sample.txt', '/home/jovyan/Desktop/.')
```

Run the script as follows:


```
$ python3 shutil_move_example.py
```

In this script, our file to move is `sample.txt`, which is in
the `/home/jovyan` directory. `/home/jovyan` is
our source folder and `/home/jovyan/Desktop` is our
destination folder. So, after running the script, `sample.txt`
will be moved from `/home/jovyan` to
the `/home/jovyan/Desktop` directory.

 


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



We will learn how to delete files and folders
using the `os` module in Python.
The `remove()` method of the `os` module will delete
a file. If you try to remove a directory using this method, it will give
you an `OSError`. To remove directories, use
`rmdir()`.

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


-   `os.path.absname(path)`: Returns the absolute version of
    your pathname.

```
>>> import os
>>> os.path.abspath('sample.txt')
'/home/jovyan/work/sample.txt'
```


-   `os.path.dirname(path)`: Returns the directory name of
    your path.

```
>>> os.path.dirname('/home/jovyan/work/sample.txt')
'/home/jovyan/work'
```


-   `os.path.basename(path)`: Returns the base name of your
    path.

```
>>> os.path.basename('/home/jovyan/work/sample.txt')
'sample.txt'
```


-   `os.path.exists(path)`: Returns `True` if path
    refers to the existing path.

```
>>> os.path.exists('/home/jovyan/work/sample.txt')
True
```


-   `os.path.getsize(path)`: Returns the size of the entered
    path in bytes.

```
>>> os.path.getsize('/home/jovyan/work/sample.txt')
39
```


-   `os.path.isfile(path)`: Checks whether the entered path is
    an existing file or not. Returns `True` if it is a file.

```
>>> os.path.isfile('/home/jovyan/work/sample.txt')
True
```


-   `os.path.isdir(path)`: Checks whether the entered path is
    an existing directory or not. Returns `True` if it is a
    directory.

```
>>> os.path.isdir('/home/jovyan/work/sample.txt')
False
```


Comparing data
--------------------------------



Here, we are going to learn about how to
compare data in Python. We will use a `pandas` module for this
purpose.

Pandas is an open source data analysis library that provides data
structures and data analysis tools that are easy to use. It makes
importing and analyzing data easier.

Before starting with the example, make sure you have `pandas`
installed on your system. You can install pandas as follows:


```
pip3 install pandas     --- For Python3

or

pip install pandas       --- For python2
```

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

In the preceding example, we are comparing the data between the two
`csv` files: `student1.csv` and
`student2.csv`. We first converted our dataframes
(`df1`, `df2`) into sets (`s1`,
`s2`). Then, we used the `symmetric_difference()`
set. So, it will check the symmetric difference between `s1`
and `s2` and then we will print the result.


Merging data
------------------------------



We are going to learn about how to merge data
in Python. For that, we are going to use Python\'s pandas library. To
merge the data, we are going to use two `csv` files that
already created in the previous section, `student1.csv` and
`student2.csv`.

Now, create a `merge_data.py` script and write the following
code in it:


```
import pandas as pd
df1 = pd.read_csv("student1.csv")
df2 = pd.read_csv("student2.csv")
result = pd.concat([df1, df2])
print(result)
```

Run the script as follows:


```
$ python3 merge_data.py

Output:
    Id    Name  Gender  Age   Address
0  101    John    Male   20  New York
1  102    Mary  Female   18    London
2  103  Aditya    Male   22    Mumbai
3  104     Leo    Male   22   Chicago
4  105     Sam    Male   21     Paris
5  106    Tina  Female   23    Sydney
0  101    John    Male   21  New York
1  102    Mary  Female   20    London
2  103  Aditya    Male   22    Mumbai
3  104     Leo    Male   23   Chicago
4  105     Sam    Male   21     Paris
5  106    Tina  Female   23    Sydney
```



Pattern matching files and directories
--------------------------------------------------------



In this section, we will learn about pattern
matching for files and directories. Python has the `glob`
module, which is used to find the names of files and directories that
match specific patterns.

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

In the previous example, we used Python\'s `glob` module for
pattern matching. `glob` (pathname) will return the list of
names that matches with the pathname. In out script, we have passed
three pathnames in three different `glob()` functions. In the
first `glob()`, we passed the pathname as
`*.txt;` this will return all the filenames with
`.txt` extensions. In the second `glob()`, we passed
`[0-9].txt`; this will return filenames that start with a
digit. In the third `glob()`, we passed `**/*.txt`,
which will return filenames as well as directory names. It will also
return the filenames from those directories. In the fourth
`glob()`, we passed `**/`, which will return
directory names only.



Metadata: data about data
-------------------------------------------



In this section, we are going learn about the
`pyPdf` module, which helps in extracting the
metadata from a `pdf` file. But
first, what is metadata? Metadata is data about data. Metadata is
structured information that describes primary data. Metadata is a
summary of that data. It contains the basic information regarding your
actual data. It helps in finding a particular instance of your data.


### Note

Make sure you have the `pdf` file present in your directory
from which you want to extract the information.


 

First, we have to install the `pyPdf` module, as follows:


```
pip install pyPdf
```

Now, we will write a `metadata_example.py` script and we will
see how we get the metadata information from it. We are going to write
this script in Python 2:


```
import pyPdf
def main():
            file_name = '/home/jovyan/sample_pdf.pdf'
            pdfFile = pyPdf.PdfFileReader(file(file_name,'rb'))
            pdf_data = pdfFile.getDocumentInfo()
            print ("----Metadata of the file----")
            for md in pdf_data:
                        print (md+ ":" +pdf_data[md])
if __name__ == '__main__':
            main()
```

Run the script as follows:


```
student@ubuntu:~$ python metadata_example.py
----Metadata of the file----
/Producer:Acrobat Distiller Command 3.0 for SunOS 4.1.3 and later (SPARC)
/CreationDate:D:19980930143358
```

In the preceding script, we used the `pyPdf` module of Python
2. First, we created a `file_name` variable that stores the
path of our `pdf`. Using `PdfFileReader()`, data
gets read. The `pdf_data` variable will hold the information
about your `pdf`. Lastly, we wrote a for loop to get the
metadata information.



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

In the preceding script, in `shutil.make_archive()` function,
we passed the first argument as a name to our compressed file.
`zip` will be our compression technique. And the,
`work/` will be the name of the directory that we want to
compress.

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



This section will help you to learn about how
we can create tar archives using Python\'s `tarfile` module.

 The `tarfile` module is used to read and write tar archives
using `gzip`, `bz2` compression techniques. Make
sure the necessary files and directories are present. Now, create a
`tarfile_example.py` script and write the following content in
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



Using a tarfile module to examine the contents of TAR files
-----------------------------------------------------------------------------



In this section, we will learn about how we
can examine the contents of a created tar archive without actually
extracting that tar file. We will do it using Python\'s
`tarfile` module.

Create a `examine_tar_file_content.py` script and write the
following content in it:


```
import tarfile
tar_file = tarfile.open("work.tar.gz", "r:gz")
print(tar_file.getnames())
```

Run the script as follows:


```
$ python3 examine_tar_file_content.py

Output:
['welcome.py', 'hello.py', 'hello.txt', 'sample.txt', 'sample1.txt']
```

In previous example, we used the `tarfile` module to examine
the contents of the created tar file. We used
the `getnames()` function to read the data.



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
