class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)

        if n%2==1:
            return False

        st1 = []

        for ch in list(s):
            if ch == "(" or ch == "[" or ch == "{":
                st1.append(ch)
            
            else:
                if len(st1) == 0:
                    return False
                
                top=st1.pop()

                if ch==")" and top!="(":
                    return False
                
                elif ch=="}" and top !="{":
                    return False
                
                elif ch=="]" and top !="[":
                    return False
        return len(st1) == 0
