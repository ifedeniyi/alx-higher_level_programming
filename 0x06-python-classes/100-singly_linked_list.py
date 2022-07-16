#!/usr/bin/python3
"""This module implements a SinglyLinkedList and Node class"""


class Node:
    """Defines a Node for a singly linked list

    Arguments:
        data (int): value of a linked list node.
        next_node (Node): Pointer to the next node of a linked list.
    """

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """int: data of a linked list node"""

        return self.__data

    @data.setter
    def data(self, data):
        if type(data) is not int:
            raise TypeError("data must be an integer.")

        self.__data = data

    @property
    def next_node(self):
        """Node: Pointer to the Next node of a linked list"""

        return self.__next_node

    @next_node.setter
    def next_node(self, next_node):
        if type(next_node) != Node and next_node is not None:
            raise TypeError("next_node must be a Node object")

        self.__next_node = next_node


class SinglyLinkedList:
    """Defines a Singly linked list"""

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new Node into linked list in descending order"""

        new_node = Node(value)

        if self.__head is None:
            self.__head = new_node
            return

        ptr = self.__head
        prev = ptr

        while(True):
            if ptr is None:
                # reaches last node without finding greater value
                prev.next_node = new_node
                break

            if ptr.data > value:
                new_node.next_node = ptr

                if ptr == self.__head:
                    self.__head = new_node
                else:
                    prev.next_node = new_node

                break

            if prev != ptr:
                prev = prev.next_node
            ptr = ptr.next_node

    def __str__(self):
        final_str = ""
        ptr = self.__head

        while(ptr):
            final_str += str(ptr.data)
            ptr = ptr.next_node
            if ptr is not None:
                final_str += '\n'

        return final_str
