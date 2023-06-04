import re
import pandas as pd
import numpy as np

# Prepare data
trump = pd.read_csv('dataset\\fsas\\fsas_full_utf8.csv')
trump.abstract = trump.apply(lambda row: re.sub(r"http\S+", "", row.abstract).lower(), 1)
trump.abstract = trump.apply(lambda row: " ".join(filter(lambda x: x[0] != "@", row.abstract.split())), 1)
trump.abstract = trump.apply(lambda row: " ".join(re.sub("[^a-zA-Z]+", " ", row.abstract).split()), 1)
# trump = trump.loc[(trump.isRetweet == "f") & (trump.abstract != ""), :]
timestamps = trump.book.to_list()
abstracts = trump.abstract.to_list()

arr_multi = np.array(abstracts)
print(arr_multi)
# [list([0, 1, 2, [10, 20, 30]]) list([3, 4, 5]) 100]

# print(arr_multi.size)
# print(arr_multi.shape)
