class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # rows=len(matrix)
        # cols=len(matrix[0])
        # t=rows*cols
        # l=0
        # r=t-1
        # while l<=r:
        #     mid=(l+r)//2
        #     i=mid//cols
        #     j=mid%cols
        #     elem=matrix[i][j]
        #     if target==elem:
        #         return True
        #     elif target>elem:
        #         l+=1
        #     else:
        #         r-=1
        # return False

        r=0
        c=len(matrix[0])-1
        while (r<len(matrix) and c>=0):
            if matrix[r][c] == target:
                return True
            elif target>matrix[r][c]:
                r+=1
            else:
                c-=1
        return False


        