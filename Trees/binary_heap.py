# Implementation of binary heap

class BinaryHeaP(Object):
    def __init__(self, arr=None):
        self._list = [0]
        if arr:
            for value in arr:
                self.push(value)

    def push(self, value):
        self._list.append(value)
        self._bubble_up(len(self._list) - 1)

    def pop(self):
        value = self._list[1]
        self._swap(1, -1)
        self._list = self._list[:-1]
        self._bubble_down(1)
        return value

    def min(self):
        return self._list[1]

    def __len__(self):
        return len(self._list) - 1

    def __iter__(self):
        yield from iter(self._list[1:])

    def _bubble_up(self, index):
        parent = index // 2
        #swap eelements if parent node is greater than the current value
        while index > 1 and self._list[parent] > self._list[index]:
            self._swap(parent, index)
            index = parent
            parent = index // 2

    def _bubble_down(self, index):
        while 2 * index < len(self._list):
            if len(self._list) == 2 * index + 1:
                minchild = 2 * index

            else:
                if self._list[2 * index] < self._list[2 * index + 1]:
                    minchild = 2 * index
                else:
                    minchild = 2 * index + 1

            self._swap(index, minchild)
            index = minchild


    def _swap(self, index1, index2):
        temp = self._list[index1]
        self._list[index1] = self._list[index2]
        self._list[index2] = temp 
