
class Solution:
    def addBinary(self, A, B):
        res = []
        carry = 0
        while A or B or carry:
            carry += (A or [0]).pop(0) + (B or [0]).pop(0)
            res.append(carry & 1)
            carry = carry >> 1
        return res

    def addNegabinary(self, A, B):
        res = []
        carry = 0
        while A or B or carry:
            carry += (A or [0]).pop(0) + (B or [0]).pop(0)
            res.append(carry & 1)
            carry = (carry - res[-1]) // -2
        while len(res) > 1 and res[-1] == 0:
            res.pop()
        return res[::-1]

if __name__ == "__main__":
    # 创建 Solution 类的实例
    solution = Solution()

    # "examples": [
    #         "Input: arr1 = [1,1,1,1,1], arr2 = [1,0,1]\nOutput: [1,0,0,0,0]\nExplanation: arr1 represents 11, arr2 represents 5, the output represents 16.",
    #         "Input: arr1 = [0], arr2 = [0]\nOutput: [0]",
    #         "Input: arr1 = [0], arr2 = [1]\nOutput: [1]"
    #     ],

    arr1 = [1,1,1,1,1]
    arr2 = [1,0,1]

   # 调用 countMaxOrSubsets 方法
    result = solution.addBinary(arr1,arr2)
    result2 = solution.addNegabinary(arr1,arr2)

    print(result)
    print(result2)
