class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mem = {}
        for idx, num in enumerate(nums):
            if num in mem:
                return [mem[num],idx]
            n = target - num
            mem[n] = idx
            # print(idx, num, mem)
        return []