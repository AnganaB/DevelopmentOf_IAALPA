import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import math

#Intersection of neighbor set
def neighbor(x,y, graph):
    nbr_x = set([n for n in graph.neighbors(x)])
    nbr_y = set([n for n in graph.neighbors(y)])
    intsctn = nbr_x.intersection(nbr_y)
    return intsctn

#Index 1: Salton
def salton(pair, graph):
    x,y = pair
    kx = graph.degree(x)
    ky = graph.degree(y)
    deno = math.sqrt(kx*ky)
    
    nume = len(neighbor(x,y,graph))
    if deno == 0:
        s = 0
    else:
        s = nume/deno
    return s
    
#Index 2: Sorenson
def sorenson(pair,graph):
    x,y = pair
    kx = graph.degree(x)
    ky = graph.degree(y)
    deno = kx + ky
    
    nume = 2 * len(neighbor(x,y,graph))
    
    if deno == 0:
        s = 0
    else:
        s = nume/deno
    
    return s
    
#Index 3: HPI
def hpi(pair,graph):
    x,y = pair
    kx = graph.degree(x)
    ky = graph.degree(y)
    deno = min(kx,ky)
    
    nume = len(neighbor(x,y,graph))
    
    if deno == 0:
        s = 0
    else:
        s = nume/deno
    
    return s
    
#Index 4: HDI
def hdi(pair,graph):
    x,y = pair
    kx = graph.degree(x)
    ky = graph.degree(y)
    deno = max(kx,ky)
    
    nume = len(neighbor(x,y,graph))
    
    if deno == 0:
        s = 0
    else:
        s = nume/deno
    
    return s


#Index 5: LHN
def lhn(pair,graph):
    x,y = pair
    kx = graph.degree(x)
    ky = graph.degree(y)
    deno = kx*ky
    
    nume = len(neighbor(x,y,graph))
    
    if deno == 0:
        s = 0
    else:
        s = nume/deno

    return s


#Index 6: PA
def pa(pair,graph):
    x,y = pair
    kx = graph.degree(x)
    ky = graph.degree(y)
    
    s = kx * ky
    
    return s


#Index 7: RA
def ra(pair,graph):
    x,y = pair
    n_list = neighbor(x,y,graph)
    
    s = 0
    
    for n in n_list:
        kn = graph.degree(n)
        if kn == 0:
            continue
        s = s + (1/kn)
    
    return s


#Index 8: RAA
def raa(pair,graph):
    x,y = pair
    n_list = neighbor(x,y,graph)
    kx = graph.degree(x)
    ky = graph.degree(y)
    k = max(kx,ky)
    
    s = 0
    
    for n in n_list:
        kn = graph.degree(n)
        if kn == 0:
            continue
        s = s + (k/kn)
        
    return s
    

#Index 9: WA1
def wa1(pair,graph):
    x,y = pair
    n_list = neighbor(x,y,graph)
    s = 0
        
    for n in n_list:
        n_n_list = [n_n for n_n in graph.neighbors(n)]
        n_sum = 0
        for node in n_n_list:
            kn = graph.degree(node)
            if kn == 0:
                continue
            n_sum = n_sum + (1/kn)
        s = s + n_sum
        
    return s
        

#Index 10: WA2
def wa2(pair,graph,rho,phi):
    x,y = pair
    n_list = neighbor(x,y,graph)
    s = 0
    
    for n in n_list:
        c_n = nx.clustering(graph,n)
        kn = graph.degree(n)
        val = kn * ((rho*c_n) + (phi* (1-c_n)))
        if val == 0:
            continue
        s = s + (1/val)
    
    return s



