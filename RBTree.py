from display_RBTree import *
from RBNode import *


class RBTree:
    """
    this is tree with
    """

    def __init__(self):
        self.sentry = Sentry()
        self.root = None
        self.tree_size = 0


    def get_tree_size(self):
        return self.tree_size

    def insert(self, key:int, data):
        """
        inserts key and value into the red-black tree
        :param key:
        :param value:
        :return: None
        """
        self.sentry.size = 0
        self.sentry.left, self.sentry.right, self.sentry.parent = self.sentry, self.sentry, self.sentry
        self.tree_size += 1
        new_node = RBNode(key, data, self.sentry)

        if self.root is None:
            self.root = new_node
            self.root.color = Color.BLACK
            self.root.parent = self.sentry
            return

        # insert like BST, happened only if size > 0
        y_node = None
        x_node = self.root
        while not x_node.isSentry():
            y_node = x_node
            y_node.size += 1
            x_node = x_node.left if x_node > new_node else x_node.right

        new_node.parent = y_node
        # if y_node.isSentry(): # empty tree
        #     self.root = new_node
        if new_node < y_node:
            y_node.left = new_node
        else:
            y_node.right = new_node
        self._insert_fixup(new_node)




    def search(self, key):
        """

        :param key:
        :return: array of the nodes with the given key
        """
        x_node = self.root
        while not x_node.isSentry():
            if x_node.key == key:
                return x_node
            x_node = x_node.left if x_node.key > key else x_node.right



    def delete(self, z_node: RBNode):
        """
        removes node from red-black tree. (correcting the field size)
        :param z_node: RBNode
        :return: the node with the given key and value if it exists, else None
        """
        if z_node is None or z_node.isSentry():
            return
        # fixing sentry
        self.sentry.size = 0
        self.sentry.left, self.sentry.right, self.sentry.parent = self.sentry, self.sentry, self.sentry
        self.tree_size -= 1

        self._size_delete_fixup(z_node)
        if z_node.left.isSentry() or z_node.right.isSentry():
            y_node = z_node
        else:
            y_node = self.successor(z_node)
        x_node = y_node.left if not y_node.left.isSentry() else y_node.right
        x_node.parent = y_node.parent

        if y_node.parent.isSentry():
            self.root = x_node
        elif y_node is y_node.parent.left:
            y_node.parent.left = x_node
        else:
            y_node.parent.right = x_node

        if y_node is not z_node:
            y_node.exchange_key_data(z_node)

        if y_node.color == Color.BLACK:
            self._delete_fixup(x_node)
        return y_node


    def successor(self, x_node):
        """
        returns the successor of the given node
        :param x_node: RBNode
        :return: RBNode
        """
        if not x_node.right.isSentry():
            return self.minimum(x_node.right)
        y_node = x_node.parent
        while not y_node.isSentry() and x_node is y_node.right:
            x_node = y_node
            y_node = y_node.parent
        return y_node if not y_node.isSentry() else self.maximum()



    def predecessor(self, x_node):
        """
        returns the predecessor of the given node
        :param x_node: RBNode
        :return:RBNode
        """
        if not x_node.left.isSentry():
            return self.maximum(x_node.left)
        y_node = x_node.parent
        while not y_node.isSentry() and x_node is y_node.left:
            x_node = y_node
            y_node = y_node.parent
        return y_node if not y_node.isSentry() else self.minimum(x_node)


    def minimum(self, x_node = None):
        """
        returns the minimum node
        :param x_node: RBNode. by default its the root of the tree. optional => for getting the minimum in sub tree
        :return: RBNode or None
        """
        x_node = self.root if x_node is None else x_node
        while not x_node.left.isSentry():
            x_node = x_node.left
        return x_node


    def maximum(self, x_node = None):
        """
        :param x_node: optional. to get the maximum in sub tree
        :return:
        """
        x_node = self.root if x_node is None else x_node
        while not x_node.right.isSentry():
            x_node = x_node.right
        return x_node



    def select(self, i:int = 0, x_node = None):
        """
        return the node with the given index, (the smallest node). the indexes started from 1 -> tree_size() (including both)
        :param i: index (rank)
        :return: Node with given index (not deleting it!)
        """
        if x_node is None:
            x_node = self.root
        index = x_node.left.size + 1
        if i == index:
            return x_node
        elif i < index:
            if x_node.left.isSentry():
                raise Exception("index out of range, your index is bigger then the size of the tree")
            return self.select(i, x_node.left)
        else:
            if x_node.right.isSentry():
                raise Exception("index out of range, your index is smaller than 1")
            return self.select(i - index, x_node.right)


    def rank(self, x_node = None):
        """
        return the rank (index) of node if the Nodes were sorted
        :param x_node: RBNode
        :return: its rank / index if the Nodes were sorted
        """
        if type(x_node) != RBNode:
            raise Exception("x_node is not RBNode")

        index = x_node.left.size + 1
        y_node = x_node
        while y_node is not self.root:
            if y_node is y_node.parent.right:
                index = index + y_node.parent.left.size + 1
            y_node = y_node.parent
        return index


    def display(self):
        display_tree(self.root)

