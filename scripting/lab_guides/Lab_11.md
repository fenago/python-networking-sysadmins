

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



Email message format
---------------------------------------



In this section, we\'re going to learn about the email[]{#id326367321
.indexterm} message format. Email messages consist of three primary
components:


-   The receiver\'s email address
-   The sender\'s email address
-   The message
:::

There are other components also included in the message format, such as
the subject line, email signatures, and attachments.

 

 

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

In the preceding example, we used the `smtplib`Python module
to send an email. Make sure you\'re sending an email from a Gmail ID to
the receiver. The `sender` variable saves the sender\'s email
address. In the `password` variable, you can either enter your
password or you can prompt for a password using the `getpass`
module. Here, we prompt for the password. Next, we created a variable
named `msg`, which will be our actual email message. In that,
we first mentioned a subject and then the message we want to send. Then,
in `login()`, we mentioned the `sender` and
`password` variables. Next, in `sendmail()`, we
mentioned the `sender`, `receivers`, and
`text` variables. So, using this process, we sent the email
successfully.



POP3 and IMAP servers
----------------------------------------



In this section, you\'ll learn about
receiving emails via POP and IMAP servers.
Python offers the `poplib` and `imaplib` libraries
for receiving emails via Python scripts.



### Receiving email using the poplib library



**POP3** stands for **Post Office Protocol version
3**. This standard protocol helps
you receive emails from a remote server to our local machine. The main
advantage of POP3 is that it allows us to download[]{#id326064756
.indexterm} emails on to our local machine and read the downloaded
emails offline.

The POP3 protocol works on two ports:


-   Port `110`: The default non-encrypted port
-   Port `995`: The encrypted port
:::

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

In the preceding example, first we\'re importing the `poplib`
library, which is used in Python for the POP3 protocol to receive an
email securely. Then, we state the specific email server and our email
credentials---that is, our username and password. After that, we print
the response message from the server and provide the username and
password to the POP3 SSL server. After login, we get mailbox stats and
print them to the Terminal in the form of a number of emails.

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

 

 

In the preceding example, we imported the `poplib` library
used in Python to supply the POP3 protocol to receive an email securely.
After stating the specific email server and the username and password,
we printined the response message from the server and providing the
username and password to the POP3 SSL server. Then, we\'re fetching the
latest email from the mailbox.

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



IMAP stands for Internet Message Access Protocol. It\'s used to access
emails on a remote server through your local
machine. IMAP allows simultaneous access by multiple
clients to your email. IMAP is more suitable
when you access your email via different locations.

The IMAP protocol works on two ports:


-   Port `143`: The default non-encrypted port
-   Port `993`: The encrypted port
:::

 

 

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

In the preceding example, first, we\'re importing the
`imaplib` library, which is used in Python to receive an email
securely via the IMAP protocol. Then, we state the specific email server
and our user credentials---that is, our username and password. After
that, we provide that username and password to the IMAP SSL server.
We\'re using the `'select('Inbox')'` function over
`imap_obj` to display messages in the inbox. Then we use a
`for` loop to display messages that have been fetched one by
one. To display messages, we use \"pretty print\"---that is, the
`pprint.pprint()`** **function-because it formats
your object, writes it into the data stream, and passes it as an
argument. Then, finally, the connection is closed.



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
