/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
  prevMap = {};

  for (let i; i < nums.length; i++) {
    let diff = target - nums[i];
    if (diff in prevMap) {
      return [prevMap[diff], i];
    }
    prevMap[nums[i]] = i;
  }
};