# private

    def _right_rotate(self, x_node):
        y_node = x_node.left
        x_node.left = y_node.right
        if not y_node.right.isSentry():
            y_node.right.parent = x_node
        y_node.parent = x_node.parent
        if x_node.parent.isSentry():
            self.root = y_node
        elif x_node is x_node.parent.right:
            x_node.parent.right = y_node
        else:
            x_node.parent.left = y_node
        y_node.right = x_node
        x_node.parent = y_node
        y_node.size = x_node.size
        x_node.size = x_node.left.size + x_node.right.size + 1

    def _left_rotate(self, x_node):
        y_node = x_node.right
        x_node.right = y_node.left
        if not y_node.left.isSentry():
            y_node.left.parent = x_node
        y_node.parent = x_node.parent
        if x_node.parent.isSentry():
            self.root = y_node
        elif x_node is x_node.parent.left:
            x_node.parent.left = y_node
        else:
            x_node.parent.right = y_node
        y_node.left = x_node
        x_node.parent = y_node
        y_node.size = x_node.size
        x_node.size = x_node.left.size + x_node.right.size + 1



    def _insert_fixup(self, new_node):
        # correct the tree according the RBTree conditions
        while new_node.parent.color == Color.RED:
            if new_node.parent is new_node.parent.parent.left:
                node = new_node.parent.parent.right
                # case 1
                if node.color == Color.RED:
                    new_node.parent.color = Color.BLACK
                    node.color = Color.BLACK
                    new_node.parent.parent.color = Color.RED
                    new_node = new_node.parent.parent
                else:
                    # case 2
                    if new_node is new_node.parent.right:
                        new_node = new_node.parent
                        self._left_rotate(new_node)
                    # case 3
                    new_node.parent.color = Color.BLACK
                    new_node.parent.parent.color = Color.RED
                    self._right_rotate(new_node.parent.parent)
            else:
                node = new_node.parent.parent.left
                # case 1
                if node.color == Color.RED:
                    new_node.parent.color = Color.BLACK
                    node.color = Color.BLACK
                    new_node.parent.parent.color = Color.RED
                    new_node = new_node.parent.parent
                else:
                    # case 2
                    if new_node is new_node.parent.left:
                        new_node = new_node.parent
                        self._right_rotate(new_node)
                    # case 3
                    new_node.parent.color = Color.BLACK
                    new_node.parent.parent.color = Color.RED
                    self._left_rotate(new_node.parent.parent)
            self.root.color = Color.BLACK


    def _delete_fixup(self, x_node):
        while x_node is not self.root and x_node.color == Color.BLACK and x_node is not self.sentry:
            if x_node is x_node.parent.left:
                w_node = x_node.parent.right
                if w_node.color == Color.RED:
                    w_node.color = Color.BLACK
                    x_node.parent.color = Color.RED
                    self._left_rotate(x_node.parent)
                    w_node = x_node.parent.right
                if w_node.left.color == Color.BLACK and w_node.right.color == Color.BLACK:
                    w_node.color = Color.RED
                    x_node = x_node.parent
                else:
                    if w_node.right.color == Color.BLACK:
                        w_node.left.color = Color.BLACK
                        w_node.color = Color.RED
                        self._right_rotate(w_node)
                        w_node = x_node.parent.right
                    w_node.color = x_node.parent.color
                    x_node.parent.color = Color.BLACK
                    w_node.right.color = Color.BLACK
                    self._left_rotate(x_node.parent)
                    x_node = self.root
            else:
                w_node = x_node.parent.left
                if w_node.color == Color.RED:
                    w_node.color = Color.BLACK
                    x_node.parent.color = Color.RED
                    self._right_rotate(x_node.parent)
                    w_node = x_node.parent.left
                if w_node.right.color == Color.BLACK and w_node.left.color == Color.BLACK:
                    w_node.color = Color.RED
                    x = x_node.parent
                else:
                    if w_node.left.color == Color.BLACK:
                        w_node.right.color = Color.BLACK
                        w_node.color = Color.RED
                        self._left_rotate(w_node)
                        w_node = x_node.parent.left
                    w_node.color = x_node.parent.color
                    x_node.parent.color = Color.BLACK
                    w_node.left.color = Color.BLACK
                    self._right_rotate(x_node.parent)
                    x_node = self.root
        x_node.color = Color.BLACK


    def _size_delete_fixup(self, x_node):
        """
        corrct the size field of all nodes that x_node are their grand_child
        :param x_node:
        :return: None
        """
        while x_node is not self.sentry:
            x_node = x_node.parent
            x_node.size -= 1


