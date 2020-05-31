#Sell stock needs

import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("../cibus-2738b-firebase-adminsdk-mgedu-04c7819042.json")
default_app = firebase_admin.initialize_app(cred, {"databaseURL": "https://cibus-2738b.firebaseio.com"})

selling = 1
food = "tomato"
usuario = "andre"

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
    else:
        print("Voce nao tem quantidade suficiente")
else:
    print("Voce nao tem no estoque")




#print {"banana":435}