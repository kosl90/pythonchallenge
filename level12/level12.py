#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''python challenge level 12
question url: http://www.pythonchallenge.com/pc/return/evil.html
answer url: http://www.pythonchallenge.com/pcc/return/disproportional.html
'''

from .. import pjoin

f = open(pjoin('evil2.gfx'),'rb')
content = f.read()
f.close()

for i in xrange(5):
    f = open(pjoin('%d' % i), 'wb')
    f.write(content[i::5])
    f.close()
