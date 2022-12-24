def sqrtx(x):
    """
    二分法求平方根
    - https://leetcode.cn/problems/sqrtx/description/
    """
    low, high, result = 0, x, -1
    while low <= high:
        mid = low + ((high - low) >> 1)
        sqrt = mid ** 2
        if sqrt <= x:
            result = mid
            low = mid + 1
        else:
            high = mid - 1
    return result


if __name__ == '__main__':
    # 调用 sqrt 函数
    result = sqrtx(9)
    print(result)
