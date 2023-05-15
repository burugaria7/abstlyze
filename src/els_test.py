# -*- coding: utf-8 -*-
"""An example program that uses the elsapy module"""

from elsapy.elsclient import ElsClient
from elsapy.elsprofile import ElsAuthor, ElsAffil
from elsapy.elsdoc import FullDoc, AbsDoc
from elsapy.elssearch import ElsSearch
import json

encoding = "utf-8"

## Load configuration
con_file = open("config.json")
config = json.load(con_file)
con_file.close()

# ## Initialize client
# client = ElsClient(config['apikey'])
# client.inst_token = config['insttoken']

## Initialize client
client = ElsClient(config['apikey'])
client.inst_token = config['insttoken']

client.local_dir = "C:/elsapy"
# uri = 'http://api.elsevier.com/content/search/scopus?query=srctitle("fuzzy-sets-and-systems")'
# print(uri)
# my_auth = ElsAuthor(uri)
# # Read author data, then write to disk
# if my_auth.read(myCl):
#     print("my_auth.data", my_auth)
#     my_auth.write()
# else:
#     print("unknown")

## ScienceDirect (full-text) document example using DOI
# doi_doc = FullDoc(doi='10.1016/j.fss.2022.12.014')
# if doi_doc.read(client):
#     print("doi_doc.title: ", doi_doc.title)
#     print("doi_doc.title: ", doi_doc.id)
#     doi_doc.write()
# else:
#     print("Read document failed.")

# DOIからFullDocオブジェクトを作成
doi = '10.1016/j.fss.2022.12.014'
doc = FullDoc(doi=doi)

# Elsevierサーバーから論文情報を取得
if doc.read(client):
    # 論文情報を表示
    print("Title:", doc.title)
    # print("Authors:", doc.authors) # これをコメントアウト
    print("Authors:", doc.data["coredata"]["dc:creator"])  # これを追加
    print("Abstract:", doc.data["coredata"]["dc:description"])
else:
    # エラーメッセージを表示
    print("Unable to read document.")
