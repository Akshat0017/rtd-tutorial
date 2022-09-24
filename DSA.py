################################## Data Structures ################################

# ------------------------------- Singly Linked List -----------------------------


class SinglyLinkedListNode:
    """| This class is used to implement the SinglyLinkedNode structure 
    | List of Member Functions:

    * __init__(self, data)
    * __str__(self)
    
    """

    def __init__(self, data):
        """This is a constructor for the Class SInglyLinkedListNode

        :param data: Value of the node
        :type data: int

        :Example:
            >>> from DSA import SinglyLinkedListNode
            >>> l=SinglyLinkedListNode(4)
            >>> print(l.data)
            4
            >>> print(l.next)
            None
        """
        self.data = data
        self.next = None

    def __str__(self):
            
        """This a constructor for the Class Singly Linked List which is called when we want to print the object class
        :Example:
            >>> from DSA import SinglyLinkedListNode
            >>> l=SinglyLinkedListNode(4)
            >>> print(l)
            4
        """
        return str(self.data)

        


class SinglyLinkedList:
    """| This class is used to implement the SinglyLinkedList structure
    | List of Member Functions:

    * __init__(self, data)
    * insert(self, data)
    * find(self, data)
    * deleteVal(self, data)
    * printer(self, sep=', ')
    * reverse(self)

    """

    def __init__(self):
        """This is a constructor for the Class SInglyLinkedList setting the head and tail to none

        :Example:
            >>> from DSA import SinglyLinkedList
            >>> l=SinglyLinkedList()
            >>> print(l.head)
            None
            >>> print(l.tail)
            None
        """
       
        self.head = None
        self.tail = None

    def insert(self, data):
        """This Function is used to insert data into Linked Listby creating a node and updating head and tail values

        :param data: value of the node to be inserted
        :type data: int

        :Example:
            >>> from DSA import SinglyLinkedList
            >>> l=SinglyLinkedList()
            >>> l.insert(1)
            >>> print(l.head)
            1
            >>> print(l.tail)
            1
        """

        node = SinglyLinkedListNode(data)  # new node
        if not self.head:  # no head
            self.head = node
        else:
            self.tail.next = node  # add behind tail
        self.tail = node  # move tail

    def find(self, data):
        """This Function is used to find a particular element in a Linked List by matching values till match is found or head is none

        :param data: value of the element to be found
        :type data: int

        :return: returns the node prev to the element searched & if node is not present it returns the tail of the node
        :rtype: int

        :Example:
            >>> from DSA import SinglyLinkedList
            >>> l=SinglyLinkedList()
            >>> l.insert(1)
            >>> l.insert(2)
            >>> l.insert(3)
            >>> print(l.find(2))
            1
        """
        head = self.head
        prev = None
        while head != None and head.data != data:
            prev = head
            head = head.next
        return prev

    def deleteVal(self, data):
        """This Function is used to delete a particular element in a Linked List by finding the element using find function annd updating the head an prev values

        :param data: value of the element to be found
        :type data: int

        :return: True is found & deleted else false
        :rtype: bool

         :Example:
            >>> from DSA import SinglyLinkedList
            >>> l=SinglyLinkedList()
            >>> l.insert(1)
            >>> l.insert(2)
            >>> l.insert(3)
            >>> print(l.deleteVal(2))
            True
        """
        prevPos = self.find(data)
        if prevPos == None:
            self.head=self.head.next
        else:
            if prevPos.next == None:
                return False
            prevPos.next = prevPos.next.next
        return True

    def printer(self, sep=', '):
        """This Function is used to find print the Linked List by traversing the linked list till the node becomes null.

        :param sep: seperator used to seperate the nodes while printing
        :type data: string

        :Example:
            >>> from DSA import SinglyLinkedList
            >>> l=SinglyLinkedList()
            >>> l.insert(1)
            >>> l.insert(2)
            >>> l.insert(3)
            >>> l.printer()
            [1, 2, 3]
        """
        ptr = self.head
        print('[', end='')
        while ptr != None:
            print(ptr, end='')
            ptr = ptr.next
            if ptr != None:
                print(sep, end='')
        print(']')

    def reverse(self):
        """This Function is used to reverse Linked List by switching the head and tail values of a particular node till head becomes null.
        
        :Example:
            >>> from DSA import SinglyLinkedList
            >>> l=SinglyLinkedList()
            >>> l.insert(1)
            >>> l.insert(2)
            >>> l.insert(3)
            >>> l.reverse()
            >>> l.printer()
            [3, 2, 1]
        """
        head = self.head  # head pointer
        prev = None  # previous pointer
        while head != None:  # while there is forward link left
            newHead = head.next  # save extra pointer to next element
            head.next = prev  # reverse the link of current element
            prev = head  # move pointer to previous element
            head = newHead  # use extra pointer to move to next element
        self.tail = self.head
        self.head = prev


