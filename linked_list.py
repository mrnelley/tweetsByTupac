class Node(object):
    """docstring for Node."""
    def __init__(self, data = None):
        self.data = None
        self.next = None

class linked_list(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        if not self.head:
            return True
        else
            return False

    def append(self, data):

        new_node = Node(data)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, data):

        new_node = Node(data)

        if not self.head:

# later TODO:
def test_delete_with_3_items(self):
    ll = LinkedList(['A','B','C'])
    assert ll.find(lambda item: item == 'B') == 'B'
    #Match Equlity
    #Match Less Than
    #Match Greater Than
    #No Matching Item
