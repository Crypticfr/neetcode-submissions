class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        result = []

        for num in count:
            if count[num] > len(nums) // 3:
                result.append(num)

        return result