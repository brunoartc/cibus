import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from datetime import date
import json

usuario = "brunoartc"
nutricional_info = "Carboidratos"
number = 20


def handler_name(event, context): 
    event["body"] = json.loads(event["body"])
    usuario = event["body"]["usuario"]
    nutricional_info = event["body"]["nutricional_info"]
    number = event["body"]["number"]

    cred = credentials.Certificate("./cibus-2738b-firebase-adminsdk-mgedu-04c7819042.json")
    firebase_admin.initialize_app(cred, {"databaseURL": "https://cibus-2738b.firebaseio.com"})



    ref = db.reference('consumer')




    ref.child(f"stats/{usuario}/week/{date.today().isocalendar()[1]}/{nutricional_info}").set(number)

    return {
        'statusCode': 200,
        'body': "OKK"
    }


