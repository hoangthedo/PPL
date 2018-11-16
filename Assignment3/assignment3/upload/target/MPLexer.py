# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2@")
        buf.write("\u0241\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\t")
        buf.write("U\4V\tV\4W\tW\4X\tX\4Y\tY\4Z\tZ\3\2\3\2\3\3\3\3\3\4\3")
        buf.write("\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13")
        buf.write("\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3")
        buf.write("\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25\3\26")
        buf.write("\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3")
        buf.write(" \3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3")
        buf.write("#\3#\3#\3#\3$\3$\3$\3$\3$\3%\3%\3%\3&\3&\3&\3&\3&\3&\3")
        buf.write("\'\3\'\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3(\3)\3)\3)\3*")
        buf.write("\3*\3*\3*\3*\3*\3*\3+\3+\3+\3+\3+\3,\3,\3,\3,\3,\3,\3")
        buf.write("-\3-\3-\3-\3.\3.\3.\3.\3.\3.\3.\3.\3.\3/\3/\3/\3/\3/\3")
        buf.write("/\3/\3/\3/\3/\3\60\3\60\3\60\3\60\3\61\3\61\3\61\3\61")
        buf.write("\3\61\3\61\3\62\3\62\3\62\3\63\3\63\3\63\3\63\7\63\u0176")
        buf.write("\n\63\f\63\16\63\u0179\13\63\3\63\3\63\3\63\3\63\3\63")
        buf.write("\3\64\3\64\7\64\u0182\n\64\f\64\16\64\u0185\13\64\3\64")
        buf.write("\3\64\3\64\3\64\3\65\3\65\3\65\3\65\7\65\u018f\n\65\f")
        buf.write("\65\16\65\u0192\13\65\3\65\3\65\3\66\3\66\3\66\3\67\3")
        buf.write("\67\38\38\39\39\3:\3:\3;\3;\3;\3;\3<\3<\3<\3<\3=\3=\3")
        buf.write(">\3>\3?\3?\3?\3@\3@\3A\3A\3A\3B\3B\3B\3B\3C\3C\3C\3D\3")
        buf.write("D\3D\3E\3E\3E\3E\3F\3F\3G\3G\3G\3H\3H\3I\3I\3J\3J\3K\3")
        buf.write("K\3L\3L\3M\3M\3N\3N\3O\3O\3P\6P\u01d9\nP\rP\16P\u01da")
        buf.write("\3Q\6Q\u01de\nQ\rQ\16Q\u01df\3R\5R\u01e3\nR\3R\5R\u01e6")
        buf.write("\nR\3R\6R\u01e9\nR\rR\16R\u01ea\3S\3S\3S\3S\3S\3S\3S\3")
        buf.write("S\5S\u01f5\nS\3S\3S\3S\7S\u01fa\nS\fS\16S\u01fd\13S\3")
        buf.write("S\5S\u0200\nS\3S\3S\3S\5S\u0205\nS\3T\3T\3T\3T\3T\3T\3")
        buf.write("T\3T\3T\3T\3T\5T\u0212\nT\3U\3U\7U\u0216\nU\fU\16U\u0219")
        buf.write("\13U\3V\6V\u021c\nV\rV\16V\u021d\3V\3V\3W\3W\3W\3X\3X")
        buf.write("\3X\3X\7X\u0229\nX\fX\16X\u022c\13X\3X\3X\3X\3Y\3Y\3Y")
        buf.write("\3Y\7Y\u0235\nY\fY\16Y\u0238\13Y\3Y\3Y\3Y\3Y\3Y\3Z\3Z")
        buf.write("\3Z\5\u0177\u0183\u0236\2[\3\2\5\2\7\2\t\2\13\2\r\2\17")
        buf.write("\2\21\2\23\2\25\2\27\2\31\2\33\2\35\2\37\2!\2#\2%\2\'")
        buf.write("\2)\2+\2-\2/\2\61\2\63\2\65\3\67\49\5;\6=\7?\bA\tC\nE")
        buf.write("\13G\fI\rK\16M\17O\20Q\21S\22U\23W\24Y\25[\26]\27_\30")
        buf.write("a\31c\32e\33g\34i\35k\36m\37o q!s\"u#w$y%{&}\'\177(\u0081")
        buf.write(")\u0083*\u0085+\u0087,\u0089-\u008b.\u008d/\u008f\60\u0091")
        buf.write("\61\u0093\62\u0095\63\u0097\64\u0099\65\u009b\66\u009d")
        buf.write("\67\u009f\2\u00a18\u00a3\2\u00a59\u00a7:\u00a9;\u00ab")
        buf.write("<\u00ad=\u00af>\u00b1?\u00b3@\3\2$\4\2CCcc\4\2DDdd\4\2")
        buf.write("EEee\4\2FFff\4\2GGgg\4\2HHhh\4\2IIii\4\2JJjj\4\2KKkk\4")
        buf.write("\2MMmm\4\2NNnn\4\2OOoo\4\2PPpp\4\2QQqq\4\2RRrr\4\2SSs")
        buf.write("s\4\2TTtt\4\2UUuu\4\2VVvv\4\2WWww\4\2XXxx\4\2YYyy\4\2")
        buf.write("ZZzz\4\2[[{{\4\2\\\\||\4\2\f\f\17\17\3\2\62;\5\2C\\aa")
        buf.write("c|\6\2\62;C\\aac|\5\2\13\f\16\17\"\"\n\2$$))^^ddhhppt")
        buf.write("tvv\b\2\f\f\17\17$$GHQQ^^\4\2$$^^\3\2^^\2\u023a\2\65\3")
        buf.write("\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2")
        buf.write("?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2")
        buf.write("\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2")
        buf.write("\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2")
        buf.write("\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3")
        buf.write("\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o")
        buf.write("\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2")
        buf.write("y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081")
        buf.write("\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2")
        buf.write("\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f")
        buf.write("\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2")
        buf.write("\2\2\u0097\3\2\2\2\2\u0099\3\2\2\2\2\u009b\3\2\2\2\2\u009d")
        buf.write("\3\2\2\2\2\u00a1\3\2\2\2\2\u00a5\3\2\2\2\2\u00a7\3\2\2")
        buf.write("\2\2\u00a9\3\2\2\2\2\u00ab\3\2\2\2\2\u00ad\3\2\2\2\2\u00af")
        buf.write("\3\2\2\2\2\u00b1\3\2\2\2\2\u00b3\3\2\2\2\3\u00b5\3\2\2")
        buf.write("\2\5\u00b7\3\2\2\2\7\u00b9\3\2\2\2\t\u00bb\3\2\2\2\13")
        buf.write("\u00bd\3\2\2\2\r\u00bf\3\2\2\2\17\u00c1\3\2\2\2\21\u00c3")
        buf.write("\3\2\2\2\23\u00c5\3\2\2\2\25\u00c7\3\2\2\2\27\u00c9\3")
        buf.write("\2\2\2\31\u00cb\3\2\2\2\33\u00cd\3\2\2\2\35\u00cf\3\2")
        buf.write("\2\2\37\u00d1\3\2\2\2!\u00d3\3\2\2\2#\u00d5\3\2\2\2%\u00d7")
        buf.write("\3\2\2\2\'\u00d9\3\2\2\2)\u00db\3\2\2\2+\u00dd\3\2\2\2")
        buf.write("-\u00df\3\2\2\2/\u00e1\3\2\2\2\61\u00e3\3\2\2\2\63\u00e5")
        buf.write("\3\2\2\2\65\u00e7\3\2\2\2\67\u00ef\3\2\2\29\u00f5\3\2")
        buf.write("\2\2;\u00fe\3\2\2\2=\u0103\3\2\2\2?\u0107\3\2\2\2A\u010c")
        buf.write("\3\2\2\2C\u010f\3\2\2\2E\u0117\3\2\2\2G\u011e\3\2\2\2")
        buf.write("I\u0123\3\2\2\2K\u0126\3\2\2\2M\u012c\3\2\2\2O\u0133\3")
        buf.write("\2\2\2Q\u0138\3\2\2\2S\u013b\3\2\2\2U\u0142\3\2\2\2W\u0147")
        buf.write("\3\2\2\2Y\u014d\3\2\2\2[\u0151\3\2\2\2]\u015a\3\2\2\2")
        buf.write("_\u0164\3\2\2\2a\u0168\3\2\2\2c\u016e\3\2\2\2e\u0171\3")
        buf.write("\2\2\2g\u017f\3\2\2\2i\u018a\3\2\2\2k\u0195\3\2\2\2m\u0198")
        buf.write("\3\2\2\2o\u019a\3\2\2\2q\u019c\3\2\2\2s\u019e\3\2\2\2")
        buf.write("u\u01a0\3\2\2\2w\u01a4\3\2\2\2y\u01a8\3\2\2\2{\u01aa\3")
        buf.write("\2\2\2}\u01ac\3\2\2\2\177\u01af\3\2\2\2\u0081\u01b1\3")
        buf.write("\2\2\2\u0083\u01b4\3\2\2\2\u0085\u01b8\3\2\2\2\u0087\u01bb")
        buf.write("\3\2\2\2\u0089\u01be\3\2\2\2\u008b\u01c2\3\2\2\2\u008d")
        buf.write("\u01c4\3\2\2\2\u008f\u01c7\3\2\2\2\u0091\u01c9\3\2\2\2")
        buf.write("\u0093\u01cb\3\2\2\2\u0095\u01cd\3\2\2\2\u0097\u01cf\3")
        buf.write("\2\2\2\u0099\u01d1\3\2\2\2\u009b\u01d3\3\2\2\2\u009d\u01d5")
        buf.write("\3\2\2\2\u009f\u01d8\3\2\2\2\u00a1\u01dd\3\2\2\2\u00a3")
        buf.write("\u01e2\3\2\2\2\u00a5\u0204\3\2\2\2\u00a7\u0211\3\2\2\2")
        buf.write("\u00a9\u0213\3\2\2\2\u00ab\u021b\3\2\2\2\u00ad\u0221\3")
        buf.write("\2\2\2\u00af\u0224\3\2\2\2\u00b1\u0230\3\2\2\2\u00b3\u023e")
        buf.write("\3\2\2\2\u00b5\u00b6\t\2\2\2\u00b6\4\3\2\2\2\u00b7\u00b8")
        buf.write("\t\3\2\2\u00b8\6\3\2\2\2\u00b9\u00ba\t\4\2\2\u00ba\b\3")
        buf.write("\2\2\2\u00bb\u00bc\t\5\2\2\u00bc\n\3\2\2\2\u00bd\u00be")
        buf.write("\t\6\2\2\u00be\f\3\2\2\2\u00bf\u00c0\t\7\2\2\u00c0\16")
        buf.write("\3\2\2\2\u00c1\u00c2\t\b\2\2\u00c2\20\3\2\2\2\u00c3\u00c4")
        buf.write("\t\t\2\2\u00c4\22\3\2\2\2\u00c5\u00c6\t\n\2\2\u00c6\24")
        buf.write("\3\2\2\2\u00c7\u00c8\t\13\2\2\u00c8\26\3\2\2\2\u00c9\u00ca")
        buf.write("\t\f\2\2\u00ca\30\3\2\2\2\u00cb\u00cc\t\r\2\2\u00cc\32")
        buf.write("\3\2\2\2\u00cd\u00ce\t\16\2\2\u00ce\34\3\2\2\2\u00cf\u00d0")
        buf.write("\t\17\2\2\u00d0\36\3\2\2\2\u00d1\u00d2\t\20\2\2\u00d2")
        buf.write(" \3\2\2\2\u00d3\u00d4\t\21\2\2\u00d4\"\3\2\2\2\u00d5\u00d6")
        buf.write("\t\22\2\2\u00d6$\3\2\2\2\u00d7\u00d8\t\23\2\2\u00d8&\3")
        buf.write("\2\2\2\u00d9\u00da\t\24\2\2\u00da(\3\2\2\2\u00db\u00dc")
        buf.write("\t\25\2\2\u00dc*\3\2\2\2\u00dd\u00de\t\26\2\2\u00de,\3")
        buf.write("\2\2\2\u00df\u00e0\t\27\2\2\u00e0.\3\2\2\2\u00e1\u00e2")
        buf.write("\t\30\2\2\u00e2\60\3\2\2\2\u00e3\u00e4\t\31\2\2\u00e4")
        buf.write("\62\3\2\2\2\u00e5\u00e6\t\32\2\2\u00e6\64\3\2\2\2\u00e7")
        buf.write("\u00e8\5\5\3\2\u00e8\u00e9\5\35\17\2\u00e9\u00ea\5\35")
        buf.write("\17\2\u00ea\u00eb\5\27\f\2\u00eb\u00ec\5\13\6\2\u00ec")
        buf.write("\u00ed\5\3\2\2\u00ed\u00ee\5\33\16\2\u00ee\66\3\2\2\2")
        buf.write("\u00ef\u00f0\5\5\3\2\u00f0\u00f1\5#\22\2\u00f1\u00f2\5")
        buf.write("\13\6\2\u00f2\u00f3\5\3\2\2\u00f3\u00f4\5\25\13\2\u00f4")
        buf.write("8\3\2\2\2\u00f5\u00f6\5\7\4\2\u00f6\u00f7\5\35\17\2\u00f7")
        buf.write("\u00f8\5\33\16\2\u00f8\u00f9\5\'\24\2\u00f9\u00fa\5\23")
        buf.write("\n\2\u00fa\u00fb\5\33\16\2\u00fb\u00fc\5)\25\2\u00fc\u00fd")
        buf.write("\5\13\6\2\u00fd:\3\2\2\2\u00fe\u00ff\5\13\6\2\u00ff\u0100")
        buf.write("\5\27\f\2\u0100\u0101\5%\23\2\u0101\u0102\5\13\6\2\u0102")
        buf.write("<\3\2\2\2\u0103\u0104\5\r\7\2\u0104\u0105\5\35\17\2\u0105")
        buf.write("\u0106\5#\22\2\u0106>\3\2\2\2\u0107\u0108\5#\22\2\u0108")
        buf.write("\u0109\5\13\6\2\u0109\u010a\5\3\2\2\u010a\u010b\5\27\f")
        buf.write("\2\u010b@\3\2\2\2\u010c\u010d\5\23\n\2\u010d\u010e\5\r")
        buf.write("\7\2\u010eB\3\2\2\2\u010f\u0110\5\23\n\2\u0110\u0111\5")
        buf.write("\33\16\2\u0111\u0112\5\'\24\2\u0112\u0113\5\13\6\2\u0113")
        buf.write("\u0114\5\17\b\2\u0114\u0115\5\13\6\2\u0115\u0116\5#\22")
        buf.write("\2\u0116D\3\2\2\2\u0117\u0118\5#\22\2\u0118\u0119\5\13")
        buf.write("\6\2\u0119\u011a\5\'\24\2\u011a\u011b\5)\25\2\u011b\u011c")
        buf.write("\5#\22\2\u011c\u011d\5\33\16\2\u011dF\3\2\2\2\u011e\u011f")
        buf.write("\5+\26\2\u011f\u0120\5\35\17\2\u0120\u0121\5\23\n\2\u0121")
        buf.write("\u0122\5\t\5\2\u0122H\3\2\2\2\u0123\u0124\5\t\5\2\u0124")
        buf.write("\u0125\5\35\17\2\u0125J\3\2\2\2\u0126\u0127\5-\27\2\u0127")
        buf.write("\u0128\5\21\t\2\u0128\u0129\5\23\n\2\u0129\u012a\5\27")
        buf.write("\f\2\u012a\u012b\5\13\6\2\u012bL\3\2\2\2\u012c\u012d\5")
        buf.write("%\23\2\u012d\u012e\5\'\24\2\u012e\u012f\5#\22\2\u012f")
        buf.write("\u0130\5\23\n\2\u0130\u0131\5\33\16\2\u0131\u0132\5\17")
        buf.write("\b\2\u0132N\3\2\2\2\u0133\u0134\5-\27\2\u0134\u0135\5")
        buf.write("\23\n\2\u0135\u0136\5\'\24\2\u0136\u0137\5\21\t\2\u0137")
        buf.write("P\3\2\2\2\u0138\u0139\5\'\24\2\u0139\u013a\5\35\17\2\u013a")
        buf.write("R\3\2\2\2\u013b\u013c\5\t\5\2\u013c\u013d\5\35\17\2\u013d")
        buf.write("\u013e\5-\27\2\u013e\u013f\5\33\16\2\u013f\u0140\5\'\24")
        buf.write("\2\u0140\u0141\5\35\17\2\u0141T\3\2\2\2\u0142\u0143\5")
        buf.write("\'\24\2\u0143\u0144\5\21\t\2\u0144\u0145\5\13\6\2\u0145")
        buf.write("\u0146\5\33\16\2\u0146V\3\2\2\2\u0147\u0148\5\5\3\2\u0148")
        buf.write("\u0149\5\13\6\2\u0149\u014a\5\17\b\2\u014a\u014b\5\23")
        buf.write("\n\2\u014b\u014c\5\33\16\2\u014cX\3\2\2\2\u014d\u014e")
        buf.write("\5\13\6\2\u014e\u014f\5\33\16\2\u014f\u0150\5\t\5\2\u0150")
        buf.write("Z\3\2\2\2\u0151\u0152\5\r\7\2\u0152\u0153\5)\25\2\u0153")
        buf.write("\u0154\5\33\16\2\u0154\u0155\5\7\4\2\u0155\u0156\5\'\24")
        buf.write("\2\u0156\u0157\5\23\n\2\u0157\u0158\5\35\17\2\u0158\u0159")
        buf.write("\5\33\16\2\u0159\\\3\2\2\2\u015a\u015b\5\37\20\2\u015b")
        buf.write("\u015c\5#\22\2\u015c\u015d\5\35\17\2\u015d\u015e\5\7\4")
        buf.write("\2\u015e\u015f\5\13\6\2\u015f\u0160\5\t\5\2\u0160\u0161")
        buf.write("\5)\25\2\u0161\u0162\5#\22\2\u0162\u0163\5\13\6\2\u0163")
        buf.write("^\3\2\2\2\u0164\u0165\5+\26\2\u0165\u0166\5\3\2\2\u0166")
        buf.write("\u0167\5#\22\2\u0167`\3\2\2\2\u0168\u0169\5\3\2\2\u0169")
        buf.write("\u016a\5#\22\2\u016a\u016b\5#\22\2\u016b\u016c\5\3\2\2")
        buf.write("\u016c\u016d\5\61\31\2\u016db\3\2\2\2\u016e\u016f\5\35")
        buf.write("\17\2\u016f\u0170\5\r\7\2\u0170d\3\2\2\2\u0171\u0172\7")
        buf.write("*\2\2\u0172\u0173\7,\2\2\u0173\u0177\3\2\2\2\u0174\u0176")
        buf.write("\13\2\2\2\u0175\u0174\3\2\2\2\u0176\u0179\3\2\2\2\u0177")
        buf.write("\u0178\3\2\2\2\u0177\u0175\3\2\2\2\u0178\u017a\3\2\2\2")
        buf.write("\u0179\u0177\3\2\2\2\u017a\u017b\7,\2\2\u017b\u017c\7")
        buf.write("+\2\2\u017c\u017d\3\2\2\2\u017d\u017e\b\63\2\2\u017ef")
        buf.write("\3\2\2\2\u017f\u0183\5\u009bN\2\u0180\u0182\13\2\2\2\u0181")
        buf.write("\u0180\3\2\2\2\u0182\u0185\3\2\2\2\u0183\u0184\3\2\2\2")
        buf.write("\u0183\u0181\3\2\2\2\u0184\u0186\3\2\2\2\u0185\u0183\3")
        buf.write("\2\2\2\u0186\u0187\5\u009dO\2\u0187\u0188\3\2\2\2\u0188")
        buf.write("\u0189\b\64\2\2\u0189h\3\2\2\2\u018a\u018b\7\61\2\2\u018b")
        buf.write("\u018c\7\61\2\2\u018c\u0190\3\2\2\2\u018d\u018f\n\33\2")
        buf.write("\2\u018e\u018d\3\2\2\2\u018f\u0192\3\2\2\2\u0190\u018e")
        buf.write("\3\2\2\2\u0190\u0191\3\2\2\2\u0191\u0193\3\2\2\2\u0192")
        buf.write("\u0190\3\2\2\2\u0193\u0194\b\65\2\2\u0194j\3\2\2\2\u0195")
        buf.write("\u0196\7<\2\2\u0196\u0197\7?\2\2\u0197l\3\2\2\2\u0198")
        buf.write("\u0199\7-\2\2\u0199n\3\2\2\2\u019a\u019b\7/\2\2\u019b")
        buf.write("p\3\2\2\2\u019c\u019d\7,\2\2\u019dr\3\2\2\2\u019e\u019f")
        buf.write("\7\61\2\2\u019ft\3\2\2\2\u01a0\u01a1\5\t\5\2\u01a1\u01a2")
        buf.write("\5\23\n\2\u01a2\u01a3\5+\26\2\u01a3v\3\2\2\2\u01a4\u01a5")
        buf.write("\5\31\r\2\u01a5\u01a6\5\35\17\2\u01a6\u01a7\5\t\5\2\u01a7")
        buf.write("x\3\2\2\2\u01a8\u01a9\7?\2\2\u01a9z\3\2\2\2\u01aa\u01ab")
        buf.write("\7@\2\2\u01ab|\3\2\2\2\u01ac\u01ad\7@\2\2\u01ad\u01ae")
        buf.write("\7?\2\2\u01ae~\3\2\2\2\u01af\u01b0\7>\2\2\u01b0\u0080")
        buf.write("\3\2\2\2\u01b1\u01b2\7>\2\2\u01b2\u01b3\7?\2\2\u01b3\u0082")
        buf.write("\3\2\2\2\u01b4\u01b5\5\3\2\2\u01b5\u01b6\5\33\16\2\u01b6")
        buf.write("\u01b7\5\t\5\2\u01b7\u0084\3\2\2\2\u01b8\u01b9\5\35\17")
        buf.write("\2\u01b9\u01ba\5#\22\2\u01ba\u0086\3\2\2\2\u01bb\u01bc")
        buf.write("\7>\2\2\u01bc\u01bd\7@\2\2\u01bd\u0088\3\2\2\2\u01be\u01bf")
        buf.write("\5\33\16\2\u01bf\u01c0\5\35\17\2\u01c0\u01c1\5\'\24\2")
        buf.write("\u01c1\u008a\3\2\2\2\u01c2\u01c3\7.\2\2\u01c3\u008c\3")
        buf.write("\2\2\2\u01c4\u01c5\7\60\2\2\u01c5\u01c6\7\60\2\2\u01c6")
        buf.write("\u008e\3\2\2\2\u01c7\u01c8\7<\2\2\u01c8\u0090\3\2\2\2")
        buf.write("\u01c9\u01ca\7=\2\2\u01ca\u0092\3\2\2\2\u01cb\u01cc\7")
        buf.write("]\2\2\u01cc\u0094\3\2\2\2\u01cd\u01ce\7_\2\2\u01ce\u0096")
        buf.write("\3\2\2\2\u01cf\u01d0\7*\2\2\u01d0\u0098\3\2\2\2\u01d1")
        buf.write("\u01d2\7+\2\2\u01d2\u009a\3\2\2\2\u01d3\u01d4\7}\2\2\u01d4")
        buf.write("\u009c\3\2\2\2\u01d5\u01d6\7\177\2\2\u01d6\u009e\3\2\2")
        buf.write("\2\u01d7\u01d9\t\34\2\2\u01d8\u01d7\3\2\2\2\u01d9\u01da")
        buf.write("\3\2\2\2\u01da\u01d8\3\2\2\2\u01da\u01db\3\2\2\2\u01db")
        buf.write("\u00a0\3\2\2\2\u01dc\u01de\t\34\2\2\u01dd\u01dc\3\2\2")
        buf.write("\2\u01de\u01df\3\2\2\2\u01df\u01dd\3\2\2\2\u01df\u01e0")
        buf.write("\3\2\2\2\u01e0\u00a2\3\2\2\2\u01e1\u01e3\t\6\2\2\u01e2")
        buf.write("\u01e1\3\2\2\2\u01e3\u01e5\3\2\2\2\u01e4\u01e6\7/\2\2")
        buf.write("\u01e5\u01e4\3\2\2\2\u01e5\u01e6\3\2\2\2\u01e6\u01e8\3")
        buf.write("\2\2\2\u01e7\u01e9\t\34\2\2\u01e8\u01e7\3\2\2\2\u01e9")
        buf.write("\u01ea\3\2\2\2\u01ea\u01e8\3\2\2\2\u01ea\u01eb\3\2\2\2")
        buf.write("\u01eb\u00a4\3\2\2\2\u01ec\u01ed\5\u009fP\2\u01ed\u01ee")
        buf.write("\7\60\2\2\u01ee\u0205\3\2\2\2\u01ef\u01f0\7\60\2\2\u01f0")
        buf.write("\u0205\5\u009fP\2\u01f1\u01f2\7\60\2\2\u01f2\u01f4\5\u009f")
        buf.write("P\2\u01f3\u01f5\5\u00a3R\2\u01f4\u01f3\3\2\2\2\u01f4\u01f5")
        buf.write("\3\2\2\2\u01f5\u0205\3\2\2\2\u01f6\u01f7\5\u009fP\2\u01f7")
        buf.write("\u01fb\7\60\2\2\u01f8\u01fa\t\34\2\2\u01f9\u01f8\3\2\2")
        buf.write("\2\u01fa\u01fd\3\2\2\2\u01fb\u01f9\3\2\2\2\u01fb\u01fc")
        buf.write("\3\2\2\2\u01fc\u01ff\3\2\2\2\u01fd\u01fb\3\2\2\2\u01fe")
        buf.write("\u0200\5\u00a3R\2\u01ff\u01fe\3\2\2\2\u01ff\u0200\3\2")
        buf.write("\2\2\u0200\u0205\3\2\2\2\u0201\u0202\5\u009fP\2\u0202")
        buf.write("\u0203\5\u00a3R\2\u0203\u0205\3\2\2\2\u0204\u01ec\3\2")
        buf.write("\2\2\u0204\u01ef\3\2\2\2\u0204\u01f1\3\2\2\2\u0204\u01f6")
        buf.write("\3\2\2\2\u0204\u0201\3\2\2\2\u0205\u00a6\3\2\2\2\u0206")
        buf.write("\u0207\5\'\24\2\u0207\u0208\5#\22\2\u0208\u0209\5)\25")
        buf.write("\2\u0209\u020a\5\13\6\2\u020a\u0212\3\2\2\2\u020b\u020c")
        buf.write("\5\r\7\2\u020c\u020d\5\3\2\2\u020d\u020e\5\27\f\2\u020e")
        buf.write("\u020f\5%\23\2\u020f\u0210\5\13\6\2\u0210\u0212\3\2\2")
        buf.write("\2\u0211\u0206\3\2\2\2\u0211\u020b\3\2\2\2\u0212\u00a8")
        buf.write("\3\2\2\2\u0213\u0217\t\35\2\2\u0214\u0216\t\36\2\2\u0215")
        buf.write("\u0214\3\2\2\2\u0216\u0219\3\2\2\2\u0217\u0215\3\2\2\2")
        buf.write("\u0217\u0218\3\2\2\2\u0218\u00aa\3\2\2\2\u0219\u0217\3")
        buf.write("\2\2\2\u021a\u021c\t\37\2\2\u021b\u021a\3\2\2\2\u021c")
        buf.write("\u021d\3\2\2\2\u021d\u021b\3\2\2\2\u021d\u021e\3\2\2\2")
        buf.write("\u021e\u021f\3\2\2\2\u021f\u0220\bV\2\2\u0220\u00ac\3")
        buf.write("\2\2\2\u0221\u0222\13\2\2\2\u0222\u0223\bW\3\2\u0223\u00ae")
        buf.write("\3\2\2\2\u0224\u022a\7$\2\2\u0225\u0226\7^\2\2\u0226\u0229")
        buf.write("\t \2\2\u0227\u0229\n!\2\2\u0228\u0225\3\2\2\2\u0228\u0227")
        buf.write("\3\2\2\2\u0229\u022c\3\2\2\2\u022a\u0228\3\2\2\2\u022a")
        buf.write("\u022b\3\2\2\2\u022b\u022d\3\2\2\2\u022c\u022a\3\2\2\2")
        buf.write("\u022d\u022e\7$\2\2\u022e\u022f\bX\4\2\u022f\u00b0\3\2")
        buf.write("\2\2\u0230\u0236\7$\2\2\u0231\u0232\7^\2\2\u0232\u0235")
        buf.write("\t \2\2\u0233\u0235\n\"\2\2\u0234\u0231\3\2\2\2\u0234")
        buf.write("\u0233\3\2\2\2\u0235\u0238\3\2\2\2\u0236\u0237\3\2\2\2")
        buf.write("\u0236\u0234\3\2\2\2\u0237\u0239\3\2\2\2\u0238\u0236\3")
        buf.write("\2\2\2\u0239\u023a\t#\2\2\u023a\u023b\n \2\2\u023b\u023c")
        buf.write("\3\2\2\2\u023c\u023d\bY\5\2\u023d\u00b2\3\2\2\2\u023e")
        buf.write("\u023f\7$\2\2\u023f\u0240\bZ\6\2\u0240\u00b4\3\2\2\2\26")
        buf.write("\2\u0177\u0183\u0190\u01da\u01df\u01e2\u01e5\u01ea\u01f4")
        buf.write("\u01fb\u01ff\u0204\u0211\u0217\u021d\u0228\u022a\u0234")
        buf.write("\u0236\7\b\2\2\3W\2\3X\3\3Y\4\3Z\5")
        return buf.getvalue()


class MPLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    BOOLEAN = 1
    BREAK = 2
    CONTINUE = 3
    ELSE = 4
    FOR = 5
    REAL = 6
    IF = 7
    INTEGER = 8
    RETURN = 9
    VOIDTYPE = 10
    DO = 11
    WHILE = 12
    STRING = 13
    WITH = 14
    TO = 15
    DOWNTO = 16
    THEN = 17
    BEGIN = 18
    END = 19
    FUNCTION = 20
    PROCEDURE = 21
    VAR = 22
    ARRAY = 23
    OF = 24
    TRADBLOCK = 25
    BLOCK = 26
    LINE = 27
    ASSIOP = 28
    ADDOP = 29
    SUBOP = 30
    MULOP = 31
    DIVOP = 32
    DIVINOP = 33
    MODOP = 34
    EQUOP = 35
    GTOP = 36
    GTEOP = 37
    LTOP = 38
    LTEOP = 39
    ANDOP = 40
    OROP = 41
    NEOP = 42
    NOTOP = 43
    COMMA = 44
    DOUDOT = 45
    COLON = 46
    SEMI = 47
    LSB = 48
    RSB = 49
    LB = 50
    RB = 51
    LP = 52
    RP = 53
    INTLIT = 54
    REALLIT = 55
    BOOLLIT = 56
    ID = 57
    WS = 58
    ERROR_CHAR = 59
    STRINGLIT = 60
    ILLEGAL_ESCAPE = 61
    UNCLOSE_STRING = 62

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "':='", "'+'", "'-'", "'*'", "'/'", "'='", "'>'", "'>='", "'<'", 
            "'<='", "'<>'", "','", "'..'", "':'", "';'", "'['", "']'", "'('", 
            "')'", "'{'", "'}'", "'\"'" ]

    symbolicNames = [ "<INVALID>",
            "BOOLEAN", "BREAK", "CONTINUE", "ELSE", "FOR", "REAL", "IF", 
            "INTEGER", "RETURN", "VOIDTYPE", "DO", "WHILE", "STRING", "WITH", 
            "TO", "DOWNTO", "THEN", "BEGIN", "END", "FUNCTION", "PROCEDURE", 
            "VAR", "ARRAY", "OF", "TRADBLOCK", "BLOCK", "LINE", "ASSIOP", 
            "ADDOP", "SUBOP", "MULOP", "DIVOP", "DIVINOP", "MODOP", "EQUOP", 
            "GTOP", "GTEOP", "LTOP", "LTEOP", "ANDOP", "OROP", "NEOP", "NOTOP", 
            "COMMA", "DOUDOT", "COLON", "SEMI", "LSB", "RSB", "LB", "RB", 
            "LP", "RP", "INTLIT", "REALLIT", "BOOLLIT", "ID", "WS", "ERROR_CHAR", 
            "STRINGLIT", "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

    ruleNames = [ "Ca", "Cb", "Cc", "Cd", "Ce", "Cf", "Cg", "Ch", "Ci", 
                  "Ck", "Cl", "Cm", "Cn", "Co", "Cp", "Cq", "Cr", "Cs", 
                  "Ct", "Cu", "Cv", "Cw", "Cx", "Cy", "Cz", "BOOLEAN", "BREAK", 
                  "CONTINUE", "ELSE", "FOR", "REAL", "IF", "INTEGER", "RETURN", 
                  "VOIDTYPE", "DO", "WHILE", "STRING", "WITH", "TO", "DOWNTO", 
                  "THEN", "BEGIN", "END", "FUNCTION", "PROCEDURE", "VAR", 
                  "ARRAY", "OF", "TRADBLOCK", "BLOCK", "LINE", "ASSIOP", 
                  "ADDOP", "SUBOP", "MULOP", "DIVOP", "DIVINOP", "MODOP", 
                  "EQUOP", "GTOP", "GTEOP", "LTOP", "LTEOP", "ANDOP", "OROP", 
                  "NEOP", "NOTOP", "COMMA", "DOUDOT", "COLON", "SEMI", "LSB", 
                  "RSB", "LB", "RB", "LP", "RP", "DIGIT", "INTLIT", "EXPONENT", 
                  "REALLIT", "BOOLLIT", "ID", "WS", "ERROR_CHAR", "STRINGLIT", 
                  "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

    grammarFileName = "MP.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[85] = self.ERROR_CHAR_action 
            actions[86] = self.STRINGLIT_action 
            actions[87] = self.ILLEGAL_ESCAPE_action 
            actions[88] = self.UNCLOSE_STRING_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
             
                        raise ErrorToken(self.text) 
                    
     

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                        s=self.text[1:-1]
                        self.text=s
                    
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                        
                         raise IllegalEscape(self.text[1:])
                    
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                        if self.text[-1]=='\n':
                            raise UncloseString(self.text[1:-1])
                        else:
                            raise UncloseString(self.text[1:])
                    
     


