import auc_new
import itertools
from scipy.spatial import distance
from scipy.stats import pearsonr,spearmanr
import pandas as pd
from sklearn.preprocessing import StandardScaler
import numpy as np
if __name__=='__main__':
    stop=False
    while(not stop):
        stop=True

        # res[0] will contain a dictionary where the keys are the node pairs selected at random for calculation of AUC
        # and best AAI and corresponding to each node pair is a list containing the values for the AAIs in order.
        # That is 0th index will contain the value of S1 AAI, 1st index will contain that of S2 AAI.
        # Please refer the Paper for details about how the AAI algorithms are represented
        #
        # res[1] will contain the index of the best AAI based on random sampling
        #
        # res[2] will contain the complementary indices of the best AAI based on random sampling

        # replace sample.csv with your own edgelist.csv
        res=auc_new.main("sample.csv")
        
        if len(res[2]) ==0:
            continue
        aai_idx=range(25)
        aai_sets=list(itertools.product(aai_idx,aai_idx))
        aai_sets=[i for i in aai_sets if i[0]<i[1]]

        # aai_sets will contain all possible 300 pairs of AAI from the 25 AAIs
        
        aai_vectors={k:[] for k in range(25)}
        for i in range(25):
            for j in res[0]:
                d=res[0][j]
                d=d[i]
                aai_vectors[i].append(d)
                
        # aai_vectors will contain the list of values for each AAI based on the random samples

        # The code below forms the dataset by calculating the 7 similarity indices between AAI pairs
    
        dataset={"aai_pair":[],"euclidean":[],"standard_euclidean":[],"manhattan":[],"chebyshev":[],"cosine":[],"pearson":[],"spearman":[],"M":[]}
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

            if (i[0]==res[1] and (i[1] in res[2])) or (i[1]==res[1] and (i[0] in res[2])):
                dataset["M"].append(1)
            else:
                dataset["M"].append(-1)
        df=pd.DataFrame(dataset)
        df.to_csv("train_sample.csv")
        f=open("details.txt","w")
        f.write(str(res[0])+"\n"+str(res[1])+"\n"+str(res[2]))



