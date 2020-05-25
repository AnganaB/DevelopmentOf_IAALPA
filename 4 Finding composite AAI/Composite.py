import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from getAAI import s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18,s19,s20,s21,s22,s23,s24,s25
from auc import getNetworkAUC, getBestAUC, getComplementaryAAI, functionList, getEdgelist


def getCompositeIndex(pair,graph,best_idx,complm_idx,nw_auc):
    
    #get AUC of best index and complementary indices
    all_idx = [best_idx] + [i for i in complm_idx]
    auc_val = []

    for i in all_idx:
        auc_val.append(nw_auc[i-1])
    
    #index values for a node pair
    fn_list = functionList()
    aai_val = []

    for idx in complm_idx:
        aai_val.append(eval(fn_list[idx-1])(pair,graph))
    
    s = sum([a*b for a,b in zip(auc_val,aai_val)])
    
    return s

def main():
    csv = "Dataset/network_edgelist.csv"

    #load the edgelist from the csv file 
    n = pd.read_csv(csv)

    #create a networkx graph from the edgelist and display
    network = nx.from_pandas_edgelist(n, source="Source", target="Target", create_using=nx.DiGraph()).to_undirected()


    ###################################################################
    #In the actual implementation
    #network_auc and best_idx will be the output of the decision tree
    #complm_idx will be the output of the SVM
    #This is just for demonstration
    ###################################################################


    #computing the AUC of all the AAIs of the given network
    #computed by random sampling as mentioned in theory and hence the value changes everytime it is run

    network_auc = getNetworkAUC(csv)

    #get the best auc of the network
    # 1 indicates s1, 2 indicated s2 and so on
    #computed by random sampling as mentioned in theory and hence the value changes everytime it is run

    best_idx = getBestAUC(csv)

    #get the complementary AAIs for the network given best index is 11
    # 1 indicates s1, 2 indicated s2 and so on

    complm_idx = getComplementaryAAI(csv,best_idx)

    #get AUC of best index and complementary indices

    all_idx = [best_idx] + [i for i in complm_idx]
    auc_val = []

    for i in all_idx:
        auc_val.append(network_auc[i-1])
        
    #let us pick a random pair of nodes from the graph, say (4,10)
    e = (4,10)

    #composite index
    cmpst_idx = getCompositeIndex(e,network,best_idx,complm_idx,network_auc)


if __name__=="__main__":
    main()

