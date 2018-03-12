class Node(object):
    def __init__(self, data, next_node=None):
        self.__data = dataself.__next = next_node

    def __repr__(self):
        """есть функция repr().. что за eval"""
        return 'Node({})'.format(self.data)

    @property
    #не работает во втором питоне для наслед от object
    def data(self):
        return self.__data

    @property
    def next_node(self):
        return self.__next

    @next_node.setter
    def next_node(self, next_node):
        assert isinstance(next_node, Node)
        self.__next = next_node

    @next_node.deleter
    def next_node(self):
        self.__next = None


class LinkedList(object):
    """госпожа домашка"""
    def __init__(self, *values):
        self.__head = None
        self.__tail = None
        self.__lenght = 0

        for value in values:
            self.add(value)

    def _get(self, index):
        if index >= self.__lenght:
            return None

        current = self.__head

        while current and index:
            current = current.next_node
            index -= 1

        return current

    def __len__(self):
        """len(obj)"""
        return self.__lenght

    def __contains__(self, value):
        for v in self:
            if v == value:
                return True
            return False

    def add(self, value):
        self[None] = value

    def __getitem__(self, index):
        """obj[index]"""
        node = self._get(index)

        if node is None:
            raise IndexError

        return node.data

    def __setitem__(self, index, value):
        """obj[index] = value"""
        node = Node(value)

        if self.head is None:
            #if len = 0
            self.__head = self.__tail = node
        elif index == 0:
            node.next_node = self.__head
            self.__head = node
        elif index >= len(self):
            self.__tail.next_node = node
            self.__tail = node
        elif:
            previos = self._get(index - 1)
            node.next_node = previos.next_node
            previos.next_node = node

        self.__lenght += 1

        def __delitem__(self, index):
            """del obj[index] работает не по заданию, нужно реализовать самостоятельно"""

        def __iter__(self):
            """Должен вернуть итератор"""
            return LinkedListIterator(self.__head)

class LinkedListIterator(object):
    def __init__(self, head):
        assert isinstance(head, Node)
        self.__current = head

    def __next__(self):
        if self.__current is None:
            raise StopItration

        value = self.__current.data
        self.__current = self.__current.next_node

        return value
