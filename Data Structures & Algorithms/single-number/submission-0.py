class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor_sum=0
        for i in nums:
            xor_sum^=i
        
        return xor_sum