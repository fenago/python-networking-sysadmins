from ftplib import FTP

## Browser Url: ftp://speedtest.tele2.net/
        
ftp = FTP("speedtest.tele2.net")
ftp.login("anonymous", "anonymous")

ftp.cwd("/")
files = ftp.nlst()
# Print out the files
for file in files:
    print("FileName..." + file)

filename='512KB.zip'

try:
    ftp.retrbinary("RETR " + filename ,open(filename, 'wb').write)
except:
    print ("Error")
    

ftp.close()

