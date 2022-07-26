class Solution:
    # @param A : root node of tree
    # @return an integer
    def solve(self, A):
        count = 0
        queue = [] 
        queue.append(A) 
        while(len(queue) > 0): 
            node = queue.pop(0) 
            if node is None:
                continue
            count = count+1
            queue.append(node.left) 
            queue.append(node.right) 
        return count