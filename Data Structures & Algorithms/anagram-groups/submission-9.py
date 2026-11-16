class Solution:
    def StortedStr(self, st):
        s1 = list(st)
        s1.sort()
        return"".join(s1)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dict1 = {}

        for str1 in strs:
            key = self.StortedStr(str1)

            if key in dict1:
                dict1[key].append(str1)
            else:
                dict1[key] = [str1]
        return list(dict1.values())

        