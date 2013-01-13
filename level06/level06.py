#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''python challenge level 6
question url: http://www.pythonchallenge.com/pc/def/channel.html
answer url: http://www.pythonchallenge.com/pcc/def/oxygen.html
'''

from os.path import dirname, join as pjoin

import zipfile

DATA_DIR = pjoin(dirname(__file__), 'data')

# zipfile and string version
def zsv():
    zf = zipfile.ZipFile(pjoin(DATA_DIR, 'channel.zip'))

    zc = []
    name = '90052.txt'
    while True:
        f = open(pjoin(DATA_DIR, name))
        data = f.read().split()[-1]
        f.close()
        zc.append(zf.getinfo(name).comment)
        if data.isdigit():
            name = '%s.txt' % data
        else:
            break

    # the loop break because there is not match string or the file is not in the files
    # anyway, print the content of the last file
    f = open(pjoin(DATA_DIR, name))
    print f.read()
    f.close()
    print ''.join(zc)


import re
# unzip and regRex version
def rev():
    findnum = re.compile(r'\d{2,}').findall
    zf = zipfile.ZipFile(pjoin(DATA_DIR, 'channel.zip'))

    zc = []
    name = '90052.txt'
    while True:
        f = open(pjoin(DATA_DIR, name))
        data = findnum(f.read())
        f.close()
        zc.append(zf.getinfo(name).comment)
        if data:
            name = '%s.txt' % data[0]
        else:
            break

    # the loop break because there is not match string or the file is not in the files
    # anyway, print the content of the last file
    f = open(pjoin(DATA_DIR, name))
    print f.read()
    f.close()
    print ''.join(zc)


# unzip and regRex version
def rev2():
    findnum = re.compile(r'\d+$').findall
    zf = zipfile.ZipFile(pjoin(DATA_DIR, 'channel.zip'))

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


def main():
    zsv()
    rev()
    rev2()

if __name__ == '__main__':
    main()
