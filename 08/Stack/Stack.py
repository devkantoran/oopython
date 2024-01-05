# Stack class


class Stack:
    """Stack class implements a last in first out LIFO algorithm"""

    def __init__(self, startingStackAsList=None):
        if startingStackAsList is None:
            self.__dataList = []
        else:
            self.__dataList = startingStackAsList[:]  # make a copy

    def push(self, item):
        self.__dataList.append(item)

    def pop(self):
        if len(self.__dataList) == 0:
            raise IndexError
        element = self.__dataList.pop()
        return element

    def peek(self):
        # Retrieve the top item, without removing it
        item = self.__dataList[-1]
        return item

    def getSize(self):
        nElements = len(self.__dataList)
        return nElements

    def show(self):
        # Show the stack in a vertical orientation
        print("Stack is:")
        for value in reversed(self.__dataList):
            print("   ", value)
