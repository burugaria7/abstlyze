import numpy as np
import matplotlib.pyplot as plt
from gensim.models.doc2vec import Doc2Vec
from scipy.cluster.hierarchy import linkage, fcluster, dendrogram
from matplotlib.font_manager import FontProperties


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

if __name__ == '__main__':
    #使用するデータ数
    num = 2000
    m = Doc2Vec.load("./doc2vec.model")
    # vectors_list = [m.docvecs[n] for n in range(len(m.docvecs))]
    vectors_list = [m.docvecs[n] for n in range(len(m.docvecs))]
    vectors_list = vectors_list[:num]

    threshold = 0.8
    linkage_result, threshold, clustered = hierarchical_clustering(emb=vectors_list, threshold=threshold)
    plot_dendrogram(linkage_result=linkage_result, doc_labels=list(range(num)), threshold=threshold)
    save_cluster(list(range(num)), clustered)