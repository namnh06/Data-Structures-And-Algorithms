# https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
# Best Conceivable Runtime: O(n)
# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import Optional, List

class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode' = None) -> None:
        self.val = val
        self.next = next
        
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        current: ListNode = head
        nextNode: ListNode = current.next
        
        while nextNode is not None:
            if current.val == nextNode.val:
                current.next = nextNode.next
            else:
                current = current.next
            nextNode = nextNode.next
            
        return head
    
if __name__ == "__main__":
    def list_to_linked_list(elements: Optional[List[int]]) -> Optional[ListNode]:
        if len(elements) == 0:
            return
        
        linked_list: ListNode = ListNode(elements[0])
        current = linked_list
        for i in range(1, len(elements)):
            node: ListNode = ListNode(elements[i])
            current.next = node
            current = current.next
            
        return linked_list
    
    def linked_list_to_list(head: Optional[ListNode]) -> Optional[List[int]]:
        if head is None:
            return []
        
        nums: List[int] = []
        current: ListNode = head
        while current is not None:
            nums.append(current.val)
            current = current.next
        
        return nums
    
    s = Solution()
    
    # Test case 1: List with duplicates
    head = list_to_linked_list([1, 1, 2])
    new_head = s.deleteDuplicates(head)
    assert linked_list_to_list(new_head) == [1, 2]

    # Test case 2: List with consecutive duplicates
    head = list_to_linked_list([1, 1, 2, 3, 3])
    new_head = s.deleteDuplicates(head)
    assert linked_list_to_list(new_head) == [1, 2, 3]

    # Test case 3: List with no duplicates
    head = list_to_linked_list([1, 2, 3])
    new_head = s.deleteDuplicates(head)
    assert linked_list_to_list(new_head) == [1, 2, 3]

    # Test case 4: Empty list
    head = list_to_linked_list([])
    new_head = s.deleteDuplicates(head)
    assert linked_list_to_list(new_head) == []

    # Test case 5: Single element list
    head = list_to_linked_list([1])
    new_head = s.deleteDuplicates(head)
    assert linked_list_to_list(new_head) == [1]

    print("All test cases pass")
        