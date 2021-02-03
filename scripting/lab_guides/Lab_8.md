<img align="right" src="./logo.png">

Lab 8. Documentation and Reporting
-----------------------------------------------



In this lab, you will learn how to document and report information
using Python. You will also learn how to take input using Python scripts
and how to print output. Writing scripts for receiving emails is easier
in Python. You will learn how to format information.

In this lab, you will learn about the following:


-    Standard input and output
-    Information formatting
-    Sending emails



Standard input and output
-------------------------

Now, we will see an example of `stdin` and `stdout`.
For that purpose, create a script,`stdin_stdout_example.py`,
and write the following content in it:


```
import sys

print("Enter number1: ")
a = int(sys.stdin.readline())

print("Enter number2: ")
b = int(sys.stdin.readline())

c = a + b
sys.stdout.write("Result: %d " % c)
```

Run the script and you will get the output as follows:


```
student@ubuntu:~/work$ python3 stdin_stdout_example.py
Enter number1:
10
Enter number2:
20
Result: 30
```

**Exercise** Write a program to get name, age and email of a person using sys.stdin.readline().


Now, we will learn about the `input()` and `print()`
functions. The `input()` function is used for taking input
from the user. The function has an optional parameter: prompt string.

Syntax:


```
            input(prompt)
```

The `input()` function returns a string value. If you want a
number value, simply write the \'`int` keyword before
`input()`. You can do this as follows:


```
            int(input(prompt))
```

Similarly, you can write `float` for float values. Now, we
will look at an example. Create a `input_example.py` script
and write the following code in it:


```
str1 = input("Enter a string: ")
print("Entered string is: ", str1)
print()

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = a + b
print("Value of c is: ", c)
print()

num1 = float(input("Enter num 1: "))
num2 = float(input("Enter num 2: "))
num3 = num1/num2
print("Value of num 3 is: ", num3)
```

Run the script and you will get the output as follows:


```
student@ubuntu:~/work$ python3 input_example.py
Output:
Enter a string: Hello
Entered string is:  Hello
Enter the value of a: 10
Enter the value of b: 20
Value of c is:  30
Enter num 1: 10.50
Enter num 2: 2.0
Value of num 3 is:  5.25
```


**Exercise** Write a program to subtract two numbers using input function.


We will look at a simple example for the `print()` function.
Create a `print_example.py` script and write the following
content in it:


```
# printing a simple string on the screen.
print("Hello Python")

# Accessing only a value.
a = 80
print(a)

# printing a string on screen as well as accessing a value.
a = 50
b = 30
c = a/b
print("The value of c is: ", c)
```

Run the script and you will get the output as
follows:


```
student@ubuntu:~/work$ python3 print_example.py
Hello Python
80
The value of c is:  1.6666666666666667
```

In the preceding example, first, we simply printed a string on the
screen. Next, we just accessed the value of
`a` and printed it on the screen. Lastly, we entered the
values of `a` and `b`, then added them and stored
the result in the variable `c`, and then we printed a
statement and accessed a value from the same `print()`
function.



Information formatting
----------------------------------------


Create a `format_example.py`script and write the following
content in it:


```
# Using single formatter
print("{}, My name is John".format("Hi"))
str1 = "This is John. I am learning {} scripting language."
print(str1.format("Python"))

print("Hi, My name is Sara and I am {} years old !!".format(26))

# Using multiple formatters
str2 = "This is Mary {}. I work at {} Resource department. I am {} years old !!"
print(str2.format("Jacobs", "Human", 30))

print("Hello {}, Nice to meet you. I am {}.".format("Emily", "Jennifer"))
```

Run the script as follows:


```
student@ubuntu:~/work$ python3 format_example.py
Output:
Hi, My name is John
This is John. I am learning Python scripting language.
Hi, My name is Sara and I am 26 years old !!
This is Mary Jacobs. I work at Human Resource department. I am 30 years old !!
Hello Emily, Nice to meet you. I am Jennifer.
```

In the preceding example, we did string formatting using the
`format()` method of `string` class using single and
multiple formatters.

Now, we are going to learn about string formatting using the
`%` operator. There are format symbols used with the
`%` operator. Here are some commonly used symbols:


-   `%d`: Decimal integer
-   `%s`: String
-   `%f`: Floating point number
-   `%c`: Character


Now, we will look at an example. Create a
`string_formatting.py`script and write the following content
in it:


```
# Basic formatting
a = 10
b = 30
print("The values of a and b are %d %d" % (a, b))
c = a + b
print("The value of c is %d" % c)

str1 = 'John'
print("My name is %s" % str1)

x = 10.5
y = 33.5
z = x * y
print("The value of z is %f" % z)
print()

# aligning
name = 'Mary'
print("Normal: Hello, I am %s !!" % name)

print("Right aligned: Hello, I am %10s !!" % name)

print("Left aligned: Hello, I am %-10s !!" % name)
print()

# truncating
print("The truncated string is %.4s" % ('Examination'))
print()

# formatting placeholders
students = {'Name' : 'John', 'Address' : 'New York'}
print("Student details: Name:%(Name)s Address:%(Address)s" % students)
```

