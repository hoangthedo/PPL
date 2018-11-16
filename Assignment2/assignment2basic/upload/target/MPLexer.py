# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\f")
        buf.write("\u00a2\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\6\6U\n\6\r\6\16\6")
        buf.write("V\3\7\6\7Z\n\7\r\7\16\7[\3\7\3\7\6\7`\n\7\r\7\16\7a\3")
        buf.write("\b\3\b\3\t\3\t\3\n\6\ni\n\n\r\n\16\nj\3\13\3\13\3\f\3")
        buf.write("\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21\3\22")
        buf.write("\3\22\3\23\3\23\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27")
        buf.write("\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35")
        buf.write("\3\35\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3")
        buf.write("$\3$\3%\3%\2\2&\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23")
        buf.write("\13\25\2\27\2\31\2\33\2\35\2\37\2!\2#\2%\2\'\2)\2+\2-")
        buf.write("\2/\2\61\2\63\2\65\2\67\29\2;\2=\2?\2A\2C\2E\2G\2I\f\3")
        buf.write("\2 \3\2\62;\4\2--//\4\2,,\61\61\3\2c|\4\2CCcc\4\2DDdd")
        buf.write("\4\2EEee\4\2FFff\4\2GGgg\4\2HHhh\4\2IIii\4\2JJjj\4\2K")
        buf.write("Kkk\4\2LLll\4\2MMmm\4\2NNnn\4\2OOoo\4\2PPpp\4\2QQqq\4")
        buf.write("\2RRrr\4\2SSss\4\2TTtt\4\2UUuu\4\2VVvv\4\2WWww\4\2XXx")
        buf.write("x\4\2YYyy\4\2ZZzz\4\2[[{{\4\2\\\\||\2\u008b\2\3\3\2\2")
        buf.write("\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2")
        buf.write("\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2I\3")
        buf.write("\2\2\2\3K\3\2\2\2\5M\3\2\2\2\7O\3\2\2\2\tQ\3\2\2\2\13")
        buf.write("T\3\2\2\2\rY\3\2\2\2\17c\3\2\2\2\21e\3\2\2\2\23h\3\2\2")
        buf.write("\2\25l\3\2\2\2\27n\3\2\2\2\31p\3\2\2\2\33r\3\2\2\2\35")
        buf.write("t\3\2\2\2\37v\3\2\2\2!x\3\2\2\2#z\3\2\2\2%|\3\2\2\2\'")
        buf.write("~\3\2\2\2)\u0080\3\2\2\2+\u0082\3\2\2\2-\u0084\3\2\2\2")
        buf.write("/\u0086\3\2\2\2\61\u0088\3\2\2\2\63\u008a\3\2\2\2\65\u008c")
        buf.write("\3\2\2\2\67\u008e\3\2\2\29\u0090\3\2\2\2;\u0092\3\2\2")
        buf.write("\2=\u0094\3\2\2\2?\u0096\3\2\2\2A\u0098\3\2\2\2C\u009a")
        buf.write("\3\2\2\2E\u009c\3\2\2\2G\u009e\3\2\2\2I\u00a0\3\2\2\2")
        buf.write("KL\7?\2\2L\4\3\2\2\2MN\7=\2\2N\6\3\2\2\2OP\7*\2\2P\b\3")
        buf.write("\2\2\2QR\7+\2\2R\n\3\2\2\2SU\t\2\2\2TS\3\2\2\2UV\3\2\2")
        buf.write("\2VT\3\2\2\2VW\3\2\2\2W\f\3\2\2\2XZ\t\2\2\2YX\3\2\2\2")
        buf.write("Z[\3\2\2\2[Y\3\2\2\2[\\\3\2\2\2\\]\3\2\2\2]_\7\60\2\2")
        buf.write("^`\t\2\2\2_^\3\2\2\2`a\3\2\2\2a_\3\2\2\2ab\3\2\2\2b\16")
        buf.write("\3\2\2\2cd\t\3\2\2d\20\3\2\2\2ef\t\4\2\2f\22\3\2\2\2g")
        buf.write("i\t\5\2\2hg\3\2\2\2ij\3\2\2\2jh\3\2\2\2jk\3\2\2\2k\24")
        buf.write("\3\2\2\2lm\t\6\2\2m\26\3\2\2\2no\t\7\2\2o\30\3\2\2\2p")
        buf.write("q\t\b\2\2q\32\3\2\2\2rs\t\t\2\2s\34\3\2\2\2tu\t\n\2\2")
        buf.write("u\36\3\2\2\2vw\t\13\2\2w \3\2\2\2xy\t\f\2\2y\"\3\2\2\2")
        buf.write("z{\t\r\2\2{$\3\2\2\2|}\t\16\2\2}&\3\2\2\2~\177\t\17\2")
        buf.write("\2\177(\3\2\2\2\u0080\u0081\t\20\2\2\u0081*\3\2\2\2\u0082")
        buf.write("\u0083\t\21\2\2\u0083,\3\2\2\2\u0084\u0085\t\22\2\2\u0085")
        buf.write(".\3\2\2\2\u0086\u0087\t\23\2\2\u0087\60\3\2\2\2\u0088")
        buf.write("\u0089\t\24\2\2\u0089\62\3\2\2\2\u008a\u008b\t\25\2\2")
        buf.write("\u008b\64\3\2\2\2\u008c\u008d\t\26\2\2\u008d\66\3\2\2")
        buf.write("\2\u008e\u008f\t\27\2\2\u008f8\3\2\2\2\u0090\u0091\t\30")
        buf.write("\2\2\u0091:\3\2\2\2\u0092\u0093\t\31\2\2\u0093<\3\2\2")
        buf.write("\2\u0094\u0095\t\32\2\2\u0095>\3\2\2\2\u0096\u0097\t\33")
        buf.write("\2\2\u0097@\3\2\2\2\u0098\u0099\t\34\2\2\u0099B\3\2\2")
        buf.write("\2\u009a\u009b\t\35\2\2\u009bD\3\2\2\2\u009c\u009d\t\36")
        buf.write("\2\2\u009dF\3\2\2\2\u009e\u009f\t\37\2\2\u009fH\3\2\2")
        buf.write("\2\u00a0\u00a1\13\2\2\2\u00a1J\3\2\2\2\7\2V[aj\2")
        return buf.getvalue()


class MPLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    INTLIT = 5
    FLOATLIT = 6
    ADDOP = 7
    MULOP = 8
    ID = 9
    ERROR_CHAR = 10

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='", "';'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "INTLIT", "FLOATLIT", "ADDOP", "MULOP", "ID", "ERROR_CHAR" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "INTLIT", "FLOATLIT", 
                  "ADDOP", "MULOP", "ID", "A", "B", "C", "D", "E", "F", 
                  "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", 
                  "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "ERROR_CHAR" ]

    grammarFileName = "MP.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


