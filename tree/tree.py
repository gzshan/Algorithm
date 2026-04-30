#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from .base import TreeLinkNode, TreeNode
from typing import Optional

class TreeSolution:

    
    def FindNext(self, node: Optional[TreeLinkNode]) -> Optional[TreeLinkNode]:
        """
        二叉树中序遍历的下一个节点
        中序：左、根、右，所以主要判断有没有右子树
        1、有右子树:右子树最左边那个节点
        2、没有右子树:是左节点，那下一个就是父节点，不是左节点则往上找
        """
        if node is None:
            return None
        if node.right is not None: # 有右子树，右子树最左边那个结点是下一个
            temp = node.right
            while temp.left is not None:
                temp = temp.left
            return temp
        else:  # 没有右子树
            parent = node.next
            if parent is not None and parent.left == node: # 是父节点的左节点
                return node.left
            else:
                while parent is not None and parent.next is not None and parent.next.left != parent:
                    parent = parent.next
                if parent is None:
                    return None
                else:
                    return parent.next
    

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        114 二叉树展开为链表 前序顺序
        本地的关键在于：左子树的最下最右的节点，是右子树的父节点
        """
        cur = root
        while cur is not None:
            if cur.left is None:
                cur = cur.right
            else:
                # 找到左子树最右边的节点
                temp = cur.left
                while temp and temp.right:
                    temp = temp.right
                
                # 把右子树接到左子树的最后，将根节点释放出来
                temp.right = cur.right
                cur.right = cur.left
                cur.left = None

                cur = cur.right


    def flatten2(self, root: Optional[TreeNode]) -> None:
        """
        114 二叉树展开为链表 前序顺序
        递归写法
        """
        if root is None:
            return
        self.flatten(root.left)
        # 右边先保存
        right = root.right

        root.right = root.left
        root.left = None

        self.flatten(right)

        # 左右连起来
        temp = root
        while temp and temp.right:
            temp = temp.right
        temp.right = right

    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        236 二叉树的最近公共祖先
        递归写法
        """
        if root is None:
            return None
        if root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        elif left is None:
            return right
        else:
            return left
    

    def lowestCommonAncestor2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        236 二叉树的最近公共祖先
        迭代写法
        """
        def _helper(root, hashmap):
            if root.left:
                hashmap[root.left.val] = root
                _helper(root.left, hashmap)
            
            if root.right:
                hashmap[root.right.val] = root
                _helper(root.right, hashmap)

        if root is None:
            return None
        if root == p or root == q:
            return root

        hashmap = {}
        _helper(root, hashmap)

        # 把p的父节点保存下来
        visited = set()
        node = p
        while True:
            visited.add(node.val)
            if node.val in hashmap:
                node = hashmap[node.val]
            else:
                break
        
        # 找q的父节点
        node2 = q
        while True:
            if node2.val in visited:
                return node2
            elif node2.val in hashmap:
                node2 = hashmap[node2.val]
            else:
                break

        return root

