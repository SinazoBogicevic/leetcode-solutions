def lengthOfLongestSubstring(s: str) -> int:
    l, longest_substring = 0, 0

    sett: set[str] = set()

    for r in range(len(s)):
        print(f"current sett: {sett}")
        while s[r] in sett:
            print(f"Removing {s[r]} from {sett}")
            sett.remove(s[l])
            l += 1

        w = (r - l) + 1
        longest_substring = max(longest_substring, w)
        sett.add(s[r])

    return longest_substring


if __name__ == "__main__":
    s = "pwwkew"
    result = lengthOfLongestSubstring(s)
    print(f"Result: {result}")
