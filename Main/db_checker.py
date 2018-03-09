'''
Useful links
https://pypi.python.org/pypi/python-firebase/1.2
https://temboo.com/python/parsing-json
'''

import json
import requests
import time
import RPi.GPIO as GPIO
import pyrebase


CARD1 = '18004865AB9E'
CARD2 = '19007E5E4970'
FIREBASE_URL = 'https://twic-db.firebaseio.com'

config = {
  "apiKey": "AIzaSyAyOqg5oprERTAN8Z_aVe88mdfx9sb9l_A",
  "authDomain": "twic-db.firebaseapp.com",
  "databaseURL": "https://databaseName.firebaseio.com",
  "storageBucket": "twic-db.appspot.com"
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
user = auth.sign_in_with_email_and_password("cmoisesele@live.com", "dbtest")
db = firebase.database()
def setup_leds():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(23, GPIO.OUT)
    GPIO.setup(24, GPIO.OUT)

setup_leds()

def red_led():
    print"The red LED will turn on"
    GPIO.output(23,GPIO.HIGH)
    print"Delaying for 5 seconds"
    time.sleep(5)
    print "Now we turn it off"
    GPIO.output(23,GPIO.LOW)
    
def green_led():
    print"The green LED will turn on"
    GPIO.output(24,GPIO.HIGH)
    print"Delaying for 5 seconds"
    time.sleep(5)
    print "Now we turn it off"
    GPIO.output(24,GPIO.LOW)
def check_db(data, card_id, fingerprint):
    ''' This function checks the database for a valid card if and then looks up the corresponding fingerprint
     https://stackoverflow.com/questions/11700798/python-accessing-values-nested-within-dictionaries
     '''
    #data = get_data()
    # occurrence_of_card_id tracks if card id exists in the database
    # validateInput(data, card_id, fingerprint)
    cardIDFound = False
    occurrence_of_card_id = len(data)
    for item in data:
        occurrence_of_card_id = occurrence_of_card_id - 1
        if item['id'] != card_id:
            if cardIDFound == False:
                print('still searching for card id')
                break
            continue
        else:
            cardIDFound = True
            print('card id found')
            occurrence_of_card_id = occurrence_of_card_id + 1
            if item['card_data']['fingerprint'] == fingerprint:
                print 'Success'
            else:
                print 'Invalid fingerprint'
                red_led()
    if occurrence_of_card_id == 0:
        print 'Card ID not found'
        red_led()
        

def get_data():
    '''
    Return data as a list of values
    Firebase automatically generates random ids (keys) that match up to values
    that we upload to the database, we do not need need to know what these keys are
    so we can just work with the values
    '''
    auth = firebase.auth()
    user = auth.
    # Get data from firebase
    result = requests.get(FIREBASE_URL + '/test_data.json')
    # Convert data to json
    data = json.loads(result.text)
    print(data)
    return data.values()

get_data()
print({'craig': '5'})
