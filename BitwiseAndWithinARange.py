'''
The function takes two arguments m and n
Arg1: the lower range
Arg2: the upper range
Returns: the & operation on all the numbers from Arg1 to Arg2
'''
def rangeBitwiseAnd(m: int, n: int) -> int:
        shift_count = 0
        while m != n:
            m >>= 1
            n >>= 1
            shift_count += 1
        return m << shift_count
