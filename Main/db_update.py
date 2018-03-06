import json
import requests

FIREBASE_URL = 'https://twic-db.firebaseio.com'

def enroll(card, fingerprint):
    '''
    Used to enroll or re-enroll user on database
    '''
    data = get_data()
    if user_exists(card, fingerprint, data):
        update_info()
    else:
        add_info(card, fingerprint)

def user_exists(card, fingerprint, data):
    '''check if user is in database'''
    return card_already_exists(card, data) or fingerprint_already_exists(fingerprint, data)

def card_already_exists(card_id, data):
    '''check if there are card id has been registered with database'''
    for item in data:
        if item['id'] == card_id:
            print 'card info exists on db'
            return True
    return False

def fingerprint_already_exists(fingerprint, data):
    '''check if there are card id has been registered with database'''
    for item in data:
        if item['card_data']['fingerprint'] == fingerprint:
            print 'fingerprint info exists on db'
            return True
    return False

def update_info():
    '''update card and fingerprint information on database'''
    print 'updating user info...'

def add_info(card, fingerprint):
    '''add new card and fingerprint to database'''
    print 'adding user to system...'
    data = {
        'id': card,
        'card_data': {
            'fingerprint': fingerprint
        }
    }
    sent = json.dumps(data)
    result = requests.post(FIREBASE_URL + '/test_data.json', sent)
    print result.status_code
    print result.text
    
def send_card_info_to_database(card_id):
    '''
    This function sends the inputted card info to the database
    '''
    data={'id':card_id, 'number of times tapped': 0}
    sent = json.dumps(data)
    result = requests.post(firebase_url+'/cards.json', sent)
    print 'Success!' + str(result.status_code) + ',' + result.text


def get_data():
    '''
    Return data as a list of values
    Firebase automatically generates random ids (keys) that match up to values
    that we upload to the database, we do not need need to know what these keys are
    so we can just work with the values
    '''
    # Get data from firebase
    result = requests.get(FIREBASE_URL + '/test_data.json')
    # Convert data to json
    data = json.loads(result.text)
    return data.values()