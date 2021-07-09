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

#from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options

import time
import pyautogui

from selenium.webdriver.common.action_chains import ActionChains

import yaml, sys

import argparse
import os

parser = argparse.ArgumentParser(description='Posting an ad to Facebook')
parser.add_argument('--addir',type=str, help='Diectory of the ad to post, this is where the .yaml files are, and the photos you want to post. The geckoDriver and Mozzila package should be in there as well.')
args = parser.parse_args()

fileDir = args.addir

try:
  os.chdir(fileDir)
except:
  print("Invalid directory")

try:
  with open('marketplaceAd.yaml') as stream:
    adInfo = yaml.load(stream)
except:
  print("Could not locate the ad info yaml file")


title = adInfo['title']
price = adInfo['price']
description = adInfo['description']
productTags = adInfo['productTags']

option = Options()

driver = webdriver.Chrome(options=option)

sys.exit(1)


try:
  options = Options()
#  options.binary_location = adInfo['firefox']
  driver = webdriver.Chrome(options=options) ## executable_path=adInfo['geckoDriver'], 
except:
  print("ERROR 0001: Either the Firefox or GeckoDriver directory was invalid")
  sys.exit(1)

new = ".j83agx80 > .tojvnm2t > .oajrlxb2:nth-child(1)"
likeNew = ".tojvnm2t > .oajrlxb2:nth-child(2)"
good = ".oajrlxb2:nth-child(3) > .bp9cbjyn"
fair = ".oajrlxb2:nth-child(4) > .bp9cbjyn"

photos = []

for x in range(len(adInfo['photos'])):
  if x > 0:
    photos.append("\n")
  photos.append(os.getcwd())
  photos.append('\\')
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
  try:
    driver.get("https://www.facebook.com/")
    driver.set_window_size(1527, 869)
  except:
    print("Could not go to given website")

  try:
    driver.find_element(By.ID, "email").send_keys(email)
  except:
    print("Could not locate and/or send your given email to the email box")

  try:
    driver.find_element(By.ID, "pass").click()
    driver.find_element(By.ID, "pass").send_keys(password)
  except:
    print("Could not locate and/or send your given password to the password box")

  try:
    driver.find_element(By.NAME, "login").click()
  except:
    print("Could not locate and/or click the login box")


def gotoMarketplace():
  try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Marketplace"))
    )
    element.click()
  except:
    print("Could not find and click the Marketplace button")

  try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Create New Listing"))
    )
    element.click()
  except:
    print("Failed to navigate to create listing page")

  try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".sonix8o1:nth-child(1) .j83agx80 > .oajrlxb2 > .j83agx80 .bp9cbjyn"))
    )
    element.click()
  except:
    print("Failed to locate/click the 'item for sale' button")




def adTextboxes():
  try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//label/div/div/input"))
    )
    element.click()

    element.send_keys(title)
  except:
    print("Failed to input title into the title box")

  try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[5]/div/div/label/div/div/input"))
    )
    element.click()

    element.send_keys(price)
  except:
    print("Failed to input price into the price box")

  try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//textarea"))
    )
    element.click()

    element.send_keys(description)
  except:
    print("Failed to input description into the description box")
  try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[2]/textarea"))
    )
    element.click()

    for x in range(len(productTags)):
      element.send_keys(productTags[x])
      element.send_keys(Keys.ENTER)

  except:
    print("Failed to input the product tags")


def adDropdown():
  try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//label/div/div/div/div"))
    )
    element.click()

  except:
    print("Failed to click the category box")

  try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, category))
    )
    element.click()
  except:
    print("Failed to locate category: " + str(adInfo['category']))

  try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[7]/div/div/div/label/div/div/div/div"))
    )
    element.click()
  except:
    print("Failed to click the condtion box")

  try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, condition))
    )
    element.click()
  except:
    print("Failed to select the proper condition")

  if (adInfo['category'] == "Women's Clothing & Shoes" or adInfo['category'] == "Men's Clothing & Shoes") and adInfo['size'] != ".":
    try:
      element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[10]/div/div/label/div/div/input"))
      )
      element.click()
      element.send_keys(adInfo['size'])
    except:
      print("Failed to find or input the proper size")

  try:
    driver.find_element(By.XPATH, "//span/div/div/div/div/label/div/div/div/div").click()
    if adInfo['avalibility'] == 1:
      driver.find_element(By.CSS_SELECTOR, ".oi9244e8:nth-child(1) > .bp9cbjyn").click()
    elif adInfo['avalibility'] == 2:
      driver.find_element(By.CSS_SELECTOR, ".tojvnm2t > .oajrlxb2:nth-child(2)").click()
  except:
    print("Failed to locate and click the specified avaliblility")


def adPhotos():
  print(os.getcwd())

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
    print("Failed to navigate to the upload image screen")

  try:
    element.send_keys(photos)

    pyautogui.click(955, 21)
  except:
    print("Failed to send keys to the image uploader, and/or close it.")

def publish():
  time.sleep(3)
  try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".buofh1pr > .oajrlxb2 > .rq0escxv"))
    )
    element.click()
  except:
    print("Failed to locate and/or click publish button")


login()

gotoMarketplace()

adTextboxes()

adDropdown()

adPhotos()

#publish()

