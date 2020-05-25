import pandas as pd
import csv
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import math
from itertools import combinations
import random


# average clustering coefficient
def cluster(graph):
    return (nx.average_clustering(graph))

#average node betweenness  
def node_betw(graph, nodes):
    return (sum(nx.betweenness_centrality(graph))/nodes)

#average link betweenness
def link_betw(graph, edges):
    edge_betw = nx.edge_betweenness_centrality(graph)
    tot = 0
    for e in edge_betw: 
        tot = tot + edge_betw[e]  
    edge_betweenness = tot/edges
    return edge_betweenness

#average shortest path
def shortest(graph):
    return (nx.average_shortest_path_length(graph))

#average degree
def avg_degree(graph, nodes):
    deg = graph.degree()
    sum_deg = [d[1] for d in deg]
    average_degree = sum(sum_deg)/(nodes*2)
    return average_degree
