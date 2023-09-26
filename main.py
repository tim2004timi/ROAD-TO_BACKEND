def findComplement(num: int) -> int:
    num = bin(num)[2:]

    res = 0
    num = num[::-1]
    # return int(num)
    for i in range(len(num)):
        if num[i] == "0":
            res += 2 ** i

    return res


print(findComplement(5))
