#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List, Optional

class HeapSolution:
    """
    父节点： (i-1) // 2
    左子节点： 2*i+1
    右子节点： 2*i+2
    """

    def siftup(self, heap: List[int], i: int):
        # 上浮，插入一个元素, 先把它放到末尾，然后逐层上浮
        while i>0:
            parent = (i-1) // 2
            if heap[parent] < heap[i]:
                heap[parent], heap[i] = heap[i], heap[parent]
                i = parent
            else:
                break
    

    def siftdown(self, heap: List[int], i: int, heapSize: int):
        # 下沉：不断与较大的子节点比较，如果比子节点小就交换下去
        while 2*i+1<heapSize:
            child = 2*i + 1
            if child +1 < heapSize and heap[child+1] > heap[child]:
                child = child + 1
            if heap[i] < heap[child]:
                heap[i], heap[child] = heap[child], heap[i]
                i = child
            else:
                break


    def buildHeap(self, nums: List[int]):
        # 建堆:从最后一个非叶节点开始，逐个执行下沉操作
        heapSize = len(nums)
        for i in range(heapSize//2 - 1, -1, -1):
            self.siftdown(nums, i, heapSize)



if __name__ == "__main__":
    solution = HeapSolution()
    nums = [1, 2, 3]
    solution.buildHeap(nums)
    print(nums)
