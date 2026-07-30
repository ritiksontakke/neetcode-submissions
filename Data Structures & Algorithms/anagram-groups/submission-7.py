class Solution:
    def SortedString(self,si):
        s1 = list(si)
        s1.sort()
        return''.join(s1)
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dict1 ={}

        for s in strs:
            key = self.SortedString(s)

            if key in dict1:
                dict1[key].append(s)
            else:
                dict1[key]=[s]
        return list(dict1.values())
        