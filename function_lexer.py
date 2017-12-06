import re

from lexer_exceptions import *
from tokens import *
from string_iterator import *
from lexeme import *
from lexer import *


class FunctionLexer():
    def __init__(self, inputString, variable='x'):

        self.__lexer = Lexer(inputString)
        self.variable = variable
        self.__defineLexemes()



    def __defineLexemes(self):

        self.__setSimpleLexemes()
        self.__setDualLexemes()
        self.__setTriLexemes()
        self.__setMultipleLexemes()

    def tokenize(self):
        return self.__lexer.tokenize()

    def __setSimpleLexemes(self):
        lexemes = [

            Lexeme('PLUS', r'\+'),
            Lexeme('MINUS', r'-'),
            Lexeme('TIMES', r'\*'),
            Lexeme('DIVIDE', r'/'),
            Lexeme('POWER', r'\^'),
            Lexeme('LPAREN', r'\('),
            Lexeme('RPAREN', r'\)'),
            Lexeme('COEFF', r'[A-Z]'),
            Lexeme('VAR', r'' + self.variable),
            Lexeme('CONSTANT', r'e')

        ]
        self.__lexer.addLexemes(lexemes)

    def __setDualLexemes(self):
        lexemes = [
            Lexeme("FUNCTION", r'ln'),
            Lexeme("FUNCTION", r'tg')
        ]
        self.__lexer.addLexemes(lexemes)

    def __setTriLexemes(self):
        lexemes = [
            Lexeme("FUNCTION", r'sin'),
            Lexeme("FUNCTION", r'cos'),
            Lexeme("FUNCTION", r'log')
        ]
        self.__lexer.addLexemes(lexemes)

    def __setMultipleLexemes(self):
        lexemes = [
            Lexeme('NUMBER',r'[0-9]+(?!.)')
        ]
        self.__lexer.addLexemes(lexemes)

    def __str__(self):
        return self.__lexer.__str__()



l = FunctionLexer("sin(log(ln(x)))+cos(x)/3*x^2+tg(9*x)")

for tok in l.tokenize():
    print(tok)

print(l)