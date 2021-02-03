<img align="right" src="./logo.png">

Lab 9. Working with Various Files
----------------------------------------------


In this lab, you will learn about working with various types of
files, such as PDF files, Excel , CSV , and `txt` files.
Python has modules for performing operations on these files. You will
learn how to open, edit, and get data from these files using Python.

In this lab, the following topics will be covered:


-   Working with PDF files
-   Working with Excel files
-   Working with CSV files
-   Working with `txt` files


Working with PDF files
----------------------------------------



#### Reading a PDF document and getting the number of pages


In this section, we are going read a PDF file
using the `PyPDF2` module. Also, we are going to get the number of pages of that PDF. This module has a
function called  `PdfFileReader()` that helps in reading a PDF
file. Make sure you have a PDF file in your system. Right now, I have
the `test.pdf` file present in my system so I will use this
file throughout this section. Enter your PDF filename in place of
`test.pdf`. Create a script called `read_pdf.py` and
write the following content in it:


```
import PyPDF2

with open('test.pdf', 'rb') as pdf:
    read_pdf= PyPDF2.PdfFileReader(pdf)
    print("Number of pages in pdf : ", read_pdf.numPages)
```

Run the script and you will get the following output:


```
student@ubuntu:~/work$ python3 read_pdf.py
```

Following is the output:


```
Number of pages in pdf :  1

```


#### Extracting text



To extract the pages of the `pdf` file, the `PyPDF2`
module has the `extractText()` method. Create a script
called `extract_text.py` and write the
following content in it:


```
import PyPDF2
with open('test.pdf', 'rb') as pdf:
    read_pdf = PyPDF2.PdfFileReader(pdf)
    pdf_page = read_pdf.getPage(0)
    pdf_content = pdf_page.extractText()
    print(pdf_content)
```

Run the script and you will get the following output:


```
student@ubuntu:~/work$ python3 extract_text.py
```


In the preceding example, we created a file reader object. The
`pdf` reader object has a function
called `getPage()`, which gets the page number (it starts from
the `0th` index) as an argument and returns the page object.
Next, we used the `extractText()` method, which will extract
the text from the page number that we mentioned in
`getPage()`. The page index starts from `0`.


### Rotating PDF pages



In this section, we are going to see how to rotate PDF pages. For that,
we will use the  `rotate.Clockwise()` method of
a `PDF` object. Create a script
called `rotate_pdf.py` and write the following content in it:


```
import PyPDF2

with open('test.pdf', 'rb') as pdf:
    rd_pdf = PyPDF2.PdfFileReader(pdf)
    wr_pdf = PyPDF2.PdfFileWriter()
    for pg_num in range(rd_pdf.numPages):
        pdf_page = rd_pdf.getPage(pg_num)
        pdf_page.rotateClockwise(90)
        wr_pdf.addPage(pdf_page)

    with open('rotated.pdf', 'wb') as pdf_out:
        wr_pdf.write(pdf_out)

print("pdf successfully rotated")
```

Run the script and you will get the following output:


```
student@ubuntu:~/work$ python3 rotate_pdf.py
```

Following is the output:


```
pdf successfully rotated
```


Exercise: Rotating PDF pages
----------------------------------


1) Now, create a `rotate_pdf_exercise.py` or notebook script and write code to rotate pdf pages by rotateClockwise by `180` degree.

Run the script as follows:


```
$ python3 rotate_pdf_exercise.py

```

2) Rotate file by 360 degree and verify that rotated.pdf is same as original file:

**Hint:** Use `rotateClockwise(<degree>)` function to complete the exercise. 


Working with Excel files
------------------------------------------


In this section, we are going to work with
Excel files, which have the `.xlsx` extension. This file
extension is for an open XML spreadsheet file format, which is used by
Microsoft Excel.


#### Reading an Excel file



In this section, we will look at how to read an Excel file. We are going
to use the `xlrd` module. Create a script
called `read_excel.py` and write the following content in it:


```
import xlrd

excel_file = (r"/home/jovyan/sample.xlsx")
course_obj = xlrd.open_workcourse(excel_file)
excel_sheet = course_obj.sheet_by_index(0)
result = excel_sheet.cell_value(0, 1)
print(result)
```

Run the script and you will get the following output:


```
student@ubuntu:~$ python3 read_excel.py
```


In the preceding example, we imported the `xlrd` module to
read the Excel file. We also mentioned the location of the Excel file.
Then, we created a file object, then we mentioned the index value, so
that the reading will start from that index. Finally, we printed the
results.


#### Extracting the names of columns



In this section, we are extracting column names from the Excel sheet.
Create a script called `extract_column_names.py` and write the
following content in it:


```
import xlrd

excel_file = ("/home/jovyan/work/sample.xlsx")
course_obj = xlrd.open_workcourse(excel_file)
excel_sheet = course_obj.sheet_by_index(0)
excel_sheet.cell_value(0, 0)
for i in range(excel_sheet.ncols):
            print(excel_sheet.cell_value(0, i))
```

Run the script and you will get the following output:


```
student@ubuntu:~/work$ python3 extract_column_names.py
```

Following is the output:


```
Id
First Name
Last Name
Gender
Age
Country
```

In the preceding example, we are extracting the column names from the
Excel sheet. We fetched the column names using the `ncols`
attribute.

### Using pandas 



Before proceeding to read Excel files using Pandas, first we have to
install the `pandas` module. We can
install `pandas` using the following command:


```
            pip3 install pandas
```



Now, we will look at some examples using `pandas`.


#### Reading an Excel file


Create a script called  `rd_excel_pandas.py` and write the
following content in it:


```
import pandas as pd

excel_file = 'sample.xlsx'
df = pd.read_excel(excel_file)
print(df.head())
```

Run the preceding script and you will get the following output:


```
student@ubuntu:~/test$ python3 rd_excel_pandas.py
```

Following is the output:


```
   OrderDate     Region  ...   Unit Cost     Total
0  2014-01-09   Central  ...    125.00      250.00
1   6/17/15     Central    ...  125.00      625.00
2  2015-10-09   Central    ...    1.29        9.03
3  11/17/15     Central   ...     4.99       54.89
4  10/31/15     Central   ...     1.29       18.06
```

In the preceding example, we are reading an Excel file using the
`pandas` module. First, we imported the `pandas`
module. Then, we created a string called `excel_file` to hold
the name of the file to be opened, which we want to manipulate using
pandas. Later on, we created a `df data frame` object. In this
example, we used the `read_excel` method of pandas to read
data from the Excel file with default functions. The reading starts with
index zero. Finally, we printed the `pandas` data frame.


#### Reading specific columns in an Excel file



When we use the pandas module to read an Excel file using the `read_excel` method, we can also
read specific columns in that file. For reading specific columns, we
need to use the  `usecols` parameter in the
`read_excel` method.

 

Now, let's look at an example to read specific columns in an Excel file.
Create a script called  `rd_excel_pandas1.py`  and write the
following content in it:


```
import pandas as pd

excel_file = 'sample.xlsx'
cols = [1, 2, 3]
df = pd.read_excel(excel_file , sheet_names='sheet1', usecols=cols)

print(df.head())
```

Run the preceding script and you will get the following output:


```
student@ubuntu:~/test$ python3 rd_excel_pandas1.py
```

Following is the output:


```
    Region      Rep    Item
0  Central    Smith    Desk
1  Central   Kivell    Desk
2  Central     Gill  Pencil
3  Central  Jardine  Binder
4  Central  Andrews  Pencil
```



Now, we will look at some some examples of using `openpyxl`.



#### Creating a new Excel file



In this section, we will learn to create a new Excel file using
`openpyxl`. Create a script
called `create_excel.py` and write the following content in
it:


```
from openpyxl import Workcourse

course_obj = Workcourse()
excel_sheet = course_obj.active
excel_sheet['A1'] = 'Name'
excel_sheet['A2'] = 'student'
excel_sheet['B1'] = 'age'
excel_sheet['B2'] = '24'

course_obj.save("test.xlsx")
print("Excel created successfully")
```

Run the script and you will get the following output:


```
student@ubuntu:~/work$ python3 create_excel.py
```

Following is the output:


```
Excel created successfully
```

Now, check your current working directory and you will find that
`test.xlsx` has been created successfully. In the preceding
example, we write data into four cells. Then, from the
`openpyxl` module, we import the `Workcourse` class. A
workcourse is the container for all other parts of the document. Next, we
set the reference object to the active sheet and write values in the
cells `A1`, `A2` and `B1`, `B2`.
Finally, we\'ve written the contents to the `test.xlsx` file
with the `save()` method.


#### Appending values



In this section, we are going to append values in Excel. For that, we
are going to use the `append()`
method. We can add a group of values at the bottom of the current sheet
in which we want to put the values. Create a script
called `append_values.py` and write the following content in
it:


```
from openpyxl import Workcourse

course_obj = Workcourse()
excel_sheet = course_obj.active
rows = (
    (11, 12, 13),
    (21, 22, 23),
    (31, 32, 33),
    (41, 42, 43)
)
for values in rows:
    excel_sheet.append(values)
    print()

print("values are successfully appended")
course_obj.save('test.xlsx')wb.save('append_values.xlsx')
```

Run the script and you will get the following output:


```
student@ubuntu:~/work$ python3 append_values.py
```

Following is the output:


```
values are successfully appended
```

In the preceding example, we appended three columns of data in the
`append_values.xlsx` files sheet. The data we stored was in a
tuple of tuples and to append that data we went through the container
row by row and inserted it using the `append()` method.


#### Reading multiple cells



In this section, we are going to read
multiple cells. We will use the `openpyxl` module. Create a
script called `read_multiple.py` and write the following
content in it:


```
import openpyxl

course_obj = openpyxl.load_workcourse('sample.xlsx')
excel_sheet = course_obj.active
cells = excel_sheet['A1': 'C6']
for c1, c2, c3 in cells:
            print("{0:6} {1:6} {2:6}".format(c1.value, c2.value, c3.value))
```

Run the script and you will get the following output:


```
student@ubuntu:~/work$ python3 read_multiple.py
```

 

In the preceding example, we are reading the data of three columns by
using the `range` operation. Then, we read the data from the
cells `A1 – C6`.

Similarly, we can perform lots of operations, such as merging and,
splitting cells, on the Excel file using the `openpyxl`
module.



Working with CSV files
----------------------------------------



In this section, we are going to look at `csv.reader` and
`csv.writer`  only.



### Reading a CSV file



Python has an in-built module, `csv`, which we are going to
use here to work with CSV files. We will use
the `csv.reader` module to read a CSV file. Create a script
called `csv_read.py` and write the following content in it:


```
import csv

csv_file = open('test.csv', 'r')
with csv_file:
    read_csv = csv.reader(csv_file)
    for row in read_csv:
        print(row)
```

Run the script and you will get the following output:


```
student@ubuntu:~$ python3 csv_read.py
```


In the preceding program, we opened our `test.csv` file as
`csv_file`. Then, we used the `csv.reader()`
function to extract the data into the `reader` object, which
we can iterate over to get each line of our data. Now, we are going to
look at the second function, `csv.Writer()`


### Writing into a CSV file

To write data in a `csv` file, we use
the `csv.writer` module. In this section, we will store some
data into the Python list and then put that data into
the `csv` file. Create a script
called `csv_write.py` and write the following content in it:


```
import csv

write_csv = [['Name', 'Sport'], ['Andres Iniesta', 'Football'], ['AB de Villiers', 'Cricket'], ['Virat Kohli', 'Cricket'], ['Lionel Messi', 'Football']]

with open('csv_write.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(write_csv)
    print(write_csv)
```