def merge(list1, list2):
    """This Function is used to merge to linked list by creating the a empty list and then comparing the values of list1 and list2 and inserting lower value into the merged.

        :param list1: list which has to be merged.
        :type list1: SinglyLinkedList()
        :param list2: list which has to be merged.
        :type list2: SinglyLinkedList()

        :return: merged list of the above 2 list
        :rtype: SinglyLinkedList()

        :Example:
            >>> from DSA import SinglyLinkedList
            >>> from DSA import merge
            >>> l=SinglyLinkedList()
            >>> l.insert(1)
            >>> l.insert(3)
            >>> l.insert(4)
            >>> l2=SinglyLinkedList()
            >>> l2.insert(2)
            >>> l2.insert(5)
            >>> l2.insert(30)
            >>> merge(l,l2).printer()
            [1, 2, 3, 4, 5, 30]
        """
    merged = SinglyLinkedList()
    head1 = list1.head
    head2 = list2.head
    while head1 != None and head2 != None:  # both lists not empty
        if head1.data < head2.data:  # link node with smaller data
            merged.insert(head1.data)
            head1 = head1.next
        else:
            merged.insert(head2.data)
            head2 = head2.next
    if head1 == None and head2 != None:  # list 1 finished
        merged.tail.next = head2  # add remaining list 2 as is
    if head1 != None and head2 == None:  # list 2 finished
        merged.tail.next = head1  # add remaining list 1 as is
    return merged

# ------------------------------ Doubly Linked List ----------------------------


class DoublyLinkedListNode:
    """| This a Class used to implement DoublyLinkedLIstNode structure which can be traversed in both directions
    | List of Member Functions:

    * __init__(self, data)
    * __str__(self)
        """
    

    def __init__(self, data):
        """This is a Contructor of DoublyLinkedListNode setting the values of data,next and prev.
        :param data: value of the node
        :type data: int

        :Example:
            >>> from DSA import DoublyLinkedListNode
            >>> l=DoublyLinkedListNode(4)
            >>> print(l.data)
            4
            >>> print(l.next)
            None
            >>> print(l.prev)
            None
        """
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        """This a constructor for the Class Singly Linked List which is called when we want to print the object class

        :Example:
            >>> from DSA import DoublyLinkedListNode
            >>> l=DoublyLinkedListNode(4)
            >>> print(l.data)
            4
       
        """
        return str(self.data)


class DoublyLinkedList:
    """| This a Class used to implement DoublyLinkedList structure which is a list made of DoublyLinkedList node.
    | List of Member Functions:
    
    * __init__(self, data)
    * insert(self, data)
    * printer(self, sep=', ')
    * reverse(self)
        """

    def __init__(self):
        """This is a Contructor of DoublyLinkedListNode setting the values of head & tail.

        :Example:
            >>> from DSA import DoublyLinkedList
            >>> l=DoublyLinkedList()
            >>> print(l.head)
            None
            >>> print(l.tail)
            None
        """
        self.head = None
        self.tail = None

    def insert(self, data):
        """This Function is used to insert data into Linked Listby creating a node and updating head and tail values

        :param data: value of the node to be inserted
        :type data: int

        :Example:
            >>> from DSA import DoublyLinkedList
            >>> l=DoublyLinkedList()
            >>> l.insert(1)
            >>> print(l.head)
            1
            >>> print(l.tail)
            1
        """
        node = DoublyLinkedListNode(data)  # new node
        if not self.head:  # no head
            self.head = node
        else:
            self.tail.next = node  # add behind tail
            node.prev = self.tail
        self.tail = node  # move tail

    def printer(self, sep=', '):
        """This Function is used to find print the Linked List by traversing the linked list till the node becomes null.

        :param sep: seperator used to seperate the nodes while printing
        :type data: string

        :Example:
            >>> from DSA import DoublyLinkedList
            >>> l=DoublyLinkedList()
            >>> l.insert(1)
            >>> l.insert(2)
            >>> l.insert(3)
            >>> l.printer()
            [1, 2, 3]
        """
        ptr = self.head
        print('[', end='')
        while ptr != None:
            print(ptr, end='')
            ptr = ptr.next
            if ptr != None:
                print(sep, end='')
        print(']')

    def reverse(self):
        """This Function is used to reverse Linked List by switching the head and tail values of a particular node till head becomes null.

        :Example:
            >>> from DSA import DoublyLinkedList
            >>> l=DoublyLinkedList()
            >>> l.insert(1)
            >>> l.insert(2)
            >>> l.insert(3)
            >>> l.reverse()
            >>> l.printer()
            [3, 2, 1]
        """
        head = self.head  # head pointer
        prev = None  # previous pointer
        while head != None:  # new node left
            newHead = head.next  # save pointer to next node (cut forward link)
            if newHead != None:  # check if next node has a reverse link
                # save pointer to previous node (cut reverse link)
                newHead.prev = head
            head.next = prev  # reverse the forward link
            head.prev = newHead  # reverse the reverse link
            prev = head  # move pointer to previous element
            head = newHead  # use saved pointer to move head
        self.tail = self.head
        self.head = prev

