import sys
import pandas as pd
import itertools
args=sys.argv
from scipy.spatial import distance
from scipy.stats import pearsonr,spearmanr
from sklearn.preprocessing import StandardScaler
import numpy as np

# file.csv optimal_aai_index

if len(args)!=3:
    print("Please provide the following 2 paramters: file_name.csv (output of GenerateDataFrame.py),index of the optimal AAI (index starts from 0) separated by space")
    sys.exit(0)
print(args[1]," - - ",args[2])
file=args[1]
df=pd.read_csv(file)
best_aai=[int(args[2])]
aai_idx=range(25)
aai_sets=list(itertools.product(best_aai,aai_idx))
aai_sets=[i for i in aai_sets if i[0]!=i[1]]

aai_vectors={k:[] for k in range(25)}
dataset={"aai_pair":[],"euclidean":[],"standard_euclidean":[],"manhattan":[],"chebyshev":[],"cosine":[],"pearson":[],"spearman":[]}
for i in range(1,26):
    aai_vectors[i-1]=list(df["S"+str(i)])
for i in aai_sets:
        dataset["aai_pair"].append(i)
        dataset["euclidean"].append(distance.euclidean(aai_vectors[i[0]],aai_vectors[i[1]]))

        sc=StandardScaler()
        i_0_scaled=sc.fit_transform(np.array(aai_vectors[i[0]]).reshape(-1,1))
        i_0_scaled=list(i_0_scaled.flatten())
        i_1_scaled = sc.fit_transform(np.array(aai_vectors[i[1]]).reshape(-1, 1))
        i_1_scaled=list(i_1_scaled.flatten())

        dataset["standard_euclidean"].append(distance.euclidean(i_0_scaled,i_1_scaled))
        dataset["manhattan"].append(distance.cityblock(aai_vectors[i[0]],aai_vectors[i[1]]))
        dataset["chebyshev"].append(distance.chebyshev(aai_vectors[i[0]],aai_vectors[i[1]]))
        dataset["cosine"].append(distance.cosine(aai_vectors[i[0]],aai_vectors[i[1]]))
        dataset["pearson"].append(pearsonr(aai_vectors[i[0]],aai_vectors[i[1]])[0])
        dataset["spearman"].append(spearmanr(aai_vectors[i[0]],aai_vectors[i[1]])[0])

df=pd.DataFrame(dataset)
df.to_csv("test_sample.csv")
