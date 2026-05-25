class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapper = defaultdict(list)
        output = []
        for st in strs:
            # print(st)
            st_sorted = "".join(sorted(st))
            # print(st_sorted)
            mapper[st_sorted].append(st)
        
        for k,v in mapper.items():
            output.append(v)
        return output