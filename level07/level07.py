#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''python challenge level 7
url: http://www.pythonchallenge.com/pc/def/oxygen.html
answer url: http://www.pythonchallenge.com/pcc/def/integrity.html
'''

from os.path import dirname, join as pjoin

DATA_DIR = pjoin(dirname(__file__), 'data')

import Image


def main():
    im = Image.open(pjoin(DATA_DIR, 'oxygen.png'))

    # get the width and length of the wired bar and step via GIMP
    # x_begin, x_end = 0, 609
    # y_begin, y_end = 43, 53
    # step = 7
    # print im.getpixel((0, 43))
    msg = ''.join([chr(im.getpixel((i, 43))[0]) for i in xrange(0, 609, 7)])
    print msg

    # step 2
    import re
    print ''.join([chr(int(x)) for x in re.findall(r'\d{3}',msg)])


if __name__ == '__main__':
    main()
