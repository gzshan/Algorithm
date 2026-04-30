#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from base import TreeLinkNode, TreeNode
from typing import Optional, List
import sys

class BstSolution:

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        98 验证二叉搜索树:递归实现,注意限制最大最小值
        """
        if root is None:
            return True
        maxValue = sys.maxsize
        minValue = -sys.maxsize - 1
        return self._isValid(root, minValue, maxValue)
        
    
    def _isValid(self, root, minValue, maxValue) -> bool:
        if root is None:
            return True
        if root.left and root.left.val >= root.val:
            return False
        if root.right and root.right.val <= root.val:
            return False
        if root.val <= minValue or root.val >= maxValue:
            return False
        return self._isValid(root.left, minValue, root.val) and self._isValid(root.right, root.val, maxValue)
    

    def isValidBST2(self, root: Optional[TreeNode]) -> bool:
        """
        98 验证二叉搜索树:迭代实现,中序遍历是递增的序列
        """
        if root is None:
            return True
        stack = []
        p = root
        last = -sys.maxsize -1
        while p is not None or len(stack) > 0:
            while p:
                stack.append(p)
                p = p.left
            node = stack.pop()
            if node.val <= last:
                return False
            last = node.val
            p = node.right
        
        return True
    

    def verifyTreeOrder(self, postorder: List[int]) -> bool:
        """
        152: 验证一个序列是否为BST的后序遍历序列
        后序:左、右、根, 最右边是根，然后根据和根的大小区分左右子树,递归处理
        """
        def _check(postorder: List[int], start: int, end: int) -> bool:
            if start >= end:
                return True
            rootVal = postorder[end]

            index = start
            while postorder[index] < rootVal: # 所有小于根的是左子树
                index += 1
            
            for i in range(index, end):  # 后面如果有小于根的说明不是BST  
                if postorder[i] < rootVal:
                    return False
            
            return _check(postorder, start, index-1) and _check(postorder, index, end-1)
        
        if postorder is None:
            return False
        if len(postorder) <= 0:
            return True
        return _check(postorder=postorder, start=0, end=len(postorder)-1)
    

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        230: 二叉搜索树中第K小的数字
        中序遍历
        """
        if root is None:
            return -1
        
        stack = []
        p = root
        num = 1
        while p or len(stack) > 0:
            while p:
                stack.append(p)
                p = p.left
            node = stack.pop()
            if num == k:
                return node.val
            num += 1
            p = node.right

        return -1
    

    def convert(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        二叉搜索树与双向链表: 将二叉搜索树转为排序的双向链表
        """
        def _convert(root, endLink):
            # 中序遍历
            if root is None:
                 return None
            # 左边构建
            if root.left:
                endLink = _convert(root.left, endLink)
            
            root.left = endLink
            if endLink:
                endLink.right = root
            endLink = root

            if root.right:
                endLink = _convert(root.right, endLink)
            return endLink
        
        if root:
            endLink = None
            p = root
            _convert(root, endLink)
            
            while p and p.left:
                p = p.left
            
            return p
        
    
    def convert2(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        二叉搜索树与双向链表: 将二叉搜索树转为排序的双向链表, 迭代写法
        """
        if root is None:
            return None
        
        stack = []
        p = root
        pre = None
        head = None

        while p or len(stack) > 0:
            while p:
                stack.append(p)
                p = p.left
            node = stack.pop()
            if pre is None:
                head = node
                head.left = None
            else:
                pre.right = node
                node.left = pre
            pre = node
            
            p = node.right
        
        return head
    

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        235: 二叉搜索树的最小公共祖先
        递归实现
        """
        if root is None:
            return root
        if root.val == p.val or root.val == q.val:
            return root
        elif root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
    

    def lowestCommonAncestor2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        235: 二叉搜索树的最小公共祖先
        迭代实现
        """
        if root is None:
            return root
        
        while True:
            if root.val == p.val or root.val == q.val:
                return root
            elif root.val > p.val and root.val > q.val:
                root = root.left
            elif root.val < p.val and root.val < q.val:
                root = root.right
            else:
                return root
    

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """
        450:删除二叉搜索树中指定的节点
        """
        if root is None:
            return None
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # 相等，删除root
            if root.left is None and root.right is None: # 叶子
                root = None
            elif root.left is None:
                root = root.right
            elif root.right is None:
                root = root.left
            else:
                # 左右子树都有，找中序的后继节点替换上来
                # 即右子树最左边的节点
                temp = root.right
                if temp.left is None:
                    root.val = temp.val
                    root.right = temp.right
                else:
                    parent = None
                    while temp and temp.left:
                        parent = temp
                        temp = temp.left
                    # 删掉temp
                    root.val = temp.val
                    parent.left = None
        return root
            
    
    def numTrees(self, n: int) -> int:
        """
        96:不同的二叉搜索树
        从1-n能够构造出多少种不同的二叉搜索树
        """
        if n <= 2:
            return n
        
        # 0: 1
        # 1: 1
        # 2: 2
        # 3: 5， 1: 0*2 2:1*1 3:2*0
        # 4: 14   1: 0*3=5 2:1*2=2 3:2*1=2 4: 3*0: 5
        result = [0] * (n+1)
        result[0] = 1
        result[1] = 1
        result[2] = 2

        for i in range(3, n+1):
            for j in range(1, i+1):
                result[i] += result[j-1] * result[i-j]
        return result[n] 
    

    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        """
        95:不同的二叉搜索树
        从1-n构造对应的二叉搜索树
        """
        def _generate(begin: int, end: int) -> List[Optional[TreeNode]]:
            if begin > end:
                return [None]
            if begin == end:
                root = TreeNode(begin, None, None)
                return [root]
            
            result = []
            for i in range(begin, end+1):
                leftTrees = _generate(begin, i-1)
                rightTrees = _generate(i+1, end)

                root = TreeNode(i, None, None)
                for l in leftTrees:
                    for r in rightTrees:
                        root.left = l
                        root.right = r
                        result.append(root)
            
            return result
        return _generate(1, n)
                
                
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """
        108:将有序数据转换为平衡二叉搜索树
        """
        if nums is None or len(nums) <= 0:
            return None

        def _convert(nums: List[int], begin: int, end: int) -> Optional[TreeNode]:
            if begin > end:
                return None
            if begin == end:
                return TreeNode(nums[begin], None, None)
            
            rootIndex = begin + (end-begin) // 2
            root = TreeNode(nums[rootIndex], None, None)

            root.left = _convert(nums, begin, rootIndex-1)
            root.right = _convert(nums, rootIndex+1, end)
            return root
            
        return _convert(nums, 0, len(nums)-1) 



def main():
    solution = BstSolution()
    print(solution.numTrees(4))


if __name__ == "__main__":
    main()

            