<img align="right" src="./logo.png">

Lab 6. File Archiving, Encrypting, and Decrypting
--------------------------------------------------------------



In this lab, we will cover the following topics:


-   Creating and unpacking archives
-   Tar archives
-   ZIP creation
-   File encryption and decryption



Creating and unpacking archives
-------------------------------------------------



#### Creating archives


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

```

In the preceding example, to create an archive file, we used the
`shutil` and `tarfile` modules of Python. In
`shutil.make_archive()`, we specified
`work_sample`, which will be the name of the archive file and
will be in `gz` format. We\'ve specified our work directory
name in the base directory attribute. Finally, we printed the names of
files that are archived.


### Unpacking archives


Now, create a script called `shutil_unpack_archive.py` and
write the following code in it:


```
import pathlib
import shutil
import sys
import tempfile
with tempfile.TemporaryDirectory() as d:
 shutil.unpack_archive('work_sample.tar.gz', extract_dir='/home/jovyan/work',)
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
work/work1_1.txt
work/work1_2.txt
adding sample.txt
contents:
['work', 'work/work1_1.txt', 'work/work1_2.txt', 'sample.txt']
```


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




Exercise: ZIP creation
-------------------------


Now, create a `make_zip_file_exercise.py` or notebook script and write the code to to create a `zip` file using the `make_archive()` function of the `shutil` module.


Run the script as follows:


```
$ python3 make_zip_file_exercise.py

```


**Hint:** Send second argument 'zip' in shutil.make_archive function to complete the exercise. Solution is present in `make_zip_file.py`. 


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




Exercise: File decryption
---------------------------

Now, create a `file_decrypt_exercises.py` or notebook script and write the code to decrypt the `sample.txt.aes` file to get the
content of the file.


Run the script as follows:


```
student@ubuntu:~/work$ python3 file_decrypt_exercises.py
```


Now, check your current working directory. A file named `sampleout.txt` will be created. That\'s your decrypted file.


**Hint:** Use pyAesCrypt library's **decryptStream** function to complete the exercise. Solution is present in `file_decrypt.py`. 



**Summary**

In this lab, we learned about creating and extracting archived
files. Archiving plays an important role in managing files, directories,
and data. It also stores the files and directories into a single file. 



**Questions**

1.  Can we compress the data using password protected? if yes how ?
2.  What is context manager in python?
3.  What is pickling and unpickling?
4.  What are the different types of functions in python?


**Exercises**

1) Write the code to to create a `zip` file using the `make_archive()` function of the `shutil` module.
2) Write the code to decrypt the `sample.txt.aes` file to get the content of the file.
