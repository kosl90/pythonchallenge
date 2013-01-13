#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''python challenge level 12
question url: http://www.pythonchallenge.com/pc/return/evil.html
answer url: http://www.pythonchallenge.com/pcc/return/disproportional.html
'''

from os.path import dirname, join as pjoin

DATA_DIR = pjoin(dirname(__file__), 'data')

def main():
    f = open(pjoin(DATA_DIR, 'evil2.gfx'),'rb')
    content = f.read()
    f.close()

    for i in xrange(5):
        f = open(pjoin(DATA_DIR, '%d' % i), 'wb')
        f.write(content[i::5])
        f.close()


if __name__ == '__main__':
    main()
