#Fun Project - Web Scraper 001

#Basics -..-
import os
import pyautogui
import selenium

#For Browser !!
options = Options()
options.set_headless(headless=True)
chromedriver = r"C:/Users/NJ/Desktop/Desktop/Drivers/chromedriver_win32 (1)/chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
browser = webdriver.Chrome(chromedriver, chrome_options = options)

#Let's Begin :)
url = 'https://results.nitrr.ac.in/Default.aspx'
browser.get(url)

#Storing Name and Result(SPI & CPI)
results = []

#Let's Loopify
for i in range(1,94):
	try:
		#Roll No. 49 - Gone Missing !!
		if i == 49:
			continue
			
		num = '0' + str(i)
		if i > 90:
			num = '90' + str(i-90)
		if i < 10:
			num = '00' + str(i)
		
		input_roll = browser.find_element_by_id("txtRegno")
		roll = '16115' + num
		
		input_roll.clear()
		input_roll.send_keys(roll)

		show = browser.find_element_by_id("btnimgShow")
		show.click()

		select_element = Select(browser.find_element_by_id("ddlSemester"))
		select_element.select_by_value('6')

		showRes = browser.find_element_by_id("btnimgShowResult")
		showRes.click()

		print(roll)
		name = browser.find_element_by_id("lblStudentName").text
		spi = browser.find_element_by_id("lblSPI").text
		cpi = browser.find_element_by_id("lblCPI").text
		print(f'{name} --> {spi} --> {cpi}')
		
		results.append([name,float(cpi)])
	
	except:
		pass

#Let's Rank our Amigos :>
results.sort(key=lambda x: x[1], reverse=True)
with open('Result.txt', 'w') as f:
	i = 1
	for item in results:
		f.write(f"{i}. {item[0]} -- {item[1]}\n")
		i += 1

#Time to say Goodbye to the Browser :(		
browser.quit()
