#!/usr/bin/python
# coding: UTF-8
#作者 蒋明
#作用 reg购买存款标
#pip install pywinauto
#P6 - Time Series Forecasting
#http://www.youtubecomtomp3.com/zh/YouTube-to-MP4.php
#日期 2016-12-16
import subprocess
import redis
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime
#import win32gui
import os
from selenium.webdriver.support.ui import Select
#import win32con
import time,platform,sys, getopt,paramiko,random,re
#import socks  
#import socket 
#import requests

#back=socket.socket
#socks.set_default_proxy(socks.SOCKS5, "127.0.0.1",1080)
#print(requests.get('http://ifconfig.me/ip').text)
global index1
import psycopg2
index1=6
def l(url):
	global index1
	index1=index1+1
	e.get(url)
	for index in range(40):
		index=index+1
		try:
			e.find_element_by_xpath("//*[@id='main-layout-sidebar']/div/div[1]/ol/li["+str(index)+"]").click()
			
			page = e.page_source
			filename = 'c:\\setup.log' 
			f=open("c://ios//"+str(index1)+"_"+str(index)+".htm",mode="w",encoding="UTF-8")
			f.write( page )
			f.close()
		except:
			break
#//*[@id="main-layout-content"]/div/div[1]/div/div/ol/li[13]/div[2]/h2/a
#//*[@id="main-layout-content"]/div/div[1]/div/div/ol/li[1]/div[2]/h2/a
#//*[@id="main-layout-content"]/div/div[1]/div/div/ol/li[9]/div[2]/h2/a
#//*[@id="main-layout-content"]/div/div[1]/div/div/ol/li[1]/div[2]/h2/a
#https://classroom.udacity.com/nanodegrees/nd001/parts/00113454015
def o(url):
	e.get(url)
	time.sleep(10)
	print(url)
	for index in range(10):
		index=index+1
		try:
			e.find_element_by_xpath("//*[@id='main-layout-content']/div/div[1]/div/div/ol/li["+str(index)+"]/div[2]/h2/a").click()			
		except:
			break
	for index in range(10):
		index=index+1
		try:
			l(href[index])
		except:
			break


			
def login(root,passwd):
	url1="https://auth.udacity.com/sign-in?next=https%3A%2F%2Fclassroom.udacity.com%2Fauthenticated"
	e.get(url1)
	e.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div/div/div[2]/div/div[1]/div/form/div/div[1]/input').send_keys(root)
	e.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div/div/div[2]/div/div[1]/div/form/div/div[2]/input').send_keys(passwd)
	e.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div/div/div[2]/div/div[1]/div/form/button').click()

#	e.find_element_by_xpath("//*[@id='app']/div/div[2]/div/div/div/div[2]/div/div/form/div/div[1]/input").send_keys(root)
#	e.find_element_by_css_selector("#app > div > div.main-container--content--1CGTM > div > div > div > div.tabbed-pane--content--2o3OQ > div > div > form > div > div:nth-child(2) > input").send_keys(passwd)
#	e.find_element_by_css_selector("#app > div > div.main-container--content--1CGTM > div > div > div > div.tabbed-pane--content--2o3OQ > div > div > form > button").click()

e = webdriver.Chrome()
e.implicitly_wait(10)
login("yvcwbym0769@163.com","55nl26lda8rN")
time.sleep(5)
try:
	os.makedirs("c://ios")
except:
	time.sleep(0)
	

	

#//*[@id="main-layout-content"]/div/div[1]/div/div/ol/li[1]/div[2]/h2/a
#//*[@id="main-layout-content"]/div/div[1]/div/div/ol/li[13]/div[2]/h2/a
#main-layout-content > div > div.index--body--3G2lS > div > div > ol > li:nth-child(1) > div._item--item--1Vki7 > h2 > a

f = open('c://1udacityswift.txt','r')  
for line in open('c://1udacityswift.txt'):
	linae=f.readline()
	if line>"":
		l(line)
