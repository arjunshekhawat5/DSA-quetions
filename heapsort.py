class min_heap:
    def __init__(self):
        self.list = []
        self.count = 0

    def add(self, element):
        self.count += 1
        self.list.append(element)
        self.heapify_up()

    def get_min(self):
        if self.count == 0:
            return None
        self.swap(0, self.count-1)
        temp = self.list[self.count-1]
        self.count -= 1
        self.heapify_down()
        return temp

    def is_parent(self, idx):
        if idx*2 + 1 >= self.count:
            return False
        return True

    def parent_idx(self, idx):
        if (idx-1)//2 < 0:
            return None
        return (idx-1)//2

    def left_idx(self, idx):
        return idx*2 + 1

    def right_idx(self, idx):
        return idx*2 + 2

    def smaller_child_idx(self, idx):
        left_child_idx = self.left_idx(idx)
        right_child_idx = self.right_idx(idx)
        if right_child_idx >= self.count:
            return left_child_idx
        if self.list[left_child_idx] <= self.list[right_child_idx]:
            return left_child_idx
        else:
            return right_child_idx

    def swap(self, idx1, idx2):
        self.list[idx1], self.list[idx2] = self.list[idx2], self.list[idx1]
        return

    def heapify_up(self):
        curr_idx = self.count - 1
        while curr_idx > 0:
            parent_idx = self.parent_idx(curr_idx)
            parent_el = self.list[parent_idx]
            curr_el = self.list[curr_idx]
            if parent_el <= curr_el:
                break
            self.swap(parent_idx, curr_idx)
            curr_idx = parent_idx
        return

    def heapify_down(self):
        curr_idx = 0
        while self.is_parent(curr_idx):
            small_child_idx = self.smaller_child_idx(curr_idx)
            if self.list[curr_idx] <= self.list[small_child_idx]:
                break
            self.swap(curr_idx, small_child_idx)
            curr_idx = small_child_idx
        return


def main():
    minH = min_heap()
    for i in range(10, 0, -1):
        minH.add(i)
        print(minH.list)
    for i in range(10):
        print(minH.list[:minH.count], minH.get_min())


def heap_sort(arr):
    heapify(arr)


def heapify(arr):
    i = len(arr) - 1
    while i > 0:
        child_idx = i*2 + 1

        i -= 1
        break


main()
