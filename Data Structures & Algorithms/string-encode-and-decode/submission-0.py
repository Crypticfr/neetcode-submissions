from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        # Using list + join avoids O(N^2) memory reallocation from repeated `+=` on strings
        res = []
        for s in strs:
            res.append(str(len(s)) + "#" + s)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):          # Changed `str` to `s`
            j = i
            while s[j] != "#":     # Changed `str` to `s`
                j += 1
            length = int(s[i:j])   # Changed `str` to `s`
            res.append(s[j + 1 : j + 1 + length])  # Changed `str` to `s`
            i = j + 1 + length
        return res                 # Added missing return statement