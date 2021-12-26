import json
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options 
from dotenv import load_dotenv


load_dotenv('.env')
options = Options()
options.headless=True


def get_info():
    url = os.getenv('URL_YOUTUBE')
    driver = webdriver.Chrome(os.getenv('CHROMEDRIVER_URL'),
                              options=options)
    driver.get(url)
    References = {}

    References['Subscribers'] = "//*[@id='subscriber-count']"

    INFO_List = list()
    for i in range(0,len(References)):
        driver_elements = driver.find_element_by_xpath(
            References[list(References.keys())[i]]
        )
        INFO_List.append(driver_elements.text)

    Vid = dict(zip(list(References.keys()), INFO_List))

    with open('yt.json', 'w', encoding='utf8') as ditcu:
        json.dump(Vid, ditcu, ensure_ascii=False)
    return(Vid)


if __name__ == '__main__':
    get_info()
