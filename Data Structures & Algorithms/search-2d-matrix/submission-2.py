class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows=len(matrix)
        cols=len(matrix[0])
        t=rows*cols
        l=0
        r=t-1
        while l<=r:
            mid=(l+r)//2
            i=mid//cols
            j=mid%cols
            elem=matrix[i][j]
            if target==elem:
                return True
            elif target>elem:
                l+=1
            else:
                r-=1
        return False


        