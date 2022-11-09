class Node:
    def __init__(self, data):
        """ Store the data, and set next to None"""
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        """ Return a string representation of the data """
        return self.data


class Storage:
    def __init__(self):
        """ Creates an empty Storage class. Sets head to None. """
        self.head = None
        self.tail = None

    def __str__(self):
        node = self.head
        my_str = ""

        while node is not None:
            my_str += f"{node.data} -> "
            node = node.next

        my_str += "None"
        return my_str

    def push(self, data):
        """ Create a Node to hold the data, then put it at the head of the list. """
        new_node = Node(data)

        if self.head is None or self.tail is None:
            # List was empty
            self.head = new_node
            self.tail = new_node
        else:
            # List is not empty, just add the node to the end
            self.head.prev = new_node
            self.tail = new_node


    def pop(self):
        """ Remove the head Node and return its data. """

    def peek(self):
        """ Return the data from the head Node, without removing it. """

    def isempty(self):
        """ Return True if the list is empty, otherwise False """

if __name__ == '__main__':
    stor = Storage()
    print(stor)

    stor.push(1)
    print(stor)

    stor.push(5)
    print(stor)