import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from datetime import date
import hashlib

import json


usuario = "brunoartc"
msg = "tal produto aconteceu tal coisa"
lote = "0000002"
assinatura = "ISSO FOI ASSINADO POR MIM MESMO"
from_products_lotes = []
def handler_name(event, context): 
    event["body"] = json.loads(event["body"])
    usuario = event["body"]["usuario"]
    msg = event["body"]["msg"]
    lote = event["body"]["lote"]
    assinatura = event["body"]["assinatura"]
    from_products_lotes = json.loads(event["body"]["assinatura"])

    cred = credentials.Certificate("./cibus-2738b-firebase-adminsdk-mgedu-04c7819042.json")
    default_app = firebase_admin.initialize_app(cred, {"databaseURL": "https://cibus-2738b.firebaseio.com"})

    ref = db.reference('lotes')
    try:
        last_hash = ref.get(lote)[0][lote]
    except KeyError as e:
        ref.child(lote).set(0)
        last_hash = "Toranja"
    print("AAAAAA", last_hash)
    ref = db.reference('blockchain')

    aaa = msg + usuario + lote + assinatura + last_hash + from_products_lotes
    ref.child(hashlib.sha256(aaa.encode("UTF-8")).hexdigest()).set(aaa)

    ref = db.reference('lotes')
    ref.child(lote).set(hashlib.sha256(aaa.encode("UTF-8")).hexdigest())
