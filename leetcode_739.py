def dailyTemperatures(temperatures: list[int]) -> list[int]:
    """
    For each day, return how many days you must wait until a warmer temperature.
    Uses a monotonic stack: we keep indices of days whose "next warmer day" is not yet found.

    What's happening:
    - answer[i] = 0 by default (no warmer day found).
    - stack holds [temperature, index] for days we're still waiting on a warmer day.
    - Walk left-to-right. For each day i with temp:
      - While the stack top has a lower temp than today, that day's "warmer day" is i.
        Pop it, set answer[stack_index] = i - stack_index (days to wait).
      - Then push [temp, i] so we can resolve it when we see a warmer day later.
    - Stack stays in decreasing order of temperature (monotonic), so each element
      is pushed and popped at most once → O(n) time.

    time complexity: O(n)
    space complexity: O(n)
    """
    answer = [0] * len(temperatures)
    stack: list[list[int]] = []

    for i, temp in enumerate(temperatures):
        while stack and stack[-1][0] < temp:
            stack_temp, stack_index = stack.pop()
            answer[stack_index] = i - stack_index

        stack.append([temp, i])

    return answer


if __name__ == "__main__":
    temperatures_ = [73, 74, 75, 71, 69, 72, 76, 73]
    result = dailyTemperatures(temperatures_)
    print(f"Result: {result}")
