class Node(object):
    def __init__(self, data = None):
        # Initialize node + data + next properties
        # self.text = None
        self.prev = None
        self.data = data
        self.next = None

    def __repr__(self):
        # string representation of this.node.text
        return 'Node({!r})'.format(self.data)

class LinkedList(object):
    # ********** INHERETED CLASS METHODS **********
    def __init__(self, items=None):
        # Initialize linkedlist with property items
        # each item is a node

        self.head = None  # First node
        self.tail = None  # Last node
        self.size = 0     # Size of entire LinkedList

        if items is not None:
            for item in items:
                self.append(Node(item)) # Add each node to LinkedList

    def __str__(self):
        """Return a formatted string representation of this linitemed list."""
        # create array of node items in this.linkedlist
        items = ['({!r})'.format(item) for item in self.items()]
        # 'item' is a funny word
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []
        node = self.head
        while node is not None:
            items.append(node.data)
            node = node.next
        return items

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        # resource for getting length of LL
        return self.size

    #*********** DEV CREATED CLASS METHODS ***************
    def append(self, item) :
        # item = item.text
        node = Node(item)
        if self.tail is not None:
            node.prev = self.tail
            node.prev.next = node
            self.tail = node
        else :
            self.head = node
            self.tail = node
        self.size += 1

    def prepend(self, item) :
        # variable to carry new node instance to be added
        node = Node(item)
        # node.data = str(item)
        if self.head is not None :
            # manipulate head of LL so that:
                # old LL head is set at current node.next
                # old LL head.prev is set to current NEW node
                # current node being added is set as LL head
            node.next = self.head
            node.next.prev = node
            self.head = node
        else :
            # no manipulation just add the damn thing as the head
            self.head = node
            self.tail = node
            node.next = None;

        self.size += 1

    def find(self, item):
        # lets start at the head of LL
        p = self.head
        if p is not None:
            if p.data == item:
                # listen... if we found it on the first try @self.head.data:
                # just gimme the damn thing
                return p
            while p.next is not None:
                if p.data == item:
                    return p
                # else move on to the next one.
                p = p.next
        # else
        return None

    def delete(self, item):
        if self.find(item) == None:
            raise (ValueError)
        if item == None:
            temp = false
        if item == self.head:
            # yay... lets just make this easy on everyone
            temp = item
            # temporary storage for item
            item.next.prev = item.prev
            # next item's pointer for prev needs to be this items prev
            # what is the head's prev? None? Depends(?). Of course.
            self.head = item.next
            # reset the head :+1

        # if item == self.tail:
        #     temp = item
        # NVM this kinda doesn't matter b/c tail.next points somewhere over the rainbow.
        # but i guess we should reset the LL.tail to sumn right?
        if item == self.tail:
            # item.next.prev = item.prev
            temp = item
            self.tail = item.prev

        else:
            temp = item
            item.prev.next = item.next
            item.next.prev = item.prev

        del temp;
        return;
    # QUICK story... I started by writing the logic for
    # how this would be implemented at larger scale calling
    # self.search and what not, then after some headache inducing
    # abstraction I realized that this really just needs to do one
    # MF'in thing... just one. #SeparationOfConcerns


    # def is_empty(self):
    #     if not self.head:
    #         return True
    #     else
    #         return False

    # def prepend(self, data):
    #
    #     new_node = Node(data)
    #
    #     if not self.head:

    # later TODO:
# def test_delete_with_3_items(self):
#     ll = LinkedList(['A','B','C'])
#     assert ll.find(lambda item: item == 'B') == 'B'
#     #Match Equlity
#     #Match Less Than
#     #Match Greater Than
#     #No Matching Item
#
def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
