def isValid(s: str) -> bool:
    stack: list[str] = []
    brackets_map = {"(": ")", "{": "}", "[": "]"}

    for bracket in s:

        if bracket in brackets_map:
            stack.append(bracket)
        else:
            if not stack:
                return False

        if bracket not in brackets_map:
            if brackets_map[stack[-1]] == bracket:
                stack.pop()
            else:
                return False

    return bool(not stack)


if __name__ == "__main__":
    s_ = "(])"
    RESULT = isValid(s_)
    print(f"result: {RESULT}")
