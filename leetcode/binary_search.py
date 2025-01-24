class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)

        while left <= right:
            mid = (left + right) // 2
            num = nums[mid]
            if num == target:
                return mid
            elif num < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
