class MyHashSet:

    def __init__(self):
        self.hashMap = {}
        

    def add(self, key: int) -> None:
        self.hashMap[key] = 0
        

    def remove(self, key: int) -> None:
        if key in self.hashMap: del self.hashMap[key]
        return 
        

    def contains(self, key: int) -> bool:
        return key in self.hashMap
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)