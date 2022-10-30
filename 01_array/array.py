"""
数组实现
"""


class Array(object):
    def __init__(self, capacity: int) -> None:
        self._data = [None] * capacity
        self._capacity = capacity
        self._count = 0

    def __len__(self) -> int:
        return self._count

    @property
    def capacity(self) -> int:
        return self._capacity

    def __iter__(self):
        for i in range(self._count):
            yield self._data[i]

    def __str__(self) -> str:
        return ", ".join((str(item) for item in self))

    def __getitem__(self, index: int):
        return self.find(index)

    def find(self, position: int) -> object:
        """
        随机访问，时间复杂度为O(1)
        - 此处为模拟，随机访问应为：a[i]_address = base_address + i * data_type_size
        """
        if position < 0:
            raise IndexError("array index out of range")
        if position > self._count:
            raise IndexError("array index out of range")
        return self._data[position]

    def insert(self, index: int, value: object) -> bool:
        """
        保证插入顺序，平均时间复杂度 O(n)
        """
        if index < 0 or index > self._count:
            raise IndexError("array index out of range")
        if self._count == self._capacity:
            raise OverflowError("array is full")
        for i in range(self._count, index, -1):
            self._data[i] = self._data[i - 1]
        self._data[index] = value
        self._count += 1
        return True

    def delete(self, index: int) -> object:
        """
        保证数据插入的循序，平均时间复杂度O(n)
        """
        if index < 0:
            raise IndexError("array index out of range")
        if index > self._count:
            raise IndexError("array index out of range")
        obj = self._data[index]
        for i in range(index, self._count - 1, 1):
            self._data[i] = self._data[i+1]
        self._count -= 1
        return obj


class DynamicArray(Array):
    """
    支持存储空间伸缩，有些地方看起来没有必要，仅仅为了练习
    """
    def __init__(self, capacity: int) -> None:
        super().__init__(capacity)
        self._factor = 2

    def __extend(self):
        capacity = self._factor * self._capacity
        new_data = [None] * capacity
        for i in range(self._count):
            new_data[i] = self._data[i]
        self._data = new_data
        self._capacity = capacity
        return True

    def insert(self, index: int, value: object) -> bool:
        """
        保证插入顺序，自动扩展空间，时间复杂度 O(n)
        """
        if index < 0 or index > self._count:
            raise IndexError("array index out of range")
        if self._count == self._capacity:
            self.__extend()
        for i in range(self._count, index, -1):
            self._data[i] = self._data[i - 1]
        self._data[index] = value
        self._count += 1
        return True

    def __reduce(self):
        capacity = self._count
        new_data = [None] * capacity
        for i in range(self._count):
            new_data[i] = self._data[i]
        self._data = new_data
        self._capacity = self._count
        return True

    def delete(self, index: int) -> object:
        """
        保证数据插入时的循序，时间复杂度O(n)
        """
        if index < 0:
            raise IndexError("array index out of range")
        if index > self._count:
            raise IndexError("array index out of range")
        obj = self._data[index]
        for i in range(index, self._count - 1, 1):
            self._data[i] = self._data[i+1]
        self._count -= 1
        if self._capacity / self._count == self._factor:
            self.__reduce()
        return obj


def test_insert():
    a = Array(3)
    a.insert(0, 1)
    a.insert(1, 2)
    a.insert(2, 3)
    assert len(a) == 3
    assert a.find(2) == 3


def test_delete():
    a = Array(3)
    a.insert(0, 1)
    a.insert(1, 2)
    a.insert(2, 3)
    print(a)
    print(a.delete(1))
    print(a)
    assert a.find(1) == 3


def test_dynamic_insert():
    a = DynamicArray(2)
    for i in range(10):
        a.insert(i, i + 1)
        print(a, f"{len(a)=}, {a.capacity=}")


def test_dynamic_delete():
    a = DynamicArray(4)
    for i in range(4):
        a.insert(i, i + 1)
    print(a, f"{len(a)=}, {a.capacity=}")
    a.delete(0)
    a.delete(0)
    print(a, f"{len(a)=}, {a.capacity=}")
    assert len(a) == 2
    assert a.capacity == 2


if __name__ == '__main__':
    test_dynamic_delete()
