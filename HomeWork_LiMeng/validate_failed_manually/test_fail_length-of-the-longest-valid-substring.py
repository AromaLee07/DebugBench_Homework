from typing import List

class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        trie = {}
        for f in forbidden:
            t = trie
            for c in f:
                if c not in t:
                    t[c] = {}
                t = t[c]
            t["end"] = True
        
        def isForbidden(s):
            t = trie
            counter = 0
            for c in s:
                if c not in t:
                    return False
                t = t[c]
                counter += 1
                if "end" in t:
                    return counter
            return False
        
        res = 0
        j = len(word)
        for i in range(len(word)):
            truc = isForbidden(word[i:j])
            if truc:
                j = i + truc
            res = max(res, j - i)
        return res


if __name__ == "__main__":
    # 创建 Solution 类的实例
    solution = Solution()

    # "examples": [
    #         "Input: word = \"cbaaaabc\", forbidden = [\"aaa\",\"cb\"]\nOutput: 4\nExplanation: There are 11 valid substrings in word: \"c\", \"b\", \"a\", \"ba\", \"aa\", \"bc\", \"baa\", \"aab\", \"ab\", \"abc\"and \"aabc\". The length of the longest valid substring is 4. \nIt can be shown that all other substrings contain either \"aaa\" or \"cb\" as a substring.",
    #         "Input: word = \"leetcode\", forbidden = [\"de\",\"le\",\"e\"]\nOutput: 4\nExplanation: There are 11 valid substrings in word: \"l\", \"t\", \"c\", \"o\", \"d\", \"tc\", \"co\", \"od\", \"tco\", \"cod\", and \"tcod\". The length of the longest valid substring is 4.\nIt can be shown that all other substrings contain either \"de\", \"le\", or \"e\" as a substring."
    #     ],

    word = "cbaaaabc"
    forbidden = ["aaa","cb"]

   # 调用 countMaxOrSubsets 方法
    result = solution.longestValidSubstring(word,forbidden)

    print(result)


