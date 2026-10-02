class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = set()
        duplicates = set()

        for ch in s:
            if ch in seen:
                duplicates.add(ch)
            else:
                seen.add(ch)

        for i,ch in enumerate(s):
            if ch not in duplicates:
                return i
        return -1