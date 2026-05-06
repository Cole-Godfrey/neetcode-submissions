class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for string in strs:
            s_str = ''.join(sorted(string))
            res[s_str].append(string)
        return list(res.values())

