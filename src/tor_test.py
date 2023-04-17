import subprocess
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import chromedriver_binary
from selenium.webdriver.chrome.options import Options
import requests
import time

cmd = 'pip install --upgrade chromedriver_binary'
res = subprocess.call(cmd, shell=False)

for i in range(3):
    cmd = r'C:\Users\Re\Desktop\Tor Browser\Browser\TorBrowser\Tor\tor.exe'
    pop = subprocess.Popen(cmd, shell=False)

    # user_agent = 'Mozilla/5.0 CK={} (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'
    user_agent = 'Mozilla/5.0'
    chrome_options = Options()
    chrome_options.add_argument("user-agent=" + user_agent)
    chrome_options.add_argument("--proxy-server=socks5://127.0.0.1:9050")

    d = DesiredCapabilities.CHROME
    d['goog:loggingPrefs'] = {'performance': 'ALL'}

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options, desired_capabilities=d)
    driver.set_window_size('1200', '1000')
    # driver.get("http://icanhazip.com/")
    driver.get("https://www.sciencedirect.com/journal/fuzzy-sets-and-systems/vol/460/suppl/C")
    # print(driver.page_source)
    time.sleep(7)
    pop.kill()
    driver.close()
    time.sleep(3)
