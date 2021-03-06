from lib2to3.pgen2 import driver
from unicodedata import name
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def open_page():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("http://127.0.0.1:5500/Docs/index.html")
    return driver

def given_name(driver, name):
    name = driver.find_element(By.ID, "name_input").send_keys(name) 
    driver.find_element(By.ID, "submit_button").click()

def greetings(driver):
    hello_text = driver.find_element(By.ID, "message_p").text
    return hello_text

def test_sayhello():
    driver = open_page()
    given_name(driver, "John Doe")
    hello_text = greetings(driver)
    print(hello_text)
    assert hello_text == "Hello John Doe!"
