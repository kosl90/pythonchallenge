#!/usr/bin/env python2.7
#-*- coding: utf-8 -*-


def main(levels):
    import os
    levels_len = len(levels)

    for level in levels:
        intlevel = int(level)
        print '======= level %02d =======' % intlevel
        strlevel = 'level%02d' % intlevel
        os.system('python %s' % os.path.join(strlevel, strlevel + '.py'))
        #os.chdir(strlevel)
        #os.system('python %s.py' % strlevel)
        #os.chdir('..')

        if levels_len - 1 != levels.index(level):
            print


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print 'Usage: %s level [level...]' % sys.argv[0]
    else:
        main(sys.argv[1:])
