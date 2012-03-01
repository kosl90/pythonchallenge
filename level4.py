#! /usr/bin/env python
'''python challenge level 4
question url: http://www.pythonchallenge.com/pc/def/linkedlist.php
answer url: http://www.pythonchallenge.com/pcc/def/peak.html
'''

import re
import sys
import urllib
re_match = re.compile(r'\D+(\d+$)').findall  # search is also ok

# nothing in [12345, 8022]
nothing = sys.argv[1]
pre = ''

for i in xrange(400):
    try:
        f = urllib.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s" % nothing)
        data = f.read()
        f.close()
        pre = nothing
        nums = re_match(data)
        if nums:
            nothing = nums[0]
            print i, nothing, data
        else:
            print 'no match'
            break
    except KeyboardInterrupt:
        print 'user interrupted'
        break
    except Exception, e:
        print e
        break

print 'previous nothing: %s\nprevious data: %s' % \
    (pre, err_num, data)
