from typing import List
import collections
import itertools
import functools


def countMaxOrSubsets(nums: List[int]) -> int:
    mapping = collections.defaultdict(int)
    for count in range(1, len(nums) + 1):
        subsets = list(itertools.combinations(nums, count))
        for ele in subsets:
            mapping[functools.reduce(lambda a, b: a | b, list(ele), 0)] += 1
    return mapping[max(mapping.keys())]


if __name__ == "__main__":
    # 创建 Solution 类的实例
    # solution = Solution()

    # nums = [3,1], Output: 2
    # nums = [2,2,2], Output: 7
    # nums = [3,2,1,5], Output: 6

    # nums = [3,1] 
    # nums = [2,2,2]
    nums = [3,2,1,5]
   

    # 调用 countMaxOrSubsets 方法
    # count = solution.countMaxOrSubsets(nums)

    # 打印结果
   
    # 调用 palindromePairs 方法

    

    # 打印结果
    print("Palindrome Pairs Indices:", countMaxOrSubsets(nums))