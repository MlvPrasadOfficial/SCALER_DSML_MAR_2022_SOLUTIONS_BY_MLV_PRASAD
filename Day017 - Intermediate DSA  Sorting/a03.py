import functools
class Solution:
    def largestNumber(self, A):
        nums = A
        str_nums = map(str, nums)
        sort_rule = lambda x, y : 1 if x + y > y + x else -1
        sorted_nums = sorted(str_nums, key=functools.cmp_to_key(sort_rule), reverse=True)
        if sorted_nums[0] == '0':
            return '0'
        return ''.join(sorted_nums)