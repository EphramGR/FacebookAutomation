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

import yaml, sys

import argparse
import os

parser = argparse.ArgumentParser(description='Deleting an ad off Facebook')
parser.add_argument('--addir',type=str, nargs="+", help='Diectory of the ad to delete, this is where the .yaml files are, and the photos you wanted to post. The geckoDriver and Mozzila package should be in there as well.')
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
  print("ERROR 0002: Either the Firefox or GeckoDriver directory was invalid")
  sys.exit()

adInfo = ' '
email = ' '
password = ' '
adRemove = ' '
fourButtons = False

def setVar():
  global adInfo, email, password, adRemove, fourButtons
  
  with open('marketplaceAd.yaml') as stream:
    adInfo = yaml.load(stream, yaml.FullLoader)


  email = adInfo['loginEmail']
  password = adInfo['loginPassword']

  adRemove = "//div[@aria-label=\'" + str(adInfo['title']) + "\']"

  fourButtons = False

def login():
  try:
    driver.get("https://www.facebook.com/")
    driver.set_window_size(1527, 869)
  except:
    print("ERROR 0003: Could not go to given website")
    sys.exit()

  try:
    driver.find_element(By.ID, "email").send_keys(email)
  except:
    print("ERROR 0004: Could not locate and/or send your given email to the email box")
    sys.exit()

  try:
    driver.find_element(By.ID, "pass").click()
    driver.find_element(By.ID, "pass").send_keys(password)
  except:
    print("ERROR 0005: Could not locate and/or send your given password to the password box")
    sys.exit()

  try:
    driver.find_element(By.NAME, "login").click()
  except:
    print("ERROR 0006: Could not locate and/or click the login box")
    sys.exit()


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
    print("ERROR 0007: Could not navigate to marketplace and/or your account")
    sys.exit()

def removeAd():
  global fourButtons
  try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, adRemove))
    )
    element.click()
  except:
    print("ERROR 0008: Could not find the ad that you want removed")
    sys.exit()
  try:
    element = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".oqcyycmt:nth-child(4) > .oajrlxb2"))
    )
    fourButtons = True
  except:
    try:
      element = WebDriverWait(driver, 10).until(
          EC.presence_of_element_located((By.CSS_SELECTOR, ".oqcyycmt:nth-child(2) > .oajrlxb2"))
      )
      element.click()
    except:
      print("ERROR 0009: Could not locate delete button")
      sys.exit()
  if fourButtons == True:
    try:
      element = WebDriverWait(driver, 10).until(
          EC.presence_of_element_located((By.CSS_SELECTOR, ".oqcyycmt:nth-child(3) > .oajrlxb2"))
      )
      element.click()
    except:
      print("ERROR 0010: Could not locate delete button")
      sys.exit()
      
  try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[4]/div/div/div/div/div/div/span/span"))
    )
    element.click()

  except:
    print("ERROR 0011: Could not confirm delete")
    sys.exit()
    
def changeCWD():
  os.chdir(cwd)
  os.chdir(fileDir[x])

def home():
  try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span/div/a"))
        )

    element.click()
  except:
    print("ERROR 0025: Failed to click home button")
  
for x in range(len(fileDir)):
  if x > 0:
    changeCWD()
    home()
    
  setVar()
  
  if x == 0:
    login()
  
  gotoMarketplace()

  removeAd()
  
  time.sleep(2)
  
  if x == ((len(fileDir)) - 1):
    driver.quit()
  
  