# -------------------------- Binary Search Tree ------------------------------


class BSTNode:
    """| This a Class used to implement BSTNode structure which has info, left, right & level attribute.
    | List of Member Functions:
    
    * __init__(self, data)
    * __str__(self)
        """

    def __init__(self, info):
        """This is a Contructor of DoublyLinkedListNode setting the values of info,left,right and level.
        :param info: value of the node
        :type info: int

        :Example:
            >>> from DSA import BSTNode
            >>> l=BSTNode(4)
            >>> print(l.info)
            4
            >>> print(l.left)
            None
            >>> print(l.right)
            None
            >>> print(l.level)
            None
        """
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        """This a constructor for the Class Singly Linked List which is called when we want to print the object class

        :Example:
            >>> from DSA import BSTNode
            >>> l=BSTNode(4)
            >>> print(l)
            4
        """
        return str(self.info)


class BinarySearchTree:
    """| This a Class used to implement BinarySearchTree structure which is a list made of BSTnode.
    | List of Member Functions:

    * __init__(self)
    * insert(self, val)
    * printer(self, sep=', ')
    * traverse(self, order)
    * height(self, root)
    * reverse(self)
       
    """

    def __init__(self):
        """This is a Contructor of DoublyLinkedListNode setting the values of root to null.

        :Example:
            >>> from DSA import BinarySearchTree
            >>> l=BinarySearchTree()
            >>> print(l.root)
            None
        """
        self.root = None

    def insert(self, val):
        """This Function is used to insert data into Tree by creating a node and updating info,left, right and level.

        :param val: value of the node to be inserted
        :type val: int

        :Example:
            >>> from DSA import BinarySearchTree
            >>> l=BinarySearchTree()
            >>> l.insert(1)
            >>> print(l.root)
            1
        """
        if self.root == None:
            self.root = BSTNode(val)
        else:
            current = self.root
            while True:
                if val < current.info:  # move to left sub-tree
                    if current.left:
                        current = current.left  # root moved
                    else:
                        current.left = BSTNode(val)  # left init
                        break
                elif val > current.info:  # move to right sub-tree
                    if current.right:
                        current = current.right  # root moved
                    else:
                        current.right = BSTNode(val)  # right init
                        break
                else:
                    break  # value exists

    def traverse(self, order):
        """This Function is used to traverse through a the Tree using 3 methods based on the value of order

        :param order: dictates the type of traversal
        :type val: int

        :Example:
            >>> from DSA import BinarySearchTree
            >>> l=BinarySearchTree()
            >>> l.insert(2)
            >>> l.insert(1)
            >>> l.insert(3)
            >>> l.traverse('PRE')
            2 1 3 
            >>> l.traverse('IN')
            1 2 3 
            >>> l.traverse('POST')
            1 3 2 
        """

        def preOrder(root):
            """This Function is used trsverse in pre order by traversing through the parent first then the left child followd by the right child.

            :param root: root of the tree to be traversed
            :type val: BSTNode
            """
            print(root.info, end=' ')
            if root.left != None:
                preOrder(root.left)
            if root.right != None:
                preOrder(root.right)

        def inOrder(root):
            """This Function is used trsverse in in order by traversing through the left child, then the parent followd by the right child.

            :param root: root of the tree to be traversed
            :type val: BSTNode
            """
            if root.left != None:
                inOrder(root.left)
            print(root.info, end=' ')
            if root.right != None:
                inOrder(root.right)

        def postOrder(root):
            """This Function is used trsverse in post order by traversing through the left child first then the right child followd by the parent.

            :param root: root of the tree to be traversed
            :type val: BSTNode
            """
            if root.left != None:
                postOrder(root.left)
            if root.right != None:
                postOrder(root.right)
            print(root.info, end=' ')
        if order == 'PRE':
            preOrder(self.root)
        elif order == 'IN':
            inOrder(self.root)
        elif order == 'POST':
            postOrder(self.root)

    def height(self, root):
        """This Function is used find of the height by recursively calling the height function till we reach null node

            :param root: root of the tree to be traversed
            :type val: BSTNode

            :Example:
                >>> from DSA import BinarySearchTree
                >>> l=BinarySearchTree()
                >>> l.insert(2)
                >>> l.height(l.root)
                0
                >>> l.insert(1)
                >>> l.height(l.root)
                1
                >>> l.insert(3)
                >>> l.height(l.root)
                1
        """
        if root.left == None and root.right == None:
            return 0
        elif root.right == None:
            return 1 + self.height(root.left)
        elif root.left == None:
            return 1 + self.height(root.right)
        else:
            return 1 + max(self.height(root.left), self.height(root.right))

