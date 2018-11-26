'''
Created on 8. 7. 2018

@author: Tomáš
'''

from benchmark.model import BipartitniModel
from benchmark.powerLaw import powerLaw
import numpy as np


class BipartitniModelBuilder(object):
    '''
    A tool for simplier model creation. 
    '''

    def __init__(self, nodesCount : tuple=(50, 50)):
        '''
        Constructor
        '''
        self.setNodesCount(nodesCount)
        self.setDegreeAlpha(2.1)
        self._communities = ([], [])
        self._communityRelations = []
        
    def setNodesCount(self, nodesCount : tuple):
        self._nodesCount = nodesCount
        return self
    
    def setDegreeAlpha(self, alpha):
        self._alpha = alpha
        return self
    
    def addCommunityA(self, nodes, mu=0, force=1):
        self.addCommunity(0, nodes, mu, force)
        
    def addCommunityB(self, nodes, mu=0, force=1):
        self.addCommunity(1, nodes, mu, force)
        
    def addCommunity(self, cType, nodes, mu=0, force=1):
        '''
            mu \in [0,1) ... mixing factor
            force ... node "mixing factor" (as weight)
        '''
        assert max(nodes) < self._nodesCount[cType]
        self._communities[cType].append(dict(force=force, nodes=list(nodes)))
        return self
    
    def addCommunities(self, cType, count, mu=0, force=1):
        N = self._nodesCount
        membership = [np.random.randint(count) for n in range(N)]
        for K in range(count):
            self.addCommunity(cType, [i for i, m in zip(range(N), membership) if K == m],
                              mu, force)
        return self
    
    def addCommunityRelation(self, communityA, communityB, force=1):
        self._communityRelations.append((communityA, communityB, force))
    
    def getModel(self) -> BipartitniModel:
        A, B = self._getGroupMatrices()
        C = self._getCommunityMatrix() 
        model = BipartitniModel(A, B, C)
        return model
    
    def _getCommunityMatrix(self):  # TODO getCommunityMatrix
        Ka = len(self._communities[0])
        Kb = len(self._communities[1])
        C = np.zeros((Ka, Kb))
        for r in self._communityRelations: C[r[0], r[1]] = r[2]
        return C
        
    def _getGroupMatrices(self):
        degrees = self._getNodeDegrees()
        nodeForces = self._getNodeForces()
        N = self._nodesCount
        K = [len(self._communities[t]) for t in range(2)]
        Na = N[0]        
        Ka = K[0]
        groups = [np.array([[nodeForces(n + t * Na, c + t * Ka) * d 
                   for n, d in zip(range(N[t]), degrees[t])]
                    for c in range(K[t])])
                    for t in range(2)]
        return groups
            
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
        degrees = [[powerLaw(self._alpha) for i in range(N[t])] for t in range(2)]
        return degrees
    
    def _getMemberships(self):
        Na = self._nodesCount[0]
        Ka = len(self._communities[0])
        nodes = []
        for t in range(2): nodes.extend([n + t * Na for C in self._communities[t] for n in C['nodes']])
        memberships = {n: [] for n in nodes}
        for t in range(2):
            for c, C in enumerate(self._communities[t]):
                for n in C['nodes']:
                    memberships[n + t * Na].append(dict(community=c + t * Ka, force=C['force']))
        return memberships
    
