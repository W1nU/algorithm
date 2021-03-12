import sys
input = sys.stdin.readline

class CustomSet:
    def __init__(self):
        self.set = [False] * 21

    def add(self, value):
        self.set[value] = True
         
    def check(self, value):
        if self.set[value]:
            print("1")
        else:
            print("0")
        
    def remove(self, value):
        self.set[value] = False

    def toggle(self, value):
        self.set[value] = not self.set[value]

    def all(self):
        self.set = [True] * 21

    def empty(self):
        self.set = [False] * 21

N = int(input())
custom_set = CustomSet()

for _ in range(N):
    operation = input()
    
    if operation == "all\n":
        custom_set.all()

    elif operation == "empty\n":
        custom_set.empty() 

    else:
        op, value = operation.split()

        if op == "add":
            custom_set.add(int(value))

        elif op == "remove":
            custom_set.remove(int(value))

        elif op == "check":
            custom_set.check(int(value))

        elif op == "toggle":
            custom_set.toggle(int(value))