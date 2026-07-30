class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}

        for i , num in enumerate(nums):
            comlement =  target - num

            if comlement in seen:
                return [seen[comlement], i]

            seen[num] = i