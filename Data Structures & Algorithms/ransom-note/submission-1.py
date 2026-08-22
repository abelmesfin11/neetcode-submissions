class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom = Counter(ransomNote)
        mag = Counter(magazine)

        for let in ransomNote:
            if ransom[let] > mag[let]:
                return False

        return True
        