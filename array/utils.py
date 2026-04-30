#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List


def FindMinValueInArray(numbers: List[int]) -> int:
    if numbers is None or len(numbers) <= 0:
        return -1
    minVal = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] < minVal:
            minVal = numbers[i]
    return minVal


def countDigitOne(n: int) -> int:
    if n < 1:
        return 0
    
    weight = 0
    extra = 0
    
    base = 1
    r = n

    result = 0

    while True:
        weight = r % 10
        r = r // 10
        
        if weight > 1:
            result += (r + 1) * base
        elif weight < 1:
            result += r * base
        else:
            result += r*base + extra

        base = base * 10
        extra = n % base

        if r == 0:
            break
    
    return result


def partition(nums: List[int], low: int, high: int) -> int:
    i, j = low, high
    temp = nums[i]

    while i < j:
        while i<j and nums[j]<temp:
            j -= 1
        if i < j:
            nums[i] = nums[j]
            i += 1

        while i< j and nums[i] >= temp:
            i+=1 
        
        if i<j:
            nums[j] = nums[i]
            j-=1
    
    nums[i] = temp
    return i


def findKthLargest(nums: List[int], k: int) -> int:
    if nums is None or len(nums) <= 0:
        return -1
    
    low, high = 0, len(nums) - 1

    while low<=high:
        index = partition(nums, low, high)
        if index+1 == k:
            return nums[index]
        elif index+1 < k:
            low = index+1
        else:
            high = index-1
    
    return -1


if __name__ == "__main__":
    print(countDigitOne(13))
    print(findKthLargest([3,2,3,1,2,4,5,5,6], 4))