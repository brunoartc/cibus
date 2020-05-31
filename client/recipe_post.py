import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from datetime import date

recipe = "bananada"

cred = credentials.Certificate("./cibus-2738b-firebase-adminsdk-mgedu-04c7819042.json")
default_app = firebase_admin.initialize_app(cred, {"databaseURL": "https://cibus-2738b.firebaseio.com"})



ref = db.reference('recipe')
aa = ref.get("/{recipe}")[0]

print(aa)