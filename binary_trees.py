# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)


class Solution:
    # ----------------------- MAX DEPTH ------------------------------
    def maxDepth(self, root: TreeNode) -> int:

        if root is None:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return max(left, right) + 1

    # ----------------------- SYMMETRIC ------------------------------
    def is_mirror(self, root1, root2):
        if root1 and not root2 or not root1 and root2:
            return False
        if not root1 and not root2:
            return True
        if root1.val != root2.val:
            return False
        return self.is_mirror(root1.left, root2.right) and self.is_mirror(root1.right, root2.left)

    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        return self.is_mirror(root, root)

    # ------------------------ TREE TO LIST --------------------------
    def tree_to_list(self, top_node: TreeNode) -> list:
        if not top_node or all([v is None for v in top_node.__dict__]):
            return []

        val_list = [top_node.val]

        if not top_node.left and not top_node.right:
            return val_list

        if top_node.left:
            extension = self.tree_to_list(top_node.left)
        else:
            extension = top_node.left

        val_list.extend(extension or [None])

        if top_node.right:
            extension = self.tree_to_list(top_node.right)
        else:
            extension = top_node.right

        val_list.extend(extension or [None])

        return val_list

    # ------------------------ SAME TREE --------------------------
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def checkTree(p, q):
            if p == None and q == None:
                return True
            elif p == None and q != None:
                return False
            elif q == None and p != None:
                return False
            else:
                if q.val != p.val:
                    return False
                if checkTree(p.left, q.left) and checkTree(p.right, q.right):
                    return True
                else:
                    return False
        return checkTree(p, q)

    # ------------------------ FIND TARGET --------------------------
    def search(self, root, key):

        # Base Cases: root is null or key is present at root
        if root is None or root.val == key:
            return root

        # Key is greater than root's key
        if root.val < key:
            return self.search(root.right, key)

        # Key is smaller than root's key
        return self.search(root.left, key)

    # ------------------------ FIND TARGET --------------------------
    def count_steps(self, root, key):

        count = 1

        # Base Cases: root is null or key is present at root
        if root is None or root.val == key:
            return count

        # Key is greater than root's key
        if root.val < key:
            count += self.count_steps(root.right, key)

        # Key is smaller than root's key
        else:
            count += self.count_steps(root.left, key)

        return count


node1 = TreeNode(5)

node1.left = TreeNode(3)
node1.right = TreeNode(6)

node1.left.left = TreeNode(2)
node1.left.right = TreeNode(4)

node1.left.right.left = TreeNode(0)
node1.left.right.right = TreeNode(1)

solution = Solution()

res = solution.count_steps(node1, 5)
print(res)
