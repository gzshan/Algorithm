#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List, Optional
import sys

class MinStack:

    def __init__(self):
        self.stack = []
        self.minVal = sys.maxsize
        

    def push(self, val: int) -> None:
        if len(self.stack) <= 0:
            self.stack.append(0)
            self.minVal = val
        else:
            diff = val - self.minVal  # 当前值和最小值之间的差
            if diff < 0:
                self.minVal = val
            self.stack.append(diff)   # 注意：真正val - 旧的最小值 = diff

    def pop(self) -> None:
        if len(self.stack) > 0:
            v = self.stack.pop()
            if v < 0: 
                # 当前的最小值就是真正的val
                self.minVal = self.minVal - v
        

    def top(self) -> int:
        if len(self.stack) > 0:
            diff = self.stack[-1]
            if diff > 0:
                return diff + self.minVal
            else:
                return self.minVal

    def getMin(self) -> int:
        return self.minVal