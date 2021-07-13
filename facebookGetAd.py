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
parser.add_argument('--addir',type=str, help='Diectory of the folder with yhe .yaml file for your login info, and the dump.yaml file.')
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
    
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".bi6gxh9e > .oajrlxb2 > .rq0escxv"))
    )
    element.click() 

  except:
    print("oops")

def getAds():
  time.sleep(1)
  x = True
  y = 1
  while x == True:
    try:
      element = WebDriverWait(driver, 5).until(
          EC.presence_of_element_located((By.XPATH, "//div[3]/div/span/div/div[y]/div"))
      )
      element.click()
      pyautogui.press('escape')
    except:
      x = False
      print("TestFailed")
      
    y += 1


#After manage my listings:
#//div[3]/div/span/div/div[x+1]/div

login()
gotoMarketplace()
getAds()

#while loop try test for all of them div[0 + 1 each time]
#grabs info
#if error except: outta while loop
