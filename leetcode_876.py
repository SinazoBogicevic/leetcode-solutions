from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def middle_node(head: Optional[ListNode]) -> Optional[ListNode]:
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # this returns the node, not the value
    return slow


if __name__ == "__main__":
    head_list = [1, 2, 3, 4, 5]

    head_node = ListNode(head_list[0])
    current = head_node
    for i in range(1, len(head_list)):
        current.next = ListNode(head_list[i])
        current = current.next

    result = middle_node(head_node)
    print(f"Result: {result.val if result else "None"}")
