#!/usr/bin/python3

import selenium as se
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
import re
from datetime import datetime
from time import sleep

url = 'https://www.tinkoff.ru/about/exchange/'

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-dev-shm-usage')

try:
    driver = webdriver.Chrome(options=chrome_options)
except Exception:
    log('exception')
    raise

driver.set_page_load_timeout(60)

pat = re.compile(r'<div class="Text__text_primary_28uo7" data-qa-file="index">([\d,]+)</div>')


def log(*args, **kwargs):
    time_stamp = datetime.now()
    with open('/root/projects/currency/monitor.log','a') as fd:
        print(time_stamp, *args, **kwargs, file=fd, flush=True )


try:
    driver.get(url)
except TimeoutException:
    log('timeout')
    raise
except Exception:
    log('exception')
    raise

res = pat.findall(driver.page_source)

if len(res) < 2: 
    log('no result')
elif res[0] == '0' or res[1] == '0':
    log('result is zero')
else:
    rub_to_eur = float(res[0].replace(',','.'))
    eur_to_rub = float(res[1].replace(',','.'))
    log(rub_to_eur, eur_to_rub)

