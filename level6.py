#! /usr/bin/env python
'''python challenge level 6
question url: http://www.pythonchallenge.com/pc/def/channel.html
answer url: http://www.pythonchallenge.com/pcc/def/oxygen.html
'''

# zipfile and string version
import zipfile
zf = zipfile.ZipFile('level6.d/channel.zip')

zc = []
name = '90052.txt'
while True:
    f = open('level6.d/%s' % name)
    data = f.read().split()[-1]
    f.close()
    zc.append(zf.getinfo(name).comment)
    if data.isdigit():
        name = '%s.txt' % data
    else:
        break

# the loop break because there is not match string or the file is not in the files
# anyway, print the content of the last file
f = open('level6.d/%s' % name)
print f.read()
f.close()
print ''.join(zc)


# unzip and regRex version
import re
findnum = re.compile(r'\d{2,}').findall
zf = zipfile.ZipFile('level6.d/channel.zip')

zc = []
name = '90052.txt'
while True:
    f = open('level6.d/%s' % name)
    data = findnum(f.read())
    f.close()
    zc.append(zf.getinfo(name).comment)
    if data:
        name = '%s.txt' % data[0]
    else:
        break

# the loop break because there is not match string or the file is not in the files
# anyway, print the content of the last file
f = open('level6.d/%s' % name)
print f.read()
f.close()
print ''.join(zc)


# unzip and regRex version
findnum = re.compile(r'\d+$').findall
zf = zipfile.ZipFile('level6.d/channel.zip')

zc=[]
name = '90052.txt'
while True:
    zinfo = zf.getinfo(name)
    z = zf.open(name)
    data = findnum(z.read())
    z.close()
    zc.append(zinfo.comment)
    if data:
        name = '%s.txt' % data[0]
    else:
        break

# the loop break because there is not match string or the file is not in the files
# anyway, print the content of the last file
z = zf.open(name)
print z.read()
z.close()
print ''.join(zc)


