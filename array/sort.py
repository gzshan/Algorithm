#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List, Optional

class SortSolution:
    
    def mergeSort(self, nums: List[int]):
        """
        归并排序
        """
        if nums is None or len(nums) <= 0:
            return
        
        def merge(nums, low, mid, high):
            result = [-1] * (high - low + 1)
            i = low
            j = mid + 1
            t = 0
            while i <= mid and j <= high:
                if nums[i] <= nums[j]:
                    result[t] = nums[i]
                    i += 1
                else:
                    result[t] = nums[j]
                    j += 1
                t += 1
            
            while i<=mid:
                result[t] = nums[i]
                i += 1
                t += 1
            while j<=high:
                result[j] = nums[j]
                j += 1
                t += 1

            for i in range(len(result)):
                nums[i + low] = result[i]

        def sort(nums, low, high):
            if low >= high:
                return
            mid = low + (high-low) // 2
            sort(nums, low, mid)
            sort(nums, mid+1, high)
            # 左右归并
            merge(nums, low, mid, high)


        sort(nums, 0, len(nums) - 1)
        return nums
    

    def quickSort(self, nums: List[int]):
        """
        快速排序
        """
        if nums is None or len(nums) <= 0:
            return 
        def quicksort(nums, low, high):
            if low >= high:
                return
            temp = nums[low]
            i, j = low, high
            while i<j:
                while i<j and nums[j] >= temp:
                    j -= 1
                if i<j:
                    nums[i] = nums[j]
                    i += 1
                
                while i<j and nums[i] < temp:
                    i += 1
                if i<j:
                    nums[j] = nums[i]
                    j -= 1
            nums[i] = temp

            if low < i:
                quicksort(nums, low, i-1)
            if i< high:
                quicksort(nums, i+1, high)
        
        quicksort(nums, 0, len(nums) - 1)


if __name__ == "__main__":
    solution = SortSolution()
    nums = [4,3,2,1,0]
    # solution.mergeSort(nums)
    solution.quickSort(nums)
    print(nums)
        
        
        

