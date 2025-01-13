from typing import List

#solution 1 (best)
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        
        for i, num in enumerate(nums):
            if left_sum == (total_sum - left_sum - num):  # Check if left sum equals right sum
                return i
            left_sum += num  # Update left sum
        
        return -1
    
#accepted solution 2
class Solution2:
    def pivotIndex(self, nums: List[int]) -> int:
        sumArray = []
        currentSum = 0
        n = len(nums)-1
        if(n==0):
            return 0
        index = -1
        for i in nums:
            currentSum +=i
            sumArray.append(currentSum)

        for i in range(0, n):
            sumNo = sumArray[n]-sumArray[i]
            if sumNo == 0 and i==0:
                index = 0
                break
            elif sumNo == sumArray[i+1]:
                index = i+1
                break

        print(sumArray)
        return index