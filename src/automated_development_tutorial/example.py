def sumOfPrimes(max: int) -> int:
    """
    return sum of all prime numbers up to and including :param max:.

    :param max: only look for primes up to this number
    :type max: int
    :return: sum of all prime numbers up to :param max:
    :rtype: int
    """
    total = 0
    is_prime = [True] * (max + 1)
    s = 2
    while s*s <= max:
        if is_prime[s]:
            s_mul = s*2
            while s_mul <= max:
                is_prime[s_mul] = False
                s_mul +=s
        s+=1
    total = 0
    for i in range(2, max+1):
        if is_prime[i]:
            total += i
    return total



def fibonacci(max: int) -> list[int]:
    """
    return fibonacci sequence up to and including :param max:.

    :param max: largest element in sequence should not be bigger than this number
    :type max: int
    :return: Fibonacci sequence up to :param max:
    :rtype: list[int]
    """
    if max < 1:
        return []
    elif max <2:
        return [1]
    else:
        first = 1
        second=1
        results = []
        while second <= max:
            results.append(first)
            next= first+second
            first = second
            second =next
        results.append(first)

        return results
