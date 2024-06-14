# https://leetcode.com/problems/merge-two-sorted-lists/description/
# Constraints:
# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.
from typing import Optional, List

class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode' = None) -> None:
        self.val = val
        self.next = next
        
def create_linked_list(elements: List[int]) -> Optional[ListNode]:
    if not elements:
        return None
    head: ListNode = ListNode(elements[0])
    current: ListNode = head
    for element in elements[1:]:
        current.next = ListNode(element)
        current = current.next
    return head

def linked_list_to_list(node: Optional[ListNode]) -> Optional[List[int]]:
    elements: List[int] = []
    while node:
        elements.append(node.val)
        node = node.next
    return elements
    
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
        answer: ListNode = ListNode()
        current = answer
        
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        if list1 is not None:
            current.next = list1
        else:
            current.next = list2
            
        return answer.next

if __name__ == "__main__":
    s = Solution()
    
list1 = create_linked_list([1, 2, 4])
list2 = create_linked_list([1, 3, 4])
listresult = create_linked_list([1, 1, 2, 3, 4, 4])
assert linked_list_to_list(s.mergeTwoLists(list1, list2)) == linked_list_to_list(listresult)

list1 = create_linked_list([])
list2 = create_linked_list([])
listresult = create_linked_list([])
assert linked_list_to_list(s.mergeTwoLists(list1, list2)) == linked_list_to_list(listresult)

list1 = create_linked_list([])
list2 = create_linked_list([0])
listresult = create_linked_list([0])
assert linked_list_to_list(s.mergeTwoLists(list1, list2)) == linked_list_to_list(listresult)

list1 = create_linked_list([2, 5, 7])
list2 = create_linked_list([1, 3, 6])
listresult = create_linked_list([1, 2, 3, 5, 6, 7])
assert linked_list_to_list(s.mergeTwoLists(list1, list2)) == linked_list_to_list(listresult)

list1 = create_linked_list([1, 2, 3])
list2 = create_linked_list([4, 5, 6])
listresult = create_linked_list([1, 2, 3, 4, 5, 6])
assert linked_list_to_list(s.mergeTwoLists(list1, list2)) == linked_list_to_list(listresult)
