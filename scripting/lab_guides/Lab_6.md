<img align="right" src="./logo.png">

Lab 6. File Archiving, Encrypting, and Decrypting
--------------------------------------------------------------



In the previous lab, we learned about handling files, directories,
and data. We also learned about the `tarfile` module. In this
lab, we\'ll learn about file archiving, encryption, and decryption.
Archiving plays an important role in managing files, directories, and
data. But first, what is archiving? Archiving is a process that stores
the files and directories into a single file. Python has the
`tarfile` module for creating such archive files.

In this lab, we will cover the following topics:


-   Creating and unpacking archives
-   Tar archives
-   ZIP creation
-   File encryption and decryption



Creating and unpacking archives
-------------------------------------------------



In this section, we\'re going to learn about
how we can create and unpack archives using
the `shutil` module of Python. The `shutil` module
has the `make_archive()` function, which creates a new archive
file. Using `make_archive()`, we can archive the entire
directory with its contents.

 



### Creating archives



Now, we are going to write a script
called `shutil_make_archive.py` and write the
following content in it:


```
import tarfile
import shutil
import sys

shutil.make_archive(
            'work_sample', 'gztar',
            root_dir='..',
            base_dir='work',
)
print('Archive contents:')
with tarfile.open('work_sample.tar.gz', 'r') as t_file:
  for names in t_file.getnames():
    print(names)
```

Run the program and you\'ll get the following output:


```
$ python3 shutil_make_archive.py
Archive contents:
work
work/bye.py
work/shutil_make_archive.py
work/welcome.py
work/hello.py
```

In the preceding example, to create an archive file, we used the
`shutil` and `tarfile` modules of Python. In
`shutil.make_archive()`, we specified
`work_sample`, which will be the name of the archive file and
will be in `gz` format. We\'ve specified our work directory
name in the base directory attribute. Finally, we printed the names of
files that are archived.


### Unpacking archives



To unpack the archives, the `shutil` module has
the `unpack_archive()` function. Using this function, we can extract the archive files. We passed the
archive filename and the directory where we want to extract the
contents. If no directory name is passed, then it will extract the
contents into your current working directory.

 

Now, create a script called `shutil_unpack_archive.py` and
write the following code in it:


```
import pathlib
import shutil
import sys
import tempfile
with tempfile.TemporaryDirectory() as d:
 shutil.unpack_archive('work_sample.tar.gz', extract_dir='/home/student/work',)
 prefix_len = len(d) + 1
 for extracted in pathlib.Path(d).rglob('*'):
 print(str(extracted)[prefix_len:])
```

Run the script as follows:


```
student@ubuntu:~/work$ python3 shutil_unpack_archive.py
```

Now, check your `work/` directory and you will find the
`work/` folder in it, which will have the extracted files.



Tar archives
------------------------------



In this section, we are going to learn about the `tarfile`
module. We\'ll also learn about testing the
entered filename, assessing whether it\'s a valid archive filename or
not. We\'ll look at how to add a new file into the already archived
file, how we can read metadata using the `tarfile` module, and
how to extract the files from an archive using
the `extractall()` function.

First, we will test whether the entered filename is a valid archive file
or not. To test this, the `tarfile` module has
the `is_tarfile()` function, which returns a Boolean value.

Create a script called `check_archive_file.py` and write the
following content in it:


```
import tarfile

for f_name in ['hello.py', 'work.tar.gz', 'welcome.py', 'nofile.tar', 'sample.tar.xz']:
  try:
    print('{:} {}'.format(f_name, tarfile.is_tarfile(f_name)))
  except IOError as err:
    print('{:} {}'.format(f_name, err))
```

 

 

 

 

 

 

 

 

 

 

Run the script and you will get the following output:


```
student@ubuntu:~/work$ python3 check_archive_file.py
hello.py          False
work.tar.gz      True
welcome.py     False
nofile.tar         [Errno 2] No such file or directory: 'nofile.tar'
sample.tar.xz   True
```

So, `tarfile.is_tarfile()` will check every filename mentioned
in the list. The `hello.py, welcome.py` file are not tar files
so we got a Boolean value, `False`. `work.tar.gz`
and `sample.tar.xz` are tar files, so we got the Boolean
value, `True`. And there is no such file as
`nofile.tar` present in our directory, so we have got an
exception, as we\'ve written it in our script.

Now, we are going to add a new file into our already created archived
file. Create a script called `add_to_archive.py` and write the
following code in it:


