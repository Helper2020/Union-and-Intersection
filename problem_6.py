class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

    def __iter__(self):
        self.node = self.head
        return self

    def __next__(self):
        if self.node:
            value = self.node.value
            self.node = self.node.next
            return value
        else:
            raise StopIteration


def union(llist_1, llist_2):
    # Your Solution Here
    set1 = set(llist_1)  # O(n)
    set2 = set(llist_2)  # O(n)
    lists_union = set1.union(set2)  # O(len(s1) + len(s2))

    new_list = LinkedList()
    for element in lists_union:  # O(n)
        new_list.append(element)

    return new_list


def intersection(llist_1, llist_2):
    # Your Solution Here
    set1 = set(llist_1)  # O(n)
    set2 = set(llist_2)  # O(n)

    lists_intersect = set1.intersection(set2)  # O(min(len(s1), len(s2))

    if len(lists_intersect) == 0:
        return f'Sets do not intersect'

    new_list = LinkedList()
    for element in lists_intersect:
        new_list.append(element)

    return new_list


def test_functions(func, list_1, list_2):
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    for i in list_1:
        linked_list_1.append(i)

    for i in list_2:
        linked_list_2.append(i)

    return func(linked_list_1, linked_list_2)


print('------------------- Test Case 1 -----------------')
list_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
list_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

# Union test
print(test_functions(union, list_1, list_2))
# Should print 1,2,3,4,6,9,11,21,32,35,36
# Intersect test
print(test_functions(intersection, list_1, list_2))
# 4,6,21

print('------------------- Test Case 2 -----------------')

list_3 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
list_4 = [1, 7, 8, 9, 11, 21, 1]
# Union test
print(test_functions(union, list_3, list_4))
# Should print 1,2,3,4,6,9,11,21,32,35,36
# Intersect test
print(test_functions(intersection, list_3, list_4))
# sets do not intersect

print('------------------- Test Case 3 -----------------')
# Case where one set is empty

list_5 = []
list_6 = [1, 7, 8, 9, 11, 21, 1]

print(union(list_5, list_6))
# Should print 1-21-7-8-9-11
print(intersection(list_5, list_6))
# Should print sets do not intersect

print('------------------- Test Case 4 -----------------')
# Case where both  sets are  empty

list_7 = []
list_8 = []

print(union(list_7, list_8))
# Should be empty line
print(intersection(list_7, list_8))
# Should print sets do not intersect