'''
Created on 5. 6. 2018

@author: Tom
'''
import numpy as np


class Model(object):
    '''
    classdocs
    '''

    def __init__(self, G : np.ndarray, omega : np.ndarray):
        '''
        Constructor
        '''
        assert(np.min(G) >= 0)
        assert(np.min(omega) >= 0 and np.max(omega) <= 1)
        
        self.G = G 
        self.omega = omega 
        
        self.__LoadNumsFromMatrix(G)

    def get_num_coms(self):
        return self.__numComs

    def get_num_nodes(self):
        return self.__numNodes

    numComs = property(get_num_coms, None, None, None)
    numNodes = property(get_num_nodes, None, None, None)
        
    def getCommunities(self, node : int, edgesNum : int=None):
        treshold = self.__getMembershipTreshold(edgesNum)
        memberships = self.G[:, node]
        return tuple([n for n, v in enumerate(memberships) if v > treshold])
        
    def getMaxCommunity(self, node : int) -> int:
        ''' returns number of community with maximal node's membership '''
        memberships = self.G[:, node]
        maxcomm = np.argmax(memberships)
        if memberships[maxcomm] == 0: return -1
        return maxcomm
    
    def getMemberships(self, edgesNum=None):
        return [[(n + 1) for n in self.getMembers(c, edgesNum)] for c in range(self.get_num_coms())]
    
    def getMembers(self, community : int, edgesNum=None):
        treshold = self.__getMembershipTreshold(edgesNum)
        memberships = self.G[community, :]
        return tuple([n for n, v in enumerate(memberships) if v > treshold])
        
    def __LoadNumsFromMatrix(self, G : np.ndarray):
        self.__numComs, self.__numNodes = self.G.shape
        
    def __getMembershipTreshold(self, edgesNum :int=None):
        # treshold epsilon community podle 4.2.3 v BP
        if edgesNum:
            n = self.get_num_nodes()
            m = edgesNum
            treshold = 2 * m / n / (n - 1)
        else: treshold = 0  # np.mean(self.G)*0.1
        return treshold

        
class BipartitniModel(Model):

    def __init__(self, A : np.ndarray, B : np.ndarray, C : np.ndarray):
        '''
        Parametry:
        A: matice rozmeru kA x nA (pocet komunit x pocet uzlu typu A)
        B: matice rozmeru kB x nB (pocet komunit x pocet uzlu typu B)
        C: matice rozmeru kA x kB
        '''
        
        assert(np.min(A) >= 0 and np.min(B) >= 0)
        assert(np.min(C) >= 0 and np.max(C) <= 1)
        
        self.A = A
        self.B = B 
        self.C = C 
        
        G, omega = self.ConvertModel(A, B, C)
        super().__init__(G, omega)
        
        self.__LoadNumsFromMatrices(A, B)

    def get_num_coms_type_a(self):
        return self.__numComsTypeA

    def get_num_nodes_type_a(self):
        return self.__numNodesTypeA

    def get_num_coms_type_b(self):
        return self.__numComsTypeB

    def get_num_nodes_type_b(self):
        return self.__numNodesTypeB

    numComsTypeA = property(get_num_coms_type_a, None, None, None)
    numNodesTypeA = property(get_num_nodes_type_a, None, None, None)
    numComsTypeB = property(get_num_coms_type_b, None, None, None)
    numNodesTypeB = property(get_num_nodes_type_b, None, None, None)
        
    def GetNodeType(self, node : int) -> int:
        return 0 if node < self.A.shape[1] else 1
        
    def ConvertModel(self, A : np.ndarray, B : np.ndarray, C : np.ndarray):
        '''
        Prevede bipartitni model A,B,C na obecny G a omega
        '''
        kA, nA = A.shape
        kB, nB = B.shape
        assert(C.shape[0] == kA and C.shape[1] == kB)
        
        G = np.zeros((kA + kB, nA + nB))
        G[0:kA, 0:nA] = A
        G[kA:(kA + kB), nA:(nA + nB)] = B
        
        omega = np.zeros((kA + kB, kA + kB))
        omega[0:kA, kA:(kA + kB)] = C
        omega[kA:(kA + kB), 0:kA] = C.transpose()
        
        return G, omega
    
    def __LoadNumsFromMatrices(self, A : np.ndarray, B : np.ndarray):
        self.__numComsTypeA, self.__numNodesTypeA = A.shape
        self.__numComsTypeB, self.__numNodesTypeB = B.shape
