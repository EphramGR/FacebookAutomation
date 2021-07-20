#cd FacebookAutomation, python3 facebookPostAd.py --addir testItem
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
#from selenium.webdriver.chrome.options import Options

import time
import pyautogui

from selenium.webdriver.common.action_chains import ActionChains

import yaml, sys

import argparse
import os

parser = argparse.ArgumentParser(description='Posting an ad to Facebook')
parser.add_argument('--addir',type=str, required=True, nargs="+", help='Diectory of the ad to post, this is where the .yaml files are, and the photos you want to post. There can be multiple folders for multiple ads.')
args = parser.parse_args()

fileDir = args.addir

cwd = os.getcwd()

try:
  os.chdir(fileDir[0])
except:
  print("ERROR 0001: Invalid directory")
  sys.exit()

try:
  options = Options()
  driver = webdriver.Firefox(options=options) 
except:
  print("ERROR 0003: Either the Firefox or GeckoDriver directory was invalid")
  sys.exit()

new = ".j83agx80 > .tojvnm2t > .oajrlxb2:nth-child(1)"
likeNew = ".tojvnm2t > .oajrlxb2:nth-child(2)"
good = ".oajrlxb2:nth-child(3) > .bp9cbjyn"
air = ".oajrlxb2:nth-child(4) > .bp9cbjyn"

adInfo = ' '
title = ' '
price = ' '
description = ' '
productTags = []
photos = []
category = ' '
condition = ' '
email = ' '
password = ' '

def setVar():
  global adInfo, title, price, description, productTags, photos, category, condition, email, password
  try:
    with open('marketplaceAd.yaml') as stream:
      adInfo = yaml.load(stream, yaml.FullLoader)
  except:
    print("ERROR 0002: Could not locate the ad info yaml file")
    sys.exit()

  title = adInfo['title']
  price = adInfo['price']
  description = adInfo['description']
  productTags = adInfo['productTags']

  photos = [[],[],[],[],[],[],[],[],[],[]]

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
  try:
    driver.get("https://www.facebook.com/")
    driver.set_window_size(1527, 869)
  except:
    print("ERROR 0004: Could not go to given website")
    sys.exit()

  try:
    driver.find_element(By.ID, "email").send_keys(email)
  except:
    print("ERROR 0005: Could not locate and/or send your given email to the email box")
    sys.exit()

  try:
    driver.find_element(By.ID, "pass").click()
    driver.find_element(By.ID, "pass").send_keys(password)
  except:
    print("ERROR 0006: Could not locate and/or send your given password to the password box")
    sys.exit()

  try:
    driver.find_element(By.NAME, "login").click()
  except:
    print("ERROR 0007: Could not locate and/or click the login box")
    sys.exit()


def gotoMarketplace():

  try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Marketplace"))
    )
    element.click()
  except:
    print("ERROR 0008: Could not find and click the Marketplace button")
    sys.exit()

  try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Create New Listing"))
        
    )
    element.click()
  except:
    print("ERROR 0009: Failed to navigate to create listing page")
    sys.exit()

  try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span/div/a/div/div/div"))
    )
    element.click()
  except:
    print("ERROR 0010: Failed to locate/click the 'item for sale' button")
    sys.exit()



def adTextboxes():
  try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//label/div/div/input"))
    )
    element.click()

    element.send_keys(title)
  except:
    print("ERROR 0011: Failed to input title into the title box")
    sys.exit()

  try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[5]/div/div/label/div/div/input"))
    )
    element.click()

    element.send_keys(price)
  except:
    print("ERROR 0012: Failed to input price into the price box")
    sys.exit()

  try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//textarea"))
    )
    element.click()

    element.send_keys(description)
  except:
    print("ERROR 0013: Failed to input description into the description box")
    
  try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[2]/textarea"))
    )
    element.click()

    for x in range(len(productTags)):
      element.send_keys(productTags[x])
      element.send_keys(Keys.ENTER)

  except:
    print("ERROR 0014: Failed to input the product tags")


def adDropdown():
  try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//label/div/div/div/div"))
    )
    element.click()

  except:
    print("ERROR 0015: Failed to click the category box")
    sys.exit()

  try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, category))
    )
    element.click()
  except:
    print("ERROR 0016: Failed to locate category: " + str(adInfo['category']))
    sys.exit()

  try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[7]/div/div/div/label/div/div/div/div"))
    )
    element.click()
  except:
    print("ERROR 0017: Failed to click the condtion box")
    sys.exit()

  try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, condition))
    )
    element.click()
  except:
    print("ERROR 0018: Failed to select the proper condition")
    sys.exit()

  if (adInfo['category'] == "Women's Clothing & Shoes" or adInfo['category'] == "Men's Clothing & Shoes") and adInfo['size'] != ".":
    try:
      element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[10]/div/div/label/div/div/input"))
      )
      element.click()
      element.send_keys(adInfo['size'])
    except:
      print("ERROR 0019: Failed to find or input the proper size")

  try:
    driver.find_element(By.XPATH, "//span/div/div/div/div/label/div/div/div/div").click()
    if adInfo['avalibility'] == 1:
      driver.find_element(By.CSS_SELECTOR, ".oi9244e8:nth-child(1) > .bp9cbjyn").click()
    elif adInfo['avalibility'] == 2:
      driver.find_element(By.CSS_SELECTOR, ".tojvnm2t > .oajrlxb2:nth-child(2)").click()
  except:
    print("ERROR 0020: Failed to locate and click the specified avaliblility")


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
    print("ERROR 0021: Failed to navigate to the upload image screen")
    sys.exit()

  f = []

  for x in range(len(adInfo['photos'])):
    photos[x].append(os.getcwd())
    photos[x].append('/')
    photos[x].append(adInfo['photos'][x])
    photos[x].append('/')

    h = ''.join(photos[x])
    f.append(h)
    
  try:
    for x in range(len(adInfo['photos'])):
      g = ''.join(f[x])
      element.send_keys(g)
      time.sleep(0.2)
    
      if x == 0:
        pyautogui.press('escape')
        time.sleep(0.2)    
      try:
        if x != len(adInfo['photos']):
          for y in range(x):
            driver.find_element(By.XPATH, "//div[2]/div/div/div/div/div[2]/div/div/i").click()
            time.sleep(0.2)
      except:
        print("ERROR 0022: Failed to close duplicated photos")
        sys.exit()
  except:
    print("ERROR 0023: Failed to send keys to the image uploader, and/or close it.")
    sys.exit()

def publish():
  time.sleep(3)
  try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".buofh1pr > .oajrlxb2 > .rq0escxv"))
    )
    element.click()
  except:
    print("ERROR 0024: Failed to locate and/or click publish button")
    sys.exit()
    
def home():
  try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[3]/div/div[2]/div/div/div[3]/div[2]/div/div/div"))
        )

    element.click()
  except:
    print("ERROR 0025: Failed to click home button")


def changeCWD():
  os.chdir(cwd)
  os.chdir(fileDir[x])

for x in range(len(fileDir)):
  if x > 0:
    changeCWD()
    home()
    
  setVar()
  
  if x == 0:
    login()

  gotoMarketplace()

  adTextboxes()

  adDropdown()

  adPhotos()

  publish()
  
  try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[3]/div/div[2]/div/div/div[3]/div[2]/div/div/div"))
        )
  except:
    print("ERROR 0026: Failed to locate home button")
  
  if x == (len(fileDir) - 1):
    driver.quit()

