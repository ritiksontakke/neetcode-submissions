class Solution:
    def solve(self, index , total, subset, num,target, result):
        if total == target:
            result.append(subset.copy())
            return
        elif total > target:
            return
        if index >=len(num):
            return
        Sum = total + num[index]
        subset.append(num[index])
        self.solve(index,Sum,subset,num,target,result)
        Sum = total
        subset.pop()
        self.solve(index+1,Sum,subset,num,target,result)


    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        self.solve(0,0,[],nums,target,result)
        return result
        