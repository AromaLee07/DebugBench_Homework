from typing import List
import random

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        tree = None
        ans = []
        for i, x in enumerate(nums):
            tree = insert(tree, x)
            if size(tree) > k:
                tree = remove(tree, nums[i - k + 1])
            if size(tree) == k:
                if k % 2 == 1:
                    ans.append(get(tree, k // 2 + 1))
                else:
                    ans.append((get(tree, k // 2) + get(tree, k // 2 + 1)) / 2)
        return ans

class Node:
    __slots__ = ['val', 'count', 'weight', 'size', 'left', 'right']
    def __init__(self, val):
        self.val = val
        self.count = 1
        self.weight = random.random()
        self.size = 1
        self.left = self.right = None

def touch(root):
    if not root:
        return
    root.size = root.count + size(root.left) + size(root.right)

def size(root):
    if not root:
        return 0
    return root.size

def insert(root, val):
    t1, r, t2 = split(root, val)
    if not r:
        r = Node(val)
    else:
        r.count += 1
        touch(r)
    t2 = join(r, t2)
    return join(t1, t2)

def remove(root, val):
    t1, r, t2 = split(root, val)
    if r and r.count > 1:
        r.count -= 1
        touch(r)
        t2 = join(r, t2)

if __name__ == "__main__":
    # 创建 Solution 类的实例
    solution = Solution()

    # "examples": [
    #         "Input: nums = [1,3,-1,-3,5,3,6,7], k = 3\nOutput: [1.00000,-1.00000,-1.00000,3.00000,5.00000,6.00000]\nExplanation: \nWindow position                Median\n---------------                -----\n[1  3  -1] -3  5  3  6  7        1\n 1 [3  -1  -3] 5  3  6  7       -1\n 1  3 [-1  -3  5] 3  6  7       -1\n 1  3  -1 [-3  5  3] 6  7        3\n 1  3  -1  -3 [5  3  6] 7        5\n 1  3  -1  -3  5 [3  6  7]       6",
    #         "Input: nums = [1,2,3,4,2,3,1,4,2], k = 3\nOutput: [2.00000,3.00000,3.00000,3.00000,2.00000,3.00000,2.00000]"
    #     ],

    nums = [1,3,-1,-3,5,3,6,7]
    k = 3

   # 调用 countMaxOrSubsets 方法
    result = solution.medianSlidingWindow(nums,k)

    print(result)
