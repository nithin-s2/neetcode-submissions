class Solution:
    def findMin(self, nums: List[int]) -> int:
        # [3,4,1,2]
        l = 0
        r = len(nums) - 1

        # res = nums[0]

        while l < r:
            m = (l + r) // 2
            # print(nums[l], nums[m], nums[r])
            if nums[m] < nums[r]:
                r = m
            else:
                l = m+1
        return nums[l]


        