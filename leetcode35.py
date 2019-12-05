    def searchInsert(self, nums: List[int], target: int) -> int:
        index = 0
        if target in nums:
            return nums.index(target)
        if target < min(nums):
            return 0
        for i in range(len(nums)):
            if target > nums[i]:
                index = i
        return index + 1
            
        
