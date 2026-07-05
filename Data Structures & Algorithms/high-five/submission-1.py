class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        d = defaultdict(list)
        for idScore, score in items:
            d[idScore].append(score)
        total =  len(d.keys())

        ans = []
        for i in list(d.keys()):
            average = sum(heapq.nlargest(5, d[i])) // 5
            ans.append((i, average))
        return sorted(ans)

        




       
            