class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        maxLocation = max(trip[2] for trip in trips)

        arr = [0] * (maxLocation + 1)

        for passenger, fromLoc, toLoc in trips:
            arr[fromLoc] += passenger
            arr[toLoc] -= passenger

        return all(passenger <= capacity for passenger in accumulate(arr))


           
        