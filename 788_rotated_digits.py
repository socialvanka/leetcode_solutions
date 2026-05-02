class Solution:
    def rotatedDigits(self, n: int) -> int:
        count = 0
        for i in range(1, n + 1):
            s = str(i)
            if any(d in s for d in ('3', '4', '7')):
                continue
            if any(d in s for d in ('2', '5', '6', '9')):
                count += 1
        return count
