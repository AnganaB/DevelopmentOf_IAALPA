import pandas as pd
import csv
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import math
from itertools import combinations
import random
from auc import calculateM1, getAUCList, BestAUC, graphParams, getNetworkAUC, getBestAUC
from compute_features import cluster, node_betw, link_betw, shortest, avg_degree



def generate_df(edgelist):
    #read the csv
    network = pd.read_csv(edgelist)
    i = getBestAUC(edgelist)
    #generate a networkx graph as a directed graph as the given dataset is directional
    graph = nx.from_pandas_edgelist(network, source="Source", target="Target", create_using=nx.DiGraph())

    #create an undirected graph because freinship networks are undirected
    u_graph = graph.to_undirected()
    
    #create a list of (source, target) tuples and sort
    edgelist = [e for e in u_graph.edges]
    edgelist.sort()

    nodes = graph.number_of_nodes()
    edges = graph.number_of_edges()
    
    source = [e[0] for e in edgelist]
    target = [e[1] for e in edgelist]

    indices = []

    
    indv_indices = [
        avg_degree(graph, nodes),
        cluster(graph),
        shortest(graph),
        node_betw(graph, nodes),
        link_betw(graph, edges),
        i
    ]
    indices.append(indv_indices)
        
    data = {
        'Average_Degree': [index[0] for index in indices],
        'Average_Clustering_Coefficient': [index[1] for index in indices],
        'Average_Shortest_Path': [index[2] for index in indices],
        'Average_Node_Betweenness': [index[3] for index in indices],
        'Average_Link_Betweenness': [index[4] for index in indices],
        'Decision' : [index[5] for index in indices]
        
    }

    dataframe = pd.DataFrame(data)

    dataframe.to_csv('Dataset.csv', index=None)
    #dataframe.to_csv('Dataset.csv', mode = 'a', header=False, index=None)
    

    return dataframe
    
    
#main
def main():
    df = generate_df("/data/train/train2.csv")
    print(df.head())
		

if __name__ == "__main__":
    main()