import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from datetime import date
import json

def handler_name(event, context): 
    event["body"] = json.loads(event["body"])
    cred = credentials.Certificate("./cibus-2738b-firebase-adminsdk-mgedu-04c7819042.json")
    firebase_admin.initialize_app(cred, {"databaseURL": "https://cibus-2738b.firebaseio.com"})



    ref = db.reference('kits')
    aa = ref.get("/")[0]

    return {
        'statusCode': 200,
        'body': aa
    }

#ref.child(f"{nutricional_info}/").set(20)