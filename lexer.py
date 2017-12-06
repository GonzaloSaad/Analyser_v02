import re

from lexer_exceptions import *
from tokens import *
from string_iterator import *
from lexeme import *


class Lexer():
    def __init__(self, inputString):

        self.__lexemes = []
        self.__inputString = inputString

    def tokenize(self):

        chars = StringIterator(self.__inputString)

        while chars.hastNext():
            c = chars.getChar()

            token = None

            lexemeMatrix = self.__lexemes
            for i in range(1, len(lexemeMatrix)):
                token = self.__scan(lexemeMatrix[i], i, chars)
                if token is not None:
                    break

            if token is None:
                token = self.__scan(lexemeMatrix[0], 0, chars)

            if token is None:
                raise NoSuchSymbolException("The symbol '" + c + "' is not legal.")
            else:
                yield token

    def __scan(self, lexemes, size, chars):

        if size == 0:
            return self.__scanMultiple(lexemes, chars)

        c = chars.getChar(size)

        ret = None
        if c is not None:
            for lex in lexemes:
                if re.match(lex.getPat(), c):
                    ret = Token(lex.getType(), c)

        if ret is not None:
            for i in range(0, size):
                chars.moveNext()
        return ret

    def __scanMultiple(self, lexemes, chars):

        for lex in lexemes:
            step = 1
            found = False
            c = chars.getChar(step)
            while c is not None:
                if not re.match(lex.getPat(), c):
                    break
                found = True
                step += 1
                c = chars.getChar(step)

            if found:
                c = chars.getChar(step - 1)
                for i in range(len(c)):
                    chars.moveNext()
                return Token(lex.getType(), c)

        return None

    def addLexemes(self, lexemes):
        for lex in lexemes:
            lexemeSize = lex.size()
            lexerSize = len(self.__lexemes)
            if lexerSize - 1 < lexemeSize:
                for i in range(lexemeSize - lexerSize + 1):
                    self.__lexemes.append([])

            self.__lexemes[lexemeSize].append(lex)

    def __str__(self):
        string = "Lexer.\t\t\nInput String: '" + self.__inputString + "'\n"
        for i in range(len(self.__lexemes)):
            string += "Lenght " + str("*" if i == 0 else i) + " lexemes\n"
            lexemes = self.__lexemes[i]

            if len(lexemes) == 0:
                string += "\tNone\n"

            for lex in lexemes:
                string += "\t" + str(lex) + "\n"

        return string
