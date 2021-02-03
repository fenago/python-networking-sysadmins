<img align="right" src="./logo.png">

Lab 11. Handling Emails Using Python Scripting
-----------------------------------------------------------



In this lab, you\'ll learn about how to use Python scripts to handle
emails. You\'ll learn about the email message format. We\'re going to
explore the `smtplib` module for sending and receiving emails.
We\'re going to use the Python email package to send emails with
attachments and HTML contents. You\'ll also learn about the different
protocols used to handle emails.

In this lab, you\'ll learn about the following:


-   Email message format
-   Adding HTML and multimedia content
-   POP3 and IMAP servers


#### Gmail Credentials:

We will following credentials for sending emails in this lab:

**Username:** pythonmailer12@gmail.com

**Password:** sysadmin1234@


Email message format
---------------------------------------


In this section, we\'re going to learn about the email message format. Email messages consist of three primary
components:


-   The receiver\'s email address
-   The sender\'s email address
-   The message



Now, we\'re going to see a simple example of sending a plain text email
from your Gmail address, in which you\'ll learn about writing an email
message and sending it. Now, create a script,
`write_email_message.py`, and write the following content in
it:


```
import smtplib
import getpass

host_name = "smtp.gmail.com"
port = 465

sender = 'sender_emil_id'
receiver = 'receiver_email_id'
password = getpass.getpass()

msg = """\
Subject: Test Mail
Hello from Sender !!"""

s = smtplib.SMTP_SSL(host_name, port)
s.login(sender, password)
s.sendmail(sender, receiver, msg)
s.quit()

print("Mail sent successfully")
```

Run the script and you\'ll get the following output:


```
student@ubuntu:~/work/Lab_11$ python3 write_email_message.py
Output:
Password:
Mail sent successfully
```




### Receiving email using the poplib library



**POP3** stands for `Post Office Protocol version 3`. The POP3 protocol works on two ports:

-   Port `110`: The default non-encrypted port
-   Port `995`: The encrypted port


Now, we\'ll see some examples. First, we\'ll see an example where we get
a number of emails. For that, create a script,
`number_of_emails.py`, and write the following content in it:


```
import poplib
import getpass

pop3_server = 'pop.gmail.com'
username = 'Emaild_address'
password = getpass.getpass()

email_obj = poplib.POP3_SSL(pop3_server)
print(email_obj.getwelcome())
email_obj.user(username)
email_obj.pass_(password)
email_stat = email_obj.stat()
print("New arrived e-Mails are : %s (%s bytes)" % email_stat)
```

Run the script, as follows:


```
student@ubuntu:~$ python3 number_of_emails.py
```

As output, you\'ll get however many emails are present in your mailbox.


Now, we\'re going to write a script to get the latest email. For that,
create a script, `latest_email.py`, and write the following
content in it:


```
import poplib
import getpass

pop3_server = 'pop.gmail.com'
username = 'Emaild_address'
password = getpass.getpass()

email_obj = poplib.POP3_SSL(pop3_server)
print(email_obj.getwelcome())
email_obj.user(username)
email_obj.pass_(password)

print("\nLatest Mail\n")
latest_email = email_obj.retr(1)
print(latest_email[1])
```

Run the script, as follows:


```
student@ubuntu:~$ python3 latest_email.py
```

As output, you\'ll get the latest mail you received in your mailbox.

 


Now, we\'re going to write a script to get all of the emails. For that,
create a script, `all_emails.py`, and write the following
content in it:


```
import poplib
import getpass

pop3_server = 'pop.gmail.com'
username = 'Emaild_address'
password = getpass.getpass()

email_obj = poplib.POP3_SSL(pop3_server)
print(email_obj.getwelcome())
email_obj.user(username)
email_obj.pass_(password)

email_stat = email_obj.stat()
NumofMsgs = email_stat[0]
for i in range(NumofMsgs):
    for mail in email_obj.retr(i+1)[1]:
        print(mail)
```

Run the script, as follows:


```
student@ubuntu:~$ python3 latest_email.py
```

As output, you\'ll get all of the emails you\'ve received in your
mailbox.


### Receiving email using the imaplib library


IMAP stands for Internet Message Access Protocol. The IMAP protocol works on two ports:


-   Port `143`: The default non-encrypted port
-   Port `993`: The encrypted port



Now, we\'re going to see an example using the `imaplib`
library. Create a script, `imap_email.py`, and write the
following content in it:


```
import imaplib
import pprint
import getpass

imap_server = 'imap.gmail.com'
username = 'Emaild_address'
password = getpass.getpass()

imap_obj = imaplib.IMAP4_SSL(imap_server)
imap_obj.login(username, password)
imap_obj.select('Inbox')
temp, data_obj = imap_obj.search(None, 'ALL')
for data in data_obj[0].split():
    temp, data_obj = imap_obj.fetch(data, '(RFC822)')
    print('Message: {0}\n'.format(data))
    pprint.pprint(data_obj[0][1])
    break

imap_obj.close()
```

Run the script, as follows:


```
student@ubuntu:~$ python3 imap_email.py
```

As output, you\'ll get all of the emails from the specified folder.



Summary
--------------------------



In this lab, we learned about how to write an email message in a
Python script. We also learned about the Python `smtplib`
module, which is used for sending and receiving emails via Python
scripts. We also learned about how to receive emails through POP3 and
IMAP protocols. Python supplies the `poplib` and
`imaplib` libraries with which we can perform tasks.

In the next lab, you\'ll learn about Telnet and SSH.



Questions
----------------------------


1.  What are POP3 and IMAP?
2.  What are break and continue used for? Give an appropriate example.
3.  What is pprint?
4.  What are negative indexes and why are they used?
5.  What is the difference between the `pyc` and
    `py` file extensions?
6.  Generate following pattern using looping\'s:

```
   1010101
      10101 
       101  
        1 
```
