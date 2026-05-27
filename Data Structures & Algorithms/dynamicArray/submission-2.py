class DynamicArray:
    
    def __init__(self, capacity: int):
        self.arr = [None] * capacity
        self.size = 0
        self.capacity = capacity


    def get(self, i: int) -> int:
        return self.arr[i]


    def set(self, i: int, n: int) -> None:
        self.arr[i] = n


    def pushback(self, n: int) -> None:
        actual_length = self.getSize()
        if actual_length == self.getCapacity():
            self.resize()
        self.arr[actual_length] = n
        self.size += 1


    def popback(self) -> int:
        actual_length = self.getSize()
        popped_item = self.arr[actual_length - 1]
        self.arr[actual_length - 1] = None
        self.size -= 1
        return popped_item
 

    def resize(self) -> None:
        new_arr = [None] * (self.getCapacity() * 2)
        self.capacity *= 2 
        for i in range(len(self.arr)):
            new_arr[i] = self.arr[i]
        
        self.arr = new_arr


    def getSize(self) -> int:
        return self.size
        
    
    def getCapacity(self) -> int:
        return self.capacity
