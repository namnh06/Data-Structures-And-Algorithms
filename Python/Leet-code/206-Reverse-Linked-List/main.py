from typing import List, Optional

class ListNode:
    def __init__(self, val: int = 0, next_node: Optional["ListNode"] = None):
        self.val = val
        self.next = next_node
        
def list_to_array(head: Optional[ListNode] = None) -> List[int]:
    if head is None:
        return []
    
    array: List[int] = []
    while head is not None:
        array.append(head.val)
        head = head.next
    return array

def array_to_list(nums: List[int] = []) -> Optional[ListNode]:
    if not nums:
        return None
    
    head: ListNode = ListNode(nums[0])
    current = head
    for num in nums[1:]:
        current.next = ListNode(num)
        current = current.next
    return head

def test_reverse_linked_list():
    # Test case 1
    head = array_to_list([1, 2, 3, 4, 5])
    reversed_head = reverse_linked_list(head)
    assert list_to_array(reversed_head) == [5, 4, 3, 2, 1], "Test case 1 failed: Input [1,2,3,4,5] should reverse to [5,4,3,2,1]"
    
    # Test case 2
    head = array_to_list([1, 2])
    reversed_head = reverse_linked_list(head)
    assert list_to_array(reversed_head) == [2, 1], "Test case 2 failed: Input [1,2] should reverse to [2,1]"
    
    # Test case 3
    head = array_to_list([])
    reversed_head = reverse_linked_list(head)
    assert list_to_array(reversed_head) == [], "Test case 3 failed: Input [] should reverse to []"
    
    # Test case 4: Single element list
    head = array_to_list([1])
    reversed_head = reverse_linked_list(head)
    assert list_to_array(reversed_head) == [1], "Test case 4 failed: Input [1] should reverse to [1]"
    
    # Test case 5: Longer list
    head = array_to_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    reversed_head = reverse_linked_list(head)
    assert list_to_array(reversed_head) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], "Test case 5 failed: Input [1,2,3,4,5,6,7,8,9,10] should reverse to [10,9,8,7,6,5,4,3,2,1]"

    print("All test cases passed!")
    
def reverse_linked_list(head: Optional[ListNode]) -> Optional[ListNode]:
    # interatively
    # current: ListNode = head
    # prev: Optional[ListNode] = None
    # while current is not None:
    #     next_node = current.next
    #     current.next = prev
    #     prev = current
    #     current = next_node
    # return prev
    
    # Recursive
    if head == None or head.next == None:
            return head

    reversed_head = reverse_linked_list(head.next)
    head.next.next = head
    head.next = None
    return reversed_head

test_reverse_linked_list()