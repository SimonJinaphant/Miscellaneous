from Queue import Queue


class Node:

    def __init__(self, value=None):
        """Constructs a binary tree node

        :return: A node which can hold a value and has two pointers
         to its left and right child/subtree
        """
        self.value = value
        self.left = None
        self.right = None
        self.index_lookup = None

    def preprocess_inorder(self, inorder):
        """Build a look-up table to find the index of a value for the in-order list

        :param inorder: in-order traversal list
        :return: A dictionary with the in-order value as key and in-order index as values
        """
        return {num: i for i, num in enumerate(inorder)}

    def deserialize(self, preorder, inorder):
        """Deserialize a binary tree given its pre-order and in-order traversal

        :param preorder: pre-order traversal list
        :param inorder: in-order traversal list
        :return: The corresponding binary tree which was serialized
        """
        self.index_lookup = self.preprocess_inorder(inorder)
        return self._deserialize(preorder, inorder)

    def _deserialize(self, preorder, inorder):
        """Inner recursive implementation of the deserialization

        :param preorder: pre-order traversal list
        :param inorder: in-order traversal list
        :return: The corresponding binary tree which was serialized
        """
        if len(preorder) == 0 or len(inorder) == 0:
            return None

        assert len(preorder) == len(inorder), \
            "Require traversal list to be of same size"

        root = Node(preorder[0])
        root_index = self.index_lookup[root.value]

        root.left = self._deserialize(preorder[1:root_index+1], inorder[:root_index])
        root.right = self._deserialize(preorder[root_index+1:], inorder[root_index+1:])

        return root

    def traverse_by_level(self):
        """Traverse the binary level by level,
        printing out all non-None nodes
        """
        q = Queue()
        q.put_nowait(self)

        current_level = 1
        next_level = 0

        while not q.empty():
            current = q.get_nowait()
            current_level -= 1

            print current.value,

            if current.left is not None:
                q.put_nowait(current.left)
                next_level += 1

            if current.right is not None:
                q.put_nowait(current.right)
                next_level += 1

            if current_level == 0:
                current_level = next_level
                next_level = 0
                print

tree = Node().deserialize([1, 2, 4, 7, 3], [7, 4, 2, 1, 3])
tree.traverse_by_level()