```
import shutil
import os
import tarfile
print('creating archive')
shutil.make_archive('work', 'tar', root_dir='..', base_dir='work',)
print('\nArchive contents:')
with tarfile.open('work.tar', 'r') as t_file:
 for names in t_file.getnames():
 print(names)
os.system('touch sample.txt')
print('adding sample.txt')
with tarfile.open('work.tar', mode='a') as t:
 t.add('sample.txt')
print('contents:',)
with tarfile.open('work.tar', mode='r') as t:
 print([m.name for m in t.getmembers()])
```

Run the script and you will get the following output:


```
student@ubuntu:~/work$ python3 add_to_archive.py
Output :
creating archive
Archive contents:
work
work/bye.py
work/shutil_make_archive.py
work/check_archive_file.py
work/welcome.py
work/add_to_archive.py
work/shutil_unpack_archive.py
work/hello.py
adding sample.txt
contents:
['work', 'work/bye.py', 'work/shutil_make_archive.py', 'work/check_archive_file.py', 'work/welcome.py', 'work/add_to_archive.py', 'work/shutil_unpack_archive.py', 'work/hello.py', 'sample.txt']
```

In this example, first we created an archive file using
`shutil.make_archive()` and then we printed the contents of
the archived file. We then created a `sample.txt` file in the
next statement. Now, we want to add that `sample.txt` in the
already created `work.tar`. Here, we used the append
mode, `a`. And next, we are again displaying the contents of
the archived file.

Now, we will learn about how we can read the metadata from an archive
file. The `getmembers()` function will load the metadata of
the files. Create a script called `read_metadata.py` and write
the following content in it:


```
import tarfile
import time
with tarfile.open('work.tar', 'r') as t:
            for file_info in t.getmembers():
                        print(file_info.name)
                        print("Size   :", file_info.size, 'bytes')
                        print("Type   :", file_info.type)
                        print()
```

Run the script and you will get the following
output:


```
student@ubuntu:~/work$ python3 read_metadata.py
Output:
work/bye.py
Size : 30 bytes
Type : b'0' 
work/shutil_make_archive.py
Size : 243 bytes
Type : b'0'
work/check_archive_file.py
Size : 233 bytes
Type : b'0'

work/welcome.py
Size : 48 bytes
Type : b'0'

work/add_to_archive.py
Size : 491 bytes
Type : b'0'

work/shutil_unpack_archive.py
Size : 279 bytes
Type : b'0'
```

Now, we will extract the contents from an archive using
the `extractall()` function. For that, create a script
called `extract_contents.py` and write the following code in
it:


```
import tarfile
import os
os.mkdir('work')
with tarfile.open('work.tar', 'r') as t:
            t.extractall('work')
print(os.listdir('work'))
```

Run the script and you will get the following output:


```
student@ubuntu:~/work$ python3 extract_contents.py
```

Check your current working directory,and you will find the
`work/` directory. Navigate to that directory and you can find
your extracted files.


ZIP creation
------------------------------



In this section, we are going to work with ZIP files. We will learn
about the `zipfile` module of `python`, how to
create ZIP files, how to test whether an entered filename is a valid
`zip` filename or not, reading the metadata, and so on.

First, we will learn how to create a `zip` file using
the `make_archive()` function of the `shutil`
module. Create a script called `make_zip_file.py` and write
the following code in it:


```
import shutil
shutil.make_archive('work', 'zip', 'work')
```

Run the script as follows:


```
student@ubuntu:~$ python3 make_zip_file.py
```

Now check your current working directory and you will see
`work.zip`.

Now, we will test whether the entered filename is a `zip` file
or not. For this purpose, the `zipfile` module has
the `is_zipfile()` function.

Create a script called `check_zip_file.py` and write the
following content in it:


```
import zipfile
for f_name in ['hello.py', 'work.zip', 'welcome.py', 'sample.txt', 'test.zip']:
            try:
                        print('{:}           {}'.format(f_name, zipfile.is_zipfile(f_name)))
            except IOError as err:
                        print('{:}           {}'.format(f_name, err))
```

Run the script as follows:


```
student@ubuntu:~$ python3 check_zip_file.py
Output :
hello.py          False
work.zip         True
welcome.py     False
sample.txt       False
test.zip            True
```

In this example, we have used a `for` loop, where we are
checking the filenames in a list. The `is_zipfile()` function
will check, one by one, the filenames and will give Boolean values as a
result.

Now, we will see how we can read the metadata from an archived ZIP file
using the `zipfile` module of Python. Create a script
called `read_metadata.py` and write the following content in
it:


