import serial
import requests
import json
serial = serial.Serial("/dev/ttyUSB2", baudrate=9600)

card1 = '18004865AB9E'
card2 = '19007E5E4970'

firebase_url = 'https://twic-db.firebaseio.com/'

def send_card_info_to_database(card_id):
    '''
    This function sends the inputted card info to the database
    '''
    data={'id':card_id, 'number of times tapped': 0}
    sent = json.dumps(data)
    result = requests.post(firebase_url+'/cards.json', sent)
    print 'Success!' + str(result.status_code) + ',' + result.text

def check_card_id(code):
    '''
    This function checks if the card id is valid
    '''
    if code.find(card1) > 0:
        print('victory')
    else:
        print('failure')


def read_card():
    '''
    This is the main function which initiates the reading of the card
    and prints relevant information to the one tapping the card

    It should be noted that data is read from the card as individual symbols/variables

    '''
    code = ''
    while True:
        data = serial.read()
        if data == '\r':
            print(code)
            #print(type(code))
            #check_card_id(code)
            #send_card_info_to_database(code)
            code = ''
        else:
            code = code + data
read_card()
