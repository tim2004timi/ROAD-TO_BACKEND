import math

class Solution:
    @staticmethod
    def checkPerfectNumber(num: int) -> bool:
        s = 0
        for i in range(1, int(math.sqrt(num))+1):
            if num % i == 0:
                s += i
                if i != num // i:
                    s += num // i
            if s - num > num:
                return False
        s -= num
        if s == num:
            return True
        return False


s = print(Solution.checkPerfectNumber(28))
