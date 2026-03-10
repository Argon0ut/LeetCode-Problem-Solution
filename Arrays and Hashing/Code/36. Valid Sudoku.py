class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowBoard = {}
        colDict = {}
        blocks = {}

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != '.':

                    if i not in rowBoard:
                        rowBoard[i] = set()
                    if board[i][j] in rowBoard[i]:
                        return False
                    rowBoard[i].add(board[i][j])

                    if j not in colDict:
                        colDict[j] = set()
                    if board[i][j] in colDict[j]:
                        return False
                    colDict[j].add(board[i][j])

                    x = (i // 3) + 1
                    y = (j // 3) + 1

                    if (x, y) not in blocks:
                        blocks[(x, y)] = set()
                    if board[i][j] in blocks[(x, y)]:
                        return False
                    blocks[(x, y)].add(board[i][j])

        return True
