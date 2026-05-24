class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

    def addWord(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        res, visited = set(), set()
        ROWS, COLS = len(board), len(board[0])
        for word in words:
            root.addWord(word)

        def backtrack(r, c, node, word):
            if (
                r < 0 or c < 0 or
                r >= ROWS or c >= COLS
                or (r, c) in visited
                or board[r][c] not in node.children
            ):
                return
            visited.add((r, c))
            word += board[r][c]
            node = node.children[board[r][c]]
            if node.endOfWord:
                res.add(word)
            
            backtrack(r - 1, c, node, word)
            backtrack(r + 1, c, node, word)
            backtrack(r, c - 1, node, word)
            backtrack(r, c + 1, node, word)
            visited.remove((r, c))
        for r in range(ROWS):
            for c in range(COLS):
                backtrack(r, c, root, "")
        return list(res)
            