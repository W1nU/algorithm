import sys
input = sys.stdin.readline

class MaxHeap:
    def __init__(self):
        self.heap = [None]

    def swap(self, a_index, b_index):
        temp = self.heap[a_index]
        self.heap[a_index] = self.heap[b_index]
        self.heap[b_index] = temp

    def insert(self, value):
        self.heap.append(value)

        parent = (len(self.heap) - 1) // 2
        current_index = len(self.heap) - 1

        while parent >= 1:
            if self.heap[parent] < self.heap[current_index]:
                self.swap(parent, current_index)
                current_index = parent
                parent = current_index // 2

            else:
                break
            

    def delete(self):
        if len(self.heap) == 1:
            print(0)
            return
        
        if len(self.heap) == 2:
            print(self.heap.pop())
            return
            
        self.swap(1, len(self.heap) - 1)
        delete_value = self.heap.pop()
        print(delete_value)

        heap_size = len(self.heap) - 1
        current_index = 1

        while 1:
            left_index = current_index * 2
            right_index = current_index * 2 + 1
            
            left_available = False
            right_available = False

            if left_index <= heap_size and self.heap[left_index] > self.heap[current_index]:
                left_available = True
            
            if right_index <= heap_size and self.heap[right_index] > self.heap[current_index]:
                right_available = True

            if left_available and right_available:
                if self.heap[left_index] > self.heap[right_index]:
                    self.swap(left_index, current_index)
                    current_index = left_index

                else:
                    self.swap(right_index, current_index)
                    current_index = right_index
            
            elif left_available:
                self.swap(left_index, current_index)
                current_index = left_index

            elif right_available:
                self.swap(right_index, current_index)
                current_index = right_index
            
            else:
                break


max_heap = MaxHeap()

N = int(input())
numbers = [int(input()) for _ in range(N)]

for number in numbers:
    if number == 0:
        max_heap.delete()
    else:
        max_heap.insert(number)
