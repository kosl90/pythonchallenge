#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''python challenge level 8
question url: http://www.pythonchallenge.com/pc/def/integrity.html
answer url: http://www.pythonchallenge.com/pcc/return/good.html:huge:file
'''

import  bz2
un = 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
pw = 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'


def main():
    print "user name:", bz2.decompress(un)
    print "password:", bz2.decompress(pw)


if __name__ == '__main__':
    main()
