import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from itertools import combinations
import random
from computeAAI import salton,sorenson,hdi,hpi,pa,ra,raa,lhn,wa1,wa2,wa3,rwa
from getAAI import s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18,s19,s20,s21,s22,s23,s24,s25


#generate function list
def functionList():
    return ['s1','s2','s3','s4','s5','s6','s7','s8','s9','s10','s11','s12',
    's13','s14','s15','s16','s17','s18','s19','s20','s21','s22','s23','s24','s25']

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
    con_size = len(connected)
    uncon_size = len(unconnected)
    minval = min(len(connected),len(unconnected))
    m = random.randrange(int(7*minval/10),int(minval*9/10))
    m1 = [0]*25

    func_list = functionList()
    
    for i in range(m):
        #pick two tuples randomly, one from connected and one from unconnected 
        idx_c = random.randrange(con_size)
        idx_u = random.randrange(uncon_size)
        
        c = connected[idx_c]
        u = unconnected[idx_u]
        
        #if connected_aai > unconnected aai then increement m1
        for i in range(25):
            aai_c = eval(func_list[i])(c,u_graph)
            aai_u = eval(func_list[i])(u,u_graph)
            if aai_c > aai_u:
                m1[i] = m1[i]+1

    return m, m1


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
#takes a .csv file as input
def getNetworkAUC(csvfile):
    
    u_graph, connected, unconnected = graphParams(csvfile)

    m,m1 = calculateM1(u_graph, connected, unconnected)
    
    auc_list = getAUCList(m,m1)
    
    return auc_list


#returns a number from 1-25 stating the best AAI
#takes a .csv file as input
def getBestAUC(csvfile):
    
    m1 = getNetworkAUC(csvfile)
    chosen_AAI = BestAUC(m1)

    return chosen_AAI

#returns the complementary indices of the best index for a given network
#takes a .csv file as imput along with the best index number
def getComplementaryAAI(csvfile, best_idx):
    u_graph, connected, unconnected = graphParams(csvfile)

    con_size = len(connected)
    uncon_size = len(unconnected)
    minval = min(len(connected),len(unconnected))
    m = random.randrange(int(7*minval/10),int(minval*9/10))
    m1 = [0]*25

    func_list = functionList()
    
    for i in range(m):
        #pick two tuples randomly, one from connected and one from unconnected 
        idx_c = random.randrange(con_size)
        idx_u = random.randrange(uncon_size)
        
        c = connected[idx_c]
        u = unconnected[idx_u]
        
        best_aai_c = eval(func_list[best_idx-1])(c,u_graph)
        best_aai_u = eval(func_list[best_idx-1])(u,u_graph)

        #if connected_aai > unconnected aai then increement m1
        for i in range(25):
            aai_c = eval(func_list[i])(c,u_graph)
            aai_u = eval(func_list[i])(u,u_graph)
            if (best_aai_c + aai_c) > (best_aai_u + aai_u):
                m1[i] = m1[i]+1

    auc_list = getAUCList(m,m1)
    auc_best = auc_list[best_idx-1]

    complm_idx = []

    for i in range(25):
        if auc_list[i]>auc_best:
            complm_idx.append(i+1)
    
    
    return complm_idx
