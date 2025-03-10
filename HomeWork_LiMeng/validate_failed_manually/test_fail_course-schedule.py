from typing import List
from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre = defaultdict(list)
        for course, p in prerequisites:
            pre[course].append(p)
        taken = set()

        def dfs(course):
            if not pre[course]:
                return True
            if course in taken:
                return False
            taken.add(course)
            for p in pre[course]:
                if not dfs(p):
                    return False
            taken.remove(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
if __name__ == "__main__":
    # 创建 Solution 类的实例
    solution = Solution()

    # "examples": [
    #         "Input: numCourses = 2, prerequisites = [[1,0]]\nOutput: true\nExplanation: There are a total of 2 courses to take. \nTo take course 1 you should have finished course 0. So it is possible.",
    #         "Input: numCourses = 2, prerequisites = [[1,0],[0,1]]\nOutput: false\nExplanation: There are a total of 2 courses to take. \nTo take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible."
    #     ],

    numCourses = 2
    prerequisites = [[1,0],[0,1]]
    # prerequisites = [[1,0]]

   # 调用 countMaxOrSubsets 方法
    result = solution.canFinish(numCourses,prerequisites)

    print(result)
