import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from datetime import date

recipe = "producer"
user = "andre"
area = "AreaTomato"
wheight = 10
sample_area = 10   #m^2

ha = wheight*1000



cred = credentials.Certificate("./cibus-2738b-firebase-adminsdk-mgedu-04c7819042.json")
default_app = firebase_admin.initialize_app(cred, {"databaseURL": "https://cibus-2738b.firebaseio.com"})



ref = db.reference(f"producer/{user}/areas/{area}/Rendimento(ha)")
ref.set(f"{ha} kg/ha")