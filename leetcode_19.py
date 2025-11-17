from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummy = ListNode()
    dummy.next = head
    fast = slow = dummy
    counter = 0

    # for _ in range(n + 1):
    #     fast = fast.next

    while fast:
        if counter < n + 1:
            fast = fast.next
        else:
            fast = fast.next
            slow = slow.next

    slow.next = slow.next.next

    return dummy.next


if __name__ in "__main__":

    list_ = [1, 2, 3, 4, 5]
    head_node = ListNode(list_[0])
    curr_node = head_node

    for i in range(1, len(list_)):
        curr_node.next = ListNode(list_[i])
        current = curr_node.next

    result = removeNthFromEnd(head_node, 2)
    print(f"result: {result.val if result else None}")
