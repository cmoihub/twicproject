'''
Useful links
https://pypi.python.org/pypi/python-firebase/1.2
https://temboo.com/python/parsing-json
'''

import sys
sys.path.insert(0,"/home/pi/Downloads/twicproject")

import json
import requests
import time
import displays
import update
displays.setup()
'''import pyrebase'''


CARD1 = '18004865AB9E'
CARD2 = '19007E5E4970'
FIREBASE_URL = 'https://twic-db.firebaseio.com'
DELAY_TIME = 5
NO_DELAY_TIME = 2
DEFAULT_SECURITY_LEVEL = 2
DEFAULT_ROLE = 'Chef'
GOOD_STATUS = 'success'
BAD_STATUS = 'failure'

##150028790044
##19003F6B713C
offline_data = {
    'first':{'card_id':'19007E5E4970', 'card_data':{'fingerprint':'1', 'level':'2', 'role':'Chef'}},
    'second':{'card_id':'18004865AB9E', 'card_data':{'fingerprint':'2', 'level':'3', 'role':'Captain'}},
    'third':{'card_id':'150028790044', 'card_data':{'fingerprint':'4', 'level':'1', 'role':'Chef'}}
              }
    
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
##            if cardIDFound == False:
            print('still searching for card id')
##                break
            continue
        else:
            cardIDFound = True
            print('card id found')
            occurrence_of_card_id = occurrence_of_card_id + 1
            if item['card_data']['fingerprint'] == fingerprint and item['card_data']['level'] >= DEFAULT_SECURITY_LEVEL and item['card_data']['role'] == DEFAULT_ROLE :
                print (GOOD_STATUS)
                displays.green_led(NO_DELAY_TIME)
                displays.unlock_door(DELAY_TIME)
                update.log_access(card_id, GOOD_STATUS)
            else:
                print ('Invalid fingerprint')
                print (BAD_STATUS)
                displays.red_led(DELAY_TIME)
                update.log_access(card_id, BAD_STATUS)
    if occurrence_of_card_id == 0:
        print ('Card ID not found')
        print (BAD_STATUS)
        displays.red_led(DELAY_TIME)
        update.log_access(card_id, BAD_STATUS)

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