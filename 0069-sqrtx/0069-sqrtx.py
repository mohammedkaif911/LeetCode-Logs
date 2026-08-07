class Solution:
    def mySqrt(self, x: int) -> int:
        if x<2:
            return x
        left = 1
        right = x//2
        while left <= right:
            mid = left + (right - left) // 2
            midsq = mid* mid
            if midsq == x:
                return mid
            elif midsq < x:
                left = mid+1
            elif midsq > x:
                right = mid-1
        return right
        
        