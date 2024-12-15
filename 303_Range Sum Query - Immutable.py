class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixSumArray = []
        currentSum = 0
        for i in nums:
            currentSum += i
            self.prefixSumArray.append(currentSum)

    def sumRange(self, left: int, right: int) -> int:
        rightSum = self.prefixSumArray[right]
        leftSum = self.prefixSumArray[left-1] if left > 0 else 0
        return rightSum - leftSum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)


# Tips:
# def __init__(self, nums: List[int]):
# means
# __init__ is the constructor.
# It takes self (the object itself) and nums (a list of integers).
# self.prefix is an instance variable.
# Every object of NumArray will have its own prefix list.
# It is initialized as an empty list.
# nums = [1, 2, 3, 4]
# prefixSumArray = [1, 3, 6, 10]