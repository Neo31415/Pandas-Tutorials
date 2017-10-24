#just to check diff function

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import xlrd


def save(a, b, c, d, e, f, g, h):
    data_str = a+','+b+','+c+','+d+','+e+','+f+','+g+','+h+'\n'
    wf.write(data_str)

driver = webdriver.Chrome('C:/Users/sumit/Desktop/code/chromedriver.exe')
driver.get('https://www.mapdevelopers.com/what-is-my-zip-code.php')

workbook = xlrd.open_workbook('address.xlsx')
worksheet = workbook.sheet_by_index(0)
rows = worksheet.nrows

wf = open('Zipcode-Data.csv', 'w')
wf.write('Address'+','+'Zipcode'+','+'City'+','+'County'+','+'State'+','+'Country'+','+'Longitude'+','+'Latitude'+'\n')


for i in range(1, rows):
	inp = driver.find_element_by_xpath('//*[@id="address"]')
	address = worksheet.cell(i, 0).value
	inp.send_keys(address)
	print(address)
	#inp.send_keys(Keys.CONTROL, 'a')
	for i in range(1):
		driver.find_element_by_xpath('//*[@id="search-form"]/div[1]/span[2]/button').click()
	time.sleep(5)

	try:
		zipcode = driver.find_element_by_xpath('//*[@id="display_zip"]').text
		city = driver.find_element_by_xpath('//*[@id="display_city"]').text
		county = driver.find_element_by_xpath('//*[@id="display_county"]').text
		state = driver.find_element_by_xpath('//*[@id="display_state"]').text
		country = driver.find_element_by_xpath('//*[@id="display_country"]').text
		longitude = driver.find_element_by_xpath('//*[@id="display_lng"]').text
		latitude = driver.find_element_by_xpath('//*[@id="display_lat"]').text
		driver.find_element_by_xpath('//*[@id="address"]').send_keys(Keys.CONTROL, 'a')
		time.sleep(5)
		save(address.replace(',', '@#'), zipcode, city, county, state, country, longitude, latitude)
	except Exception as e:
		print(e)
		driver.switch_to_alert().accept()
		save(address.replace(',', '#@'), 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A')
		driver.find_element_by_xpath('//*[@id="address"]').send_keys(Keys.CONTROL, 'a')
