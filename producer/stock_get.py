#Get all stock

import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


def handler_name(event, context): 
    event["body"] = json.loads(event["body"])
    usuario = event["body"]["usuario"]
    try:
        cred = credentials.Certificate("./cibus-2738b-firebase-adminsdk-mgedu-04c7819042.json")
        firebase_admin.initialize_app(cred, {"databaseURL": "https://cibus-2738b.firebaseio.com"})
    except :
        pass

    ref = db.reference('producer')

    harvested = 0
    dict_food= {}

    sv = ref.child(f"{usuario}/areas_name").get()

    for i in sv:
        harvested = int(ref.child(f"{usuario}/areas/{i}/Harvested(t)").get())
        type_food = ref.child(f"{usuario}/areas/{i}/type").get()
        dict_food[type_food] = harvested

    ref.child(f"{usuario}/stock").set(dict_food)
    return {
        
        'statusCode': 200,
        'body': json.dumps(dict_food)
    }

#print total harvested per food {"tomato: 3", banana: 5}
