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