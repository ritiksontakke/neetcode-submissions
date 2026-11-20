class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for str1 in strs:
            key = "".join(sorted(str1))
            if key not in groups:
                groups[key] = []
            groups[key].append(str1)
        return list(groups.values())