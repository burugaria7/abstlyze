# -*- coding: utf-8 -*-
import re
import traceback

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_binary
import time
from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import nltk
from nltk.corpus import stopwords

import csv_parser

# driver = webdriver.Chrome()
driver = webdriver.Firefox()
nltk.download('stopwords')

def get_id_from_ieee(url):
    # 取得先URLにアクセス
    driver.get(url)
    # コンテンツが描画されるまで待機
    time.sleep(8)
    elements = driver.find_elements(By.CLASS_NAME, "List-results-items")

    ids = []

    for element in elements:
        ids.append(element.get_attribute("id"))
        #print(element.get_attribute("id"))
    return ids

def word_normalization(str):
    #特殊文字削除
    str_ =  re.sub(r"[^a-zA-Z0-9 ]", "", str)

    #小文字に置き換え
    str_ = str_.lower()

    #一旦改行分割し、スペースで結合
    dv_text = str_.splitlines()
    str_ = ' '.join(dv_text)

    #HTML関連タグの除去
    # changed_text = BeautifulSoup(str_)
    # str_ = changed_text.get_text()

    #一般的な単語削除(NLTK使用)
    dv_text = str_.split()
    A = [word for word in dv_text if word not in stopwords.words('english')]
    str_ = ' '.join(A)

    return str_

def search_ieee():
    for i in range(262):
        print(i,"\n")
        url = "https://ieeexplore.ieee.org/search/searchresult.jsp?queryText=" \
              "robust%20clustering&highlight=true&returnType=" \
              "SEARCH&matchPubs=true&ranges=2000_2022_Year&returnFacets=" \
              "ALL&pageNumber=" + str(i)
        ids = get_id_from_ieee(url)
        print(ids)
        num = 0
        for id in ids:

            data = [["","",""]]
            try:
                paper_url = "https://ieeexplore.ieee.org/document/" + str(id) + "/"

                data[0][1] = paper_url
                print("No.", i * 25 + num, " ", paper_url)

                driver.get(paper_url)
                time.sleep(2)

                # Get Title
                title_elem = driver.find_element("xpath",
                                                 '//*[@id="LayoutWrapper"]/div/div/div/div[3]/div/xpl-root/div/xpl-document-details/div/div[1]/section[2]/div/xpl-document-header/section/div[2]/div/div/div[1]/div/div[1]/h1/span')

                # 正規化
                title = word_normalization(title_elem.text)

                data[0][0] = title
                print("Title:", title)

                # Get Abstract
                # abstract_elem = driver.find_element("xpath", '//*[@id="LayoutWrapper"]/div/div/div/div[3]/div/xpl-root/div/xpl-document-details/div/div[1]/div/div[2]/section/div[2]/div/xpl-document-abstract/section/div[2]/div[1]/div/div/div')
                abstract_elems = driver.find_element(By.CLASS_NAME, "abstract-text.row")
                ab = abstract_elems.find_element(By.CLASS_NAME, "u-mb-1")

                # 正規化
                abstract = word_normalization(ab.text[10:])

                data[0][2] = abstract
                print("Abstract:", abstract)

            except Exception as e:  # これは最後に書く
                print('Unknown exception!')
                print(e)

            try:
                csv_parser.add_raw_csv(data)
            except Exception as e:  # これは最後に書く
                print('Unknown exception!')
                print(e)

            num += 1

    driver.quit()

if __name__ == '__main__':
    search_ieee()

