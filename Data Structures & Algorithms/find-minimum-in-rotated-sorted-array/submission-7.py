class Solution:
        def findMin(self, nums: List[int]) -> int:
                left, right = 0, len(nums) - 1
                result = nums[left]

                while left <= right:
                        middle = (left + right) // 2
                        result = min(result, nums[middle])

                        if nums[middle] >= nums[right]:
                                left = middle + 1
                        else:
                                right = middle - 1
                return result
        
                                                                                                            