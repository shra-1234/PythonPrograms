class Solution(object):
    def check(self, nums): 
        for i in range(len(nums)):
            if(nums == sorted(nums)):
                return True
            nums = nums[1:] + nums[:1] # rotating the list without mutating
        return False
