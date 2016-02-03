from Queue import Queue


class Node:

    def __init__(self):
        self.value = 0
        self.left = 0
        self.right = 0
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

    def _deserialize(self, preorder, inorder)
        """Inner recursive implementation of the deserialization

        :param preorder: pre-order traversal list
        :param inorder: in-order traversal list
        :return: The corresponding binary tree which was serialized
        """
        if len(preorder) == 0 or len(inorder) == 0:
            return None

        root = Node()
        root.value = preorder[0]
        root_index = self.index_lookup[root.value]

        #print "Preorder: {0}, Inorder: {1}".format
        #print "Root value: {0}, Index in inorder: {1}".format(root.value,root_index)

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

tree = Node().deserialize(map(int, "12473"), map(int, "74213"))
tree.traverse_by_level()
