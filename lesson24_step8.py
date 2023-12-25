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
	link = "http://suninjuly.github.io/explicit_wait2.html"
	browser.get(link)
	price = WebDriverWait(browser, 12).until(
		EC.text_to_be_present_in_element((By.ID, 'price'), "100"))
	button = browser.find_element(By.ID, "book")
	button.click()

	x = browser.find_element(By.ID, "input_value").text
	y = calc(int(x))
	button = browser.find_element(By.TAG_NAME, "button")
	input = browser.find_element(By.ID, 'answer')
	input.send_keys(y)
	button2 = browser.find_element(By.ID, "solve")
	button2.click()
	time.sleep(10)


except Exception as er:
	print(er)
finally:
	browser.quit()
