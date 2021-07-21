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
parser.add_argument('--addir',type=str, help='Diectory of the folder with the .yaml file for your login info, and the dump.yaml file.')
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
        EC.presence_of_element_located((By.LINK_TEXT, "Your Account"))
    )
    element.click()  

  except:
    print("oops")

def getAds():

  try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[2]/div/div[2]/div/div[2]/div/div[4]/div/div/div")) 
    )
    element.click()
  except:
    print("oops2")
    
  #driver.find_element(By.XPATH, "//div[2]/div/div[2]/div/div[2]/div/div[4]/div/div/div").click() #ad one
  #driver.find_element(By.XPATH, "//div[3]/div/div[2]/div/div[2]/div/div[4]/div/div/div").click() #ad two
  #driver.find_element(By.XPATH, "//div[x]/div/div[2]/div/div[2]/div/div[4]/div/div/div").click() #ad swap
  
  try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Edit Listing")) 
    )
    element.click()
  except:
    print("oops3")
    
  try:
    title = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div/input")) 
    )
  except:
    print("oops4")
  
  titleValue = title.get_attribute("value"); 
  print(titleValue)

  try:
    price = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[5]/div/div/label/div/div/input")) 
    )
  except:
    print("oops5")
    
  priceValue = price.get_attribute("value"); 
  print(priceValue)
  
  try:
    desc = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//textarea")) 
    )
  except:
    print("oops6")

  descValue = desc.get_attribute("value");
  print(descValue)

  try:
    condition = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[7]/div/div/div/label/div/div/div/div/span")) 
    )
  except:
    print("oops7")

  conditionValue = condition.get_attribute("innerText");
  print(conditionValue)

  try:
    category = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//label/div/div/div/div/span")) 
    )
  except:
    print("oops8")

  categoryValue = category.get_attribute("innerText");
  print(categoryValue)

  imageValue = ['','','','','','','','','','']
  for x in range(10):
    if x == 0:
      try:
        image = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[3]/div[2]/div/div/div/div/div/img")) 
        )
      except:
        print("oops9 ", x)

    imagePathBroke = "//div[", str(x + 1), "]/div/div/div/img"
    imagePathJoin = ''.join(imagePathBroke)

    if x > 0:
      try:
        image = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, imagePathJoin)) 
        )
      except:
        break   
    

    imageValue[x] = image.get_attribute("src");
  print(imageValue)

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
        print("oops10 ", x)

    tagPathBroke = "//div[", str(x), "]/div/span/span"
    tagPathJoin = ''.join(tagPathBroke)

    if x > 1:
      try:
        tag = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, tagPathJoin)) 
        )
      except:
        break   
        
    tagValue.append(tag.get_attribute("innerText"))
      
  print(tagValue)
  
  try:
    stock = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span/div/div/div/div/label/div/div/div/div/span")) 
    )
  except:
    print("oops11")
    
  stockValue = stock.get_attribute("innerText"); 
  print(stockValue)

login()
gotoMarketplace()
getAds()


