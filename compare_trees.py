"""

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

"""
class Solution:

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        current_nodes = [(p, q)]

        while current_nodes:
            temp = []
            for p, q in current_nodes:
                if (p and not q) or (not p and q):
                    return False
                elif p and q and p.val != q.val:
                    return False

                if p and q:
                    temp.append((p.left, q.left))
                    temp.append((p.right, q.right))

            current_nodes = temp
            print (current_nodes)

        return True