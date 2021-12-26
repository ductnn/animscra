import re
import requests
import os
import lxml
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv


load_dotenv('.env')


def get_info():
    url = os.getenv('URL_TELEGRAM')
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    follow = soup.find("div", text=re.compile('members')).get_text()

    x = re.split(",", follow)
    x_json = json.dumps(x)
    print(x)
    print(x_json)

    print(f'follows: {type(follow)}\n')


if __name__ == '__main__':
    get_info()
