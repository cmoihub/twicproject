'''
Useful links
https://pypi.python.org/pypi/python-firebase/1.2
https://temboo.com/python/parsing-json
'''

import json
import requests

FIREBASE_URL = 'https://twic-db.firebaseio.com'

def get_file():
    file = open("demo_temp.png", "r")
    return file

def upload_image():
    '''add new card and fingerprint to database'''
    print ('adding image to system...')
    data = {
        'img': get_file()
    }
    '''sent = json.dumps(data)'''
    result = requests.post(FIREBASE_URL + '/img.json', data)
    print (result.status_code)
    print (result.text)



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

def main():
    upload_image()

main()
