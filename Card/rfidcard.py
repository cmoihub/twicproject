#!/usr/bin/env python
#-*- coding:utf-8 -*-#

import serial
import requests
import json
import sys
sys.path.insert(0,"/home/pi/Downloads/twic")
serial = serial.Serial("/dev/ttyUSB3", baudrate=9600)

current_card = ''

firebase_url = 'https://twic-db.firebaseio.com/'


def read_card():
    '''
    This initiates the reading of the card
    It should be noted that data is read from the card as individual symbols/variables
    '''
    code = ''
    while True:
        data = serial.read()
        if data == '\r':
            #we splice the data because there are emoji hex boxes in front of the data
            current_card = code[1:len(code)]
            #send_card_info_to_database(code)
            #code = ''
            return current_card
        else:
            code = code + data
