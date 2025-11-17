from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    curr, prev = head, None

    while curr:
        temp = curr.next
        curr.next = prev
        print(f"curr.val: {curr.val}")
        prev = curr
        curr = temp

    return prev


if __name__ == "__main__":
    head_list = [1, 2, 3, 4, 5]

    head_node = ListNode(head_list[0])
    current = head_node
    for i in range(1, len(head_list)):
        current.next = ListNode(head_list[i])
        current = current.next

    result = reverseList(head_node)
    print(f"Result: {result.val if result else 'None'}")
