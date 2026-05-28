from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        n=len(nums)
        freq = [[] for i in range(n+1)]
        # print(freq)
        for i in range(n):
            count[nums[i]] += 1
        
        for _k,_v in count.items():
            freq[_v].append(_k)
        # print(freq)

        output = []
        for i in range(len(freq)-1, 0, -1):
            output.extend(freq[i])
            if len(output) > k:
                return output[:k]

        return output