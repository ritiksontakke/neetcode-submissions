class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        num_of_index={}

        for i, num in enumerate(nums):
            complement = target-num

            if complement in num_of_index:
                return [num_of_index[complement],i]

            num_of_index[num] =i 
