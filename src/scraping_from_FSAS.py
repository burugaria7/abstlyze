# -*- coding: utf-8 -*-
import re

import time
from selenium.webdriver.common.by import By
from selenium import webdriver
import csv_parser

# driver = webdriver.Chrome()
driver = webdriver.Firefox()


def fsas():
    driver.get("https://www.sciencedirect.com/journal/fuzzy-sets-and-systems/vol/460/suppl/C")
    time.sleep(2)
    for i in range(200):
        driver.find_element(By.XPATH,
                            "//*[@id=\"react-root\"]/div/div/div/main/section[1]/div/div/nav/div[1]/a").click()
        time.sleep(1)

        # クラスがとたまにバグるからXPATHで指定
        # info = driver.find_elements(By.CLASS_NAME, "js-special-issue-title")
        info = driver.find_elements(By.XPATH, "//*[@id=\"react-root\"]/div/div/div/main/section[1]/div/div/div")
        print(i, "--------------------")
        for j in info:
            print(j.text)
            print(j.get_attribute("href"))
            # with open('./fsas.csv', 'a', newline='', encoding='utf-8') as f:
            #     writer = csv_parser.writer(f, dialect='excel', delimiter=',', quoting=csv_parser.QUOTE_ALL)
            #     writer.writerow([j.text, j.get_attribute("href")])
        time.sleep(1)


if __name__ == "__main__":
    fsas()
