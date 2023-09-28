def lengthOfLongestSubstring(s: str) -> int:
    curr = ""
    m = 0

    for i in s:

        if i not in curr:
            curr += i
        else:
            m = max(m, len(curr))
            index = curr.index(i)
            curr = curr[index:] + i

    return m


print(lengthOfLongestSubstring("aabaab!bb"))
