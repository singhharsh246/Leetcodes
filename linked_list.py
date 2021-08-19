"""
This is an example of linked list implementation in Python.
I have tried to include (from various sources) all possible function one might
need to write a basic linked list function in Python.
Source = https://realpython.com/linked-lists-python/
"""

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def traverse(self, starting_point=None):
        if starting_point is None:
            starting_point = self.head
        node = starting_point
        while node is not None and (node.next != starting_point):
            yield node
            node = node.next
        yield node

    def print_list(self, starting_point=None):
        nodes = []
        for node in self.traverse(starting_point):
            nodes.append(str(node))
        print(" -> ".join(nodes))


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None ## only if we want a doubly linked list

    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def add_first(self, node):
        node.next = self.head
        self.head = node

    def add_last(self, node):
        if self.head is None:
            self.head = node
            self.next = None
            return

        for current_node in self:
            pass ## iterate to the last node ##

        # once we have reached the end
        current_node.next = node

    def add_after(self, target_node_data, new_node):

        if self.head is None:
            raise Exception("List is empty")

        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return

        raise Exception("Node with data '%s' not found" % target_node_data)

    def add_before(self, target_node_data, new_node):

        if self.head is None:
            raise Exception("list is empty")

        if self.head.data == target_node_data:
            return self.add_first(new_node)

        prev_node = self.head

        for node in self:
            if node.data == target_node_data:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node

        raise Exception("Node with data '%s' not found" % target_node_data)

    def remove_node(self, target_node_data):
        if self.head is None:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            self.head = self.head.next
            return

        previous_node = self.head
        for node in self:
            if node.data == target_node_data:
                previous_node.next = node.next
                return
            previous_node = node

        raise Exception("Node with data '%s' not found" % target_node_data)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

llist = LinkedList()
print(llist)

first_node = Node("a")
llist.head = first_node
print(llist)

second_node = Node("b")
third_node = Node("c")
first_node.next = second_node
second_node.next = third_node
print(llist)

### adding head element  ###
llist.add_first(Node("z"))

print(llist)
print(llist.head.data)
print(llist.head.next)
print(llist.head.next.next)
print(llist.head.next.next.next)

llist.add_last(Node("l"))

print(llist)

llist.add_after("z", Node("ll"))

print(llist)

for node in llist:
    print(node, node.next)
