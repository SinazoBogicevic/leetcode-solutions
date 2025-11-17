from collections import Counter


def findAnagrams(s: str, p: str) -> list[int]:
    result: list[int] = []
    counter = Counter(p)

    k = len(p)

    for i in range(len(s)):
        if k > len(s):
            break
        curr_counter = Counter(s[i:k])

        if curr_counter == counter:
            result.append(i)
        k += 1

    return result


if __name__ == "__main__":
    s_ = "abab"
    p_ = "ab"
    result = findAnagrams(s_, p_)
    print(f"Result: {result}")
