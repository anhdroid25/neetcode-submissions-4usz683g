class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []

        for i in range(len(nums)):
            production = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                else:
                    production *= nums[j]
            result.append(production)

        return result

