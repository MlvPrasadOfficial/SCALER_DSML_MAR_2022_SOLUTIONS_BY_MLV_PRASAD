from collections import defaultdict
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def lszero(self, A):
        N = len(A)
        pre = []
        curr = 0
        for i in range(N):
            curr += A[i]
            pre.append(curr)        
        #print pre            
        seen_table = defaultdict(list)
        seen_table[0]=[-1]
        longest = -1
        indices = None
        for i in range(N):
            s = pre[i]
            seen_table[s].append(i)
            gap = seen_table[s][-1] - seen_table[s][0]
            if gap > longest:
                longest = gap
                indices = (seen_table[s][0]+1,seen_table[s][-1]+1)
        if indices:
            return A[indices[0]:indices[1]]
        else:
            return []