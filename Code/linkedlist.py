#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return f'Node({self.data})'


class LinkedList:

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __repr__(self):
        """Return a string representation of this linked list."""
        ll_str = ""
        for item in self.items():
            ll_str += f'({item}) -> '
        return ll_str

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        NOTE: Running time: O(n) Why and under what conditions?
        -> Have to loop through each node to know of its existence to update the count
        and know location, else it may not know what its already looped through"""
        # NOTE: Loop through all nodes and count one for each
        count = 0
        node = self.head
        while node is not None:
            count += 1
            node = node.next
        return count

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        NOTE: Running time: O(???) Why and under what conditions?
        -> Run time: O(1) since there are no loops at all, tail.node is already defined
        so theres no need to loop, its just reassignment and assignment"""
        # NOTE: Create new node to hold given item
        node = Node(item)
        # NOTE: If self.is_empty() == True set the head and the tail to the new node
        if self.is_empty():
            self.head = node
            self.tail = node
        # NOTE: Else append node after tail
        # and make new node the tail node
        else:
            self.tail.next = node
            self.tail = node

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        NOTE: Running time: O(???) Why and under what conditions?
        -> O(1): no loops, just assignment and reassignment"""
        # NOTE: Create new node to hold given item
        node = Node(item)
        # NOTE: Prepend node before head, if it exists
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node

    def find(self, matcher):
        """Return an item from this linked list if it is present.
        NOTE: Best case running time: O(???) Why and under what conditions
        -> O(1): if item is in head, 
        since head and tail already defined simple look up or matching
        NOTE: Worst case running time: O(???) Why and under what conditions?
        -> O(n): if item not in head or tail, and especially if node does not exist,
        must run through each node until found or not found"""
        # NOTE: Loop through all nodes to find item, if present return item, else none
        node = self.head
        while node is not None:
            if matcher(node.data):
                return node.data
            node = node.next
        return None

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(???) Why and under what conditions?
        -> O(1): if item is in head, 
        since head and tail already defined simple look up or matching
        TODO: Worst case running time: O(???) Why and under what conditions?
        -> O(n): if item not in head or tail, and especially if node does not exist,
        must run through each node until found or not found"""
        # TODO: Loop through all nodes to find one whose data matches given item
        prev = None
        node = self.head
        while node is not None:
        # TODO: Update previous node to skip around node with matching data
            if node.data == item:
                if prev:
                    prev.next = node.next
                else:
                    self.head = node.next
                if node.next is None:
                    self.tail = prev
                return
            prev = node
            node = node.next
        # TODO: Otherwise raise error to tell user that delete has failed
        # Hint: raise ValueError('Item not found: {}'.format(item))
        raise ValueError('Item not found: {}'.format(item))
    
    def replace(self, target, item):
        """'Replacing' node data if present, else raise ValueError"""
        prev = None
        node = self.head
        while node is not None:
            if node.data == target:
                new_node = Node(item)
                new_node.next = node.next
                if prev:
                    prev.next = new_node
                else:
                    self.head = new_node
                if node.next is None:
                    self.tail = new_node
                return
            prev = node
            node = node.next
        raise ValueError('Item not found: {}'.format(item))

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
