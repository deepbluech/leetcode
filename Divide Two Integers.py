__author__ = 'samsung'

def divide(dividend, divisor):
        flag = 1
        if dividend > 0 and divisor < 0 or dividend < 0 and divisor > 0:
            flag = -1
        a = abs(dividend)
        b = abs(divisor)
        ans = 0
        while b <= a:
            shift = 0
            while (b << shift) <= a:
                shift += 1
            ans += 1 << (shift - 1)
            a = a - (b << (shift - 1))
        if flag == 1:
            return ans
        else:
            return -ans

print divide(10, 3)