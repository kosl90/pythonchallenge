#! /usr/bin/env python2.7
# -*- coding: utf-8 -*-
'''
pythonchallenge level 17
question url: http://www.pythonchallenge.com/pc/return/romance.html
answer url: http://www.pythonchallenge.com/pcc/return/balloons.html
'''

from os.path import dirname, join as pjoin
DATA_DIR = pjoin(dirname(__file__), 'data')
import sys
import os
import re

def main():
    def call(name):
        import xmlrpclib
        xmlrpc = xmlrpclib.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
        return xmlrpc.phone(name)


    def next_busynothing_from(page):
        content = page.read()
        nums = match(content)
        page.close()
        return (nums[-1] if nums else None, content)


    def cookie_info_from(page):
        req = page.info()
        cookie = req.getheader('set-cookie')
        info = cookie.split(';')[0]
        return(info.split('=')[1])

    info_file = pjoin(DATA_DIR, 'info')
    if os.path.exists(info_file):
        f = open(info_file)
        print f.read()
        f.close()
        print 'call...'
        print call('Leopold')

        import urllib2
        url = 'http://www.pythonchallenge.com/pc/stuff/violin.php'
        info = 'the flowers are on their way'
        req = urllib2.Request(url, headers={'Cookie': 'info='+info})
        print 'read request...'
        print urllib2.urlopen(req).read()
        sys.exit(0)

    match = re.compile(r'\D+(\d+$)').findall
    url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing='

    default = '12345' if len(sys.argv) == 1 else sys.argv[1]
    busynothing = default
    pre = ''


    import urllib
    mesg = []
    haserr = False
    for i in xrange(400):
        try:
            page = urllib.urlopen(url + busynothing)
            pre = busynothing
            num, data = next_busynothing_from(page)
            mesg.append(cookie_info_from(page))

            if num:
                busynothing = num
                print i, busynothing, data
            else:
                print 'no match'
                break
        except KeyboardInterrupt:
            print 'user interrupted'
            haserr = True
            break
        except Exception, e:
            print e
            haserr = True
            break

    if haserr:
        print 'previous busynothing: %s' % pre
    else:
        msg = ''.join(mesg)
        #print msg
        import bz2
        msg = bz2.decompress(urllib.unquote_plus(msg))
        f = open(info_file, 'w')
        f.write(msg)
        f.close()
        print msg


if __name__ == '__main__':
    main()
