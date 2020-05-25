import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from itertools import combinations
import random
from GenerateDataFrame import salton,sorenson,hdi,hpi,pa,ra,raa,lhn,wa1,wa2,wa3,rwa

#returns list of (a,b) pairs sorted by a and a<b 
def getEdgelist(graph):
    edgelist = [e for e in graph.edges]
    for i,e in enumerate(edgelist):
        if(e[0]>e[1]):
            edgelist[i] = (e[1],e[0])
    
    edgelist.sort()

    return edgelist


#generates all the unconnected pairs of nodes
def getUnconnectedPairs(graph,edgelist):
    unique_nodes = [u for u in graph.nodes]
    unique_nodes.sort()
    l = [c for c in combinations(unique_nodes,2)]
    unconnected = list(set(l).difference(set(edgelist)))

    return unconnected
    

#picks an m and calculated m1 values 
def calculateM1(u_graph,connected,unconnected):

    aai_d=dict({})
    
    con_size = len(connected)
    uncon_size = len(unconnected)
    minval = min(len(connected),len(unconnected))
    m = random.randrange(int(7*minval/10),int(minval*9/10))
    m1 = [0]*25
    for i in range(m):
        #pick two tuples randomly, one from connected and one from unconnected 
        idx_c = random.randrange(con_size)
        idx_u = random.randrange(uncon_size)
        
        c = connected[idx_c]
        
        aai_c = [
            salton(c,u_graph),
            sorenson(c,u_graph),
            hpi(c,u_graph),
            hdi(c,u_graph),
            lhn(c,u_graph),
            pa(c,u_graph),
            ra(c,u_graph),
            wa1(c,u_graph),
            wa2(c,u_graph,1,4),
            wa2(c,u_graph,1,1),
            wa2(c,u_graph,4,1),
            raa(c,u_graph),
            wa3(c,u_graph),
            rwa(c,u_graph,1,1,1,1,4),
            rwa(c,u_graph,4,1,1,1,4),
            rwa(c,u_graph,1,4,1,1,4),
            rwa(c,u_graph,1,1,4,1,4),
            rwa(c,u_graph,1,1,1,1,1),
            rwa(c,u_graph,4,1,1,1,1),
            rwa(c,u_graph,1,4,1,1,1),
            rwa(c,u_graph,1,1,4,1,1),
            rwa(c,u_graph,1,1,1,4,1),
            rwa(c,u_graph,4,1,1,4,1),
            rwa(c,u_graph,1,4,1,4,1),
            rwa(c,u_graph,1,1,4,4,1),
        ]
        
        u = unconnected[idx_u]
        
        aai_u = [
            salton(u,u_graph),
            sorenson(u,u_graph),
            hpi(u,u_graph),
            hdi(u,u_graph),
            lhn(u,u_graph),
            pa(u,u_graph),
            ra(u,u_graph),
            wa1(u,u_graph),
            wa2(u,u_graph,1,4),
            wa2(u,u_graph,1,1),
            wa2(u,u_graph,4,1),
            raa(u,u_graph),
            wa3(u,u_graph),
            rwa(u,u_graph,1,1,1,1,4),
            rwa(u,u_graph,4,1,1,1,4),
            rwa(u,u_graph,1,4,1,1,4),
            rwa(u,u_graph,1,1,4,1,4),
            rwa(u,u_graph,1,1,1,1,1),
            rwa(u,u_graph,4,1,1,1,1),
            rwa(u,u_graph,1,4,1,1,1),
            rwa(u,u_graph,1,1,4,1,1),
            rwa(u,u_graph,1,1,1,4,1),
            rwa(u,u_graph,4,1,1,4,1),
            rwa(u,u_graph,1,4,1,4,1),
            rwa(u,u_graph,1,1,4,4,1),
        ]
        #if connected_aai > unconnected aai then increement m1
        for i in range(25):
            if aai_c[i] > aai_u[i]:
                m1[i] = m1[i]+1

        aai_d[c]=aai_c
        aai_d[u]=aai_u
    
    return aai_d,m, m1


#generates a list of AUC for all AAIs
def getAUCList(m,m1):
    auc_list = []
    for i in range(25):
        if m==0:
            auc_list.append(0)
        else:
            auc_list.append(0.5+(m1[i]/(2*m)))
    
    return auc_list


#selecting aai with max auc value
#if multiple aai has the max value, any one of them can be chosen at random
#returns an integer between 1 to 25 denoting the aai 

def BestAUC(m1):
    max_m1 = max(m1)
    max_idx = []

    for i in range(25):
        if m1[i] == max_m1:
            max_idx.append(i)

    max_idx_size = len(max_idx)

    index = random.randrange(max_idx_size)
    chosen_idx = max_idx[index] + 1
    
    return chosen_idx



#read csv
def graphParams(csvfile):
    network = pd.read_csv(csvfile)
    g_network = nx.from_pandas_edgelist(network, source='Source', target='Target', create_using=nx.DiGraph()) 

    #create undirected graph
    u_graph = g_network.to_undirected()
    edgelist = getEdgelist(u_graph)

    #get unconnected pairs
    unconnected = getUnconnectedPairs(u_graph,edgelist)
    connected = edgelist

    return u_graph,connected,unconnected


#returns a list of AUC for a network
def getNetworkAUC(csvfile):
    
    u_graph, connected, unconnected = graphParams(csvfile)

    aai_d,m,m1 = calculateM1(u_graph, connected, unconnected)
    
    auc_list = getAUCList(m,m1)
    
    return auc_list


#returns a number from 1-25 stating the best AAI
def getBestAUC(csvfile):
    
    m1 = getNetworkAUC(csvfile)
    chosen_AAI = BestAUC(m1)

    return chosen_AAI

def getComplementaryAAI(csvfile, best_idx):
    u_graph, connected, unconnected = graphParams(csvfile)

    aai_d,m,m1 = calculateM1(u_graph, connected, unconnected)

    best_m1 = m1[best_idx - 1]

    complm_idx = []

    auc_best = 0.5+(best_m1/(2*m))

    for i in range(25):
        new_m1 = best_m1 + m1[i]
        new_m = 2*m

        new_auc = 0.5+(new_m1/(2*new_m))

        if new_auc > auc_best:
            complm_idx.append(i)
    
    return aai_d,complm_idx



def main(dataset="dataset_renamed.csv"):
    i = getBestAUC(dataset)-1
    aai_d,complm_idx = getComplementaryAAI("dataset_renamed.csv",i)
    print(i,complm_idx)
    return aai_d,i,complm_idx

if __name__ == "__main__":
    main()
