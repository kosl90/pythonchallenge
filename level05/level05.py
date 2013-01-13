#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''python challenge level 5
question url: http://www.pythonchallenge.com/pc/def/peak.html
answer url: http://www.pythonchallenge.com/pcc/def/channel.html
'''

from os.path import dirname, join as pjoin
DATA_DIR = pjoin(dirname(__file__), 'data')


def main():
    global content
    import pickle
    info = pickle.load(open(pjoin(DATA_DIR, 'banner.p')))
    for line in info:
        #print ''.join(map(lambda i:i[0]*i[1], line))
        print ''.join([x[0] * x[1] for x in line])


if __name__ == '__main__':
    main()