```
import zipfile

def meta_info(names):
            with zipfile.ZipFile(names) as zf:
                        for info in zf.infolist():
                                    print(info.filename)
                                    if info.create_system == 0:
                                                system = 'Windows'
                                    elif info.create_system == 3:
                                                system = 'Unix'
                                    else:
                                                system = 'UNKNOWN'
                                    print("System         :", system)
                                    print("Zip Version    :", info.create_version)
                                    print("Compressed     :", info.compress_size, 'bytes')
                                    print("Uncompressed   :", info.file_size, 'bytes')
                                    print()

if __name__ == '__main__':
    meta_info('work.zip')
```

Execute the script as follows:


```
student@ubuntu:~$ python3 read_metadata.py
Output:
sample.txt
System         : Unix
Zip Version    : 20
Compressed     : 2 bytes
Uncompressed   : 0 bytes

bye.py
System         : Unix
Zip Version    : 20
Compressed     : 32 bytes
Uncompressed   : 30 bytes

extract_contents.py
System         : Unix
Zip Version    : 20
Compressed     : 95 bytes
Uncompressed   : 132 bytes

shutil_make_archive.py
System         : Unix
Zip Version    : 20
Compressed     : 160 bytes
Uncompressed   : 243 bytes
```

To get the metadata information about the
`zip` file, we used the `infolist()` method of
the `ZipFile` class.



File encryption and decryption
------------------------------------------------



In this section, we will learn about
the `pyAesCrypt` module of Python. `pyAesCrypt` is a
file encryption module that uses
`AES256-CBC` to encrypt/decrypt files and binary streams.

Install `pyAesCrypt` as follows:


```
pip3 install pyAesCrypt
```

Create a script called `file_encrypt.py` and write the
following code in it:


```
import pyAesCrypt

from os import stat, remove
# encryption/decryption buffer size - 64K
bufferSize = 64 * 1024
password = "#Training"
with open("sample.txt", "rb") as fIn:
 with open("sample.txt.aes", "wb") as fOut:
 pyAesCrypt.encryptStream(fIn, fOut, password, bufferSize)
# get encrypted file size
encFileSize = stat("sample.txt.aes").st_size
```

Run the script as follows:


```
student@ubuntu:~/work$ python3 file_encrypt.py
Output :
```

Please check your current working directory. You will find
the `sample.txt.aes` encrypted file in it.

In this example, we\'ve already mentioned the buffer size and password.
Next, we mentioned our filename that will be encrypted. In
`encryptStream`, we mentioned `fIn`, which is our
file to encrypt, and `fOut`, which is our filename after
encryption. We\'ve stored our encrypted file as
`sample.txt.aes`.

Now, we will decrypt the `sample.txt.aes` file to get the
content of the file. Create a script called `file_decrypt.py`
and write the following content in it:


```
import pyAesCrypt
from os import stat, remove
bufferSize = 64 * 1024
password = "#Training"
encFileSize = stat("sample.txt.aes").st_size
with open("sample.txt.aes", "rb") as fIn:
 with open("sampleout.txt", "wb") as fOut:
 try:
 pyAesCrypt.decryptStream(fIn, fOut, password, bufferSize, encFileSize)
 except ValueError:
 remove("sampleout.txt")
```

 

 

 

 

 

 

Run the script as follows:


```
student@ubuntu:~/work$ python3 file_decrypt.py
```

Now, check your current working directory. A file named
`sampleout.txt` will be created. That\'s your decrypted file.

In this example, we mentioned the filename to decrypt, which is
`sample.txt.aes`. Next, our decrypted file will be
`sampleout.txt`. In `decryptStream()`, we mentioned
`fIn`, which is our file to decrypt, and `fOut`,
which is the name of the `decrypted` file.



Summary
-------------------------



In this lab, we learned about creating and extracting archived
files. Archiving plays an important role in managing files, directories,
and data. It also stores the files and directories into a single file. 

We learned in detail about the `tarfile` and
`zipfile` Python modules that enable you to create, extract,
and test archive files. You will be able to add a new file into the
already archived file, read metadata, extract the files from an archive.
You also learned about file encryption and decryption using
the `pyAescrypt` module. 

In the next lab, you will learn about text processing and regular
expressions in python. Python has a very powerful library called regular
expressions that does tasks such as searching and extracting the data.



Questions
---------------------------




1.  Can we compress the data using password protected? if yes how ?
2.  What is context manager in python?
3.  What is pickling and unpickling?
4.  What are the different types of functions in python?



Further reading
---------------------------------




-   Data Compression and
    Archiving: <https://docs.python.org/3/library/archiving.html>
-   `tempfile`
    documentation: <https://docs.python.org/2/library/tempfile.html>
-   Cryptography Python
    documentation: <https://docs.python.org/3/library/crypto.html>
-   `shutil`
    documentation: <https://docs.python.org/3/library/shutil.html>
