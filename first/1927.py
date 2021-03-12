import sys
input = sys.stdin.readline

class MinHeap:
    def __init__(self):
        self.tree = [None]

    def _exchange_node(self, a_index, b_index):
        temp = self.tree[a_index]
        self.tree[a_index] = self.tree[b_index]
        self.tree[b_index] = temp
        
    def insert(self, value):
        self.tree.append(value)

        current_index = len(self.tree) - 1
        parent_index = current_index // 2

        while 1:
            if parent_index == 0:
                break

            elif self.tree[parent_index] >= value:
                temp = self.tree[parent_index]
                self.tree[parent_index] = value
                self.tree[current_index] = temp

                current_index = parent_index
                parent_index = current_index // 2

            else:
                break

    def delete(self):
        if len(self.tree) == 1:
            print(0)
            return 

        if len(self.tree) == 2:
            print(self.tree.pop())
            return 

        current_node = 1

        self._exchange_node(current_node, len(self.tree) - 1)
        delete_value = self.tree.pop()
        print(delete_value)

        while 1:
            root_value = self.tree[current_node]
            left = current_node * 2
            right = current_node * 2 + 1
            left_available = False
            right_available = False

            left_value = float("inf")
            right_value = float("inf")

            if left < len(self.tree):
                left_value = self.tree[left]

            if right < len(self.tree):
                right_value = self.tree[right]

            if left_value < root_value:
                left_available = True

            if right_value < root_value:
                right_available = True

            if left_available and right_available:
                if left_value < right_value:
                    self._exchange_node(left, current_node)
                    current_node = left

                else:
                    self._exchange_node(right, current_node)
                    current_node = right

            elif left_available:
                self._exchange_node(left, current_node)
                current_node = left

            elif right_available:
                self._exchange_node(right, current_node)
                current_node = right

            else:
                break        

min_heap = MinHeap()

N = int(input())
numbers = [int(input()) for _ in range(N)]

for number in numbers:
    if number == 0:
        min_heap.delete()
    
    else:
        min_heap.insert(number)


# while 1:
#     number = int(input())
#     if number == 0:
#         min_heap.delete()
    
#     else:
#         min_heap.insert(number)
    
#     print(min_heap.tree)