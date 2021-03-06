#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''python challenge level 16
question url: http://www.pythonchallenge.com/pc/return/mozart.html
answer url: http://www.pythonchallenge.com/pcc/return/romance.html
'''

from os.path import dirname, join as pjoin
DATA_DIR = pjoin(dirname(__file__), 'data')

import Image


def main():
    im = Image.open(pjoin(DATA_DIR, 'mozart.gif'))
    w, h = im.size
    # print im.mode, im.size

    data = list(im.getdata())
    data = [data[i * w:(i + 1) * w] for i in xrange(h)]
    # print data

    PINK = 195  # get it via GIMP
    for row in xrange(h):
        for col in xrange(w):
            if data[row][col] == PINK:
                data[row] = data[row][col:] + data[row][:col]

    # better version
    # for row in xrange(h):
    #     col = data[row].index(PINK)  # there must be PINK every line
    #     data[row] = data[row][col:] + data[row][:col]

    im.putdata(reduce(lambda x,y: x+y, data))
    im.save(pjoin(DATA_DIR, 'res.gif'))


if __name__ == '__main__':
    main()
