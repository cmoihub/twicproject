'''
Useful links
https://pypi.python.org/pypi/python-firebase/1.2
https://temboo.com/python/parsing-json
'''

import sys
sys.path.insert(0,"/home/pi/Downloads/twic")

import json
import requests
import time
import displays
displays.setup()
'''import pyrebase'''


CARD1 = '18004865AB9E'
CARD2 = '19007E5E4970'
FIREBASE_URL = 'https://twic-db.firebaseio.com'

offline_data = {
    'first':{'card_id':'19007E5E4970', 'card_data':{'fingerprint':'1'}},
    'second':{'card_id':'18004865AB9E', 'card_data':{'fingerprint':'2'}},
    'third':{'card_id':'19003F6B713C', 'card_data':{'fingerprint':'4'}}
              }

def setup_leds():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(23, GPIO.OUT)
    GPIO.setup(24, GPIO.OUT)
    GPIO.setup(18, GPIO.OUT)

setup_leds()

def red_led():
    print ("The red LED will turn on")
    GPIO.output(23,GPIO.HIGH)
    print ("Delaying for 5 seconds")
    time.sleep(5)
    print ("Now we turn it off")
    GPIO.output(23,GPIO.LOW)
    
def green_led():
    print ("The green LED will turn on")
    GPIO.output(24,GPIO.HIGH)
    print ("Delaying for 5 seconds")
    time.sleep(5)
    print ("Now we turn it off")
    GPIO.output(24,GPIO.LOW)
    
def unlock_door():
    print ("Unlock the door")
    GPIO.output(18,GPIO.HIGH)
    print ("Delaying for 5 seconds")
    time.sleep(5)
    print ("lock it back")
    GPIO.output(18,GPIO.LOW)
    print("Lock the door")
    
def check_db(card_id, fingerprint):
    ''' This function checks the database for a valid card if and then looks up the corresponding fingerprint
     https://stackoverflow.com/questions/11700798/python-accessing-values-nested-within-dictionaries
     '''
    data = get_data()
    # occurrence_of_card_id tracks if card id exists in the database
    # validateInput(data, card_id, fingerprint)
    cardIDFound = False
    occurrence_of_card_id = len(data)
    for item in data:
        occurrence_of_card_id = occurrence_of_card_id - 1
        if item['card_id'] != card_id:
            if cardIDFound == False:
                print('still searching for card id')
                break
            continue
        else:
            cardIDFound = True
            print('card id found')
            occurrence_of_card_id = occurrence_of_card_id + 1
            if item['card_data']['fingerprint'] == fingerprint:
                print ('Success')
                green_led()
            else:
                print ('Invalid fingerprint')
                red_led()
    if occurrence_of_card_id == 0:
        print ('Card ID not found')
        red_led()
        
def secure_get_data():
    '''config = {
      "apiKey": "AIzaSyAyOqg5oprERTAN8Z_aVe88mdfx9sb9l_A",
      "authDomain": "twic-db.firebaseapp.com",
      "databaseURL": "https://databaseName.firebaseio.com",
      "storageBucket": "twic-db.appspot.com"
    }
    firebase = pyrebase.initialize_app(config)
    auth = firebase.auth()
    user = auth.sign_in_with_email_and_password("cmoisesele@live.com", "dbtest")
    db = firebase.database()
    test = db.child("test-data").get()
    print(test.val())
    '''
    

def get_data():
    '''
    Return data as a list of values
    Firebase automatically generates random ids (keys) that match up to values
    that we upload to the database, we do not need need to know what these keys are
    so we can just work with the values
    '''
    
    # Get data from firebase
    result = requests.get(FIREBASE_URL + '/users.json')
    # Convert data to json
    data = json.loads(result.text)
    data = data.values()
    
    data = step_down(data)
    data = step_down(data)
    return data

def step_down(data):
    data = data[0]
    data = data.values()
    return data