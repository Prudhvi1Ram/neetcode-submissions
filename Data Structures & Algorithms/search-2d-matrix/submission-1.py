class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l=[i for row in matrix for i in row]
        le=0
        re=len(l)-1
        while le<=re:
            mid=(re+le)//2
            if l[mid] == target:
                return True
            elif target>l[mid]:
                le+=1
            else:
                re-=1
        return False

        