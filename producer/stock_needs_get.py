#Show stock needs

import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

def handler_name(event, context): 
    event["body"] = json.loads(event["body"])
    try:
        cred = credentials.Certificate("./cibus-2738b-firebase-adminsdk-mgedu-04c7819042.json")
        firebase_admin.initialize_app(cred, {"databaseURL": "https://cibus-2738b.firebaseio.com"})
    except :
        pass

    ref = db.reference("stock_needs")

    sv = ref.get()
    return {
        
        'statusCode': 200,
        'body': json.dumps(sv)
    }

#print {"banana":435}