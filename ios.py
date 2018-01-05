#!/usr/bin/python
# coding: UTF-8
#作者 蒋明
#作用 安卓自动测试
#pip install pywinauto
#日期 2016-12-16
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import re,time,platform,sys, getopt

import io
import sys
#import urllib.request
import os
from Crypto.Cipher import AES

from binascii import b2a_hex, a2b_hex
 
class prpcrypt():
 def __init__(self, key):
  self.key = key
  self.mode = AES.MODE_CBC
     
    #加密函数，如果text不是16的倍数【加密文本text必须为16的倍数！】，那就补足为16的倍数
 def encrypt(self, text):
  key=self.key
  length = 16
  count = len(key)
  add = length - (count % length)
  key = key + ('\0' * add)
  cryptor = AES.new(key, self.mode, b'0000000000000000')
  #这里密钥key 长度必须为16（AES-128）、24（AES-192）、或32（AES-256）Bytes 长度.目前AES-128足够用
  length = 16
  count = len(text)
  add = length - (count % length)
  text = text + ('\0' * add)
  self.ciphertext = cryptor.encrypt(text)
        #因为AES加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题
        #所以这里统一把加密后的字符串转化为16进制字符串
  return b2a_hex(self.ciphertext)
     
    #解密后，去掉补足的空格用strip() 去掉
 def decrypt(self, text):
  key=self.key
  length = 16
  count = len(key)
  add = length - (count % length)
  key = key + ('\0' * add)

  cryptor = AES.new(key, self.mode, b'0000000000000000')
  plain_text = cryptor.decrypt(a2b_hex(text))
  return plain_text.rstrip('\0')

print os.getcwd()
pc = prpcrypt(os.getcwd())      #初始化密钥

e = pc.encrypt("810830.")
print e

apptestname=""
appname="c:\\r5380_laicunba_360sz_20205_2.2.5.apk"


def load(filename):
 # win32gui
 #dialog = win32gui.FindWindow('#32770', u'文件上传')  # 对话框
 dialog = win32gui.FindWindow('#32770', u'打开')  # 对话框
 ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None) 
 ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
 Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)  # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄
 button = win32gui.FindWindowEx(dialog, 0, 'Button', None)  # 确定按钮Button
 win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, filename)  # 往输入框输入绝对地址
 win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 按button
 time.sleep(10)
def login():
 url="https://login.taobao.com/member/login.jhtml?redirectURL=https%3A%2F%2Flogin.taobao.com%2Fjump%3Ftarget%3Dhttp%253A%252F%252Fmqc.yunos.com%252FtestManager.htm"
# d.set_window_size(1024, 768)
 d.get(url)
 time.sleep(1)
 d.find_element_by_css_selector("#J_Quick2Static").click()
 d.find_element_by_css_selector("#TPL_username_1").send_keys("99806761@qq.com")
 d.find_element_by_css_selector("#TPL_password_1").send_keys(pc.decrypt("c8f49e848f8bdfb800a5c78a9ec07a1d"))
 d.find_element_by_css_selector("#J_SubmitStatic").click()
 time.sleep(5)

def xingneng():
 url="http://mqc.yunos.com/performance.htm?spm=0.0.0.0.Eu5mDe"
 d.get(url)
 time.sleep(1)
 d.find_element_by_xpath('//*[@id="upload-chooseApp"]/div/input').send_keys("/Users/a/Downloads/MobileAssistant_1.apk")
# load(appname)
#upload-chooseApp > div > input[type="file"]
 d.find_element_by_xpath('//*[@id="Step-two-next"]').click()
 time.sleep(1)

def jianrong():
 url="http://mqc.yunos.com/compatibility.htm?spm=a2c0i.8742162.1999348069.4.4k2MMH"
 d.get(url)
 d.find_element_by_css_selector("#chooseApp > div:nth-child(2) > input:nth-child(1)").click()
 time.sleep(1)
 load(appname)
 d.find_element_by_css_selector("#Step-two-next").click()
 time.sleep(1)
 d.find_element_by_css_selector("div.device-tab-box:nth-child(1) > h3:nth-child(1)").click()
 time.sleep(15)
 d.find_element_by_id("Submit-test").click()
 time.sleep(5)
 d.find_element_by_id("Submit-test").click()
 time.sleep(5)
def anquan():
 url="http://mqc.yunos.com/security.htm?spm=0.0.0.0.8V43DV"
 d.get(url)
 d.find_element_by_css_selector("#submitInputFile").click()
 time.sleep(1)
 load(appname)
 time.sleep(1)
 d.find_element_by_css_selector("#Step-two-next").click()
 time.sleep(10)
