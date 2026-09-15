# Problem 2
# Step 1: Create a Node Class
class Node:

    # Each Node should contain:
    # A payload (an integer is fine)
    def __init__(self, payload):
        self.payload = payload
        self.left = None
        self.right = None

    # A left child (optionally empty)
    def get_left(self):
        return self.left

    def set_left(self, left):
        self.left = left

    # A right child (optionally empty)
    def get_right(self):
        return self.right

    def set_right(self, right):
        self.right = right

    # Applicable methods
    def get_payload(self):
        return self.payload

    def set_payload(self, payload):
        self.payload = payload

# Step 2: Create a Binary Search Tree Class
class BinarySearchTree:

    def __init__(self):
        self.root = None

    # Implement the following operations:
    # Insertion
    def insert(self, payload):
        new_node = Node(payload)
        if self.root is None:
            self.root = new_node
            return
        current = self.root
        while True:
            if payload < current.payload:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            elif payload > current.payload:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right
            else:
                return

    # Deletion
    def delete(self, payload):
        self.root = self._delete(self.root, payload)

    def _delete(self, node, payload):

        if node is None:
            return None

        if payload < node.payload:
            node.left = self._delete(node.left, payload)

        elif payload > node.payload:
            node.right = self._delete(node.right, payload)

        else:

            if node.left is None:
                return node.right

            if node.right is None:
                return node.left

            current = node.right

            while current.left is not None:
                current = current.left

            node.payload = current.payload
            node.right = self._delete(node.right, current.payload)

        return node

    # Search
    def search(self, payload):
        current = self.root
        while current is not None:
            if payload == current.payload:
                return True
            elif payload < current.payload:
                current = current.left
            else:
                current = current.right
        return False

    # Step 3: Implement Traversals
    def Traversal(self):
        # Inorder
        print("Inorder:")
        self.inorder(self.root)
        print()
        # Preorder
        print("Preorder:")
        self.preorder(self.root)
        print()
        # Postorder
        print("Postorder:")
        self.postorder(self.root)
        print()

    def inorder(self, node):

        if node is not None:
            self.inorder(node.left)
            print(node.payload, end=" ")
            self.inorder(node.right)

    def preorder(self, node):

        if node is not None:
            print(node.payload, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):

        if node is not None:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.payload, end=" ")


# Note: You do not need to implement balancing features,
# but you are welcome to include them if desired.
