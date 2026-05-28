from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)
        # box = (row // 3, col // 3) --> tuple from (0,0) to (2,2)
        # this represents each of the 9 boxes

        for r, row in enumerate(board):
            for c, val in enumerate(row):
                if val == ".":
                    continue
                box = (r // 3, c // 3)
                if val in rows[r] or val in cols[c] or val in boxes[box]:
                    return False
                rows[r].add(val)
                cols[c].add(val)
                boxes[box].add(val)

        return True