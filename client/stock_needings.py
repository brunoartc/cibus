import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from datetime import date

kit_name = "kit-foo"

cred = credentials.Certificate("./cibus-2738b-firebase-adminsdk-mgedu-04c7819042.json")
default_app = firebase_admin.initialize_app(cred, {"databaseURL": "https://cibus-2738b.firebaseio.com"})






ref = db.reference('kit')
aa = ref.get("/{kit_name}")[0][kit_name]['itens']


ref = db.reference('stock_needs')
today_stock = ref.get("/")[0]
print("aa", aa)
for i in dict(aa):
    print(i)
    ref.child(i).set(today_stock[i] + aa[i])



print(aa)