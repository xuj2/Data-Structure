class StaticArrayException(Exception):
    pass


class StaticArray:
    def __init__(self, size=10):
        if size < 1:
            raise StaticArrayException
        self._data = [None] * size

    def __str__(self):
        out = "STAT_ARR Size: "
        out += str(len(self._data))
        out += " " + str(self._data)
        return out

    def get(self, index: int) -> object:
        if index < 0 or index >= self.size():
            raise StaticArrayException
        return self._data[index]

    def set(self, index: int, value: object) -> None:
        if index < 0 or index >= self.size():
            raise StaticArrayException
        self._data[index] = value

    def __getitem__(self, index) -> object:
        return self.get(index)

    def __setitem__(self, index, value) -> object:
        self.set(index, value)

    def size(self):
        return len(self._data)
