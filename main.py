import pyrebase
import urllib

firebaseConfig = {
    "apiKey": "AIzaSyD7yguTY2u6iGiHKQOCUo-QARhpuslMwrU",
    "authDomain": "rolodeck-a782f.firebaseapp.com",
    "databaseURL": "https://rolodeck-a782f.firebaseio.com",
    "projectId": "rolodeck-a782f",
    "storageBucket": "rolodeck-a782f.appspot.com",
    "messagingSenderId": "55154756730",
    "appId": "1:55154756730:web:5c14df8a40fb0c68d27fc3",
}

firebase = pyrebase.initialize_app(firebaseConfig)

auth = firebase.auth()
storage = firebase.storage()

# email = input("email?:")
# password = input("password?:")
# try:
#     auth.sign_in_with_email_and_password(email, password)
#     print("success")
# except:
#     print("invalid user or password. try again")


# # Signup
# email = input("Enter email: ")
# password = input("Enter your password: ")
# confirmpass = input("Confirm password: ")
# if password == confirmpass:
#     try:
#         auth.create_user_with_email_and_password(email, password)
#         print("Success!")
#     except:
#         print("Email already exists")

# Storage
# file is which file i want to upload.
# cloudfile name is just the name in the database. for ex: hello.txt on local computer. i could say its actually mainText.txt and that's what the db will say

# UPLOAD
# filename = input("Enter filename: ")
# cloudfilename = input("Enter filename of file on cloud: ")
# storage.child(cloudfilename).put(filename)

# print(storage.child(cloudfilename).get_url(None))

# DOWNLOAD
# how to get a file from the cloud
# cloudfilename = input("Enter the name of file I want to download: ")
# storage.child(cloudfilename).download("", "downloaded.txt")
# first entry is empty string because this is the directory we are downloadinig it.


# reading file
# cloudfilename = input("Enter the name of file you want to download: ")
# url = storage.child(cloudfilename).get_url(None)
# f = urllib.request.urlopen(url).read()
# print(f)


# DATABASE
db = firebase.database()
# data = {"age": 40, "address": "new York", "employed": True, "name": "John Smith"}
# db.child("people").child("myownid").set(data)

# # Update UPDATE
# db.child("people").child("myownid").update({"name": "Mark"})

# people = db.child("people").get()
# # # to iterate, we must use .each()
# for person in people.each():
#     if person.val()["name"] == "Mark":
#         db.child("people").child(person.key()).update({"name": "Jane"})

