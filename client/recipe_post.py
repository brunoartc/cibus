import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from datetime import date
import json
recipe = "bananada"


def handler_name(event, context):
    event["body"] = json.loads(event["body"])
    recipe = event["body"]["recipe"]
    cred = credentials.Certificate("./cibus-2738b-firebase-adminsdk-mgedu-04c7819042.json")
    firebase_admin.initialize_app(cred, {"databaseURL": "https://cibus-2738b.firebaseio.com"})



    ref = db.reference('recipe')
    aa = ref.get(f"/{recipe}")[0]

    return {
        'statusCode': 200,
        'body': aa
    }