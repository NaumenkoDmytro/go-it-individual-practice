# # Node class for the linked list
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# # Linked list class
# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         new_node = Node(data)
#         if not self.head:
#             self.head = new_node
#             return
#         last_node = self.head
#         while last_node.next:
#             last_node = last_node.next
#         last_node.next = new_node

#     def sum_of_linked_list(self):
#         current_node = self.head
#         total_sum = 0
#         while current_node:
#             total_sum += current_node.data
#             current_node = current_node.next
#         return total_sum

# # Example usage:
# my_linked_list = LinkedList()
# my_linked_list.append(1)
# my_linked_list.append(2)
# my_linked_list.append(3)
# my_linked_list.append(4)
# my_linked_list.append(5)
# print("Sum of linked list:", my_linked_list.sum_of_linked_list())
