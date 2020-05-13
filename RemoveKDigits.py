class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        res = ''
        
        for i in num:
            while res and k and res[-1] > i:
                res = res[:-1]
                k -= 1
            res += i
        
        res = res[0: -k] if k > 0 else res
        
        return str(int(res)) if res else '0'
