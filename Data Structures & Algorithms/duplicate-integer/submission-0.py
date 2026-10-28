class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        newNum = []
        for num in nums:
            if num not in newNum:
                newNum.append(num)
            else:
                return True
        return False