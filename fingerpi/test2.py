#!/usr/bin/env python

import fingerpi as fp
# from fingerpi import base

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

f.EnrollStart(2)
f.Enroll1()
f.Enroll2()
f.Enroll3()