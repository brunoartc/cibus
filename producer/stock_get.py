#Get all stock

import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("../cibus-2738b-firebase-adminsdk-mgedu-04c7819042.json")
default_app = firebase_admin.initialize_app(cred, {"databaseURL": "https://cibus-2738b.firebaseio.com"})

ref = db.reference('producer')

usuario = "andre"


harvested = 0


dict_food= {}

sv = ref.child(f"{usuario}/areas_name").get()

for i in sv:
    harvested = int(ref.child(f"{usuario}/areas/{i}/Harvested(t)").get())
    type_food = ref.child(f"{usuario}/areas/{i}/type").get()
    dict_food[type_food] = harvested
dict_food[type_food]

ref.child(f"{usuario}/stock").set(dict_food)

#print total harvested per food {"tomato: 3", banana: 5}
