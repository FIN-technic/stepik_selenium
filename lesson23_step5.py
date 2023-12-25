from selenium import webdriver
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import os


def calc(x):
	return str(math.log(abs(12 * math.sin(int(x)))))


def btn_click(browser):
	button = browser.find_element(By.TAG_NAME, "button")
	button.click()


try:
	browser = webdriver.Chrome()
	link = "http://suninjuly.github.io/redirect_accept.html"
	browser.get(link)
	btn_click(browser)
	time.sleep(1)
	first_window = browser.window_handles[0]
	print(f'first_window = {first_window}')
	new_window = browser.window_handles[1]
	print(f'new_window = {new_window}')
	browser.switch_to.window(new_window)

	x = browser.find_element(By.ID, "input_value").text
	y = calc(int(x))
	button = browser.find_element(By.TAG_NAME, "button")
	input = browser.find_element(By.ID, 'answer')
	input.send_keys(y)
	btn_click(browser)
	time.sleep(10)


except Exception as er:
	print(er)
finally:
	browser.quit()
