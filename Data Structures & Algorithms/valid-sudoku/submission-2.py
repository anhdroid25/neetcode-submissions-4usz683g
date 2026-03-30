class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #checking for rows
        
        for row in board:
            seen = set()
            for v in row:
                if v == ".":
                    continue
                if v in seen:
                    return False
                seen.add(v)
        

        for c in range(9):
            seen=set()
            for r in range(9):
                v = board[r][c]
                if v == ".":
                    continue
                if v in seen:
                    return False
                seen.add(v)
        

        for r0 in (0, 3, 6):
            for c0 in (0, 3, 6):
                seen = set()
                for r in range(r0, r0+3):
                    for c in range (c0, c0+3):
                        v = board[r][c]
                        if v == ".":
                            continue
                        if v in seen:
                            return False
                        seen.add(v)
        return True
                
                    
                    
