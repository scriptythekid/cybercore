# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 19:45:35 2013

@author: scripty


cybercore text generatino script - wip - blabla


cyber cyber...
"""

import sys
import os
os.getcwd()
import codecs
import re
import random

import pyttsx
import time

from pprint import pprint

try:
    fd = codecs.open(sys.argv[1], 'r',encoding='utf-8')
    data = fd.read()
    fd.seek(0)
    flines = fd.readlines()
    fd.close()
except:
    print "missing filename as arg1"
    sys.exit(1)
    

abrs = []

for line in flines:
    sepchar=u'\u2014'
    if sepchar in line:
        abbr,descr = line.strip().split(u'\u2014')
        abrs.append([abbr,descr,descr[-3:]])

endings = {}
for abr in abrs:
    end = abr[2]
    if not endings.has_key(end):
        endings[end] = []
    endings[end].append(abr)

rapwords = []
for ending,abbrs in endings.items():
    
    if len(abbrs) > 1:
        for abbr in abbrs:
            words = abbr[1].split(" ")
            lword = words[len(words)-1].lower()
            if not lword in rapwords:
                rapwords.append(lword)

v = pyttsx.init("espeak")
#v.say("cyber cyber")
#v.runAndWait()

for rw in rapwords:
    print rw
    v.say(rw)

v.runAndWait()





