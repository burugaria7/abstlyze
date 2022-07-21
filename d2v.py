#coding: UTF-8
from gensim.models.doc2vec import Doc2Vec
from gensim.models.doc2vec import TaggedDocument

from gensim.models.doc2vec import Doc2Vec
from gensim.models.doc2vec import TaggedDocument
from tensorboardX import SummaryWriter
import gensim
import torch
import pandas as pd
import csv

from torch import FloatTensor
from gensim.models import KeyedVectors
from tensorboardX import SummaryWriter

def make_vec():
    # 空白で単語を区切り、改行で文書を区切っているテキストデータ
    with open("./data.txt",'r') as f:
         # 文書ごとに単語を分割してリストにする。
      trainings = [TaggedDocument(words = data.split(),tags = [i]) for i,data in enumerate(f)]
    # 学習の実行

    rows = len(trainings)
    columns = len(trainings[0])
    print('行：{},列：{}'.format(rows, columns))  # 行：3,列：2

    m = Doc2Vec(documents= trainings, dm = 1, vector_size=300, window=8, min_count=10, workers=4)
    # モデルのセーブ
    m.save("./doc2vec.model")

def save_embedding_projector_files():
    vector_file = "./vec.tsv"
    metadata_file = "./meta.tsv"
    m = Doc2Vec.load("./doc2vec.model")
    with open(vector_file, 'w', encoding='utf-8') as f, \
            open(metadata_file, 'w', encoding='utf-8') as g:
        # metadata file needs header
        g.write('Word\n')

        for word in m.wv.index_to_key:
            embedding = m.wv[word]

            # Save vector TSV file
            f.write('\t'.join([('%f' % x) for x in embedding]) + '\n')

            # Save metadata TSV file
            g.write(word + '\n')

def convert_to_tsv():
    m = Doc2Vec.load("./doc2vec.model")
    weights = []
    labels = []
    for i in range(0, len(m.docvecs)):
        weights.append(m.docvecs[i].tolist())
        labels.append(m.docvecs.index_to_doctag(i))

    # DEBUG: visualize vectors up to 1000
    weights = weights[:2000]
    labels = labels[:2000]

    writer = SummaryWriter()
    writer.add_embedding(FloatTensor(weights), metadata=labels)

if __name__ == '__main__':
    make_vec()
    convert_to_tsv()