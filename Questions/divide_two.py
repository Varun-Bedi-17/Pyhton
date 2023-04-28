# -------------------------------------------- Leetcode 29 -----------------------------------------------

#  Basic Approach

def divide(dividend, divisor):
        count = 0
        d = 1
        if (dividend >= 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            d = -1
        MAX = 2147483647
        MIN = -2147483648
        if divisor == -1:
            if dividend == MIN:
                return MAX
            else:
                return -1*dividend
        elif divisor == 1:
            if dividend == -1*MIN:
                return MIN+1
            return dividend
        else:
            divid = abs(dividend)
            divis = abs(divisor)
            while divid >= divis:
                divid = divid - divis
                count += 1
            return count*d
        

print(divide(10,3))


#   Using math formula

import math

def divide_math(dividend, divisor):

        d = 1
        if (dividend >= 0 and divisor < 0) or (dividend < 0 and divisor >= 0):
            d = -1
        MAX = 2147483647
        MIN = -2147483648
        if divisor == -1:
            if dividend == MIN:
                return MAX
            else:
                return -1*dividend
        elif divisor == 1:
            if dividend == -1*MIN:
                return MIN+1
            return dividend
        else:
            ans = math.exp(math.log(abs(dividend)) - math.log(abs(divisor)))
            ans += 0.0000000001
            return int(ans) if(d == 1) else -int(ans)
        

# print(divide_math(10,3))
print(divide_math(2147483647, 2))