from urllib.parse import urlparse
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import re
from selenium.webdriver.chrome.options import Options
import time



url = 'https://web.whatsapp.com'
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)

input('im there')
counter = 0 
while True: 
	time.sleep(2)
	try: 
		counter += 1 
		driver.find_element_by_xpath("//span[@title= 'online']")
		print('LA CACHORRA ESTA ONLINE')
		print('LA CACHORRA ESTUVO ONLINE HOY ' + str(counter) + ' veces')
	except:
		print('LA CACHORRA NO ESTA ONLINE')
		continue

