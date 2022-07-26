# # This is the interface that allows for creating nested lists.
# # You should not implement it, or speculate about its implementation
# class NestedInteger:
#     def __init__(self, x):
        
#     # Return true if this NestedInteger holds a single integer, rather than a nested list.
#     def isInteger(self):
        
#     # Return the single integer that this NestedInteger holds, if it holds a single integer
#     # The result is 1e9 if this NestedInteger holds a nested list
#     def getInteger(self):
        
#     # Return the nested list that this NestedInteger holds, if it holds a nested list
#     # The result is an empty list if this NestedInteger holds a single integer
#     def getList(self):
        
class NestedIterator:
    def __init__(self, nestedList):
        self.nestedList = nestedList
        self.flattened_list = []
        self.flatten(nestedList)
    
    def flatten(self,nestedList):
        for el in nestedList:
            if el.isInteger():
                self.flattened_list.append(el.getInteger())
            else:
                self.flatten(el.getList())

    def next(self):
        if self.hasNext():
            return self.flattened_list.pop(0)        
    def hasNext(self):
        return bool(len(self.flattened_list))