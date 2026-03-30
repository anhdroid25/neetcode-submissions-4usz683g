class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sort_array = sorted(nums)
        result = []
        
        for i in range(len(sort_array)):
            if i > 0 and sort_array[i] == sort_array[i-1]:
                continue
            left = i + 1
            right = len(nums) - 1 #pointers start at opposite ends
            while left < right:
                if sort_array[left] + sort_array[right] + sort_array[i] < 0: #left pointer moves right
                    left += 1
                elif sort_array[left] + sort_array[right] + sort_array[i] > 0: #right pointer moves left
                    right -= 1
                elif sort_array[left] + sort_array[right] + sort_array[i] == 0: #accept this case
                    result.append([sort_array[left], sort_array[right], sort_array[i]]) #add to the list of result
                    left += 1
                    while sort_array[left] == sort_array[left -1] and left < right:
                        left += 1
        return result