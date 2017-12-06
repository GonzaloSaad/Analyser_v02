class StringIterator():
    def __init__(self, string):
        self.__string = string
        self.__current = 0

    def getChar(self, cant=1):
        try:
            return self.__string[self.__current:self.__current + cant]
        except IndexError:
            return None

    def moveNext(self):
        self.__current += 1

    def movePrev(self):
        self.__current -= 1

    def hastNext(self):
        return self.__current < len(self.__string)

    def next(self):
        try:
            return self.__string[self.__current + 1]
        except IndexError:
            return None



