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
response = f.GetTemplate(2)[1]['Data']
insert = f.SetTemplate(0, response)
