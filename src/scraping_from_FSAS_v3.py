# -*- coding: utf-8 -*-
import re

import random
import time
from selenium.webdriver.chrome import service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import csv_parser

driver = webdriver.Chrome()


# driver = webdriver.Firefox()


def fsas():
    url = "https://www.sciencedirect.com/journal/fuzzy-sets-and-systems/vol/460/suppl/C"
    driver.get(url)
    time.sleep(1 + random.random())
    driver.find_element(By.XPATH,
                        "//*[@id=\"aa-expand-all-articles-previews\"]/div/label/span[1]").click()
    time.sleep(2 + random.random())

    for i in range(200):
        # driver.find_element(By.XPATH,
        #                     "//*[@id=\"react-root\"]/div/div/div/main/section[1]/div/div/nav/div[1]/a").click()

        if (i != 0):
            url = driver.find_element(By.XPATH,
                                      "//*[@id=\"react-root\"]/div/div/div/main/section[1]/div/div/nav/div[1]/a").get_attribute(
                'href')
            driver.get(url)
            time.sleep(1 + random.random())
        print(url)

        driver.find_element(By.XPATH,
                            "//*[@id=\"aa-expand-all-articles-previews\"]/div/label/span[1]").click()
        time.sleep(2 + random.random())

        # クラスがとたまにバグるからXPATHで指定
        # info = driver.find_elements(By.CLASS_NAME, "js-special-issue-title")
        info = driver.find_elements(By.XPATH, "//*[@id=\"react-root\"]/div/div/div/main/section[1]/div/div/div")
        print(i, "----------------------------------------")
        for j in info:
            print(j.text)
            print(j.get_attribute("href"))
        print("-  -  -  -  -  -  -  -")
        time.sleep(1 + random.random())

        # 書く記事のツリーをリストとして取得
        articles_tree = driver.find_elements(By.CLASS_NAME, "js-article.article-content")
        print("articles_num", len(articles_tree))

        for j in range(len(articles_tree)):
            # 内容があるか確認
            abst = articles_tree[j].find_elements(By.CLASS_NAME, "js-abstract-body-text.branded")
            if (len(abst) == 0):
                print("No abstract ^^ continue")
                continue
            else:
                title = articles_tree[j].find_element(By.CLASS_NAME, "js-article-title").text
                authour = articles_tree[j].find_element(By.CLASS_NAME,
                                                        "text-s.u-clr-grey8.js-article__item__authors").text
                abst = articles_tree[j].find_element(By.CLASS_NAME, "js-abstract-body-text.branded").find_element(
                    By.TAG_NAME, "p").text

                print("Article", j, "----------------------------------------")
                print("Title\t", title)
                print("Author\t", authour)
                print("Abstract\t", abst)

        # リンク取得
        # urls = driver.find_elements(By.CLASS_NAME, "anchor.article-content-title.u-margin-xs-top.u-margin-s-bottom.anchor-default")
        # for j in range(len(urls)):
        #     print("URL", j, urls[j].get_attribute('href'))

        # # タイトル取得
        # titles = driver.find_elements(By.CSS_SELECTOR, "*.js-article-title")
        # for j in range(len(titles)):
        #     print("Title", j, titles[j].text)
        # # 著者
        # authors = driver.find_elements(By.CSS_SELECTOR, "*.text-s.u-clr-grey8.js-article__item__authors")
        # for j in range(len(authors)):
        #     print("Author", j, authors[j].text)
        # # 概要
        # abstracts = driver.find_elements(By.CSS_SELECTOR, "*.js-abstract-body-text.branded")
        # for j in range(len(abstracts)):
        #     print("Abstract", j, abstracts[j].text)


if __name__ == "__main__":
    fsas()
