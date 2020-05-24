import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from computeAAI import salton,sorenson,hdi,hpi,pa,ra,raa,lhn,wa1,wa2,wa3,rwa

def s1(pair,graph):
    s = salton(pair,graph)
    return s

def s2(pair,graph):
    s = sorenson(pair,graph)
    return s

def s3(pair,graph):
    s = hpi(pair,graph)
    return s

def s4(pair,graph):
    s = hdi(pair,graph)
    return s

def s5(pair,graph):
    s = lhn(pair,graph)
    return s

def s6(pair,graph):
    s = pa(pair,graph)
    return s

def s7(pair,graph):
    s = ra(pair,graph)
    return s

def s8(pair,graph):
    s = wa1(pair,graph)
    return s

def s9(pair,graph):
    s = wa2(pair,graph,1,4)
    return s

def s10(pair,graph):
    s = wa2(pair,graph,1,1)
    return s

def s11(pair,graph):
    s = wa2(pair,graph,4,1)
    return s

def s12(pair,graph):
    s = raa(pair,graph)
    return s

def s13(pair,graph):
    s = wa3(pair,graph)
    return s

def s14(pair,graph):
    s = rwa(pair,graph,1,1,1,1,4)
    return s

def s15(pair,graph):
    s = rwa(pair,graph,4,1,1,1,4)
    return s

def s16(pair,graph):
    s = rwa(pair,graph,1,4,1,1,4)
    return s

def s17(pair,graph):
    s = rwa(pair,graph,1,1,4,1,4)
    return s

def s18(pair,graph):
    s = rwa(pair,graph,1,1,1,1,1)
    return s

def s19(pair,graph):
    s = rwa(pair,graph,4,1,1,1,1)
    return s

def s20(pair,graph):
    s = rwa(pair,graph,1,4,1,1,1)
    return s

def s21(pair,graph):
    s = rwa(pair,graph,1,1,4,1,1)
    return s

def s22(pair,graph):
    s = rwa(pair,graph,1,1,1,4,1)
    return s

def s23(pair,graph):
    s = rwa(pair,graph,4,1,1,4,1)
    return s

def s24(pair,graph):
    s = rwa(pair,graph,1,4,1,4,1)
    return s

def s25(pair,graph):
    s = rwa(pair,graph,1,1,4,4,1)
    return s
