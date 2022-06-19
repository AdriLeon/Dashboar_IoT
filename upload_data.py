import firebase_config as token
import pyrebase

firebase = pyrebase.initialize_app(token.firebaseConfig)
auth = firebase.auth()
db = firebase.database()
storage = firebase.storage()
name = "asdjughjkl"
email = "aosf@ghjk.com"
password = "6985425685"
image = "static\images\image.jpg"


id = "9p5QrpT7NKOHw64RUsNZB1hPGPL2"
print(id)
data = {
    "name": name,
    "email": email
}

db.child("users").child(id).child("data_user").update(data)
storage.child("users").child(id).child("data_user/profile.jpg").put(image)
url = storage.child("users").child(id).child("data_user/profile.jpg").get_url(id)
print(url)