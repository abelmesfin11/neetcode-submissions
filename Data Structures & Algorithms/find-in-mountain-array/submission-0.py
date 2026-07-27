class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        """
        Use the binary search three times!!!

        [2,4,5,2,1]


        """
        length = mountainArr.length()
        l = 1
        r = length - 2
        while l <= r:
            m = (l + r) // 2
            left =  mountainArr.get(m - 1)
            mid =  mountainArr.get(m)
            right =  mountainArr.get(m + 1)
            if left < mid < right:
                l = m + 1
            elif left > mid > right:
                r = m - 1
            else:
                break
        peak = m
         
   
        # search left portion
        l2, r2 = 0, peak - 1
        while l2 <= r2:
            m = (l2 + r2) // 2
            val = mountainArr.get(m)
            if val > target:
                r2 = m - 1
            elif val < target:
                l2 = m + 1
            else:
                return m

        l3, r3 = length - 1, peak
        while r3 <= l3:
            m = (l3 + r3) // 2
            val = mountainArr.get(m)
            if val > target:
                r3 = m + 1
            elif val < target:
                l3 = m - 1
            else:
                return m

        return -1

        


        








      



        