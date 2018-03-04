# twicproject

Please note for the webapp to add polymer elements you must put an html link in the my-app.html file 

I and Liam were able to get the card and the fingerprint reader to work together

This is done using four python scripts - twic, db_checker, verify, rfidcard

twic basically acts as a main function that runs everything

twic calls the rfidcard (which initiates the card reader) and verify (which initiates the fingerprint reader) scripts

twic extracts the card id and fingerprint id from the scripts and passes them alongside the database to the db_checker script

the database is set up like this for one field for example
{
“first”: {
        “id”:“1”,
        “card_data”:{
                “fingerprint”:“1"
                }
    }
}

The db_checker looks at the items in the database and first checks that the card id passed exists in our system

If the card id is registered in the database we match the fingerprint value of card_data to the fingerprint passed by the user
If they match we print an encouraging message to the console
If they don’t we print some message about the card id not matching to the fingerprint

We use a counter variable to keep track of if the card ever shows up in our database

If the card is found the counter variable is altered and at the end of the iteration we check if the variable was altered or not, if it wasn’t then we print some message to the console to let us know so
