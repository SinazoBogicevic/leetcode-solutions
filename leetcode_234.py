from threading import _DummyThread
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def isPalindrome(head: Optional[ListNode]) -> bool:
    # Time: O(n)
    # Space: O(n)
    # prev, curr = None, head

    # while curr:
    #     temp = curr.next
    #     curr.next = prev
    #     prev = curr
    #     curr = temp

    # comp = head

    # while prev and comp:
    #     if prev.val != comp.val:
    #         return False
    #     prev = prev.next
    #     comp = comp.next

    # Time: O(n)
    # Space: O(1)

    fast, slow = head, head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    prev = None

    while slow:
        temp = slow.next
        slow.next = prev
        prev = slow
        slow = temp

    left, right = head, prev

    while right:
        if right.val != left.val:
            return False

        left = left.next
        right = right.next

    return True


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
    print(isPalindrome(head))