def wending():
 url="http://mqc.yunos.com/stability.htm?spm=0.0.0.0.TSRijd"
 d.get(url)
 d.find_element_by_css_selector("#appFileText").click()
 time.sleep(1)
 load(appname)
 time.sleep(10)
 d.find_element_by_css_selector("#Step-two-next").click()
 time.sleep(1)
 d.find_element_by_css_selector('#EmulatorTable > li:nth-child(1) > dl').click()
 d.find_element_by_css_selector('#EmulatorTable > li:nth-child(2) > dl').click()
 d.find_element_by_css_selector('#EmulatorTable > li:nth-child(3) > dl').click()
 d.find_element_by_css_selector('#EmulatorTable > li:nth-child(4) > dl').click()
 d.find_element_by_css_selector('#EmulatorTable > li:nth-child(5) > dl').click()
 d.find_element_by_css_selector('#EmulatorTable > li:nth-child(6) > dl').click()
 time.sleep(5)
 d.find_element_by_id("Submit-test").click()
 time.sleep(5)
def zidonghua(apptestfilename):
 url="http://mqc.yunos.com/function.htm?spm=0.0.0.0.S2x35H"
 d.get(url)
 time.sleep(4)
 d.find_element_by_css_selector("#chooseScript > div:nth-child(1) > label:nth-child(2) > span:nth-child(2)").click()
 #d.find_element_by_css_selector("#chooseScriptUpload > div:nth-child(1) > div:nth-child(1) > span:nth-child(2) > button:nth-child(1)").click()
 file_input = d.find_element_by_xpath('//*[@id="upload-chooseApp"]/div/div[1]/input')
 file_input.send_keys("/users/a/ios.py")
#//*[@id="upload-chooseApp"]/div/div[1]/input
 #time.sleep(1)
 #load(apptestfilename)
 #d.attach_file('file_chooser_id',fully_qualified_file_path)
 time.sleep(1)
# d.find_element_by_css_selector("#upload-chooseApp > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)").click()
# time.sleep(1)
# load(appname)
 time.sleep(1)
 d.find_element_by_css_selector("#Step-two-next").click()
 time.sleep(1)
 d.find_element_by_css_selector("div.device-tab-box:nth-child(1) > h3:nth-child(1)").click()
 time.sleep(15)
 d.find_element_by_css_selector("#Submit-test").click()
 time.sleep(15)
 d.find_element_by_css_selector("#Submit-test").click()
 time.sleep(15)


 
 
def zidonghuaios(apptestfilename):
 url="http://mqc.yunos.com/iosFuncPub.htm?spm=a2c0i.7764369.1999348069.11.sTveJq"
 d.get(url)
 time.sleep(4)
 d.find_element_by_css_selector("#chooseScript > div:nth-child(1) > label:nth-child(2) > span:nth-child(2)").click()
 d.find_element_by_css_selector("#upload-script > div > div.input-group > span > button").click()
 time.sleep(1)
 load(apptestfilename)
 time.sleep(1)
 
 d.find_element_by_css_selector("#chooseApp > div.radio-tab > label:nth-child(2) > span").click()
 time.sleep(1)
 
 d.find_element_by_css_selector("#download-chooseApp > div > div.input-group > input").click()
 time.sleep(1)
 load(appname)
 time.sleep(1)
 d.find_element_by_css_selector("#Step-two-next").click()
 
def zidonghuaios():
 url="https://mqc.aliyun.com/iosFuncPub.htm?spm=0.0.0.0.9rNExc"
 d.get(url)
 time.sleep(4)
 d.find_element_by_css_selector("#upload-chooseApp > div > div.input-group > input").click()
 time.sleep(4)
 load("c:\\test.ipa")
 time.sleep(1)
 d.find_element_by_css_selector("#upload-script > div > div.input-group > input").click()
 time.sleep(4)
 load("c:\\iosscript.zip")

 #d.find_element_by_css_selector("#multi-userList").send_keys("18999999999 123456")
 time.sleep(2)
 d.find_element_by_css_selector("#Step-two-next").click()
 time.sleep(2)
 d.find_element_by_css_selector("#device-tab-box-wrapper > div:nth-child(1) > h3").click()
 time.sleep(30)
 d.find_element_by_css_selector("#Submit-test").click()
 time.sleep(2)




if platform.system()=="Linux":
  d = webdriver.PhantomJS()
else:
  d = webdriver.Chrome()
  d.implicitly_wait(30)

#sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030') #改变标准输出的默认编码
#res=urllib.request.urlopen('http://www.baidu.com')
#htmlBytes=res.read()
login()
a=d.find_element_by_css_selector("body").text
print (a)

#zidonghuaios()
xingneng()
#zidonghua("c:\\temp.zip")

