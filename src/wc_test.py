import csv
import collections
import datetime
from janome.tokenizer import Tokenizer
from wordcloud import WordCloud
import nltk
from nltk.corpus import stopwords


# nltk.download('stopwords')


def load_words_from_file(path_to_file):
    sw_list = []
    with open(path_to_file, 'r') as f:
        [sw_list.append(word) for line in f for word in line.split()]
    return sw_list


def wc():
    list = []
    with open("dataset/fsas/fsas_155-459(2005-).csv", 'r', encoding='utf-16') as f:
        # カラムの値を抽出
        for row in csv.reader(f, dialect='excel', delimiter='\t', quoting=csv.QUOTE_ALL):
            list.append(row[2])

        # 先頭文字を削除
        # del list[0]

        # 文字列をつなげる
        b = ""
        # from:0 to:1194 is 2018-2023
        # from:2569 to:none is 2005-2010
        # ここでCSVの対象とする行の範囲を指定する
        from_ = 2569
        to_ = None
        for a in reversed(list[from_:]):
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
                      "method", "non", "an", "toward", "towards", "this", "that", "based", "proposed", "fuzzy"]
        stop_words += stopwords.words('english')

        # Load stop words
        UniNE_sw = load_words_from_file('englishST.txt')
        stop_words += UniNE_sw

        wordcloud = WordCloud(width=1920, height=1080, background_color="white",
                              stopwords=stop_words).generate(c_word)

        ## 結果を画像に保存
        now = datetime.datetime.now()
        wordcloud.to_file('./wc_img/wc_' + now.strftime('%Y%m%d-%H%M%S') + '_' + str(from_) + ":" + str(to_) + '.png')

        # 単語を多い順に並べる
        c = collections.Counter(docs)
        print(c)


if __name__ == '__main__':
    wc()
