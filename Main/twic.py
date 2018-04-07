import sys
sys.path.insert(0,"/home/pi/Downloads/twicproject")

from Card import rfidcard
import fingerpi.verify as verify
import Database.compare as db_checker

#liam is 1 and 2
#craig is 4

def run():
    '''runs the card and biometric readers'''
    card_id = rfidcard.read_card()
    print(card_id)
    fingerprint = verify.read_fp()
    print(fingerprint)
    #convert database data from dictionary to list
##    values = data.values()
    db_checker.check_db(str(card_id), str(fingerprint))

run()
