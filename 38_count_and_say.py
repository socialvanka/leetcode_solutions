class Solution:
    def countAndSay(self, n: int) -> str:
        result = "1"
        for _ in range(n - 1):
            current = ""
            i = 0
            while i < len(result):
                char = result[i]
                count = 1
                while i + count < len(result) and result[i + count] == char:
                    count += 1
                current += str(count) + char
                i += count
            result = current
        return result
