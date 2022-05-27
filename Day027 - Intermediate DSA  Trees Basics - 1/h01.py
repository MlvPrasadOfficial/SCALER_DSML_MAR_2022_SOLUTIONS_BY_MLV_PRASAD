from collections import deque
class Solution:
	# @param A : root node of tree
	# @param B : root node of tree
	# @return an integer
	def isSameTree(self, A, B):


        p = A 
        q = B
         
        def check(p, q):
            # if both are None
            if not p and not q:
                return 1
            # one of p and q is None
            if not q or not p:
                return 0
            if p.val != q.val:
                return 0
            return 1
        
        deq = deque([(p, q),])
        while deq:
            p, q = deq.popleft()
            if not check(p, q):
                return 0
            
            if p:
                deq.append((p.left, q.left))
                deq.append((p.right, q.right))
                    
        return 1