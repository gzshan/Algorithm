#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List
from utils import FindMinValueInArray


def minNumberInRotateArray(numbers: List[int]) -> int:
    """
    旋转数组的最小数字
    解法:二分法
    """
    if numbers is None or len(numbers) <= 0:
        return -1
    
    low = 0
    high = len(numbers) - 1

    if numbers[low] < numbers[high]:
        return numbers[low]

    while low < high:
        mid = low + (high - low) // 2
        if numbers[mid] == numbers[low] and numbers[low] == numbers[high]:
            return  FindMinValueInArray(numbers)
        
        if numbers[mid] <= numbers[high]:
            high = mid
        elif numbers[mid] >= numbers[low]:
            low = mid
        
        if high - low == 1:
            return numbers[high]
    
    return -1


def FindGreatestSumOfSubArray(numbers: List[int]) -> int:
    """
    连续子数组的最大和
    解法: 动态规划 result = max(numbers[i], result[i-1]+numbers[i])
    """
    if numbers is None or len(numbers) <= 0:
        return -1
    
    # 以第i个元素结尾的数组的子数组的最大和
    endAsI = numbers[0]
    result = endAsI
    for i in range(1, len(numbers)):
        endAsI = max(result + numbers[i], numbers[i])
        if endAsI > result:
            endAsI = result
    
    return result


def MoreThanHalfNum_Solution(numbers: List[int]):
    """
    数组中出现次数超过一半的数字
    解法:
    1. 哈希表
    2. 排序
    3. 摩尔投票法
    """
    if numbers is None or len(numbers) <= 0:
        return 0
    
    result = numbers[0]
    times = 1

    for i in range(1, len(numbers)):
        if times == 0: # 计数归0，重新选择候选
            result = numbers[i]
            times = 1
        elif result == numbers[i]:
            times += 1
        else:
            times -= 1
    
    # 验证
    times = 0
    for i in range(len(numbers)):
        if numbers[i] == result:
            times += 1
    
    if times > len(numbers) // 2:
        return result
    else:
        return 0
    

def FindNumsAppearOnce(numbers: List[int]):
    """
    数组中只出现一次的两个数字: 两个数字出现一次，其他数字出现两次
    解法:
    1. 哈希表
    2. 位运算
    """
    if numbers is None or len(numbers) <= 0:
        return -1, -1
    
    # 1. 位异或，得到两个数字的异或值, 若只有一个数字出现一次，异或即可
    xor: int = 0
    for number in numbers:
        xor ^= number
    
    # 2. 找到异或值中第一个为1的位，作为分组依据
    index = 0
    while index < 32:
        if ((xor >> index) & 1) == 1:
            break
        index += 1
    
    # 3. 根据该位将数组分为两组，分别异或得到两个只出现一次的数
    num1 = 0
    num2 = 0
    for number in numbers:
        if ((number >> index) & 1) == 1:
            num1 ^= number
        else:
            num2 ^= number
    
    return num1, num2


def main():
    print(minNumberInRotateArray([1, 2, 3, 4, 5]))
    print(MoreThanHalfNum_Solution([1, 2, 3, 2, 2, 2, 5, 4, 2]))
    print(FindNumsAppearOnce([2,4,3,6,3,2,5,5]))


if __name__ == "__main__":
    main()


    
