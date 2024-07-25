from typing import List, Optional

class ListNode:
    def __init__(self, val: int = 0, next_node: Optional["ListNode"] = None):
        self.val = val
        self.next = next_node
        
class Helper:
    def list_to_array(self, head: Optional[ListNode]) -> List[int]:
        result: List[int] = []

        while head != None:
            result.append(head.val)
            head = head.next
        
        return result
    
    def array_to_list(self, nums: List[int]) -> Optional[ListNode]:
        if len(nums) == 0:
            return None
        
        linked_list: ListNode = ListNode(nums[0])
        current = linked_list
        for num in nums[1:]:
            current.next = ListNode(num)
            current = current.next
            
        return linked_list
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = self.head
        
    def addAtHead(self, val: int) -> None:
        new_head = ListNode(val)
        new_head.next = self.head
        self.head = new_head
        if self.tail == None:
            self.tail = self.head
        return None
    
    def addAtTail(self, val: int) -> None:
        new_tail = ListNode(val)
        if self.tail == None:
            self.head = new_tail
            self.tail = new_tail
        else:
            self.tail.next = new_tail
            self.tail = new_tail
        return None
    
    def addAtIndex(self, index: int, val: int) -> None:
        new_node = ListNode(val)
        if index == 0:
            self.addAtHead(val)
            return None
        
        i: int = 0
        current: ListNode = self.head
        while i < index-1 and current != None:
            i += 1
            current = current.next
        
        if current == None:
            return None
        
        temp_current = current.next
        if self.tail == current or self.tail == None:
            self.tail = new_node
        current.next = new_node
        current.next.next = temp_current
        return None
    
    def get(self, index: int) -> int:
        i: int = 0
        current: ListNode = self.head
        while current != None:
            if i == index:
                return current.val
            i += 1
            current = current.next
        return -1
    
    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            self.head = self.head.next
            return None
        
        i: int = 0
        current = self.head
        while i < index-1 and current != None:
            i += 1
            current = current.next
        
        if current == None:
            return None
        
        if current != None and current.next != None:
            if self.tail == current.next:
                self.tail = current
            current.next = current.next.next
            
        return None
        
        
        
# Test cases
helper = Helper()
linked_list = LinkedList()
linked_list.addAtHead(1)
assert helper.list_to_array(linked_list.head) == [1], "Test case 1 failed."
linked_list.addAtHead(5)
assert helper.list_to_array(linked_list.head) == [5, 1], "Test case 2 failed."
linked_list.addAtTail(3)
assert helper.list_to_array(linked_list.head) == [5, 1, 3], "Test case 3 failed."
linked_list.addAtTail(7)
assert helper.list_to_array(linked_list.head) == [5, 1, 3, 7], "Test case 4 failed."
linked_list.addAtIndex(1, 9)
assert helper.list_to_array(linked_list.head) == [5, 9, 1, 3, 7], "Test case 5 failed."
assert linked_list.get(1) == 9, "Test case 6 failed"
assert linked_list.get(3) == 3, "Test case 7 failed"
assert linked_list.get(6) == -1, "Test case 8 failed"
assert linked_list.get(-1) == -1, "Test case 9 failed"
linked_list.addAtTail(11)
assert helper.list_to_array(linked_list.head) == [5, 9, 1, 3, 7, 11], "Test case 10 failed."
linked_list.addAtIndex(5, 15)
assert helper.list_to_array(linked_list.head) == [5, 9, 1, 3, 7, 15, 11], "Test case 11 failed."
linked_list.addAtIndex(7, 2)
assert helper.list_to_array(linked_list.head) == [5, 9, 1, 3, 7, 15, 11, 2], "Test case 12 failed."
linked_list.deleteAtIndex(2)
assert helper.list_to_array(linked_list.head) == [5, 9, 3, 7, 15, 11, 2], "Test case 13 failed."
linked_list.deleteAtIndex(6)
assert helper.list_to_array(linked_list.head) == [5, 9, 3, 7, 15, 11], "Test case 14 failed."
assert linked_list.tail.val == 11, "Test case 15 failed."

linked_list = LinkedList()
linked_list.addAtHead(1)
linked_list.addAtTail(3)
linked_list.addAtIndex(1,2)
linked_list.get(1)
linked_list.deleteAtIndex(0)
linked_list.get(0)
assert helper.list_to_array(linked_list.head) == [2, 3], "Test case 16 failed."

linked_list = LinkedList()
linked_list.addAtIndex(0, 10)
linked_list.addAtIndex(0, 20)
linked_list.addAtIndex(1, 30)
assert linked_list.get(0) == 20, "Test case 17 failed."

print("All test cases passed.")