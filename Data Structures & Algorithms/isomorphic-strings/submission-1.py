class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_t = Counter()
        t_s = Counter()

        for i in range(len(s)):
            if s[i] in s_t and s_t[s[i]] != t[i]:
                return False

            if t[i] in t_s and t_s[t[i]] != s[i]:
                return False

            s_t[s[i]] = t[i]
            t_s[t[i]] = s[i]

        return True




        