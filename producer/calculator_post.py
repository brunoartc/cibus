import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from datetime import date


def handler_name(event, context): 
    event["body"] = json.loads(event["body"])
    usuario = event["body"]["usuario"]
    wheight = int(event["body"]["wheight"])
    sample_area = int(event["body"]["sample_area"])
    area = event["body"]["area"]
    try:
        cred = credentials.Certificate("./cibus-2738b-firebase-adminsdk-mgedu-04c7819042.json")
        firebase_admin.initialize_app(cred, {"databaseURL": "https://cibus-2738b.firebaseio.com"})
    except :
        pass

    ha = (sample_area/wheight)*1000

    ref = db.reference(f"producer/{usuario}/areas/{area}/Profit(ha)")
    ref.set(f"{ha} kg/ha")
    return {
        
        'statusCode': 200,
        'body': json.dumps(ha)
    }
