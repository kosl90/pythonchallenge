#!/usr/bin/env python2.7
#-*- coding: utf-8 -*-

__all__ = ['pjoin']

import os

def pjoin(fn, dn='data'):
    return os.path.join(dn, fn)
