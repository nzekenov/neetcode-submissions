class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.items = [None] * capacity


    def get(self, i: int) -> int:
        return self.items[i]


    def set(self, i: int, n: int) -> None:
        self.items[i] = n


    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self._resize(self.capacity * 2)
        self.items[self.size] = n
        self.size += 1


    def popback(self) -> int:
        retval = self.items[self.size - 1]
        self.size -= 1
        if self.size > 0 and self.capacity <= self.capacity // 4:
            self._resize(max(self.capacity // 2, 1))
        return retval
        
    def _resize(self, new_capacity):
        new_items = [None] * new_capacity
        for i in range(self.size):
            new_items[i] = self.items[i]
        self.items = new_items
        self.capacity = new_capacity

    def resize(self) -> None:
        self._resize(self.capacity * 2)

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity