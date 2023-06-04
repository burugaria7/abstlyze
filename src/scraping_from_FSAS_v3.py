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
    url = "https://www.sciencedirect.com/journal/fuzzy-sets-and-systems/vol/30/index/I"
    driver.get(url)
    time.sleep(1 + random.random())

    try:
        driver.find_element(By.XPATH,
                            "//*[@id=\"aa-expand-all-articles-previews\"]/div/label/span[1]").click()
    except:
        print("EEE")

    time.sleep(2 + random.random() + random.random())

    for i in range(2000):
        # driver.find_element(By.XPATH,
        #                     "//*[@id=\"react-root\"]/div/div/div/main/section[1]/div/div/nav/div[1]/a").click()
        print("--------------------------------------------------------------------------------")
        print(i, "--------------------------------------------------------------------------------")
        print("--------------------------------------------------------------------------------")

        if (i != 0):
            url = driver.find_element(By.XPATH,
                                      "//*[@id=\"react-root\"]/div/div/div/main/section[1]/div/div/nav/div[1]/a").get_attribute(
                'href')
            driver.get(url)
            time.sleep(1 + random.random() + random.random())

        print(url)

        try:
            # ここでAbstract全表示を有効にする
            driver.find_element(By.XPATH,
                                "//*[@id=\"aa-expand-all-articles-previews\"]/div/label/span[1]").click()
            time.sleep(2 + random.random() + random.random())
        except:
            print("EEEE")

        # クラスがとたまにバグるからXPATHで指定
        # info = driver.find_elements(By.CLASS_NAME, "js-special-issue-title")
        info = driver.find_elements(By.XPATH, "//*[@id=\"react-root\"]/div/div/div/main/section[1]/div/div/div")

        jj = ""
        for j in info:
            print("Journal", j.text.replace("\n", " "))
            jj += j.text.replace("\n", " ")
            # print("URL", j.get_attribute("href"))
        print("-  -  -  -  -  -  -  -")
        time.sleep(1 + random.random() + random.random())

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
                title = articles_tree[j].find_element(By.CLASS_NAME, "js-article-title").text.replace("\n", " ")
                author = articles_tree[j].find_element(By.CLASS_NAME,
                                                       "text-s.u-clr-grey8.js-article__item__authors").text.replace(
                    "\n", " ")
                abst = articles_tree[j].find_element(By.CLASS_NAME, "js-abstract-body-text.branded").find_element(
                    By.TAG_NAME, "p").text.replace("\n", " ")
                url_ = articles_tree[j].find_element(By.CLASS_NAME,
                                                     "anchor.article-content-title.u-margin-xs-top.u-margin-s-bottom.anchor-default").get_attribute(
                    'href')

                print("Article", j, "--------------------------------------------------------------------------------")
                print("URL\t", url_)
                print("Title\t", title)
                print("Author\t", author)
                print("Abstract\t", abst)

                # data = [[title], [author], [abst], [url_], [jj], [url]]
                data = [title, author, abst, url_, jj, url]
                csv_parser.add_raw_csv_with_filepath(data, "fsas.csv")

        time.sleep(random.random())


if __name__ == "__main__":
    fsas()
