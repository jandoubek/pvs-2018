'''
Created on 4. 6. 2018

@author: Tom
'''

import networkx as nx
import numpy as np

from .zadani import *
from benchmark.model import BipartitniModel


class Generator(object):
    '''
    classdocs
    '''

    def __init__(self, zadaniNeboModel):
        '''
        Constructor
        '''
        if isinstance(zadaniNeboModel, Zadani):
            self.zadani = zadaniNeboModel
        elif isinstance(zadaniNeboModel, Model):
            self.zadani = Zadani(zadaniNeboModel, count=1)
        else: raise NotImplementedError()
        
    def __call__(self) -> list:
        return [graph for graph in self]
    
    def __iter__(self):
        return (self.generate(model) for model in self.zadani.getModels())
    
    def next(self):
        for graph in self: break
        return graph
        
    def generate(self, model):
        weights = self.__vyrobVahy(model)
        graph = self.__generuj(weights)
        comsLabels = self.__getCommunityLabels(model)
        nx.set_node_attributes(graph, comsLabels, 'community')
        if isinstance(model, BipartitniModel):
            positions = self.__getNodePositions(model)
            nx.set_node_attributes(graph, positions, 'viz')
            types = {n + 1: model.GetNodeType(n) for n in range(model.get_num_nodes())}
            nx.set_node_attributes(graph, types, 'type')
        return graph
        
    def __vyrobVahy(self, model):
        groups = model.G
        behavior = model.omega
        return groups.transpose().dot(behavior).dot(groups)
    
    def __generuj(self, weights : np.array) -> nx.Graph:
        G = nx.Graph()
        N, _ = weights.shape
        for i in range(N):
            G.add_node(i + 1, node_index=i)
        for i in range(N):
            for j in range(i + 1, N):
                if np.random.rand() < 1 - np.exp(-weights[i, j]):
                    G.add_edge(i + 1, j + 1)
        return G
    
    def __getCommunityLabels(self, model):
        coms = {}
        for n in range(model.get_num_nodes()):
            coms[n + 1] = str(model.getCommunities(n))
        return coms
    
    def __getNodePositions(self, model):
        viz = {}
        nums = [0, 0]
        for n in range(model.get_num_nodes()):
            t = model.GetNodeType(n)
            viz[n + 1] = {'position':{'x':nums[t] * 10.0, 'y':1000.0 * t, 'z':0.0}}
            nums[t] += 1
        return viz
    
        
BipartitniGenerator = Generator
