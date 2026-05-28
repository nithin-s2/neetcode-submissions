from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        n=len(nums)
        for i in range(n):
            freq[nums[i]] += 1
        # print(freq)
        # in_freq = defaultdict(list)
        # for k,v in freq.items():
        #     in_freq[v].append(k)
        # in_freq = sorted(in_freq.items(), key=lambda x: x[0])
        in_freq = sorted(freq.items(), reverse=True, key=lambda x: x[-1])
        # print(in_freq)
        output = []
        out_len = k
        for _k,_v in in_freq:

            if out_len < 1:
                break
            output.append(_k)
            out_len -= 1
        return output