
from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val: int= 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TreeLinkNode:
    def __init__(self, val: int=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class TreeBaseSolution:
    # 二叉树基础，树的深度、广度遍历

    def __init__(self):
        pass

    def bfs(self, root: TreeNode) -> List[List[int]]:
        # 按层遍历二叉树
        result = []
        if root is None:
            return result
        queue = deque()
        queue.append(root)

        while len(queue) > 0:
            size = len(queue) # 当前层的节点个数
            layer = []
            for i in range(size):
                node = queue.popleft()
                layer.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
            result.append(layer)
        return result
    

    def preOrder(self, root: TreeNode) -> List[int]:
        # 前序遍历
        result = []
        def dfs(root: TreeNode):
            if root is None:
                return
            result.append(root.val)
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        return result
    

    def preOrderV2(self, root: TreeNode) -> List[int]:
        # 前序遍历，迭代法
        result = []
        if root is None:
            return result
        stack = []
        p = root
        while p or len(stack) > 0:
            while p:
                stack.append(p)
                result.append(p.val)
                p = p.left
            node = stack.pop()
            p = node.right
        
        return result
    

    def inOrder(self, root: TreeNode) -> List[int]:
        result = []
        def dfs(root):
            if root is None:
                return
            dfs(root.left)
            result.append(root.val)
            dfs(root.right)
        dfs(root)
        return result
    

    def inOrderV2(self, root: TreeNode) -> List[int]:
        result = []
        if root is None:
            return result
        stack = []
        p = root
        while p or len(stack) > 0:
            while p:
                stack.append(p)
                p = p.left
            node = stack.pop()
            result.append(node.val)
            p = node.right
        
        return result
    

    def postOrder(self, root: TreeNode) -> List[int]:
        result = []
        def dfs(root: TreeNode):
            if root is None:
                return 
            dfs(root.left)
            dfs(root.right)
            result.append(root.val)
        dfs(root)
        return result
    

    def postOrderV2(self, root: TreeNode) -> List[int]:
        # 后序遍历迭代写法
        result = []
        if root is None:
            return result
        stack = []
        p = root
        pre = None
        while p or len(stack) > 0:
            while p:
                stack.append(p)
                p = p.left
            node = stack.pop()
            if node.right is None or node.right == pre:
                result.append(node.val)
                pre = node
                p = None
            else:
                stack.append(node)
                p = node.right
        
        return result


if __name__ == "__main__":
    solution = TreeBaseSolution()
    root = TreeNode(0, None, None)
    root.left = TreeNode(1, TreeNode(3, None, None), TreeNode(4, None, None))
    root.right = TreeNode(2, TreeNode(5, None, None), TreeNode(6, None, None))

    print(solution.bfs(root))
    print(solution.preOrder(root))
    print(solution.preOrderV2(root))
    print(solution.inOrder(root))
    print(solution.inOrderV2(root))
    print(solution.postOrder(root))
    print(solution.postOrderV2(root))

