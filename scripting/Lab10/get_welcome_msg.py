from ftplib import FTP

## Browser Url: ftp://speedtest.tele2.net/

ftp = FTP("speedtest.tele2.net")
ftp.login("anonymous", "anonymous")

welcome_msg = ftp.getwelcome()
print(welcome_msg)

ftp.close()
