''' Create a linked list class for RC Start Codjo: https://github.com/reeddunkle/Codjo/tree/master/Problem4_Linked_List. By Lin and Khalid.'''
class Node(object):
    def __init__(self, value):
        self.data = value
        self.next_node  = None


class LinkedList(object):
    def __init__(self, value=None):
        self.head = Node(value)


    # def __repr__(self):
    #     if self.head.data == None:
    #         return "[*None]"
    #     else:
    #         rep = "[*" + str(self.head.data) + "]"
    #         pointer = self.head.next_node
    #         while pointer:
    #             rep = rep + "->[" + str(pointer.data) + "]"
    #             pointer = pointer.next_node
    #         return rep


    def append(self, value):
        if self.head.data == None:
            self.head = Node(value)
            return self

        prev_head = self.head  # Track previous head
        self.head = Node(value)  # Create new head
        self.head.next_node = prev_head  # Point to previous head
        return self


    def __len__(self):
        '''Calculate the size of the linked list, by traversing the linked list till the tail node (i.e. next_node is None)'''

        count = 0
        pointer = self.head.next_node

        if pointer == None:  # Return 0 if the value of the node is None, otherwise, return 1
            if self.head.data:
                return 1
            else:
                return 0

        while pointer:
            count += 1
            pointer = pointer.next_node
        return count + 1


    def __getitem__(self, index, node=False):
        #if the index is larger than the length -1, raise IndexError
        if index > self.__len__() - 1:
            raise IndexError

        if index == 0:
            if not node:
                return self.head.data
            else:
                return self.head

        track = 1
        pointer = self.head.next_node

        while track != index:
            pointer = pointer.next_node
            track += 1
        if not node:
            return pointer.data
        else:
            return pointer


    def __delitem__(self, index):
        if index > self.__len__() - 1:
            raise IndexError

        if index == 0:  # Replace the head with the head's next_node, if the index is 0
            self.head = self.__getitem__(1, True)
            return self

        if index == self.__len__() - 1:  # Replace the 2nd last node's next_node to None, if the given index is the tail
            self.__getitem__(index - 1, True).next_node = None
            return self

        self.__getitem__(index - 1, True).next_node = self.__getitem__(index + 1, True)  # Get the previous node, and set its next_node to the next node of this index node
        return self


    def pop(self):
        ''' Pop head node off and reset pointer to the next node '''
        if self.head.data == None:
            raise IndexError

        old_head = self.head
        self.head = self.head.next_node
        return old_head
