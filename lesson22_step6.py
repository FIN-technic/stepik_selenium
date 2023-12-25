from selenium import webdriver
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
	browser = webdriver.Chrome()
	link = "https://SunInJuly.github.io/execute_script.html"
	browser.get(link)

	x = browser.find_element(By.ID, "input_value").text
	y = calc(int(x))
	button = browser.find_element(By.TAG_NAME, "button")
	input = browser.find_element(By.ID, 'answer')
	input.send_keys(y)
	option1 = browser.find_element(By.ID, "robotCheckbox")
	browser.execute_script("return arguments[0].scrollIntoView(true);", option1)
	option1.click()
	option2 = browser.find_element(By.ID, "robotsRule")
	browser.execute_script("return arguments[0].scrollIntoView(true);", option2)
	option2.click()
	browser.execute_script("return arguments[0].scrollIntoView(true);", button)
	button.click()
	time.sleep(5)

except Exception as er:
	print(er)
finally:
	browser.quit()