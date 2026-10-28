def backspaceCompare(s: str, t: str) -> bool:

    # Time: O(n+m)
    # Space: O(n+m)

    if len(s) != len(t):
        return False

    def build_stack(s: str) -> list[str]:
        stack = []
        for char in s:
            if char != "#":
                stack.append(char)
            else:
                if stack:
                    stack.pop()

        return stack

    if build_stack(s) != build_stack(t):
        return False

    # Two pointer solution

    return True


if __name__ == "__main__":
    s = "###c"
    t = "ad#c"
    result = backspaceCompare(s, t)
    print(f"Result: {result}")
