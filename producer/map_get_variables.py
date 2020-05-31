#Get details of specifc area

import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("../cibus-2738b-firebase-adminsdk-mgedu-04c7819042.json")
default_app = firebase_admin.initialize_app(cred, {"databaseURL": "https://cibus-2738b.firebaseio.com"})


usuario = "andre"
area = "AreaTomato"
ref = db.reference('producer')


sv = ref.child(f"{usuario}/areas/{area}").get()

#print: {'Area(m2)': 1000, 'Cultivated(m2)': 100, 'DateCultivated': '06/05/2020', 'DateHarvested': '06/05/2020', 'Harvested(t)': 1, 'Latitude': 20, 'Longitude': 60}