Run the script and you will get the following output:


```
student@ubuntu:~$ python3 csv_write.py
```

Following is the output:


```
[['Name', 'Sport'], ['Andres Iniesta', 'Football'], ['AB de Villiers', 'Cricket'], ['Virat Kohli', 'Cricket'], ['Lionel Messi', 'Football']]
```

In the preceding program, we created a list named `write_csv`
with a `Name` and its `Sport`. Then, after creating
the list, we opened the newly created `csv_write.csv` file and
inserted the `write_csv` list into it using
the `csvWriter()` function.



Working with txt files
----------------------------------------


A plain text file is used to store data that
represents only characters or strings and doesn\'t consider any
structured metadata. In Python, there\'s no need to import any external
library to read and write text files. Python provides an built-in
function to create, open, close, and write and read text files. To do
the operations, there are different access modes to govern the type of
operation possible in an opened file.


### The open() function


This function is used to open a file and does not require any external module to be imported.

The syntax is as follows:


```
            Name_of_file_object = open("Name of file","Access_Mode")
```

For the preceding syntax, the file must be in the same directory that
our Python program resides in. If the file is not in the same directory,
then we also have to define the file path while opening the file. The
syntax for such a condition is shown here:


```
Name_of_file_object = open("/home/……/Name of file","Access_Mode")
```


#### File opening



The `open` function to open the
file is `"test.txt"` .

The file is in the same directory as the `append` mode:


```
text_file = open("test.txt","a")
```

If the file is not in the same directory, we have to define the path in
the `append` mode:


```
text_file = open("/home/…../test.txt","a")
```


### The close() function



This function is used to close the file,
which frees the memory acquired by the file. This function is used when
the file is not needed anymore or it is going to be opened in a
different file mode.

The syntax is as follows:


```
            Name_of_file_object.close()
```

The following code syntax can be use to simply open and close a file:


```
#Opening and closing a file test.txt:
text_file = open("test.txt","a")
text_file.close()
```


### Writing a text file


By using Python, you can create a text file
(`test.txt`). By using the code, writing to a text file is
easy. To open a file for writing, we set the second parameter that is in
access mode to `"w"`. To write the data into this
`test.txt` file, we use the `write()` method of the
`file handle` object. Create a script
called  `text_write.py` and write the following content in it:


```
text_file = open("test.txt", "w")
text_file.write("Monday\nTuesday\nWednesday\nThursday\nFriday\nSaturday\n")
text_file.close()
```

Run the preceding script and you will get the output as follows:


![](./images/b39a0d8e-8927-45a1-9e97-89980aa39ce7.jpg)


Now, check your current working directory. You\'ll find a
`test.txt` file that we created.



Exercise: Reading a text file
----------------------------------

To open a file for reading, we set the second parameter that is the access mode  to `"r"` instead of `"w"`. To read the
data from this file, we use the `read()` method of the `file handle` object.


Now, create a `text_read_exercise.py` or notebook script and write the code to read a text file.


Run the script as follows:


```
$ python3 text_read_exercise.py

```


**Hint:** Use `.read()` instead of `.write()` function to complete the exercise. Solution is present in `text_read_exercise.py`. 


Following is the output:


```
student@ubuntu:~$ python3 text_read.py
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
```



Summary
-------------------------



In this lab, we learned about various files. We learned about PDF,
Excel, CSV, and text files. We used Python modules to perform some
operations on these types of files.

In the next lab, we are going to learn about basic networking and
internet modules in Python.



Questions
---------------------------


1.  What is the difference between `readline()` and
    `readlines()` ?
2.  What is the difference between `open()` and
    `with open()`?
3.  What is the significance of `r c:\\Downloads` at starting?
4.  What is the generators object?
5.  What is the use of `pass`?
6.  What is a lambda expression?


Exercises
----------

1. Write a program to rotate pdf pages by rotateClockwise by `180` and `360` degree.
2. Write a program to read a text file.
