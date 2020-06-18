from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import speech_recognition as sr

driver = webdriver.Chrome("C:/Users/Adithan/Documents/Downloads/chromedriver_win32/chromedriver.exe")
driver.get('https://skribbl.io/?XF64ukNwyZXw')
input('Enter any key to start recognizing : ')

while 1:
	# n = input('Enter any key to start recognizing : ')
	# if n == 'stop':
	# 	break
	
	r = sr.Recognizer()

	with sr.Microphone() as source:
		print("SAY Something")
		audio = r.listen(source)
		print("Thanks")

	try:
		text = r.recognize_google(audio)
		if text == 'stop':
			break
		chat = driver.find_element_by_id('inputChat')
		chat.send_keys(text)
		chat.send_keys(Keys.ENTER)
	except:
		pass;
