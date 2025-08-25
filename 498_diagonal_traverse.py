class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        result = []
        diagonal = {}
        m=len(mat)
        n = len(mat[0])
        for i in range(m):
            for j in range(n):
                d = i + j
                
                if d in diagonal.keys():
                    diagonal[d].append(mat[i][j])
                else:
                    diagonal[d] = [mat[i][j]]
        
        for k in diagonal.keys():
            if k % 2 == 0:
                result.extend(reversed(diagonal[k]))
            else:
                result.extend(diagonal[k])


        return result

        