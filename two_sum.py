class Solution:
    def bruteForce(self, nums: List[int], target: int) -> List[int]:
        dict_ = {}
        for idx, val in enumerate(nums):
            if val in dict_:
                return [idx, nums.index(dict_[val]  )   ]
            else:
                dict_[target-val] = val 
        return [ -1, -1 ]
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_ = {}
        for i in range(len(nums)):
            dict_[nums[i]] = i
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in dict_ and dict_[compliment] != i:
                return [i, dict_[compliment]]
        return [-1,-1]
