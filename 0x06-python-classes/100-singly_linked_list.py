#!/usr/bin/python3
"""Defines a node of a singly linked list"""


class Node:
    """Represent node of linked list"""
    def __init__(self, data, next_node=None):
        """constructor"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get/set data property"""
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get/set next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node):
            if value is not None:
                raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represent a singly linked list"""

    def __init__(self):
        """constructor"""
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a new Node into the correct sorted position in the list"""
        newnode = Node(value)
        if self.__head is None:
            self.__head = newnode
        elif self.__head.data > newnode.data:
            newnode.next_node = self.__head
            self.__head = newnode
        else:
            tmp = self.__head
            while tmp.next_node is not None:
                if newnode.data >= tmp.data and \
                        newnode.data <= tmp.next_node.data:
                    newnode.next_node = tmp.next_node
                    tmp.next_node = newnode
                    break
                tmp = tmp.next_node
            if tmp.next_node is None:
                tmp.next_node = newnode

    def __str__(self):
        """Print the list"""
        elements = []
        current = self.__head
        while current:
            elements.append(str(current.data))
            current = current.next_node
        return "\n".join(elements)
