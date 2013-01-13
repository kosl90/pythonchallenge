#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''python challenge level 13
question url: http://www.pythonchallenge.com/pc/return/disproportional.html
answer url: http://www.pythonchallenge.com/pcc/return/italy.html
'''

import xmlrpclib
xmlrpc = xmlrpclib.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
print xmlrpc.system.listMethods()
print xmlrpc.system.methodHelp('phone')
print xmlrpc.phone('Bert')
