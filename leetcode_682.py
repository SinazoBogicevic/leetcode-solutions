from typing import List


def calPoints(operations: List[str]) -> int:
    score = 0
    stack = []

    for val in operations:

        if val == "C":
            score -= stack[-1]
            stack.pop()
        elif val == "D":
            num = stack[-1]
            doubled_digit = num * 2
            stack.append(doubled_digit)
            score += doubled_digit
        elif val == "+":
            last_digit = stack[-1]
            second_last_digit = stack[-2]
            sum_ = last_digit + second_last_digit
            stack.append(sum_)
            score += sum_
        else:
            stack.append(int(val))
            score += int(val)

    # return sum(stack) this works as well, same time complexity

    return score


if __name__ == "__main__":
    operations_list = ["1", "C"]
    result = calPoints(operations_list)
    print(f"Result: {result}")
