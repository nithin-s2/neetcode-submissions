class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0

        # if len(s) <= 2:
        #     return len(set(s))
        
        mapper = set()
        max_count = 0
        # ababc

        while l<len(s) and r < len(s):
            if s[r] in mapper:
                max_count = max(len(mapper), max_count)
                mapper.remove(s[l])
                l += 1
            else:
                mapper.add(s[r])
                r += 1

        max_count = max(len(mapper), max_count)
        return max_count
            


        