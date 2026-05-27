class DynamicArray:
    
    def __init__(self, capacity: int):
        self.arr = [None] * capacity


    def get(self, i: int) -> int:
        return self.arr[i]


    def set(self, i: int, n: int) -> None:
        self.arr[i] = n


    def pushback(self, n: int) -> None:
        actual_length = self.getSize()
        if actual_length == self.getCapacity():
            self.resize()
        self.arr[actual_length] = n


    def popback(self) -> int:
        actual_length = self.getSize()
        popped_item = self.arr[actual_length - 1]
        self.arr[actual_length - 1] = None
        return popped_item
 

    def resize(self) -> None:
        new_arr = [None] * (self.getCapacity() * 2)
        for i in range(len(self.arr)):
            new_arr[i] = self.arr[i]
        
        self.arr = new_arr


    def getSize(self) -> int:
        actual_length = 0
        for i in range(len(self.arr)):
            if self.arr[i] is not None:
                actual_length = actual_length + 1
            else:
                return actual_length
        return actual_length
        
    
    def getCapacity(self) -> int:
        return len(self.arr)
