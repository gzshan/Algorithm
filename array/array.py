#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List

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


def main():
    print(MoreThanHalfNum_Solution([1, 2, 3, 2, 2, 2, 5, 4, 2]))


if __name__ == "__main__":
    main()


    
