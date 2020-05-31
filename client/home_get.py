import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from datetime import date
import json

usuario = "brunoartc"


def handler_name(event, context): 
    event["body"] = json.loads(event["body"])
    usuario = event["body"]["usuario"]
    try:
        cred = credentials.Certificate("./cibus-2738b-firebase-adminsdk-mgedu-04c7819042.json")
        firebase_admin.initialize_app(cred, {"databaseURL": "https://cibus-2738b.firebaseio.com"})
    except :
        pass


    ref = db.reference('consumer')

    sv_normal = ref.get(f"stats/{usuario}/normal")
    sv_normal = sv_normal[0]["stats"][usuario]["normal"]
    print(sv_normal)

    sv = ref.get(f"stats/{usuario}/week/{date.today().isocalendar()[1]}")

    sv = sv[0]["stats"][usuario]["week"][str(date.today().isocalendar()[1])]
    print([{i:sv[i]/sv_normal[i]} for i in dict(sv_normal)])




    return {
        'statusCode': 200,
        'body': json.dumps(sv)
    }



