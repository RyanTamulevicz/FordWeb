import os
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.keys import Keys
import time
import webbrowser
import threading
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys


options = Options()
#options.add_argument("--headless") # Runs Chrome in headless mode.
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36")

part1 = ''
part2 = ''
part3 = ''
part4 = ''
part5 = ''

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)

driver = webdriver.Chrome(resource_path('./driver/chromedriver.exe'), options=options)
driver.get('https://parts.ford.com/shop/SearchDisplay?searchTerm=jj&storeId=1405&catalogId=251&langId=-1&searchType=partnumber')

def startup():
    wait = WebDriverWait(driver, 5)
    driver.set_window_size(1600,1000)


    searchbox = driver.find_element_by_xpath('//*[@id="SimpleSearchForm_SearchTerm"]')
    searchbox.send_keys(Keys.CONTROL, 'a')
    searchbox.send_keys(Keys.BACKSPACE)
    searchbox.send_keys('jj')



    searchbutton = driver.find_element_by_xpath('//*[@id="searchTermButton"]')
    searchbutton.click()


    zipbox = driver.find_element_by_xpath('//*[@id="autocompleteAddressHomePage"]')
    zipbox.send_keys('32960')
    zipbox.send_keys(Keys.ENTER)


    element = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Sunrise Ford Company')))
    sunrisebox = driver.find_element_by_link_text('Sunrise Ford Company')
    sunrisebox.click()

st = threading.Thread(target=startup)
st.start()

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

def getPartLink(*argv):
    for arg in argv:
        secsearch = driver.find_element_by_xpath('//*[@id="keywordNumber_glob"]')
        secsearch.send_keys(arg)
        secsearch.send_keys(Keys.ENTER)
        urls = driver.current_url
        time.sleep(3)
        backorerfinder = driver.find_element_by_xpath('//*[@id="product_page_details_pg"]/div[2]/b').text
        webbrowser.get(chrome_path).open(driver.current_url)
        price = driver.find_element_by_xpath('//*[@id="product_page_details_pg"]/div[3]/div[1]/div[2]/div[1]/div[1]/h3/span').text
        if (backorerfinder == "Item is currently on back order. Contact Your Dealer to check on part availability."):
            return("Part Number: " + arg  + " " + price + " ** See below for more information on this part" + "\n \nDirect Link: " + driver.current_url + '\n \n')        
        else:
            return ("Part Number: " + arg + " " + price + "\n \nDirect Link: " + driver.current_url + '\n \n')
        
def getDealer(zip):
    wait = WebDriverWait(driver, 5)
    driver.get("https://parts.ford.com/shop/en/us/find-a-dealer")
    element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="searchInput"]')))
    searchBox = driver.find_element_by_xpath('//*[@id="searchInput"]')
    time.sleep(2)
    searchBox.send_keys(zip)
    searchBox.send_keys(Keys.ENTER)
    time.sleep(3)
    dealerInfo = driver.find_element_by_xpath('/html/body/div[1]/div[9]/div[5]/div/div/div/div[2]/div[2]').text
    dealerInfo = dealerInfo[1:]
    dealerInfo = dealerInfo[:-19]
    return(dealerInfo.strip())