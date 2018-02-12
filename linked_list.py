class Node(object):
    def __init__(self, data = None):
        self.data = None
        self.next = None
    def __repr__(self):
        return 'Node({!r})'.format(self.data)

class Linked_list(object):

    def __init__(self, items=None):
        self.head = None  # First node
        self.tail = None  # Last node
        self.size = 0
        if items is not None:
            for item in items:
                self.append(item)

    def is_empty(self):
        if not self.head:
            return True
        else
            return False

    # def prepend(self, data):
    #
    #     new_node = Node(data)
    #
    #     if not self.head:

# later TODO:
def test_delete_with_3_items(self):
    ll = LinkedList(['A','B','C'])
    assert ll.find(lambda item: item == 'B') == 'B'
    #Match Equlity
    #Match Less Than
    #Match Greater Than
    #No Matching Item
