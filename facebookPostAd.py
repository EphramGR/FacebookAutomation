# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.firefox.options import Options

import time
import pyautogui

from selenium.webdriver.common.action_chains import ActionChains

import yaml

with open('marketplaceAd.yaml') as stream:
  adInfo = yaml.load(stream)

with open('dump.yaml') as stream:
  oldTitles = yaml.load(stream)

title = adInfo['title']
price = adInfo['price']
description = adInfo['description']
productTags = adInfo['productTags']

options = Options()
options.binary_location = adInfo['firefox']
driver = webdriver.Firefox(executable_path=adInfo['geckoDriver'], firefox_options=options)

new = ".j83agx80 > .tojvnm2t > .oajrlxb2:nth-child(1)"
likeNew = ".tojvnm2t > .oajrlxb2:nth-child(2)"
good = ".oajrlxb2:nth-child(3) > .bp9cbjyn"
fair = ".oajrlxb2:nth-child(4) > .bp9cbjyn"

photos = []

for x in range(len(adInfo['photos'])):
  if x > 0:
    photos.append("\n")
  photos.append(adInfo['photos'][x])

for x in range(len(adInfo['categories'])):
  if adInfo['categories'][x] == adInfo['category']:
    category = adInfo['categoriesTag'][x]

if adInfo['condition'] == 1:
  condition = new
elif adInfo['condition'] == 2:
  condition = likeNew
elif adInfo['condition'] == 3:
  condition = good
elif adInfo['condition'] == 4:
  condition = fair

email = adInfo['loginEmail']
password = adInfo['loginPassword']

def login():
  driver.get("https://www.facebook.com/")
  driver.set_window_size(1527, 869)
  driver.find_element(By.ID, "email").send_keys(email)
  driver.find_element(By.ID, "pass").click()
  driver.find_element(By.ID, "pass").send_keys(password)
  driver.find_element(By.NAME, "login").click()


def gotoMarketplace():
  try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Marketplace"))
    )
    element.click()

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Create New Listing"))
    )
    element.click() 

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".sonix8o1:nth-child(1) .j83agx80 > .oajrlxb2 > .j83agx80 .bp9cbjyn"))
    )
    element.click() 

  except:
    print("oops")


def adTextboxes():
  try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//label/div/div/input"))
    )
    element.click()
  
    element.send_keys(title)

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[5]/div/div/label/div/div/input"))
    )
    element.click()

    element.send_keys(price)

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//textarea"))
    )
    element.click() 

    element.send_keys(description)

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[2]/textarea"))
    )
    element.click() 

    for x in range(len(productTags)):
      element.send_keys(productTags[x])
      element.send_keys(Keys.ENTER)

  except:
    print("oops2")


def adDropdown():
  try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//label/div/div/div/div"))
    )
    element.click()

  except:
    print("oops2")

  driver.find_element(By.CSS_SELECTOR, category).click()
  driver.find_element(By.XPATH, "//div[7]/div/div/div/label/div/div/div/div").click()

  try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, condition))
    )
    element.click()
  except:
    print("oops7")

  if (adInfo['category'] == "Women's Clothing & Shoes" or adInfo['category'] == "Men's Clothing & Shoes") and adInfo['size'] != ".":
    try:
      element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[10]/div/div/label/div/div/input"))
      )
      element.click()
      element.send_keys(adInfo['size'])
    except:
      print("oops3")

  driver.find_element(By.XPATH, "//span/div/div/div/div/label/div/div/div/div").click()
  if adInfo['avalibility'] == 1:
    driver.find_element(By.CSS_SELECTOR, ".oi9244e8:nth-child(1) > .bp9cbjyn").click()
  elif adInfo['avalibility'] == 2:
    driver.find_element(By.CSS_SELECTOR, ".tojvnm2t > .oajrlxb2:nth-child(2)").click()


def adPhotos():

  try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//label/div/div/input"))
    )
    element.click()

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[3]/div/div[2]/div/div/div[3]/div[2]/div/div/div"))
        )

    element.click()

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
        )

  except:
    print("oops4")

  element.send_keys(photos)

  pyautogui.click(955, 21) 

def publish():
  time.sleep(3)
  try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".buofh1pr > .oajrlxb2 > .rq0escxv"))
    )
    element.click()
  except:
    print("oops5")
    
  write_yaml()


def write_yaml():
  oldTitles['previousTitles'].append(title)
  with open("dump.yaml", 'w') as stream:
    try:
      yaml.dump(oldTitles, stream)
    except:
      print("oops6")


login()

gotoMarketplace()

adTextboxes()

adDropdown()

adPhotos()

publish()

