'''
Created on 8. 7. 2018

@author: Tomáš
'''

from benchmark.model import Model
from benchmark.powerLaw import powerLaw
import numpy as np


class ModelBuilder(object):
    '''
    A tool for simplier model creation. 
    '''

    def __init__(self, nodesCount : int=100):
        '''
        Constructor
        '''
        self.setNodesCount(nodesCount)
        self._alpha = 2.1
        self._communities = []
        
    def setNodesCount(self, nodesCount : int):
        self._nodesCount = nodesCount
        return self
    
    def setDegreeAlpha(self, alpha):
        self._alpha = alpha
        return self
        
    def addCommunity(self, nodes, mu=0, force=1):
        '''
            mu \in [0,1) ... mixing factor
            force ... node "mixing factor" (as weight)
        '''
        self._communities.append(dict(mu=mu, force=force, nodes=list(nodes)))
        return self
    
    def addCommunities(self, count, mu=0, force=1):
        N = self._nodesCount
        membership = [np.random.randint(count) for n in range(N)]
        for K in range(count):
            self.addCommunity([i for i, m in zip(range(N), membership) if K == m],
                              mu, force)
        return self
    
    def getModel(self) -> Model:
        G = self._getGroupMatrix()
        omega = self._getCommunityMatrix()
        model = Model(G, omega)
        return model
    
    def _getCommunityMatrix(self):
        K = len(self._communities)
        return np.eye(K, K)
        
    def _getGroupMatrix(self):
        degrees = self._getNodeDegrees()
        nodeForces = self._getNodeForces()
        N = self._nodesCount
        K = len(self._communities)
        groups = [[nodeForces(n, c) * d 
                   for n, d in zip(range(N), degrees)]
                    for c in range(K)]
        return np.array(groups)
            
    def _getNodeForces(self):
        '''
        return a function that contains a dictionary 
        with key (node,community)
        and value fraction of node's force in this community
        returns zero if key is missing
        '''
        memberships = self._getMemberships()
        forceSums = {n: sum([M['force'] for M in memberships[n]])
                      for n in memberships}
        nodeForces = {(n, M['community']) : M['force'] / forceSums[n]
                      for n in memberships
                      for M in memberships[n]}

        def nodeForcesCall(node, community):
            if (node, community) in nodeForces:
                return nodeForces[(node, community)]
            else: return 0

        return nodeForcesCall
        
    def _getNodeDegrees(self):
        N = self._nodesCount
        degrees = [powerLaw(self._alpha) for i in range(N)]
        return degrees
    
    def _getMemberships(self):
        nodes = [n for C in self._communities for n in C['nodes']]
        memberships = {n: [] for n in nodes}
        for c, C in enumerate(self._communities):
            for n in C['nodes']:
                memberships[n].append(dict(community=c, force=C['force']))
        return memberships
    
