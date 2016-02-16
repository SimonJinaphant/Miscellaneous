class Node:

    def __init__(self, value=None):
        """Constructs a binary tree node

        :return: A node which can hold a value and has two pointers
         to its left and right child/subtree
        """
        self.value = value
        self.left = 0
        self.right = 0

    def deserialize(self, preorder):
        """Deserialize a binary search tree given its pre-order traversal

        :param preorder: pre-order traversal list
        :return: The corresponding binary tree which was serialized
        """
        root = Node(preorder[0])

        right_start = -1
        for i in xrange(len(preorder)):
            if preorder[i] > root.value:
                right_start = i
                break

        if right_start != -1:
            root.right = self.deserialize(preorder[i:])

        if right_start != 1:
            root.left = self.deserialize(preorder[1:i])

        return root