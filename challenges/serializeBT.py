from Queue import Queue

class Node:   

    def __init__(self):
        self.value = 0
        self.left = 0
        self.right = 0
        self.index_lookup = None

    def preprocess_inorder(self, inorder):
        return { num:i for i, num in enumerate(inorder)}

    def deserialize(self, preorder, inorder):
        self.index_lookup = self.preprocess_inorder(inorder) 
        return self._deserialize(preorder, inorder)


    def _deserialize(self, preorder, inorder):
        if len(preorder) == 0 or len(inorder) == 0:
            return None

        #print preorder
        #print inorder

        root = Node()
        root.value = preorder[0]
        root_index = self.index_lookup[root.value]

        #print "Root value: {0}, Index in inorder: {1}".format(root.value,root_index) 

        root.left = self._deserialize(preorder[1:root_index+1], inorder[:root_index])
        root.right = self._deserialize(preorder[root_index:], inorder[root_index+1:])

        return root

    def traverse_by_level(self):
        q = Queue()
        q.put_nowait(self)

        current_level = 1
        next_level = 0

        while not q.empty():
            current = q.get_nowait()
            current_level -= 1

            if(current == None):
                print "#",
                continue

            print current.value,
            #if current.left != None:
            q.put_nowait(current.left)
            #if current.right != None:
            q.put_nowait(current.right)
            next_level += 2

            if current_level == 0:
                current_level = next_level
                next_level = 0
                print

        
            
tree = Node().deserialize(map(int, "12473"), map(int, "74213"))
print tree.value
print tree.left.value
print tree.right.value
#tree.traverse_by_level()
