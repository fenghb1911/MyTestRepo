import math
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # if num1 == "0" or num2 == "0":
        #     return '0'
        # strSum = ''
        # listLen = len(num1) + len(num2)
        # numList = [0] * listLen
        # for ki,vi in enumerate(num1[::-1]):
        #     for kj,vj in enumerate(num2[::-1]):
        #         idx = listLen-ki-kj-1
        #         numList[idx] += int(vi) * int(vj)
        #         numList[idx-1] += int(numList[idx]/10)
        #         numList[idx] %= 10

        # beginAdd = False
        # for i in numList:
        #     if i == 0 and not beginAdd:
        #         continue
        #     else:
        #         beginAdd = True
        #         strSum += str(i)
        
        # return strSum

    ############################ 2 ############################
        carry1 = 1
        sumNum = 0
        for i in num1[::-1]:
            carry2 = 1
            for j in num2[::-1]:
                sumNum += int(i) * int(j) * carry1 * carry2
                carry2 *= 10
            carry1 *= 10

        return sumNum

    ############################ 1 ############################
    #     len1 = len(num1)
    #     len2 = len(num2)
    #     sumNum = 0
    #     for i in range(0, len2):
    #         curIdxVal = 0
    #         nextIdxVal = '0'
    #         n1 = int(num2[len2-i-1])
    #         mulAfterNum = ""
    #         for _ in range(0, i):
    #             mulAfterNum = mulAfterNum + "0"
            
    #         for j in range(0, len1):
    #             n2 = int(num1[len1-j-1])
    #             mulNum = n1 * n2
    #             addNum = int(nextIdxVal) + mulNum
    #             if mulNum > 9:
    #                 curIdxVal = addNum % 10
    #                 mulAfterNum = str(curIdxVal) + mulAfterNum
    #                 nextIdxVal = str(addNum)[0]
    #             else:
    #                 curIdxVal = addNum % 10
    #                 mulAfterNum = str(curIdxVal) + mulAfterNum
    #                 nextIdxVal = '0' if addNum < 10 else '1'
    #         mulAfterNum = nextIdxVal + mulAfterNum
    #         sumNum += int(mulAfterNum)

    #     return str(sumNum)

if __name__ == "__main__":
    s = Solution()
    num1 = "999999999999999999999999999999999999999"
    num2 = "99"
    # num1 = "2"
    # num2 = "333333"
    # num1 = "123"
    # num2 = "456"
    mulNum = s.multiply(num1, num2)
    print(mulNum)