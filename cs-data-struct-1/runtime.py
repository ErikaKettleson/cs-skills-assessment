def string_compare(s1, s2):
    """Given two strings, figure out if they are exactly the same (without using ==).

    Put runtime here:
    -----------------
    [       O(n)        ]


    """

    if len(s1) != len(s2):
        # 0(1) to compare at any length
        return False

    # s1 = "bleep" len= 5 s2 = "bloop" len =5
    # have to examine each n 
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False

    return True


def has_exotic_animals(animals):
    """Determine whether a list of animals contains exotic animals.

    Put runtime here:
    -----------------
    [       O(n)        ]

    """
    # searching a set is O(1), this is a list so O(n) - really O(2n)
    if "hippo" in animals or "platpypus" in animals:
        return True
    else:
        return False


def sum_zero_1(numbers):
    """Find pairs of integers that sum to zero.

    Put runtime here:
    -----------------
    [       O(n)        ]

    """
    # only does operation on each item once
    result = []

    # Hint: the following line, "s = set(numbers)", is O(n) ---
    # we'll learn exactly why later
    s = set(numbers)

    for x in s:
        if -x in s:
            result.append([-x, x])

    return result


def sum_zero_2(numbers):
    """Find pairs of integers that sum to zero.

    Put runtime here:
    -----------------
    [       O(n^2)        ]

    """

    result = []
    # 2 nested foor loops means O(n^2)
    for x in numbers:
        for y in numbers:
            if x == -y:
                result.append((x, y))
    return result


def sum_zero_3(numbers):
    """Find pairs of integers that sum to zero.

    This version gets rid of duplicates (it won't add (1, -1) if (-1, 1) already there.

    Put runtime here:
    -----------------
    [       O(n^2)      ]

    """

    result = []
    # also O(n^2) but also have to search 2 more times over results (a list: O(2n)) 
    for x in numbers:
        for y in numbers:
            if x == -y and (x, y) not in result and (y, x) not in result:
                result.append((x, y))
    return result
