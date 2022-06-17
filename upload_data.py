import firebase_config as token
import pyrebase

firebase = pyrebase.initialize_app(token.firebaseConfig)
auth = firebase.auth()
db = firebase.database()
storage = firebase.storage()
name = "asdfghjkl"
email = "asdf@ghjk.com"
password = "6985425685"
image = input("/static/images/image.jpg")

user= auth.create_user_with_email_and_password(email, password)
id = user['localId']
print(id)
data = {
    "name": name,
    "email": email
}

db.child("users").child(id).child("data_user").set(data)
storage.child("users", "/", id, "/data_user/profile.jpg").put(image)