# --------------------------------- Suffix Trie --------------------------------


class Trie:
    """| This a Class used to implement Suffix Trie structure which is used to store words in a Trie
    | List of Member Functions:

    * __init__(self)
    * find(self, root, c)
    * insert(self, s)
    * checkPrefix(self, s)
    * countPrefix(self, s)
        """

    def __init__(self):
        """This is a Contructor of Suffix Trie creating a empty dictionary.

        :Example:
            >>> from DSA import Trie
            >>> l=Trie()
            >>> print(l.T)
            {}
        """

        self.T = {}

    def find(self, root, c):
        """This function finds a particular element in a trie by giving the element and trie

        :param root: the dictionary storing the trie
        :type root: dictionary
        :param c: character to be searched
        :type c: string

        :return: true if found else false
        :rtype: bool

        :Example:
            >>> from DSA import Trie
            >>> l=Trie()
            >>> l.insert("apple")
            >>> l.find(l.T,"a")
            True
            >>> l.find(l.T,"p")
            False
            >>> l.insert("pear")
            >>> l.find(l.T,"p")
            True
        """
        return (c in root)

    def insert(self, s):
        """This function insert a particular word in a trie by finding its charater in the trie and updating the Trie

        :param s: word to be added
        :type s: string

        :Example:
            >>> from DSA import Trie
            >>> l=Trie()
            >>> l.insert("apple")
            >>> print(l.T)
            {'a': {'#': 1, 'p': {'#': 1, 'p': {'#': 1, 'l': {'#': 1, 'e': {'#': 1}}}}}}
        """
        root = self.T
        for c in s:
            if not self.find(root, c):
                root[c] = {}
            root = root[c]
            root.setdefault('#', 0)
            root['#'] += 1

    def checkPrefix(self, s):
        """This function checks if a particular prefix is presen in the Trie or not.

        :param s: prefix to be checked in the Trie
        :type s: string

        :return: true if found else false
        :rtype: bool

        :Example:
            >>> from DSA import Trie
            >>> l=Trie()
            >>> l.insert("apple")
            >>> l.checkPrefix("app")
            True
            >>> l.find(l.T,"apl")
            False
        """
        root = self.T
        for idx, char in enumerate(s):
            if char not in root:
                if idx == len(s) - 1:
                    root[char] = '#'
                else:
                    root[char] = {}
            elif root[char] == '#' or idx == len(s) - 1:
                return True
            root = root[char]
        return False

    def countPrefix(self, s):
        """This function counts the number of times a particular prefix is present in the Trie or not by going till the last charater and return the default value of that dictionary

        :param s: prefix to be checked in the Trie
        :type s: string

        :return: 0 if not present else returns the number of times that string has been executed
        :rtype: bool

        :Example:
            >>> from DSA import Trie
            >>> l=Trie()
            >>> l.insert("apple")
            >>> l.countPrefix("app")
            1
            >>> l.insert("approx")
            >>> l.countPrefix("app")
            2
        """
        found = True
        root = self.T
        for c in s:
            if self.find(root, c):
                root = root[c]
            else:
                found = False
                break
        if found:
            return root['#']
        return 0
