#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''python challenge level 4
question url: http://www.pythonchallenge.com/pc/def/linkedlist.php
answer url: http://www.pythonchallenge.com/pcc/def/peak.html
'''

import re
import sys
import urllib
re_match = re.compile(r'\D+(\d+$)').findall  # search is also ok

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="

def main():
    global url, re_match
    default_nothing = '12345' if len(sys.argv) == 1 else sys.argv[1]
    # nothing in [12345, 8022]
    nothing = default_nothing
    pre = ''

    for i in xrange(400):
        try:
            f = urllib.urlopen(url + nothing)
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

    print 'previous nothing: %s\nprevious data: %s' % (pre, data)


if __name__ == '__main__':
    main()
