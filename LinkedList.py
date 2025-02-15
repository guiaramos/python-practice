class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    ### Traversing Linked List Items ###
    def traverse_list(self):
        if self.head is None:
            print('list has no element')
            return
        else:
            node = self.head
            while node is not None:
                print(node.data, ' ')
                node = node.next

    ### function for creating list ###
    def make_new_list(self):
        qtd = int(input('How many nodes do you want to create: '))
        if qtd == 0:
            return
        for i in range(qtd):
            data = int(input('Enter the value for the node:'))
            self.insert_at_end(data)

    ### Inserting Items ###
    # Inserting Items at the Beginning
    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Inserting Item at the End
    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        node = self.head

        while node.next is not None:
            node = node.next

        node.next = new_node

    # Inserting item after another item
    def insert_after_item(self, target, data):
        node = self.head

        while node is not None:
            if node.data == target:
                break
            node = node.next

        if node is Node:
            print('item not in the list')
        else:
            new_node = Node(data)
            new_node.next = node.next
            node.next = new_node

    # Inserting item before another item
    def insert_before_item(self, target, data):
        if self.head is None:
            print('list has no element')
            return

        if target == self.head.data:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            return

        node = self.head
        while node.next is not None:
            if node.next.data == target:
                break
            node = node.next

        if node.next is None:
            print('item not in the list')
        else:
            new_node = Node(data)
            new_node.next = node.next
            node.next = new_node

    # insert item at Specific Index
    def insert_at_index(self, index, data):
        if index == 1:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            return

        i = 1
        node = self.head
        while i < index-1 and node is not None:
            node = node.next
            i = i+1

        if node is None:
            print('index out of bound')
        else:
            new_node = Node(data)
            new_node.next = node.next
            node.next = new_node

    ### Counting Elements ###
    def get_len(self):
        if self.head is None:
            return 0

        node = self.head
        count = 0
        while node is not None:
            count = count + 1
            node = node.next

        return count

    ### Searching Elements ###
    def search_item(self, data):
        if self.head is None:
            print('list has no elements')
            return

        node = self.head
        while node is not None:
            if node.data == data:
                return true
            node = node.next

        return false

    ### Deleting Elements ###
    # Delete from the start
    def delete_at_start(self):
        if self.head is None:
            print('The list has no element to delete')
            return
        self.head = self.head.next

    # Delete at the end
    def delete_at_end(self):
        if self.head is None:
            print('The list has no element to delete')
            return

        node = self.head
        while node.next.next is not None:
            node = node.next

        node.next = None

    # Delete by item value
    def delete_by_value(self, data):
        if self.head is None:
            print('The list has no element to delete')
            return

        # Deleting first node
        if self.head.data == data:
            self.head = self.head.next
            return

        node = self.head
        while node.next is not None:
            if node.next.data == x:
                break
            node = node.next

        if node.next is None:
            print('item not found in the list')
        else:
            node.next = node.next.next

    # Reversing a Linked List
    def reverse_list(self):
        prevNode = None
        node = self.head

        while node is not None:
            nextNode = node.next
            node.next = prevNode
            prev = node
            node = nextNode

        self.head = prevNode
