import re
import pandas as pd
import numpy as np

# Prepare data
trump = pd.read_csv('https://drive.google.com/uc?export=download&id=1xRKHaP-QwACMydlDnyFPEaFdtskJuBa6')
trump.text = trump.apply(lambda row: re.sub(r"http\S+", "", row.text).lower(), 1)
trump.text = trump.apply(lambda row: " ".join(filter(lambda x: x[0] != "@", row.text.split())), 1)
trump.text = trump.apply(lambda row: " ".join(re.sub("[^a-zA-Z]+", " ", row.text).split()), 1)
trump = trump.loc[(trump.isRetweet == "f") & (trump.text != ""), :]
timestamps = trump.date.to_list()
tweets = trump.text.to_list()

arr_multi = np.array(tweets)
print(arr_multi)
# [list([0, 1, 2, [10, 20, 30]]) list([3, 4, 5]) 100]

print(arr_multi.size)
# 3

print(arr_multi.shape)
# (3,)
