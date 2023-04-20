import csv
import collections
import datetime
from janome.tokenizer import Tokenizer
from wordcloud import WordCloud
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

list = []
with open("dataset/fsas/fsas_155-459(2005-).csv", 'r', encoding='utf-16') as f:
    # カラムの値を抽出
    for row in csv.reader(f, dialect='excel', delimiter='\t', quoting=csv.QUOTE_ALL):
        list.append(row[2])

    # 先頭文字を削除
    # del list[0]

    # 文字列をつなげる
    b = ""
    for a in reversed(list):
        b += a

    # 文字の整形（改行削除）
    text = "".join(b.splitlines())

    # 単語ごとに抽出
    docs = []
    t = Tokenizer()
    tokens = t.tokenize(text)
    for token in tokens:
        if len(token.base_form) > 2:
            docs.append(token.surface)

    ## wordcloud の実行
    c_word = ' '.join(docs)
    stop_words = ["based", "using", "via", "for", "with", "on", "in", "of", "a", "and", "the", "to", "from", "by",
                  "method", "non", "an", "toward", "towards", "this", "that"]
    stop_words += stopwords.words('english')
    wordcloud = WordCloud(width=1920, height=1080, max_words=50, background_color="white",
                          stopwords=stop_words).generate(c_word)

    ## 結果を画像に保存
    now = datetime.datetime.now()
    wordcloud.to_file('./wordcloud_' + now.strftime('%Y%m%d_%H%M%S') + '.png')

    # 単語を多い順に並べる
    c = collections.Counter(docs)
    print(c)
