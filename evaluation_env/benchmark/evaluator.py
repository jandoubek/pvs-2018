'''
Created on 26. 8. 2018

@author: Tomáš
'''

from benchmark.membershipList import MembershipsList
import numpy as np
from builtins import callable
import matplotlib.pyplot as plt


class Evaluator(object):
    '''
    classdocs
    '''

    def __init__(self, original : MembershipsList, detected : MembershipsList):
        '''
        Constructor
        '''
        self.__original = original if isinstance(original, MembershipsList) else MembershipsList(original)
        self.__detected = detected if isinstance(detected, MembershipsList) else MembershipsList(detected)
        self._computeNodes()
        self.plot = EvaluatorPlotter(self)

    def get_nodes_count(self):
        return self.__nodesCount

    def get_original(self) -> MembershipsList:
        return self.__original

    def get_detected(self) -> MembershipsList:
        return self.__detected
    
    def __call__(self):
        return self.compare()
    
    def evaluate(self, fraction=True):
        aggregated = self.aggregate(self.get_original(), self.get_detected())
        if fraction:
            selfAggregated = self.selfFraction(aggregated)
            selfOriginal = self.selfFraction(self.get_original())
            return self._frobenius(selfAggregated, selfOriginal)
        selfAggregated = self.selfJaccard(aggregated)
        selfOriginal = self.selfJaccard(self.get_original())
        return self._frobenius(selfAggregated, selfOriginal)
    
    def selfJaccard(self, memberhips : MembershipsList) -> np.ndarray:
        return self.jaccard(memberhips, memberhips)
    
    def jaccard(self, original : MembershipsList=None, detected : MembershipsList=None) -> np.ndarray:
        if not original: original = self.get_original()
        if not detected: detected = self.get_detected()
        return self._compare(original, detected, lambda a, b: self._setJaccard(a, b))
    
    def selfFraction(self, memberhips : MembershipsList) -> np.ndarray:
        return self.fraction(memberhips, memberhips)
    
    def fraction(self, original : MembershipsList=None, detected : MembershipsList=None) -> np.ndarray:
        if not original: original = self.get_original()
        if not detected: detected = self.get_detected()
        return self._compare(original, detected, lambda a, b: self._setFraction(a, b))
    
    def aggregate(self, original : MembershipsList=None, detected : MembershipsList=None):
        if not original: original = self.get_original()
        if not detected: detected = self.get_detected()
        matches = [self._bestMatch(m, original) for m in detected.getMemberships()]
        aggregated = self._joinByMatches(matches, detected, original.getCommunityCount())
        return MembershipsList(aggregated)
        
    def _bestMatch(self, members : list, original : MembershipsList):
        memberSet = set(members)
        maximum = 0
        maximumIndex = None
        for ci, m in enumerate(original.getMemberships()):
            value = self._setJaccard(memberSet, m)
            if value > maximum:
                maximum = value
                maximumIndex = ci
        return maximumIndex
    
    def _joinByMatches(self, matches : list, detected : MembershipsList, outComsCount : int):
        transposed = self._transposeMatches(matches, outComsCount)
        # spoji vrcholy v komunitach ze seznamu coms v transpozed
        # udela z nich mnozinu (odstrani se duplicity) a pak zase seznam 
        aggregated = [list(set([m for i in coms for m in detected.getCommunityMembers(i)])) for coms in transposed]
        return aggregated
    
    def _transposeMatches(self, matches : list, outComsCount : int) -> list:
        transposed = [[] for c in range(outComsCount)]
        for c, m in enumerate(matches):
            if m is not None: transposed[m].append(c)
        return transposed
        
    def _compare(self, original : MembershipsList, detected : MembershipsList, metricsFcn : callable) -> np.ndarray:
        matrix = np.zeros((detected.getCommunityCount(), original.getCommunityCount()))
        for dci in detected.getCommunities():
            detectedMembersSet = set(detected.getCommunityMembers(dci))
            for oci in original.getCommunities():
                matrix[dci, oci] = metricsFcn(detectedMembersSet, original.getCommunityMembers(oci))
        return matrix
    
    def _setJaccard(self, A, B):
        As = set(A)
        Bs = set(B)
        denom = len(As | Bs)
        return float(len(As & Bs)) / denom if denom > 0 else 0
    
    def _setFraction(self, A, B):
        As = set(A)
        Bs = set(B)
        return float(len(As & Bs)) / self.get_nodes_count()
        
    def _frobenius(self, A, B):
        X = A - B 
        return np.sqrt(np.sum([x * x for x in X.flat]))
    
    def _computeNodes(self):
        nodes = set()    
        coms = self.get_original().getMemberships() + self.get_detected().getMemberships()
        for c in coms: nodes |= set(c)
        self.__nodesCount = len(nodes)

    original = property(get_original, None, None, "original community membership list")
    detected = property(get_detected, None, None, "detected detected membership list")
    nodesCount = property(get_nodes_count, None, None, "count of nodes")

    
