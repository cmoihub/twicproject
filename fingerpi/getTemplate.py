#!/usr/bin/env python

import fingerpi as fp
# from fingerpi import base
from PIL import Image
# import struct
import time
# import matplotlib.pyplot as plt
import pickle


def printByteArray(arr):
    return map(hex, list(arr))

f = fp.FingerPi()


print 'Opening connection...'
f.Open(extra_info = True, check_baudrate = True)

print 'Changing baudrate...'
f.ChangeBaudrate(115200)
f.CmosLed(True)

print 'Doing some crazy stuff on <Enter>'
_ = raw_input()
response = f.GetTemplate(2)
print (response)
f = open('exp.txt', 'w')
#f.write('liamail')
#f.write(response)
for i in response:
    print (i['Parameter'])
    #f.write(i)

insert = f.SetTemplate(99, response[1]['Data'])
print insert
