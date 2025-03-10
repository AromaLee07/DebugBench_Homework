from collections import defaultdict

class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        rec, track = [0], defaultdict(int) 
        ct = start = ptr1 = ptr2 = 0

        if not set(s2).issubset(set(s1)): return 0

        s1 = ''.join(char for char in s1 if char in set(s2))
        
        while True:
            for char in s2:
                ptr = s1.find(char, start)
                if ptr == -1:
                    ct += 1
                    ptr = s1.find(char)
                start = ptr + 1
            rec.append(ct + 1)

            if rec[-1] >= n1: return (len(rec) - 2) // n2

            if start not in track:  # 这里应该是start，原代码使用ptr错误
                track[start] = len(rec) - 1
            else:
                break
        
        cycleStart = rec[track[start]]
        cycle1, cycle2 = rec[-1] - cycleStart, len(rec) - 1 - track[start]
        rest = n1 - cycleStart
        
        rem = cycleStart + (rest % cycle1)  # 这里计算剩余部分的逻辑修改

        ptr2 = 0
        while rec[ptr2] <= rem:
            ptr2 += 1

        return (cycle2 * (rest // cycle1) + (ptr2 - 1)) // n2

    def calculateRemainder(self, a, b):  # 原代码中使用了未定义的方法，这里添加简单计算余数的方法
        return a % b

if __name__ == "__main__":
    # 创建 Solution 类的实例
    solution = Solution()

    # "examples": [
    #         "Input: s1 = \"acb\", n1 = 4, s2 = \"ab\", n2 = 2\nOutput: 2",
    #         "Input: s1 = \"acb\", n1 = 1, s2 = \"acb\", n2 = 1\nOutput: 1"
    #     ],

    # nums = [2,3,5]
    s1="acb"
    n1=1
    s2="acb"
    n2=1

   # 调用 countMaxOrSubsets 方法
    result = solution.getMaxRepetitions(s1,n1,s2,n2)

    print(result)
