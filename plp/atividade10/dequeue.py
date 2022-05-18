import gc


class Node:
    def __init__(self, element):
        self.__element = element
        self.__next = None
        self.__previous = None

    def __del__(self):
        del self
        gc.collect()
        return "Node eliminated"

    def getElement(self):
        return self.__element

    def getPrevious(self):
        return self.__previous

    def setPrevious(self, previous):
        self.__previous = previous

    def getNext(self):
        return self.__next

    def setNext(self, next):
        self.__next = next


class Dequeue:
    def __init__(self, max: int):
        self.__max = max
        self.__header: Node = None
        self.__tailer: Node = None

    def __del__(self):
        del self
        gc.collect()
        return "Dequeue eliminated"

    def empty(self):
        if not self.__header and not self.__tailer:
            return True
        else:
            return False

    def size(self):
        size = 0
        element = self.__header
        while element is not None:
            size += 1
            element = element.getNext()
        return size

    def offerFirst(self, element):
        if self.size() < self.__max:
            NewNode = Node(element)
            if self.__header is not None:
                aux = self.__header
                self.__header = NewNode
                aux.setPrevious(self.__header)
                self.__header.setNext(aux)
            else:
                self.__header = NewNode
                self.__tailer = self.__header
            return True

    def offerLast(self, element):
        if self.__max > self.size():
            NewNode = Node(element)
            if self.__tailer is None and self.__header is None:
                self.__header = NewNode
                self.__tailer = self.__header
            else:
                last = self.__tailer
                self.__tailer = NewNode
                last.setNext(self.__tailer)
                self.__tailer.setPrevious(last)
            return True

    def peekFirst(self):
        if not self.empty():
            return self.__header.getElement()
        else:
            return None

    def peekLast(self):
        if not self.empty():
            return self.__tailer.getElement()
        else:
            return None

    def pollFirst(self):
        mostrar = self.__header
        self.__header = self.__header.getNext()
        return mostrar.getElement()

    def pollLast(self):
        mostrar = self.__tailer
        self.__tailer = self.__tailer.getPrevious()
        self.__tailer.setNext(None)
        return mostrar.getElement()
