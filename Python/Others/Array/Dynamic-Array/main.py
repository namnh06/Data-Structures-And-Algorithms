# https://neetcode.io/problems/dynamicArray
class DynamicArray:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.array = [None] * capacity
        self.size = 0
        
    def get(self, i: int) -> int:
        if 0 <= i < self.size:
            return self.array[i]
        raise IndexError("Index out of bounds.")
    
    def set(self, i: int, n: int) -> None:
        if 0 <= i < self.size:
            self.array[i] = n
        else:
            raise IndexError("Index out of bounds.")
        return None
    
    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        self.array[self.size] = n
        self.size += 1
        return None
    
    def popback(self) -> int:
        if self.size == 0:
            raise IndexError("Pop from an empty array.")
        value = self.array[self.size - 1]
        self.array[self.size - 1] = None
        self.size -= 1
        return value
    
    def resize(self) -> None:
        new_capacity = self.capacity * 2
        new_array = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity
        return None
    
    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity
    
# Test initialization
dyn_array = DynamicArray(1)
assert dyn_array.getSize() == 0, "Error in getSize after initialization"
assert dyn_array.getCapacity() == 1, "Error in getCapacity after initialization"

# Test pushback and automatic resizing
dyn_array.pushback(1)
assert dyn_array.getSize() == 1, "Error in getSize after first pushback"
assert dyn_array.getCapacity() == 1, "Error in getCapacity after first pushback"

dyn_array.pushback(2)
assert dyn_array.getSize() == 2, "Error in getSize after second pushback"
assert dyn_array.getCapacity() == 2, "Error in getCapacity after second pushback"

dyn_array.pushback(3)
assert dyn_array.getSize() == 3, "Error in getSize after third pushback"
assert dyn_array.getCapacity() == 4, "Error in getCapacity after third pushback"

# Test get and set
assert dyn_array.get(0) == 1, "Error in get at index 0"
assert dyn_array.get(1) == 2, "Error in get at index 1"
assert dyn_array.get(2) == 3, "Error in get at index 2"

dyn_array.set(1, 5)
assert dyn_array.get(1) == 5, "Error in set at index 1"

# Test popback
assert dyn_array.popback() == 3, "Error in popback first call"
assert dyn_array.getSize() == 2, "Error in getSize after popback first call"
assert dyn_array.popback() == 5, "Error in popback second call"
assert dyn_array.getSize() == 1, "Error in getSize after popback second call"
assert dyn_array.popback() == 1, "Error in popback third call"
assert dyn_array.getSize() == 0, "Error in getSize after popback third call"

print("All test cases passed.")