#Index 11: WA3
def wa3(pair,graph):
    x,y = pair
    n_list = neighbor(x,y,graph)
    kx = graph.degree(x)
    ky = graph.degree(y)
    c_x = nx.clustering(graph,x)
    c_y = nx.clustering(graph,y)
    
    if kx == 0 or c_x == 0:
        val1 = 0
    else:
        val1 = 1/(kx*c_x)
    
    if ky == 0 or c_y == 0:
        val2 = 0
    else:
        val2 = 1/(ky*c_y)
    
    s = 0
    
    for n in n_list:
        kn = graph.degree(n)
        c_n = nx.clustering(graph,n)
        if c_n == 1 or kn == 0:
            val3 = 0
        else:
            val3 = 1/(kn*(1-c_n))
        s = s+val1+val2+val3
        
    return s


#Index 12: RWA
def rwa(pair,graph,a,b,c,rho,phi):
    s = a*ra(pair,graph) + b*wa2(pair,graph,rho,phi) + c*wa3(pair,graph)
    return s


#Function to generate a pandas dataframe from an edgelist
#Pass a csv file containing edgelist labeled Source and Target
def generate_df(edgelist):
    #read the csv
    network = pd.read_csv(edgelist)
    
    #generate a networkx graph as a directed graph as the given dataset is directional
    graph = nx.from_pandas_edgelist(network, source="Source", target="Target", create_using=nx.DiGraph())
    
    #create an undirected graph because freinship networks are undirected
    u_graph = graph.to_undirected()

    #create a list of (source, target) tuples and sort
    edgelist = [e for e in u_graph.edges]
    edgelist.sort()

    source = [e[0] for e in edgelist]
    target = [e[1] for e in edgelist]

    indices = []

    for e in edgelist:
        indv_indices = [
            salton(e,u_graph),
            sorenson(e,u_graph),
            hpi(e,u_graph),
            hdi(e,u_graph),
            lhn(e,u_graph),
            pa(e,u_graph),
            ra(e,u_graph),
            wa1(e,u_graph),
            wa2(e,u_graph,1,4),
            wa2(e,u_graph,1,1),
            wa2(e,u_graph,4,1),
            raa(e,u_graph),
            wa3(e,u_graph),
            rwa(e,u_graph,1,1,1,1,4),
            rwa(e,u_graph,4,1,1,1,4),
            rwa(e,u_graph,1,4,1,1,4),
            rwa(e,u_graph,1,1,4,1,4),
            rwa(e,u_graph,1,1,1,1,1),
            rwa(e,u_graph,4,1,1,1,1),
            rwa(e,u_graph,1,4,1,1,1),
            rwa(e,u_graph,1,1,4,1,1),
            rwa(e,u_graph,1,1,1,4,1),
            rwa(e,u_graph,4,1,1,4,1),
            rwa(e,u_graph,1,4,1,4,1),
            rwa(e,u_graph,1,1,4,4,1),
        ]
        indices.append(indv_indices)
        
    data = {
        'Source':source,
        'Target':target,
        'S1': [index[0] for index in indices],
        'S2': [index[1] for index in indices],
        'S3': [index[2] for index in indices],
        'S4': [index[3] for index in indices],
        'S5': [index[4] for index in indices],
        'S6': [index[5] for index in indices],
        'S7': [index[6] for index in indices],
        'S8': [index[7] for index in indices],
        'S9': [index[8] for index in indices],
        'S10': [index[9] for index in indices],
        'S11': [index[10] for index in indices],
        'S12': [index[11] for index in indices],
        'S13': [index[12] for index in indices],
        'S14': [index[13] for index in indices],
        'S15': [index[14] for index in indices],
        'S16': [index[15] for index in indices],
        'S17': [index[16] for index in indices],
        'S18': [index[17] for index in indices],
        'S19': [index[18] for index in indices],
        'S20': [index[19] for index in indices],
        'S21': [index[20] for index in indices],
        'S22': [index[21] for index in indices],
        'S23': [index[22] for index in indices],
        'S24': [index[23] for index in indices],
        'S25': [index[24] for index in indices]
    }

    dataframe = pd.DataFrame(data)

    dataframe.to_csv('Dataset.csv',index=None)
    
    return dataframe


#main
def main():
    df = generate_df("dataset_renamed.csv")
    print(df.head())


if __name__ == "__main__":
    main()