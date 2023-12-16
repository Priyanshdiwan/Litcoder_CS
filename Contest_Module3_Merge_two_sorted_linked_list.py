import sys
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next
def merge_sorted_lists(headA, headB):
    dummy = ListNode()
    current = dummy
    while headA is not None and headB is not None:
        if headA.value < headB.value:
            current.next = headA
            headA = headA.next
        else:
            current.next = headB
            headB = headB.next
        current = current.next
    if headA is not None:
        current.next = headA
    elif headB is not None:
        current.next = headB
    return dummy.next
def create_linked_list(length, elements):
    if length == 0:
        return None
    head = ListNode(elements[0])
    current = head
    for i in range(1, length):
        current.next = ListNode(elements[i])
        current = current.next
    return head
def print_linked_list(head):
    current = head
    while current is not None:
        print(current.value)
        current = current.next
if __name__ == "__main__":
    lengthA = int(input())
    elementsA = [int(input()) for _ in range(lengthA)]
    headA = create_linked_list(lengthA, elementsA)
    lengthB = int(input())
    elementsB = [int(input()) for _ in range(lengthB)]
    headB = create_linked_list(lengthB, elementsB)
    merged_head = merge_sorted_lists(headA, headB)
    print_linked_list(merged_head)
