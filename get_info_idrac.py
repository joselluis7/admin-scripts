# This script get information from (iDRAC)
# The Integrated Dell Remote Access Controller Web Page 
# Using selenium to send event's to the web page
# By: José Luís 

import time
import vault

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

browser = webdriver.Chrome()
browser.get('https://10.151.11.43')

advanced_link = browser.find_element_by_id('details-button')
advanced_link.click()
proced_link = browser.find_element_by_id('proceed-link')
proced_link.click()
time.sleep(10)
current_url = browser.current_url
print("URL BEFORE: ",current_url)
username_input = browser.find_element_by_name('user')
username_input.send_keys(vault.user_name)
password_input = browser.find_element_by_id('password')
password_input.send_keys(vault.user_pass)
btn_submit = browser.find_element_by_id('btnOK')
btn_submit.click()
try:
    WebDriverWait(browser, 60).until(EC.url_changes(current_url))
except TimeoutException:
    print("A busca levou muito tempo")
    time.sleep(10)
## Set if to test if the url has changed
current_url = browser.current_url
print("URL AFTER: ",current_url)
time.sleep(15)
browser.switch_to.frame(browser.find_element_by_name('da')) # switching to first frame
# get the second frame and switch
frame2 = browser.find_element_by_xpath("//iframe[@id='sysIframe']"); 
browser.switch_to.frame(frame2)
try:
    get_osname = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.ID, "osName"))).text
    get_hostname = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.ID, "osName"))).text
except TimeoutException:
    print("A busca levou muito tempo")

print("PEGO O FRAME", type(frame2))
print("GET: ", get_hostname.text, get_osname.text)
#type(get_osname)
browser.close()