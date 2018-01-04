

from datetime import *  
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#import win32gui
import os
from selenium.webdriver.support.ui import Select
import getpass, poplib
#import win32con
import time,platform,sys, getopt,paramiko,random,re
#import socks  
#import socket 
#import requests
import io
import sys
#import urllib.request

from selenium.webdriver.chrome.options import Options





#back=socket.socket
#socks.set_default_proxy(socks.SOCKS5, "127.0.0.1",1080)
#print(requests.get('http://ifconfig.me/ip').text)



url=""
argv=sys.argv[1:]
try:
  opts, args = getopt.getopt(argv,"i:")
except getopt.GetoptError:
  print ('test.py -i <inputfile> -o <outputfile>')
  sys.exit(2)
for opt, arg in opts:
  if opt in ("-i","--invite"):
    url = arg
    print (url)

def mail():
  email = 'a@iigogo.com'
  password = 'jmdjsj903291A'
  pop3_server ='pop.exmail.qq.com'
  server = poplib.POP3(pop3_server)
  server.set_debuglevel(1)
  print(server.getwelcome().decode('utf-8'))
  server.user(email)
  server.pass_(password)
  print('Messages: %s. Size: %s' % server.stat())
  resp, mails, octets = server.list()
  print(mails)
  index = len(mails)
  resp, lines, octets = server.retr(index)
  msg_content = b'\r\n'.join(lines).decode('utf-8')
  msg = Parser().parsestr(msg_content)
  a=print_info(msg)
  # server.dele(index)
  server.quit()
  return a

def login(root,passwd):


  url1="http://8.laicunba.com/login.jsp"
  d.get(url1)
  time.sleep(9)
  d.find_element_by_css_selector("#loginName").send_keys(root)
  d.find_element_by_css_selector("#loginPwd").send_keys(passwd)
  time.sleep(10)
def loginypy(root,passwd):


  url1="https://console.upyun.com/login/"
  d.get(url1)
  d.find_element_by_css_selector("#username").send_keys(root)
  d.find_element_by_css_selector("#password").send_keys(passwd)
  d.find_element_by_css_selector("#submit").click()
  time.sleep(1)

  url1="https://console.upyun.com/billing/charge/"
  d.get(url1) 
  time.sleep(5)
  yue=d.find_element_by_css_selector("usagevalue > span").text
  matchObj = re.search( r'(\d*)',yue, re.M|re.I)
  print (yue)
  print (matchObj.group(1))
  d.quit()

  

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
#login("root","root")
#update("360sz_20202")
if platform.system()=="Linux":
  d = webdriver.PhantomJS()
else:
  d = webdriver.Chrome(chrome_options=chrome_options )
  d.implicitly_wait(30)

print (url)


loginypy("a110110","jmdjsj903291")
d.quit()
