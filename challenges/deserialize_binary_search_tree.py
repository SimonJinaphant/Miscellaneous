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

    def deserialize(self, preorder):
        """Deserialize a binary search tree given its pre-order traversal

        :param preorder: pre-order traversal list
        :return: The corresponding binary tree which was serialized
        """
        root = Node(preorder[0])

        if len(preorder) > 1:
            right_start = None
            for i in xrange(len(preorder)):
                if preorder[i] > root.value:
                    right_start = i
                    break

            if right_start is not None:
                root.right = self.deserialize(preorder[right_start:])

            if right_start != 1:
                root.left = self.deserialize(preorder[1:right_start])

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

tree = Node().deserialize([30, 15, 1, 25, 20, 100])
tree.traverse_by_level()