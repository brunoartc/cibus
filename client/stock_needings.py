import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from datetime import date
import json 


kit_name = "kit-foo"
usuario = "brunoartc"
def handler_name(event, context): 
    event["body"] = json.loads(event["body"])
    kit_name = event["body"]["kit_name"]
    usuario = event["body"]["usuario"]

    cred = credentials.Certificate("./cibus-2738b-firebase-adminsdk-mgedu-04c7819042.json")
    firebase_admin.initialize_app(cred, {"databaseURL": "https://cibus-2738b.firebaseio.com"})






    ref = db.reference('kit')
    aa = ref.get("/{kit_name}")[0][kit_name]['itens']


    ref = db.reference('orders')

    ref.push({"user" : usuario, "kit": kit_name, "date": date.today().isocalendar()})


    ref = db.reference('stock_needs')
    today_stock = ref.get("/")[0]
    print("aa", aa)
    for i in dict(aa):
        ref.child(i).set(today_stock[i] + aa[i])



    return {
            'statusCode': 200,
            'body': aa
        }