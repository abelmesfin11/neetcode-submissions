class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
            
        q = deque([('0000', 0)])
        visit = set(deadends)


        def children(lock):
            res = []
            for i in range(4):
                dig = str((int(lock[i]) + 1) % 10)
                res.append(lock[:i] + dig + lock[i+1:])
                dig = str((int(lock[i]) - 1) % 10)
                res.append(lock[:i] + dig + lock[i+1:])
            return res



        while q:
            for _ in range(len(q)):
                lock, turns = q.popleft()
                if lock == target:
                    return turns
                for child in children(lock):
                    if child not in visit:
                        visit.add(child)
                        q.append((child, turns + 1))
        return -1




        