class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Traversing Linked List Items
    def traverse_list(self):
        if self.head is None:
            print('list has no element')
            return
        else:
            node = self.head
            while node is not None:
                print(node.data, ' ')
                node = node.next

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

        if target == self.head.data:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

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

        i = 1
        node = self.head
        while i < index-1 and node is not None:
            node = node.next
            i = i+1

        if node is None:
            print("index out of bound")
        else:
            new_node = Node(data)
            new_node.next = node.next
            node.next = new_node

    # Counting Elements
    def get_len(self):
        if self.head is None:
            return 0

        node = self.head
        count = 0
        while node is not None:
            count = count + 1
            node = node.next

        return count
