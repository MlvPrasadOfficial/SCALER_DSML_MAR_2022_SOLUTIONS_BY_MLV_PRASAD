class Solution:
	# @param A : tuple of integers
	# @return an integer
	def longestConsecutive(self, A):
        hMap = {}
        maxCount = 0
        for ele in A:
            if(hMap.get(ele) == None):
                lCount = 0
                rCount = 0
                if(hMap.get(ele - 1) != None):
                    lCount = hMap[ele - 1]
                if(hMap.get(ele + 1) != None):
                    rCount = hMap[ele + 1]
                hMap[ele] = lCount + 1 + rCount
                hMap[ele - lCount] = hMap[ele]
                hMap[ele + rCount] = hMap[ele]
                if(maxCount < lCount + 1 + rCount):
                    maxCount = lCount + 1 + rCount
        return maxCount