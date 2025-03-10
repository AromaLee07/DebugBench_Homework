from typing import List

class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        total = sum(nums)
        s1 = 0
        s2 = total
        arr = []
        for i in range(n):
            arr.append(self.calculateAbsoluteDifference(s1, nums[i], i, s2, n))
            s1 = s1 + nums[i]
            s2 = total - s1  # 修正此处的计算
        return arr

    def calculateAbsoluteDifference(self, s1, num, i, s2, n):
        return s1 + s2 - num * (2 * i + 1) + num * (n - 1)

if __name__ == "__main__":
    # 创建 Solution 类的实例
    solution = Solution()

    # "examples": [
    #         "Input: nums = [2,3,5]\nOutput: [4,3,5]\nExplanation: Assuming the arrays are 0-indexed, then\nresult[0] = |2-2| + |2-3| + |2-5| = 0 + 1 + 3 = 4,\nresult[1] = |3-2| + |3-3| + |3-5| = 1 + 0 + 2 = 3,\nresult[2] = |5-2| + |5-3| + |5-5| = 3 + 2 + 0 = 5.",
    #         "Input: nums = [1,4,6,8,10]\nOutput: [24,15,13,15,21]"
    #     ],

    # nums = [2,3,5]
    nums = [1,4,6,8,10]

   # 调用 countMaxOrSubsets 方法
    result = solution.getSumAbsoluteDifferences(nums)

    print(result)
