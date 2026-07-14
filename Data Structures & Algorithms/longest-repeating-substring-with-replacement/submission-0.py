class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = ans = 0
        count = Counter()
        maxFreq = 0

        for r in range(len(s)):
            count[s[r]] += 1
            maxFreq = max(maxFreq, count[s[r]])

            while (r-l+1) - maxFreq > k:
                count[s[l]] -= 1
                l += 1

            ans = max(ans, r - l + 1)

        return ans
        