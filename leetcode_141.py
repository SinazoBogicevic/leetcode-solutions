from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def has_cycle(head: Optional[ListNode]) -> bool:
    if head is None:
        return False

    slow, fast = head, head

    # fast always takes 2 steps, slow takes 1 step
    # the condition, only checks if fast and fast.next are not None, it doesn't move the pointer
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


if __name__ == "__main__":
    head_list = [1, 1, 1, 1]

    head_ = ListNode(head_list[0])
    current = head_
    for i in range(1, len(head_list)):
        current.next = ListNode(head_list[i])
        current = current.next

    result = has_cycle(head_)
    print(f"Result: {result}")
