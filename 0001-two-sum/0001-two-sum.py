class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        size = len(nums)
        for i in range(size):
            for j in range(i,size-1):
                if nums[i] + nums[j+1] == target:
                    return [i,j+1]
