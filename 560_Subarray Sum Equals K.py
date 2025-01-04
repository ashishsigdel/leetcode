from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        currSum = 0  #tracks current sum
        count = 0   # tracks total count 
        prefixMap = {0: 1}  # prefix sum map initially sum=0 and count = 1

        for num in nums: 
            currSum += num

            if currSum - k in prefixMap:
                count += prefixMap[currSum - k]

            prefixMap[currSum] = prefixMap.get(currSum, 0) +1   # here get is like prefixMap[currSum] but may bring error so use get so that if error happens due to absent of currSum in prefixMap it returns 0
        return count