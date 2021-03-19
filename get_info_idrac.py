import time
from . import vault

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

browser = webdriver.Chrome()
browser.get('https://10.151.11.43')

moredetails = browser.find_element_by_id('details-button')
moredetails.click()
go = browser.find_element_by_id('proceed-link')
go.click()
time.sleep(10)
current_url = browser.current_url
print("URL BEFORE: ",current_url)
emailElem = browser.find_element_by_name('user')
emailElem.send_keys(vault.user_name)
passwordElem = browser.find_element_by_id('password')
passwordElem.send_keys(vault.user_pass)
btn_submit = browser.find_element_by_id('btnOK')
btn_submit.click()

WebDriverWait(browser, 60).until(EC.url_changes(current_url))
current_url = browser.current_url
print("URL AFTER: ",current_url)
time.sleep(15)
frame1 = browser.switch_to.frame(browser.find_element_by_name('da'))
frame2 = browser.find_element_by_xpath("//iframe[@id='sysIframe']");
browser.switch_to_frame(frame2)
try:
    text_of_element_on_new_page = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.ID, "osName"))).text
except TimeoutException:
    print("A busca levou muito tempo")

print("PEGO O FRAME", type(frame1) )
print("PEGO O FRAME", type(frame2) )
get_hostname = browser.find_element_by_id('hostName')
get_osname = browser.find_element_by_id('osName')
print("GET: ", get_hostname.text, get_osname.text)
#type(get_osname)
browser.close()