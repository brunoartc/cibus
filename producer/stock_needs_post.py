#Sell stock needs

import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

def handler_name(event, context): 
    event["body"] = json.loads(event["body"])
    usuario = event["body"]["usuario"]
    selling = int(event["body"]["selling"])
    food = event["body"]["food"]
    area = event["body"]["area"]
    try:
        cred = credentials.Certificate("./cibus-2738b-firebase-adminsdk-mgedu-04c7819042.json")
        firebase_admin.initialize_app(cred, {"databaseURL": "https://cibus-2738b.firebaseio.com"})
    except :
        pass

    ref = db.reference("stock_needs")

    #total of needs of food
    food_stock_needs = ref.child(f"{food}").get()

    ref_2 = db.reference("producer")
    food_stock = ref_2.child(f"{usuario}/stock/{food}").get()

    if food_stock:
        if food_stock >= selling:
            food_stock = food_stock - selling
            food_stock_needs = food_stock_needs - selling
            ref_2.child(f"{usuario}/stock/{food}").set(food_stock)
            ref.child(f"{food}").set(food_stock_needs)
            return {
        
                'statusCode': 200,
                'body': f"You have sold {selling}"
            }


        else:
            return {
        
                'statusCode': 300,
                'body': "You don't have enough in stock"
            }
            
    else:
        return {
        
            'statusCode': 300,
            'body': "You don't have this product in stock"
        }



#print {"banana":435}