class ListNode:
    def __init__(self, data=0, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head_node = None
        self.tail_node = None

    def insert_first_node(self, data):
        new_node = ListNode(data)
        current_node = self.head_node
        if self.head_node is None:
            self.head_node = new_node
        else:
            new_node.next = current_node
            current_node.prev = new_node
            self.head_node = new_node

    def insert_last_node(self, data):
        new_node = ListNode(data)
        if self.head_node is None:
            raise ValueError("This is empty node.")
        else:
            current_node = self.head_node
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node
            new_node.prev = current_node

    def delete_first_node(self):
        if self.head_node is None:
            raise ValueError("This is empty node.")
        else:
            current_node = self.head_node.next
            current_node.prev = None
            self.head_node = current_node

    def delete_last_node(self):
        if self.head_node is None:
            raise ValueError("This is empty node.")
        else:
            current_node = self.head_node
            while current_node.next.next:
                current_node = current_node.next
            current_node.next = None

    def find_node(self, data):
        is_exist = False
        if self.head_node is None:
            raise ValueError("This is empty node.")
        else:
            current_node = self.head_node
            while current_node:
                if current_node.data == data:
                    is_exist = True
                    return is_exist
                else:
                    current_node = current_node.next
            return is_exist

    def update_node(self, data, target):
        if self.head_node is None:
            raise ValueError("This is empty node.")
        else:
            current_node = self.head_node
            while current_node:
                if current_node.data == data:
                    current_node.data = target
                    return True
                else:
                    current_node = current_node.next
            return False
        
    def reverse_node(self):
        if self.head_node is None:
            raise ValueError("This is empty node.")
        else:
            current_node = self.head_node
            previous_node = None
            while current_node:
                next_node = current_node.next  # 다음 노드를 임시 변수에 저장
                current_node.next = previous_node  # 현재 노드의 next를 이전 노드로 설정
                current_node.prev = next_node  # 현재 노드의 prev를 다음 노드로 설정
                previous_node = current_node  # 이전 노드를 현재 노드로 갱신
                current_node = next_node  # 현재 노드를 다음 노드로 갱신
            self.head_node = previous_node  # 역순으로 변환된 리스트의 첫 번째 노드를 head_node로 설정


    def print_node(self):
        if self.head_node is None:
            raise ValueError("This is empty node.")
        else:
            current_node = self.head_node
            while current_node:
                print(current_node.data)
                current_node = current_node.next


doubly_linked_list = DoublyLinkedList()
doubly_linked_list.insert_first_node(5)
doubly_linked_list.insert_first_node(4)
doubly_linked_list.insert_first_node(3)
doubly_linked_list.insert_first_node(2)
doubly_linked_list.insert_last_node(6)
doubly_linked_list.insert_last_node(7)
doubly_linked_list.insert_last_node(8)
doubly_linked_list.insert_last_node(9)
doubly_linked_list.insert_last_node(10)
doubly_linked_list.insert_last_node(11)
doubly_linked_list.insert_last_node(12)
doubly_linked_list.delete_first_node()
doubly_linked_list.delete_first_node()
doubly_linked_list.delete_first_node()
doubly_linked_list.delete_last_node()
doubly_linked_list.delete_last_node()
print(doubly_linked_list.find_node(4))
print(doubly_linked_list.update_node(5, 9))
doubly_linked_list.print_node()
print("*"*10)
doubly_linked_list.reverse_node()
doubly_linked_list.print_node()
