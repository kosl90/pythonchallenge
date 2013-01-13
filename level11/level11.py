#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''python challenge level 11
question url: http://www.pythonchallenge.com/pc/return/5808.html
answer url: http://www.pythonchallenge.com/pcc/return/evil.html
'''

from pythonchallenge import pjoin

import Image
im = Image.open(pjoin("cave.jpg"))
w, h = im.size
# print w, h 

imgs = [Image.new(im.mode, (w / 2, h / 2)) for dummy in xrange(4)]
imgs_load = [i.load() for i in imgs]
org = im.load()

for i in xrange(w):
    for j in xrange(h):
        org_pos = (i, j)
        new_pos = (i // 2, j // 2)
        imgs_load[i % 2 + j % 2 * 2 ][new_pos] = org[org_pos]

[imgs[i].save(pjoin('%02d.png' % i)) for i in xrange(4)]
