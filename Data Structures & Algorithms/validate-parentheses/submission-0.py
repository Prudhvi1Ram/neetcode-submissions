class Solution:
    def isValid(self, s: str) -> bool:
        d={")":"(","]":"[","}":"{"}
        open1=["{","[","("]
        l=[]
        for i in s:
            if i in open1:
                l.append(i)
            else:
                if l and  d[i] == l[-1]:
                    l.pop()
                else:
                    return False
        return len(l) == 0


        