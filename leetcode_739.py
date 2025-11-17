def dailyTemperatures(temperatures: list[int]) -> list[int]:
    """ """
    answer = [0] * len(temperatures)
    stack = []

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
