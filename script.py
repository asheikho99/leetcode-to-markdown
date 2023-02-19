import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

URL = input('Enter LeetCode URL\n')
driver = webdriver.Chrome()
driver.get(URL)
time.sleep(3)

problem_title = driver.find_element(By.XPATH, '//*[@id="qd-content"]/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div/div/span').text
f = open('problem.md', 'w')
f.write('#' + problem_title + '\n')
f.close()

time.sleep(3)

header = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div[3]/div')
children = header.find_elements(By.XPATH, './*')

f = open('problem.md', 'a')
for child in children:
    print()
    f.write(child.text)
f.close()

driver.close()