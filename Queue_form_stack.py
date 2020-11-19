class Stack():
    def __init__(self):
        self.stack_list = []
        self.len = 0

    def pop(self):
        if self.len == 0:
            return 'Empty pop'
        self.len -= 1
        return self.stack_list.pop()

    def push(self, val):
        self.stack_list.append(val)
        self.len += 1

    def peek(self):
        # print(self.len)
        if self.len == 0:
            return 'Empty peek'
        return self.stack_list[-1]


class Node():
    def __init__(self, val=None):
        self.val = val
        self.next = None


class LinkedStack():
    def __init__(self):
        self.head = Node()

    def push(self, val):
        value = Node(val)
        value.next = self.head
        head = value

    def pop(self):
        if not self.head:
            return False
        res = self.head.val
        self.head = self.head.next
        return res

    def peek(self):
        if not self.head:
            return False

        return self.head.val


class Que():

    def __init__(self):
        self.push_stack = LinkedStack()
        self.pull_stack = LinkedStack()

    def enque(self, val):
        self.push_stack.push(val)

    def helper(self):
        if not self.pull_stack.peek():
            if not self.push_stack.peek():
                return True
            else:
                while self.push_stack.head:
                    self.pull_stack.push(self.push_stack.pop())
        return False

    def deque(self):
        empty = self.helper()
        if empty:
            return 'Empty Queue'

        return self.pull_stack.pop()

    def peek(self):
        empty = self.helper()
        # print(empty)
        if empty:
            return 'Empty peek_que'

        return self.pull_stack.peek()


def main():
    queee = Que()

    for i in range(10):
        queee.enque(i)
        print('Queing ' + str(i))

    for i in range(10):
        print('Dequing ' + str(queee.deque()))
        print('Top value ' + str(queee.peek()))


main()
