# -*- coding: utf-8 -*-
import traceback
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_binary
import time
from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import re

# driver = webdriver.Chrome()
driver = webdriver.Firefox()

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
    #改行削除と特殊文字削除
    str_ =  re.sub(r"[^a-zA-Z0-9 ]", "", str.strip())

    #一般的な単語削除
    remove_str = ["again","ve","couldn","hasnt","yourselves"]

    return str_

def search_ieee():
    for i in range(2):
        print(i,"\n")
        url = "https://ieeexplore.ieee.org/search/searchresult.jsp?queryText=" \
              "robust%20clustering&highlight=true&returnType=" \
              "SEARCH&matchPubs=true&ranges=2018_2022_Year&returnFacets=" \
              "ALL&pageNumber=" + str(i)
        ids = get_id_from_ieee(url)
        print(ids)
        num = 0
        for id in ids:

            paper_url = "https://ieeexplore.ieee.org/document/"+str(id)+"/"
            print("No.",i*25+num," ",paper_url)

            driver.get(paper_url)
            time.sleep(2)

            # Get Title
            title_elem = driver.find_element("xpath", '//*[@id="LayoutWrapper"]/div/div/div/div[3]/div/xpl-root/div/xpl-document-details/div/div[1]/section[2]/div/xpl-document-header/section/div[2]/div/div/div[1]/div/div[1]/h1/span')

            #正規化
            title = word_normalization(title_elem.text)

            print("Title:", title)

            # Get Abstract
            # abstract_elem = driver.find_element("xpath", '//*[@id="LayoutWrapper"]/div/div/div/div[3]/div/xpl-root/div/xpl-document-details/div/div[1]/div/div[2]/section/div[2]/div/xpl-document-abstract/section/div[2]/div[1]/div/div/div')
            abstract_elems= driver.find_element(By.CLASS_NAME, "abstract-text.row")
            ab = abstract_elems.find_element(By.CLASS_NAME, "u-mb-1")

            # #改行削除
            # ab_text = ab.text[10:].strip()

            #正規化
            abstract = word_normalization(ab.text[10:])

            print("Abstract:", abstract)

            # for ab_elem in abstract_elems:
            #     ab = ab_elem.find_element(By.CLASS_NAME, "u-pb-1")
            #     print("Abstract\t", ab.text)

            # print("Abstract\t", abstract_elem[0].text)
            num += 1

    driver.quit()

if __name__ == '__main__':
    search_ieee()

