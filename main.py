import pyrebase
import urllib
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

from School import School

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
db = firebase.database()
auth = firebase.auth()
storage = firebase.storage()

PATH = "./chromedriver"
driver = webdriver.Chrome(PATH)
driver.get("https://explorecourses.stanford.edu/")
print(driver.title)


try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "mainContent"))
    )

    departments = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "departmentsContainer"))
    )
    schools = departments.find_elements_by_tag_name("h2")
    # links = main_find_elements_by_
    # departments = main.find_elements_by_class_name("departmentsContainer")
    # subjects = departments.find_elements_by_tag_name("h2")
    subjects = departments.find_elements_by_tag_name("ul")
    links = departments.find_elements_by_tag_name("a")

    # for department in departments:


except:
    driver.quit()


# for school in schools:
# departmentName = school.text
# db.child("department").child(departmentName).set(departmentName)
# print(school.text)

listOfSubjects = {}
for i in range(len(schools)):
    schoolName = schools[i].text
    schoolID = i
    school = School(schoolName, schoolID, {})
    school.addSubjectsToSchool()


for subject in subjects:
    print(subject.text)


driver.quit()

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
# db = firebase.database()
# data = {"age": 40, "address": "new York", "employed": True, "name": "John Smith"}
# db.child("people").child("myownid").set(data)

# # Update UPDATE
# db.child("people").child("myownid").update({"name": "Mark"})

# people = db.child("people").get()
# # # to iterate, we must use .each()
# for person in people.each():
#     if person.val()["name"] == "Mark":
#         db.child("people").child(person.key()).update({"name": "Jane"})

# DELETE DATA
# db.child("people").child("myownid").child("age").remove()

# people = db.child("people").get()
# for person in people.each():
#     if person.val()["name"] == "Jane":
#         print("FOUND MARY")
#         db.child("people").child(person.key()).child("employed").remove()

# READ DATA:

# data1 = {"address": "LA", "age": 29, "employed": True, "name": "Jane"}
# data2 = {"address": "Boston", "age": 50, "employed": False, "name": "Timothy"}
# data3 = {"address": "fort Worth", "age": 17, "employed": True, "name": "Raven"}
# people = db.child("people").order_by_child("age").equal_to(50).get()
# people = (
#     db.child("people")
#     .order_by_child("age")
#     .start_at(17)
#     .end_at(30)
#     .limit_to_last(1)
#     .get()
# )

# start at is >=
# end at is <=


# for person in people.each():
#     print(person.val())

# we have to index the columns in the rules section so we can
# filter database entries.

