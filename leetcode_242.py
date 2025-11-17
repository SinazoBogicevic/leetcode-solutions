from collections import Counter


def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    hash_map_t: dict[str, int] = {}
    hash_map_s: dict[str, int] = {}

    for i, letter in enumerate(s):
        if s[i] not in hash_map_s:
            hash_map_s[letter] = 1
        else:
            hash_map_s[letter] += 1

        if t[i] not in hash_map_t:
            hash_map_t[t[i]] = 1
        else:
            hash_map_t[t[i]] += 1

    return hash_map_s == hash_map_t


if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    result = isAnagram(s, t)
    print(f"Result: {result}")
