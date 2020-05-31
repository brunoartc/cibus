#Get all existent areas of user

import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("../cibus-2738b-firebase-adminsdk-mgedu-04c7819042.json")
default_app = firebase_admin.initialize_app(cred, {"databaseURL": "https://cibus-2738b.firebaseio.com"})

usuario = "andre"
ref = db.reference("producer")


sv = ref.child(f"{usuario}/areas_name").get()

#print: ['AreaTomato']