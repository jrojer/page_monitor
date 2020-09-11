import selenium as se
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re
from datetime import datetime
from time import sleep

url = 'https://www.tinkoff.ru/about/exchange/'

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=chrome_options)

pat = re.compile(r'<div class="Text__text_primary_28uo7" data-qa-file="index">([\d,]+)</div>')


def log(*args, **kwargs):
    time_stamp = datetime.now()
    with open('./monitor.log','a') as fd:
        print(time_stamp, *args, **kwargs,file=fd, flush=True )
        print(time_stamp, *args, **kwargs)


while True:
    driver.get(url)
    res = pat.findall(driver.page_source)

    if len(res) < 2: 
        log('no result')
    elif res[0] == '0' or res[1] == '0':
        log('result is zero')
    else:
        rub_to_eur = float(res[0].replace(',','.'))
        eur_to_rub = float(res[1].replace(',','.'))
        log(rub_to_eur, eur_to_rub)
    sleep(60 * 5)

