from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if nums is None or len(nums) <= 0:
            return
        n = len(nums)
        
        # 1243的下一个是1324

        # 从后往前找第一个下降的位置
        index = n-1
        while index > 0 and nums[index-1] >= nums[index]:
            index -= 1
        index = index - 1
        
        if index < 0: # 已经最大，直接反转
            self.reverse(nums, 0, n-1)
            return
        
        # 找index后面刚比它大的位置
        pos = n-1
        while pos >= 0 and nums[pos] <= nums[index]:
            pos -= 1
        print(f"{index} {pos}")
        if pos < 0:
            return
        
        
        nums[index], nums[pos] = nums[pos], nums[index]
        
        self.reverse(nums, index+1, n-1)
    

    def reverse(self, nums, begin, end):
        i, j = begin, end
        while i<j:
            nums[i], nums[j] = nums[j], nums[i]
            i+=1
            j-=1
        
    

if __name__ == "__main__":
    s = Solution()
    nums = [5, 1, 1]
    s.nextPermutation(nums)
    print(nums)