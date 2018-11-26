'''
Created on 26. 8. 2018

@author: Tomáš
'''
        
        
class MembershipsList(object):
    
    def __init__(self, param):
        self._list = param if type(param) == list else self._loadFromFile(param)
        
    def getMemberships(self):
        return self._list
    
    def getCommunities(self):
        return (c for c in range(self.getCommunityCount()))
        
    def getCommunityMembers(self, communityIndex : int):
        return self._list[communityIndex]
    
    def getCommunityCount(self):
        return len(self._list)
        
    def _loadFromFile(self, filename) -> list:    
        communities = [self._parseCommunity(community) for community in open(filename)]
        return communities
    
    def _parseCommunity(self, community) -> list:
        members = list(set([int(n) for n in community.split()]))
        return members
