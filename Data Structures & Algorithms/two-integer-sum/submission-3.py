class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in count:
                return [count.get(diff), i]
            else:
                count[nums[i]] = i