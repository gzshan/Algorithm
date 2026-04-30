#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from .base import TreeLinkNode, TreeNode
from typing import Optional, List
from collections import deque

class PathSolution:

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
        112 路径总和(判断是否存在从根到叶子的路径和为target)
        递归实现
        """
        if root is None:
            return False
        if root.left is None and root.right is None:
            if root.val == targetSum:
                return True
        
        left = self.hasPathSum(root.left, targetSum - root.val)
        right = self.hasPathSum(root.right, targetSum - root.val)
        return left or right
    

    def hasPathSum2(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
        112 路径总和(判断是否存在从根到叶子的路径和为target)
        迭代实现
        """
        if root is None:
            return False
        
        node_queue = deque()
        val_queue = deque()
        node_queue.append(root)
        val_queue.append(root.val)

        while len(node_queue) > 0:
            node = node_queue.popleft()
            val = val_queue.popleft()

            if node.left is None and node.right is None:
                if val == targetSum:
                    return True
            
            if node.left:
                node_queue.append(node.left)
                val_queue.append(node.left.val + val)

            if node.right:
                node_queue.append(node.right)
                val_queue.append(node.right.val + val)
            
        return False
    

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        """
        113 路径总和(找到所有路径和为target的路径)
        BFS解法
        """
        result = []
        if root is None:
            return result
        
        def findPath(node, parent, result):
            tmp = []
            while node:
                tmp.append(node.val)
                if node in parent:
                    node = parent[node]
                else:
                    node = None
            result.append(tmp[::-1])
            
        
        node_queue = deque()
        val_queue = deque()
        node_queue.append(root)
        val_queue.append(root.val)

        parent = {}

        while len(node_queue) > 0:
            node = node_queue.popleft()
            val = val_queue.popleft()

            if node.left is None and node.right is None:
                if val == targetSum:
                    # 找到路径, 从node一直找到根
                    findPath(node, parent, result)

            if node.left:
                parent[node.left] = node
                node_queue.append(node.left)
                val_queue.append(node.left.val+val)
            
            if node.right:
                parent[node.right] = node
                node_queue.append(node.right)
                val_queue.append(node.right.val + val)

        return result
    

    def pathSum2(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        """
        113 路径总和(找到所有路径和为target的路径)
        递归解法
        """
        result = []
        if root is None:
            return result
        
        temp = []
        def helper(root, targetSum, temp):
            temp.append(root)
            if root.left is None and root.right is None:
                if root.val == targetSum:
                    res = []
                    for t in temp:
                        res.append(t.val)
                    result.append(res)
            else:
                if root.left:
                    helper(root.left, targetSum-root.val, temp)

                if root.right:
                    helper(root.right, targetSum-root.val, temp)
            
            if len(temp)>0:
                temp.pop()

        helper(root, targetSum, temp)
        return result