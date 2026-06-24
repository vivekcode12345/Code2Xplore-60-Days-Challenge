fdef Rank(num):
    prime = []
    non_prime = []

    for i in num:
        if i < 2:
            non_prime.append(i)
            continue

        is_prime = True
        for j in range(2, i):
            if (i % j == 0):
                non_prime.append(i)
                is_prime = False
                break
        if is_prime:
            prime.append(i)

    result1 = []
    for i in num:
        if ((i % 2 != 0) and (i in prime)):
            result1.append(i)

    result = []
    for i in num:
        if (i not in result1):
            result.append(i * 2)

    result.sort()
    return result[:3]


nums = [11, 22, 13, 44, 17, 28, 19]
print(Rank(nums))
