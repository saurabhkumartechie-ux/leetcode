class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        # Step 1: Build LPS (Longest Prefix Suffix) array
        def build_lps(pattern):
            m = len(pattern)
            lps = [0] * m
            length = 0  # length of previous longest prefix suffix
            i = 1

            while i < m:
                if pattern[i] == pattern[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length != 0:
                        length = lps[length - 1]
                    else:
                        lps[i] = 0
                        i += 1
            return lps

        n, m = len(haystack), len(needle)
        lps = build_lps(needle)

        i = j = 0  # i -> haystack, j -> needle

        while i < n:
            if haystack[i] == needle[j]:
                i += 1
                j += 1

                if j == m:
                    return i - j  # match found

            else:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1

        return -1