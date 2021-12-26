import os
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.by import By
from dotenv import load_dotenv


load_dotenv('.env')
options = Options()
options.headless=True


def get_info():
    url = os.getenv('URL_TWITTER')
    driver = webdriver.Chrome(os.getenv('CHROMEDRIVER_URL'),
                              options=options)
    driver.get(url)
    References = {}
    References['Followers'] = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[1]/div/div[5]/div[2]/a/span[1]/span'
    References['Following'] = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[1]/div/div[5]/div[1]/a/span[1]/span'
    INFO_List = list()

    driver_elements = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, References['Followers']))
    )
    INFO_List.append(driver_elements.text)

    driver_elements = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, References['Following']))
    )
    INFO_List.append(driver_elements.text)

    Vid = dict(zip(list(References.keys()), INFO_List))

    with open('twitter.json', 'w', encoding='utf8') as ditcu:
        json.dump(Vid, ditcu, ensure_ascii=False)
    return(Vid)


if __name__ == '__main__':
    get_info()