Run the script and you will get the output as follows:


```
student@ubuntu:~/work$ python3 string_formatting.py
The values of a and b are 10 30
The value of c is 40
My name is John
The value of z is 351.750000
Normal: Hello, I am Mary !!
Right aligned: Hello, I am       Mary !!
Left aligned: Hello, I am Mary       !!
The truncated string is Exam
Student details: Name:John Address:New York
```

In the preceding example, we used the `%` operator to
format strings: `%d` for numbers,
`%s` for strings, and `%f` for float numbers. Then,
we aligned the string to the left and right. We also learned how to
truncate the string using the `%` operator. `%.4s`
will display only the first four characters. Next, we created a
dictionary named `students` and entered `Name` and
`Address` key value pairs. Next, we placed our key names after
the `%` operator to get the strings.



Sending email
-------------------------------


We are going to look at an example. In this example, we will send an
email containing a simple text from Gmail to the recipients.


#### Gmail Credentials:

We will following credentials for sending emails in this lab:

**Username:** pythonmailer12@gmail.com

**Password:** sysadmin1234@

Allow lesssecureapps option has been turned on: https://myaccount.google.com/lesssecureapps 



Create a `send_email.py`script and write the following content
in it:


```
import smtplib
from email.mime.text import MIMEText
import getpass

host_name = 'smtp.gmail.com'
port = 465

u_name = 'username/emailid'
password = getpass.getpass()
sender = 'sender_name'
receivers = ['receiver1_email_address', 'receiver2_email_address']

text = MIMEText('Test mail')
text['Subject'] = 'Test'
text['From'] = sender
text['To'] = ', '.join(receivers)

s_obj = smtplib.SMTP_SSL(host_name, port)
s_obj.login(u_name, password)
s_obj.sendmail(sender, receivers, text.as_string())
s_obj.quit()
print("Mail sent successfully")
```

Run the script as follows:


```
student@ubuntu:~/work$ python3 send_text.py
```

Output:


```
Password:
Mail sent successfully
```


Now, we will look at one more example of sending an email with an
attachment. In this example, we are going to send an image to the
recipient. We are going to send this mail via Gmail. Create a
`send_email_attachment.py`script and write the following
content in it:


```
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import getpass

host_name = 'smtp.gmail.com'
port = 465

u_name = 'username/emailid'
password = getpass.getpass()
sender = 'sender_name'
receivers = ['receiver1_email_address', 'receiver2_email_address']

text = MIMEMultipart()
text['Subject'] = 'Test Attachment'
text['From'] = sender
text['To'] = ', '.join(receivers)

txt = MIMEText('Sending a sample image.')
text.attach(txt)

f_path = '/home/jovyan/work/python-networking-sysadmins/scripting/mountain.jpg'
with open(f_path, 'rb') as f:
    img = MIMEImage(f.read())

img.add_header('Content-Disposition',
               'attachment',
               filename=os.path.basename(f_path))

text.attach(img)

server = smtplib.SMTP_SSL(host_name, port)
server.login(u_name, password)
server.sendmail(sender, receivers, text.as_string())
print("Email with attachment sent successfully !!")
server.quit()
```

 

 

Run the script as follows:


```
student@ubuntu:~/work$ python3 send_email_attachment.py
```

Output:


```
Password:
Email with attachment sent successfully!!
```

In the preceding example, we sent an image as an
attachment to the receivers. We mentioned the
sender\'s and receivers\' email IDs. Next, in the `f_path`, we
mentioned the path of the image that we sent as an attachment. Next, we
sent that image as an attachment to the receiver.


### Note

In these example, we
used `smtp.gmail.com`; for Yahoo! you can use
`smtp.mail.yahoo.com`. So, you can change the hostname as well
as the port, according to your email providers.



Summary
-------------------------



In this lab, we learned about standard input and output. We learned
how `stdin` and `stdout` act as keyboard input and
user\'s Terminal respectively. We also learned about `input()`
and `print()` functions. In addition to this, we learned about
sending an email from Gmail to the receivers. We sent an email with
simple text and also sent an attachment. Also, we learned about string
formatting using the `format()` method and the `%`
operator.

In the next lab, you will learn about how to work with different
files such as PDF, Excel, and `csv.`



Questions
---------------------------


1.  What is the difference between `stdin` and input?
2.  What is SMTP?
3.  What would be the output of the following?

```
>>> name = "Eric"
>>> profession = "comedian"
>>> affiliation = "Monty Python"
>>> age = 25
>>> message = (
...     f"Hi {name}. "
...     f"You are a {profession}. "
...     f"You were in {affiliation}."
... )
>>> message
```


4.  What would be the output of the following?

```
str1 = 'Hello'
str2 ='World!'
print('str1 + str2 = ', str1 + str2)
print('str1 * 3 =', str1 * 3)
```


Exercises
----------

1) Write a program to get name, age and email of a person using sys.stdin.readline().
2) Write a program to subtract two numbers using input function.
