    def searchRange(self, nums: List[int], target: int) -> List[int]:
        numsStr = ''.join([str(i) for i in nums])
        if target not in nums:
            return [-1, -1]
        else :
            ct = nums.count(target)
            return [nums.index(target), nums.index(target) + ct - 1]
