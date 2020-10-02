import pyrebase

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

filename = input("Enter filename: ")
cloudfilename = input("Enter filename of file on cloud: ")
storage.child(cloudfilename).put(filename)
