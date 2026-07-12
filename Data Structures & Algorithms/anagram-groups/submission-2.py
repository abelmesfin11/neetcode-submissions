class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)

        for word in strs:
            keyy = "".join(sorted(word))
            group[keyy].append(word)
        
        return list(group.values())


