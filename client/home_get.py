import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from datetime import date

usuario = "brunoartc"

cred = credentials.Certificate("./cibus-2738b-firebase-adminsdk-mgedu-04c7819042.json")
default_app = firebase_admin.initialize_app(cred, {"databaseURL": "https://cibus-2738b.firebaseio.com"})
sv_normal = {
    "Carboidratos" : 300*7,
    "Proteínas" : 75*7,
    "Gorduras Totais": 55*7,
    "Gorduras Saturadas": 22*7,
    "Fibra Alimentar": 25*7,
    "Sódio": 2.4*7
}
ref = db.reference('consumer')

sv = ref.get(f"stats/{usuario}/week/{date.today().isocalendar()[1]}")

sv = sv[0]["stats"][usuario]["week"][str(date.today().isocalendar()[1])]
print([{i:sv[i]/sv_normal[i]} for i in dict(sv_normal)])



#ref.child(f"stats/{usuario}/week/{date.today().isocalendar()[1]}").set(sv_normal)



