def maxSumRangeQuery(nums: list[int], requests: list[list[int]]) -> int:
    dct = {}

    for lst in requests:
        for i in range(lst[0], lst[1] + 1):
            if i not in dct:
                dct[i] = 1
            else:
                dct[i] += 1

    lst = list(dct.items())
    lst.sort(key=lambda x: x[1], reverse=True)
    nums.sort(reverse=True)
    res = 0

    for i in range(len(lst)):
        res += nums[i] * lst[i][1]

    print(res)



maxSumRangeQuery([1,2,3,4,5], [[1,3],[0,1]])