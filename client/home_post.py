import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from datetime import date

usuario = "brunoartc"
nutricional_info = "Carboidratos"
number = 20

cred = credentials.Certificate("./cibus-2738b-firebase-adminsdk-mgedu-04c7819042.json")
default_app = firebase_admin.initialize_app(cred, {"databaseURL": "https://cibus-2738b.firebaseio.com"})



ref = db.reference('consumer')




ref.child(f"stats/{usuario}/week/{date.today().isocalendar()[1]}/{nutricional_info}").set(20)

