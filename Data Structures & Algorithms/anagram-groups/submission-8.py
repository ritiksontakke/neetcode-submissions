class Solution:
    def SortedString(self, stri):
        s1 = list(stri)
        s1.sort()
        return"".join(s1)


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dict1 = {}

        for st in strs:

            key = self.SortedString(st)

            if key in dict1:
                dict1[key].append(st)
            else:
                dict1[key] = [st]
        return list(dict1.values())
                
        