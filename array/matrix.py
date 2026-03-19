#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List


def FindTargetInMatrix(numbers: List[List[int]], target: int) -> bool:
    """
    二维数组的查找(LeetCode 74): 从左到右递增,下一行第一个比上一行最后一个大, 查找target
    解法: 按行整体有序,打平直接二分
    """
    if numbers is None or len(numbers) <= 0:
        return False
    
    rows = len(numbers)
    cols = len(numbers[0])

    i = 0
    j = rows * cols - 1

    while i <= j:
        mid = i + (j-i) // 2

        if numbers[mid // cols][mid % cols] == target:
            return True
        elif numbers[mid // cols][mid % cols] > target:
            j = mid - 1
        else:
            i = mid + 1

    return False


def FindTargetInMatrix2(numbers: List[List[int]], target: int) -> bool:
    """
    二维数组的查找(LeetCode 240): 从上到下、从左到右递增, 查找target
    解法:右上或者左下开始
    """
    if numbers is None or len(numbers) <= 0:
        return False

    rows = len(numbers)
    cols = len(numbers[0])

    i = 0
    j = cols - 1

    while i < rows and j >= 0:
        if numbers[i][j] == target:
            return True
        elif numbers[i][j] > target:
            j -= 1
        else:
            i += 1
    
    return False


def main():
    print(FindTargetInMatrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 5))
    print(FindTargetInMatrix2([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 5))


if __name__ == "__main__":
    main()