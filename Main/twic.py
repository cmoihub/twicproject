import sys
sys.path.insert(0,"/home/pi/Downloads/twic")

from Card import rfidcard
import fingerpi.verify as verify
import db_checker as db_

#liam is 1 and 2
#craig is 4

def run(data):
    '''runs the card and biometric readers'''
    card_id = rfidcard.read_card()
    fingerprint = verify.read_fp()
    #convert database data from dictionary to list
    values = data.values()
    db_.check_db(str(card_id), str(fingerprint))

run(data)
