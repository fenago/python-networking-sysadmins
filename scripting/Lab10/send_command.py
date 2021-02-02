from ftplib import FTP

## Browser Url: ftp://speedtest.tele2.net/

ftp = FTP("speedtest.tele2.net")
ftp.login("anonymous", "anonymous")

s_cmd_stat = ftp.sendcmd('STAT')
print(s_cmd_stat)
print()
s_cmd_pwd = ftp.sendcmd('PWD')
print(s_cmd_pwd)
print()

ftp.close()

