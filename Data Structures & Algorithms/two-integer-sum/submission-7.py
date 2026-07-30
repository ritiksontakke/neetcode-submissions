class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i,num  in enumerate(nums):
            sum1 = target - num

            if sum1 in seen:
                return[seen[sum1],i]
            seen[num] = i