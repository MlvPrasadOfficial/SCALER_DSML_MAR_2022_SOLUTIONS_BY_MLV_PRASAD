class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        a = A
        hmap = dict()
        minDistance = 10**9

        # Initialize previousIndex
        # and currentIndex as 0
        previousIndex = 0
        currentIndex = 0

        # Traverse the array and
        # find the minimum distance
        # between the same elements with map
        for i in range(len(a)):

            if a[i] in hmap:
                currentIndex = i

                # Fetch the previous index from map.
                previousIndex = hmap[a[i]]

                # Find the minimum distance.
                minDistance = min((currentIndex -
                            previousIndex), minDistance)

            # Update the map.
            hmap[a[i]] = i

        # return minimum distance,
        # if no such elements found, return -1
        if minDistance == 10**9:
            return -1
        return minDistance
