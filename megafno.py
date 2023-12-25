from selenium import webdriver
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(x):
	return str(math.log(abs(12 * math.sin(int(x)))))


def btn_click(browser):
	button = browser.find_element(By.TAG_NAME, "button")
	button.click()


try:
	browser = webdriver.Chrome()
	#browser.implicitly_wait(5)
	link = "https://thefastest.megafon.ru/"
	browser.get(link)

	option1 = browser.find_element(By.CSS_SELECTOR, '[role="button"]')
	option1.click()
	time.sleep(2)
	#button = browser.find_element(By.CSS_SELECTOR, '[type="button"]')
	button = WebDriverWait(browser, 5).until(
		EC.element_to_be_clickable((By.CLASS_NAME, 'bg-brand-green')))
	button.click()
	time.sleep(20)


except Exception as er:
	print(er)
finally:
	browser.quit()
