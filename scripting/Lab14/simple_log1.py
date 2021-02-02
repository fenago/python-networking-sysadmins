f=open('/var/log/dpkg.log','r')

lines = f.readlines()
for line in lines:
	kern_log = line.split()[1:3]
	print(kern_log)

