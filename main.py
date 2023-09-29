class Stack:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def __str__(self):
        return str(self._data)

    def is_empty(self):
        return not bool(len(self._data))

    def push(self, item):
        self._data.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Стек пустой")
        return self._data.pop()


class Queue(Stack):
    def pop(self):
        if self.is_empty():
            raise IndexError("Очередь пуста")
        return self._data.pop(0)


stack = Stack()
stack.push(5)
stack.push(10)
stack.push(0)
print(stack)
print(stack.pop(), stack.pop(), stack.pop())
print(stack)

queue = Queue()
queue.push(1)
queue.push(2)
print(queue)
print(queue.pop(), queue.pop())