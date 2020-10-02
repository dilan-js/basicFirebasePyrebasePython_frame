import pyrebase
import urllib
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time


class School:
    def __init__(self, name, id, listOfSubjects):
        self.name = name
        self.id = id
        self.listOfSubjects = listOfSubjects

    def addSubjectsToSchool(self):
        print(f"This is the school name and id: {self.name},{self.id}")

