import tarfile
import os

try:
    os.mkdir('work')
except FileExistsError:
    # directory already exists
    pass

with tarfile.open('work.tar', 'r') as t:
	t.extractall('work')
print(os.listdir('work'))
