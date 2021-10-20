import itertools
from itertools import permutations
import unittest


def reverseInPlace(str): return str[::-1]


def duplicateCharactersV3(str):
    chars = []
    for k in str:
        if k not in chars and str.count(k) > 1:
            chars.append(k)
    return ''.join(chars)


def check_two_string_is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False
    arr1 = list(str1)
    arr2 = list(str2)
    arr1.sort()
    arr2.sort()
    for i in range(len(str1)):
        if arr1[i] != arr2[i]: return False

    return True


def findAllPermutationsOfString(str):
    perm = list(permutations(str))
    perm = list(set(perm))
    return perm


def reverseWithRecursion(str, n=0):
    if n == int(len(str) / 2): return reverseUtil(n, str)
    return reverseWithRecursion(reverseUtil(n, str), n + 1)


def reverseUtil(n, str):
    return str[:n] + str[len(str) - 1 - n] + str[n + 1:len(str) - 1 - n] + str[n] + str[len(str) - n:]


def quickSort(arr):
    if len(arr) == 0: return []
    return quickSort([i for i in arr[1:] if i < arr[0]]) + [arr[0]] + quickSort([i for i in arr[1:] if i >= arr[0]])


def graduate(arr):
    for i, n in enumerate(arr):
        if n % 5 > 2 and n > 37:
            arr[i] = n + 5 - n % 5
    return arr


#   Grading students
def equalsArr(arr1, arr2, unique=False):
    if len(arr1) != len(arr2):
        return False
    if not unique:
        arrClone1 = sorted(arr1)
        arrClone2 = sorted(arr2)
    else:
        arrClone1 = arr1[:]
        arrClone2 = arr2[:]
    for i in range(len(arrClone1)):
        if arrClone1[i] != arrClone2[i]:
            return False
    return True


def appleAndOrange(s, t, a, b, apples, oranges):
    for i, n in enumerate(apples):
        apples[i] = n + a
    for i, n in enumerate(oranges):
        oranges[i] = n + b
    appl = len([i for i in apples if s <= i <= t])
    orang = len([i for i in oranges if s <= i <= t])
    return [appl, orang]


def kangarooJump(x1, v1, x2, v2):
    if (x1 - x2) * (v1 - v2) >= 0:
        return False
    if abs(x1 - x2) % abs(v1 - v2) == 0:
        return True
    return False


def totalFactorX(a, b):
    ekk = int(ekuk(a, sorted(b)[-1]))
    ekb = ekub(b, sorted(a)[0])
    if ekk * ekb == 0:
        return 0
    return calculate(ekk, ekb)


def calculate(a, b):
    n = 1
    m = 1
    if a < b and b % a == 0:
        while 1:
            if b % (a + a * m) == 0:
                n = n + 1
            elif b % (a + a * m) == b:
                break
            m = m + 1
    if b % a != 0:
        return 0
    return n


def ekub(arr, validate):
    if len(arr) == 1:
        return arr[0]
    if arr is None:
        return arr
    ekb = arr[0]
    el1 = arr[0]
    el2 = arr[1]
    i = 1
    while el1 != arr[-1]:
        el1 = ekb
        ekb = ekubTwo(el1, el2)
        if ekb < validate:
            return 0
        if ekb == 1:
            return 1
        el1 = el2
        i = i + 1
        if len(arr) > i:
            el2 = arr[i]
    return ekb


def ekubTwo(el1, el2):
    while el1 * el2 != 0:
        if el1 > el2:
            el1 = el1 - el2
        else:
            el2 = el2 - el1
    return el1 + el2


def ekuk(arr, validate):
    if len(arr) == 1:
        return arr[0]
    if arr is None:
        return arr
    ekk = arr[0]
    el1 = arr[0]
    el2 = arr[1]
    i = 1
    while el1 != arr[-1]:
        el1 = ekk
        ekk = el1 * el2 / ekubTwo(el1, el2)
        if ekk > validate:
            return 0
        el1 = el2
        i = i + 1
        if len(arr) > i:
            el2 = arr[i]
    return ekk


def breakingRecords(arr):
    if len(arr) < 2:
        return [0, 0]
    mini = arr[0]
    maxi = arr[0]
    minBreak = 0
    maxBreak = 0
    for i, a in enumerate(arr):
        if a < mini:
            mini = arr[i]
            minBreak = minBreak + 1
        elif a > maxi:
            maxi = arr[i]
            maxBreak = maxBreak + 1
    return [maxBreak, minBreak]


def checkTarget(arr2, target):
    ans = 0
    for i in range(1, len(arr2) + 1):
        arrays = list(itertools.combinations(arr2, i))
        ans = ans + len([ar for ar in arrays if sum(ar) == target])
    return ans


def checkTargetV2(arr2, target):
    ans = 0
    for i in range(1, len(arr2) + 1):
        arrays = list(itertools.permutations(arr2, i))
        ans = ans + len([ar for ar in arrays if sum(ar) == target])
    return ans


def createPrimeNArrays(n):
    arr = [2]
    if n < 2:
        return arr
    k = 3
    while 1:
        tub = 1
        for t in arr:
            if k % t == 0:
                tub = 0
        if tub:
            arr.append(k)
        k = k + 1
        if len(arr) == n:
            return arr


def subsetDivV2(arr, k):
    return checkTarget(arr, k)


def subsetDivV3(arr, k):
    return checkTargetV2(arr, k)


def out(s):
    print(s)


# Main
# assert equalsArr(graduate([73, 67, 38, 33]), [75, 67, 40, 33])
# assert equalsArr(graduate([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
# assert equalsArr(appleAndOrange(7, 10, 4, 12, [2, 3, -4], [3, -2, -4]), [1, 2])
# assert equalsArr(appleAndOrange(7, 11, 5, 15, [-2, 2, 1], [5, -6]), [1, 1])
# assert kangarooJump(0, 3, 4, 2)
# assert totalFactorX([2, 6], [24, 36]) == 2
# assert totalFactorX([2, 4], [16, 32, 96]) == 3
# assert totalFactorX(list(range(100, 90, -1)), list(range(1, 11))) == 0
# assert totalFactorX([2], [20, 30, 12]) == 1
# assert equalsArr(breakingRecords([10, 5, 20, 20, 4, 5, 2, 25, 1]), [2, 4])
# assert equalsArr(breakingRecords([3, 4, 21, 36, 10, 28, 35, 5, 24, 42]), [4, 0])
if __name__ == '__main__':
    # print(subsetDivV2([i ** i for i in range(1, 7)], 50))
    # print(subsetDivV3([i ** i for i in range(1, 11)], 50))
    # assert subsetDivV2([i ** i for i in range(1, 7)], 50) == 0
    # assert subsetDivV2([i ** i for i in range(1, 11)], 50) == 21
    assert createPrimeNArrays(3) == [2, 3, 5]
