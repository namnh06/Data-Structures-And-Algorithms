# from typing import Optional

# class Node:
#     def __init__(self, data: int) -> None:
#         self.value = data
#         self.next = None
        
# # Single Linked List
# class LinkedList():
#     def __init__(self, node: Node = None) -> None:
#         self.head = node
    
#     # Append To Head
#     def append_to_head(self, node: Node) -> None:
#         temporary_head: Node = self.head
#         self.head = node
#         self.head.next = temporary_head
        
#     # Append To Tail
#     def append_to_tail(self, node: Node) -> None:
#         if self.head is None:
#             self.head = node
#             return
#         current: Node = self.head
#         while current.next is not None:
#             current = current.next
#         current.next = node
    
#     # Append To ith
#     def append_to_ith(self, node: Node, index: int) -> None:
#         if index < 0 or index >= self.size():
#             raise ValueError(f"Index must be in from 0 to {self.size() - 1}")
#         if index == 0:
#             self.append_to_head(node)
#             return
#         i: int = 0
#         current: Node = self.head
#         while i != index - 1:
#             i += 1
#             current = current.next
#         node.next = current.next
#         current.next = node
    
#     # Peek Top Node
#     def peek_top_node(self) -> Node:
#         return self.head
    
#     # Peek Last Node
#     def peek_last_node(self) -> Node:
#         if self.head is None:
#             return None
#         current: Node = self.head
#         while current.next is not None:
#             current = current.next
#         return current
    
#     # Peek the ith node
#     def peek_ith_node(self, index: int) -> Node:
#         if index < 0 or index >= self.size():
#             raise ValueError(f"Index must be in from 0 to {self.size() - 1}")
#         i: int = 0
#         current: Node = self.head
#         while i != index:
#             i += 1
#             current = current.next
#         return current
    
#     # Remove Top Node
#     def remove_top_node(self) -> None:
#         if self.head is not None:
#             self.head = self.head.next
    
#     # Remove Last Node
#     def remove_last_node(self) -> None:
#         if self.head is None:
#             return
#         if self.head.next is None:
#             self.head = None
#             return
#         current: Node = self.head
#         while current.next.next is not None:
#             current = current.next
#         current.next = None
        
#     # Remove ith Node
#     def remove_ith_node(self, index: int) -> None:
#         if index < 0 or index >= self.size():
#             raise ValueError(f"Index must be in from 0 to {self.size() - 1}")
#         if index == 0:
#             self.remove_top_node()
#             return
#         current: Node = self.head
#         i: int = 0
#         while i != index - 1:
#             current = current.next
#         current.next = current.next.next
    
#     # Linked List Size
#     def size(self) -> int:
#         current: Node = self.head
#         count: int = 0
#         while current is not None:
#             count += 1
#             current = current.next
#         return count
        
#     # Printing Linked List
#     def print_list(self) -> None:
#         current: Node = self.head
        
#         while current is not None:
#             print(current.value)
#             current = current.next

# if __name__ == "__main__":
#     # Test Node Class
#     node: Node = Node(5)
#     assert node.value == 5
#     assert node.next == None
    
#     # Test LinkedList Class
#     single_linked_list: LinkedList = LinkedList(node)
#     assert single_linked_list.head == node
#     assert single_linked_list.head.value == 5
#     assert single_linked_list.head.next == None
    
#     # Test Add New Node To Head
#     new_node: Node = Node(12)
#     assert new_node.value == 12
#     assert new_node.next == None
    
#     single_linked_list.append_to_head(new_node)
#     assert single_linked_list.head.value == 12
#     assert single_linked_list.peek_top_node().value == 12
    
#     # Test Add New Node To Tail
#     new_node: Node = Node(22)
#     assert new_node.value == 22
#     assert new_node.next == None
    
#     single_linked_list.append_to_tail(new_node)
#     assert single_linked_list.peek_last_node().value == 22
    
#     # Test Count Size
#     assert single_linked_list.size() == 3
    
#     # Test Peek At Index 2
#     assert single_linked_list.peek_ith_node(2).value == 22
    
#     # Remove Top Node
#     single_linked_list.remove_top_node()
#     assert single_linked_list.head.value == 5
    
#     # Add To ith
#     new_node: Node = Node(41)
#     # Out of Range index
#     single_linked_list.append_to_ith(new_node, 1)
#     assert single_linked_list.peek_ith_node(1).value == 41
    
#     # Remove Last Node
#     single_linked_list.remove_last_node()
#     assert single_linked_list.peek_last_node().value == 41
    
#     # Test Add New Node To Head
#     new_node: Node = Node(36)
#     assert new_node.value == 36
#     assert new_node.next == None
    
#     single_linked_list.append_to_head(new_node)
#     assert single_linked_list.head.value == 36
#     assert single_linked_list.peek_top_node().value == 36
    
#     # Test Add New Node To Head
#     new_node: Node = Node(45)
#     assert new_node.value == 45
#     assert new_node.next == None
    
#     single_linked_list.append_to_head(new_node)
#     assert single_linked_list.head.value == 45
#     assert single_linked_list.peek_top_node().value == 45
    
#     # Test Remove Node index 1st
#     single_linked_list.remove_ith_node(1)
#     assert single_linked_list.peek_ith_node(1).value == 5
    
#     # Test Print Linked List
#     single_linked_list.print_list()

from typing import List, Optional
class ListNode:
    def __init__(self, val: int = 0, next_node: Optional["ListNode"] = None):
        self.val = val
        self.next = next_node

class LinkedList:
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head
        
    def get(self, index: int) -> int:
        i = 0
        current = self.head.next
        while current != None:
            if i == index:
                return current.val
            i += 1
            current = current.next
        return -1
    
    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node
        if self.tail == self.head:
            self.tail = new_node
        return None
    
    def insertTail(self, val: int) -> None:
        new_tail = ListNode(val)
        self.tail.next = new_tail
        self.tail = new_tail
        return None
    
    def remove(self, index: int) -> bool:
        i = 0
        current = self.head
        while i < index and current.next != None:
            i += 1
            current = current.next
        
        if current.next == None:
            return False
        
        if current.next == self.tail:
            self.tail = current
            
        current.next = current.next.next
        return True
    
    def getValues(self) -> List[int]:
        values: List[int] = []
        current = self.head.next
        while current is not None:
            values.append(current.val)
            current = current.next
        return values
    
linked_list = LinkedList()
linked_list.insertHead(10)
linked_list.insertTail(20)
linked_list.insertTail(30)
assert linked_list.getValues() == [10, 20, 30], "Error: getValues should be [10, 20, 30]"
assert linked_list.get(1) == 20, "Error: get(1) should be 20"
assert linked_list.remove(1) == True, "Error: remove(1) should be successful"
assert linked_list.getValues() == [10, 30], "Error: getValues should be [10, 30]"
assert linked_list.remove(5) == False, "Error: remove(5) should fail"
assert linked_list.get(5) == -1, "Error: get(5) should return -1"
print("All test cases passed.")