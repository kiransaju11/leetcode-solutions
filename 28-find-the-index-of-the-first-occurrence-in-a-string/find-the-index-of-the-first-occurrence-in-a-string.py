class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            n=0
            for i in haystack:
                if i==needle[0]:
                    if haystack[n:n+len(needle)]==needle:
                        return n
                n=n+1
        else:
            return -1