class EvaluatorPlotter(object):

    def __init__(self, parent : Evaluator):
        self.__parent = parent
        
    def comparison(self, filename, fraction=False, ordered=True):
        if fraction: self.fraction(filename, ordered)
        else: self.jaccard(filename, ordered)
        
    def jaccard(self, filename, ordered=True):
        matrix = self.__parent.jaccard()
        self._plotOrderedMatrix(matrix, filename, ordered)
        
    def fraction(self, filename, ordered=True):
        matrix = self.__parent.fraction()
        self._plotOrderedMatrix(matrix, filename, ordered)
        
    def aggregated(self, filename, fraction=False, ordered=True):
        aggregated = self.__parent.aggregate()
        getMatrix = (lambda a, b: self.__parent.fraction(a, b)) if fraction else (lambda a,b: self.__parent.jaccard(a, b))
        matrix = getMatrix(self.__parent.get_original(), aggregated)
        self._plotOrderedMatrix(matrix, filename, ordered)
        
    def selfAggregated(self, filename, fraction=False, ordered=True):
        memberships = self.__parent.aggregate()
        self._plotSelfMemberships(filename, memberships, fraction, ordered)
        
    def selfOriginal(self, filename, fraction=False, ordered=True):
        memberships = self.__parent.get_original()
        self._plotSelfMemberships(filename, memberships, fraction, ordered)
        
    def selfDetected(self, filename, fraction=False, ordered=True):
        memberships = self.__parent.get_detected()
        self._plotSelfMemberships(filename, memberships, fraction, ordered)
        
    def _plotSelfMemberships(self, filename, memberships : MembershipsList, fraction=False, ordered=False):
        matrix = self.__parent.selfFraction(memberships) if fraction else self.__parent.selfJaccard(memberships)
        self._plotOrderedMatrix(matrix, filename, ordered)
        
    def _plotOrderedMatrix(self, matrix : np.ndarray, filename, ordered=True, _format='{:.3f}'):
        rows, cols = self._getMaxOrderedIndexes(matrix, ordered)
        self._plotMatrix(matrix, rows, cols, filename)
    
    def _plotMatrix(self, matrix : np.ndarray, rows, columns, filename, _format='{:.3f}'):
        ordered = self._getSubmatrix(matrix, rows, columns)
        _, ax = plt.subplots()
        ax.matshow(ordered, cmap='rainbow')
        
        for (i, j), z in np.ndenumerate(ordered):
            ax.text(j, i, _format.format(z), ha='center', va='center')
        
        x_labels = [j + 1 for j in columns]
        y_labels = [i + 1 for i in rows]
        ax.set_xticklabels([-1] + x_labels)
        ax.set_yticklabels([-2] + y_labels)
        
        plt.savefig(filename)
        plt.close()
    
    def _getMaxOrderedIndexes(self, matrix : np.ndarray, ordered=True):
        R = [i for i in range(matrix.shape[0])]
        C = [j for j in range(matrix.shape[1])]
        if not ordered: return R, C
        rows = []
        columns = []
        while len(R) * len(C) > 0:
            submatrix = self._getSubmatrix(matrix, R, C)
            r, c = self._findMax(submatrix)
            rows.append(R[r])
            columns.append(C[c])
            del R[r]
            del C[c]
        rows += R
        columns += C
        return  rows, columns
    
    def _getSubmatrix(self, matrix : np.ndarray, rows, columns):
        return matrix[rows][:, columns]
    
    def _findMax(self, matrix : np.ndarray):
        res = np.where(matrix == np.max(matrix))
        return tuple([v[0] for v in res])
