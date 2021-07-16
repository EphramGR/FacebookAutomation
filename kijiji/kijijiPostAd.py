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

from fake_useragent import UserAgent
import requests
from flask import Flask, session
#from flask.ext.session import Session

parser = argparse.ArgumentParser(description='Posting an ad to Facebook')
parser.add_argument('--addir',type=str, required=True, help='Diectory of the ad to post, this is where the .yaml files are, and the photos you want to post. The geckoDriver and Mozzila package should be in there as well.')
args = parser.parse_args()

fileDir = args.addir

try:
  os.chdir(fileDir)
except:
  print("ERROR 0001: Invalid directory")
  sys.exit()

try:
  with open('kijijiAd.yaml') as stream:
    adInfo = yaml.load(stream, yaml.FullLoader)
except:
  print("ERROR 0002: Could not locate the ad info yaml file")
  sys.exit()

try:
  options = Options()
  
  #ua = UserAgent()
  #userAgent = ua['Internet Explorer']
  #print(userAgent)
  #options.add_argument(f'--user-agent={userAgent}')
  
  driver = webdriver.Firefox(options=options) 
except:
  print("ERROR 0003: Either the Firefox or GeckoDriver directory was invalid")
  sys.exit()
  
email = adInfo['loginEmail']
password = adInfo['loginPassword']

ssidValue = "MTAyMzAzNzQwOHxleUowZVhBaU9pSktWMVFpTENKaGJHY2lPaUpJVXpVeE1pSjkuZXlKbGVIQWlPakUyTlRjNU9EUTBOalFzSW1saGRDSTZNVFl5TmpRME9EUTJOQ3dpYzNWaUlqb2lNVEF5TXpBek56UXdPQ0lzSW1WdFlXbHNJam9pYldGeWFIQmxNelpBWjIxaGFXd3VZMjl0SW4wLjJUMUtjUjBCZ1NZZGlrWUlrWkNXZ0dBbGw5NmtaOENHaGxiOFIxbTNGTmVPLUo0dmxJYU1tR2liYmlMYUg0UEoteWhiRU9ReUQ3NnFac0lGWXItS1Nn"

def ssid():

  #requestJar = requests.cookies.RequestsCookieJar()
  #requestJar.set("ssid", ssidValue, domain = 'https://www.kijiji.ca/', path = "/cookies")
  
  #ssid = {"ssid": ssidValue}
  #response = requests.get("https://www.kijiji.ca/", cookies=ssid)
  
  #print(response.content)
  
  try:
    driver.get("https://www.kijiji.ca/")
    driver.set_window_size(1527, 869)
  except:
    print("ERROR 0004: Could not go to given website")
    sys.exit()
  
  time.sleep(5)
  pyautogui.keyDown('ctrl')
  pyautogui.keyDown('shift')
  pyautogui.keyDown('i')
  
  pyautogui.keyUp('ctrl')
  pyautogui.keyUp('shift')
  pyautogui.keyUp('i')
  
  time.sleep(3)
  pyautogui.keyDown('shift')
  pyautogui.keyDown('f9')
  
  pyautogui.keyUp('shift')
  pyautogui.keyUp('f9')

  
  while True:
    print(pyautogui.position())
    time.sleep(3)
  
#def getPage():

#create new: (x=1395, y=691)
#adress name: (x=610, y=884)
#value: (x=666, y=883)
  
def login():
  try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Post ad"))
    )
    element.click()
  except:
    print("ERROR 0005: Could not find and click the Post Ad button")
    sys.exit()
      
  try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "emailOrNickname"))
    )
    element.click()
    element.send_keys(adInfo['loginEmail'])
  except:
    print("ERROR 0006: Could not input email")
    sys.exit()
    
  try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "password"))
    )
    element.click()
    element.send_keys(adInfo['loginPassword'])
  except:
    print("ERROR 0007: Could not input password")
    sys.exit()
    
  try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".signInButton-2798687440"))
    )
    element.click()
  except:
    print("ERROR 0008: Could not find and click the sign in button")
    sys.exit()
      

ssid()

#getPage()

#login()

