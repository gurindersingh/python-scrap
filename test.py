import os
import uuid
from time import sleep
from random import randint
from selenium import webdriver

# opts = webdriver.FirefoxOptions()

tmpFolder = os.getcwd() + '/tmp/{}'.format(uuid.uuid4())
os.makedirs(tmpFolder)
os.makedirs(tmpFolder + '/user-data')
os.makedirs(tmpFolder + '/data-path')
os.makedirs(tmpFolder + '/cache-dir')

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
options.add_argument('--window-size=1280x1696')
options.add_argument('--user-data-dir={}'.format(tmpFolder + '/user-data'))
options.add_argument('--hide-scrollbars')
options.add_argument('--enable-logging')
options.add_argument('--log-level=0')
# options.add_argument('--v=99')
options.add_argument('--single-process')
options.add_argument('--data-path={}'.format(tmpFolder + '/data-path'))
# options.add_argument('--ignore-certificate-errors')
options.add_argument('--homedir={}'.format(tmpFolder))
options.add_argument('--disk-cache-dir={}'.format(tmpFolder + '/cache-dir'))
options.add_argument('user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')

chromedriver = 'lib/chromedriver'

driver = webdriver.Chrome(chromedriver,chrome_options=options)

driver.get('https://www.gta-homes.com/')

sleep(randint(7,10))

body = driver.execute_script("return document.body.outerHTML;")

print(body)

driver.close()