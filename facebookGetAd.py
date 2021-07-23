#python3 facebookGetAd.py --addir testItem
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

import yaml, sys

import argparse
import os

parser = argparse.ArgumentParser(description='Deleting an ad off Facebook')
parser.add_argument('--addir',type=str, help='Diectory of the folder with the .yaml file for your login info, and where you want the dump.yaml files to be created.')
args = parser.parse_args()

fileDir = args.addir

try:
  os.chdir(fileDir)
except:
  print("Invalid directory")

with open('marketplaceAd.yaml') as stream:
  adInfo = yaml.load(stream, yaml.FullLoader)

try:
  options = Options()
  driver = webdriver.Firefox(options=options)
except:
  print("Either the Firefox or GeckoDriver directory was invalid")

email = adInfo['loginEmail']
password = adInfo['loginPassword']

titleValue = ''
priceValue = ''
descValue = ''
conditionValue = ''
categoryValue = ''
imageValue = ''
tagValue = ''
stockValue = ''
adFile = ''
moreAds = True
counter = 0

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
    print("ERROR 0008: Could not locate and/or click the marketplace button")
    sys.exit()
  try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Your Account"))
    )
    element.click()  

  except:
    print("ERROR 0009: Could not locate and/or click the 'Your Account' button")
    sys.exit()

def getAds():
  global titleValue, priceValue, descValue, conditionValue, categoryValue, imageValue, tagValue, stockValue, counter, moreAds

  specificAdBroke = "//div[", str(counter + 1), "]/div/div[2]/div/div[2]/div/div[4]/div/div/div"
  specificAd = ''.join(specificAdBroke)

  try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, specificAd)) 
    )
    element.click()
  except:
    if counter == 1:
      print("ERROR 0010: Could not locate any posted ads")
      sys.exit()
    moreAds = False
    return
    
  
  try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Edit Listing")) 
    )
    element.click()
  except:
    print("ERROR 0011: Could not locate and/or click the edit listing button")
    sys.exit()
    
  try:
    title = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div/input")) 
    )
  except:
    print("ERROR 0012: Could not locate the title value")
    sys.exit()
  
  titleValue = title.get_attribute("value"); 

  try:
    price = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[5]/div/div/label/div/div/input")) 
    )
  except:
    print("ERROR 0013: Could not locate the price value")
    sys.exit()
    
  priceValue = price.get_attribute("value"); 
  
  try:
    desc = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//textarea")) 
    )
  except:
    print("ERROR 0014: Could not locate the description value")
    sys.exit()

  descValue = desc.get_attribute("value");

  try:
    condition = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[7]/div/div/div/label/div/div/div/div/span")) 
    )
  except:
    print("ERROR 0015: Could not locate the condition value")
    sys.exit()

  conditionValue = condition.get_attribute("innerText");

  try:
    category = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//label/div/div/div/div/span")) 
    )
  except:
    print("ERROR 0016: Could not locate the category value")
    sys.exit()

  categoryValue = category.get_attribute("innerText");

  imageValue = []
  for x in range(10):
    if x == 0:
      try:
        image = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[3]/div[2]/div/div/div/div/div/img")) 
        )
      except:
        print("ERROR 0017: Could not locate a single image")
        sys.exit()

    imagePathBroke = "//div[", str(x + 1), "]/div/div/div/img"
    imagePathJoin = ''.join(imagePathBroke)

    if x > 0:
      try:
        image = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, imagePathJoin)) 
        )
      except:
        break   
    imageValue.append(image.get_attribute("src"))

  y = True
  x = 0
  tagValue = []
  while y == True:
    x += 1
    if x == 1:
      try:
        tag = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label/div/div/div/div/div/div/div/span/span")) 
        )
      except:
        print("ERROR 0018: Could not locate a single tag.")
        print("If your ad does not have tags ignore this error message")

    tagPathBroke = "//div[", str(x), "]/div/span/span"
    tagPathJoin = ''.join(tagPathBroke)

    if x > 1:
      try:
        tag = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, tagPathJoin)) 
        )
      except:
        break    
    try: 
      tagValue.append(tag.get_attribute("innerText"))
    except:
      tagValue.append("None")
  
  try:
    stock = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span/div/div/div/div/label/div/div/div/div/span")) 
    )
  except:
    print("ERROR 0019: Could not locate the stock value")
    sys.exit()
    
  stockValue = stock.get_attribute("innerText"); 

def makeAdFile():
  global adFile
  adFile = [{'title': titleValue}, {'price': priceValue}, {'description': descValue}, {'condition': conditionValue}, {'category': categoryValue}, {'photos': imageValue}, {'tags': tagValue}, {'stock': stockValue}]

def dump():
  global counter, adFile
  
  yamlBroke = 'adDump', str(counter), '.yaml'
  yamlJoin = ''.join(yamlBroke)

  try:
    with open(yamlJoin, 'x') as file:
      documents = yaml.dump(adFile, file)
  except:
    print("ERROR 0020: Could not create ", str(yamlJoin), " file. If this file already exists in your directory, delete it and try again")
    sys.exit()

login()
gotoMarketplace()
while moreAds == True:
  counter += 1
  getAds()
  if moreAds == False:
    break
  makeAdFile()
  dump()
  
  pyautogui.keyDown('alt')
  pyautogui.press('left')
  pyautogui.keyUp('alt')
  
sys.exit()



