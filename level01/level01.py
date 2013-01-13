#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''python challenge level 1
question url: http://www.pythonchallenge.com/pc/def/map.html
answer url: http://www.pythonchallenge.com/pcc/def/ocr.html
'''

text = '''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp.
bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle
qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. '''

# asiic version
def asiicv():
    trans_text = ''
    for i in text:
        trans_text += chr((ord(i) - ord('a') + 2) % 26 + ord('a')) if i.islower() \
                    else i

    print trans_text


from string import lowercase, maketrans
# dict version
def dictv():
    trans_text = ''

    alph_map = dict(zip(lowercase, lowercase[2:]+lowercase[:2]))
    for i in text:
        trans_text += alph_map[i] if i in alph_map else i

    print trans_text

# author version
def autv():
    alph_map = maketrans(lowercase, lowercase[2:]+lowercase[:2])
    print text.translate(alph_map)


def main():
    asiicv()
    print
    dictv()
    print
    autv()


if __name__ == '__main__':
    main()
