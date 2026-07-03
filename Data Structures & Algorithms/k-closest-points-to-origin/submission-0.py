class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [(x**2 + y**2, x, y) for x, y in points]
        distances.sort(key=lambda t : t[0])
        return [[x, y] for _, x, y in distances[:k]]



     