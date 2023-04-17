# -*- coding: utf-8 -*-
import re

import time
from selenium.webdriver.chrome import service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import csv_parser

# driver = webdriver.Chrome()
driver = webdriver.Firefox()


def fsas():
    url = "https://www.sciencedirect.com/journal/fuzzy-sets-and-systems/vol/460/suppl/C"
    driver.get(url)
    time.sleep(2)
    driver.find_element(By.XPATH,
                        "//*[@id=\"aa-expand-all-articles-previews\"]/div/label/span[1]").click()
    time.sleep(4)

    for i in range(200):
        # driver.find_element(By.XPATH,
        #                     "//*[@id=\"react-root\"]/div/div/div/main/section[1]/div/div/nav/div[1]/a").click()

        if (i != 0):
            url = driver.find_element(By.XPATH,
                                      "//*[@id=\"react-root\"]/div/div/div/main/section[1]/div/div/nav/div[1]/a").get_attribute(
                'href')
            driver.get(url)
            time.sleep(1)
        print(url)

        driver.find_element(By.XPATH,
                            "//*[@id=\"aa-expand-all-articles-previews\"]/div/label/span[1]").click()
        time.sleep(2)

        # クラスがとたまにバグるからXPATHで指定
        # info = driver.find_elements(By.CLASS_NAME, "js-special-issue-title")
        info = driver.find_elements(By.XPATH, "//*[@id=\"react-root\"]/div/div/div/main/section[1]/div/div/div")
        print(i, "----------------------------------------")
        for j in info:
            print(j.text)
            print(j.get_attribute("href"))
        print("-  -  -  -  -  -  -  -")
        time.sleep(3)

        # タイトル取得
        titles = driver.find_elements(By.CSS_SELECTOR, "*.js-article-title")
        for j in range(len(titles)):
            print("Title", j, titles[j].text)
        # 著者
        authors = driver.find_elements(By.CSS_SELECTOR, "*.text-s.u-clr-grey8.js-article__item__authors")
        for j in range(len(authors)):
            print("Author", j, authors[j].text)
        # 概要
        abstracts = driver.find_elements(By.CSS_SELECTOR, "*.js-abstract-body-text.branded")
        for j in range(len(abstracts)):
            print("Abstract", j, abstracts[j].text)


if __name__ == "__main__":
    fsas()
