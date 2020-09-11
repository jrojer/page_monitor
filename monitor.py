#!/usr/bin/python3
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

time_stamp = datetime.now()
driver.get(url)
res = pat.findall(driver.page_source)

if len(res) < 2: 
    with open('/root/projects/currency/bad_page.log','w') as fd_err:
        print(driver.page_source, file=fd_err, flush=True)
elif res[0] == '0' or res[1] == '0':
    pass
else:
    rub_to_eur = float(res[0].replace(',','.'))
    eur_to_rub = float(res[1].replace(',','.'))
    with open('/root/projects/currency/monitor.log','a') as fd:
        print(time_stamp, rub_to_eur, eur_to_rub, file=fd, flush=True)

