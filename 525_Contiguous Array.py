from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0  # count +1 if 1 comes and -1 if 0 comes
        max_length = 0 #result
        index_map = {0: -1} # map {count: index}

        for i, num in enumerate(nums):   # enumerate Qno 1
            count += 1 if num == 1 else -1

            if count in index_map:
                max_length = max(max_length, index_map[count])
            else: 
                index_map[count] = i

        return index_map