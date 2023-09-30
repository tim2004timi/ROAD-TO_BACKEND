def groupThePeople(nums: list[int]) -> list[list[int]]:
    res = []
    dct = {}

    for i in range(len(nums)):
        if not nums[i] in dct:
            dct[nums[i]] = [i]
        else:
            if len(dct[nums[i]]) == nums[i]:
                res.append(dct[nums[i]])
                del dct[nums[i]]
            else:
                dct[nums[i]].append(i)

    for i in dct.values():
        res.append(i)

    return res


print(groupThePeople([3,3,3,3,3,1,3]))