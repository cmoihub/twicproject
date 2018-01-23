import sys
sys.path.insert(0,"/home/pi/Downloads/twic")

from Card import rfidcard
import fingerpi.verify as verify
import db_checker as db_

#first = {'id':'', 'data':{'fingerprint':''}}
#second = {'id':'', 'data':{'fingerprint':''}}
data = {
    'first':{'id':'19007E5E4970', 'card_data':{'fingerprint':'1'}},
    'second':{'id':'18004865AB9E', 'card_data':{'fingerprint':'2'}}
    }
def run(data):
    '''runs the card and biometric readers'''
    card_id = rfidcard.read_card()
    fingerprint = verify.run()
    #convert database data from dictionary to list
    values = data.values()
    db_.check_db(values, str(card_id), str(fingerprint))

run(data)