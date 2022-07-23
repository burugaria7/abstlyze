import numpy as np
import matplotlib.pyplot as plt
from gensim.models.doc2vec import Doc2Vec
from scipy.cluster.hierarchy import linkage, fcluster, dendrogram
from matplotlib.font_manager import FontProperties
import csv
from sklearn.feature_extraction.text import TfidfVectorizer


# 階層型クラスタリングの実施
def hierarchical_clustering(emb, threshold):
    # ウォード法 x ユークリッド距離
    linkage_result = linkage(emb, method='ward', metric='euclidean')
    # クラスタ分けするしきい値を決める
    threshold_distance = threshold * np.max(linkage_result[:, 2])
    # クラスタリング結果の値を取得
    clustered = fcluster(linkage_result, threshold_distance, criterion='distance')
    print("end clustering.")
    return linkage_result, threshold_distance, clustered


# 階層型クラスタリングの可視化
def plot_dendrogram(linkage_result, doc_labels, threshold):
    # font_path = "font/ipaexg.ttf"
    # fp = FontProperties(fname=font_path)
    plt.figure(figsize=(16, 8), facecolor='w', edgecolor='k')
    dendrogram(linkage_result, labels=doc_labels, color_threshold=threshold)
    plt.title('Dendrogram')
    plt.xticks(fontsize=10)
    print('end plot.')
    plt.savefig("./hierarchy.png")


# 階層型クラスタリング結果の保存
def save_cluster(doc_index, clustered):
    doc_cluster = np.array([doc_index, clustered])
    doc_cluster = doc_cluster.T
    doc_cluster = doc_cluster.astype(np.dtype(int).type)
    doc_cluster = doc_cluster[np.argsort(doc_cluster[:, 1])]
    np.savetxt("./cluster.csv", doc_cluster, delimiter=',', fmt='%.0f')
    print('save cluster.')

def analyze():
    print("")

    with open("./data.txt", 'r') as f:
        datas = [[i, data] for i, data in enumerate(f)]
        #datas = [[i, data.split('\t')[2]] for i, data in enumerate(f)]

    docs = ['', '', '', '', '', '']

    # クラスタリング結果を読み込む
    with open("./cluster.csv", 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            doc = datas[int(row[0])][1]
            # doc = ' '.join(set(doc.split())) #同一タイトル内で重複削除
            # クラスター毎に本文を纏める
            docs[int(row[1]) - 1] += ' {0}'.format(doc)

    # tf-idfの計算
    vectorizer = TfidfVectorizer(max_df=0.90, max_features=100)
    # 文書全体の90%以上で出現する単語は無視する
    # 且つ、出現上位100までの単語で計算する
    X = vectorizer.fit_transform(docs)
    # print('feature_names:', vectorizer.get_feature_names())

    words = vectorizer.get_feature_names()
    for doc_id, vec in zip(range(len(docs)), X.toarray()):
        print('doc_id:', doc_id + 1)
        for w_id, tfidf in sorted(enumerate(vec), key=lambda x: x[1], reverse=True)[:20]:
            lemma = words[w_id]
            print('\t{0:s}: {1:f}'.format(lemma, tfidf))

if __name__ == '__main__':

    #####
    #クラスタリングの実行
    #####

    #使用するデータ数
    # num = 2000
    # m = Doc2Vec.load("./doc2vec.model")
    # # vectors_list = [m.docvecs[n] for n in range(len(m.docvecs))]
    # vectors_list = [m.docvecs[n] for n in range(len(m.docvecs))]
    # vectors_list = vectors_list[:num]
    #
    # threshold = 0.2
    # linkage_result, threshold, clustered = hierarchical_clustering(emb=vectors_list, threshold=threshold)
    # plot_dendrogram(linkage_result=linkage_result, doc_labels=list(range(num)), threshold=threshold)
    # save_cluster(list(range(num)), clustered)

    ###
    #分析の実行
    ###
    analyze()