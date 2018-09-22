# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2A")
        buf.write("\u0248\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("U\4V\tV\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\3\2\3\2\3\3\3\3")
        buf.write("\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3")
        buf.write("\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20")
        buf.write("\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25")
        buf.write("\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3 \3 \3")
        buf.write(" \3 \3 \3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3#\3")
        buf.write("#\3#\3#\3#\3#\3#\3$\3$\3$\3$\3$\3%\3%\3%\3&\3&\3&\3&\3")
        buf.write("&\3&\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3(\3(\3(\3)\3)\3")
        buf.write(")\3)\3)\3*\3*\3*\3+\3+\3+\3+\3+\3+\3+\3,\3,\3,\3,\3,\3")
        buf.write("-\3-\3-\3-\3-\3-\3.\3.\3.\3.\3/\3/\3/\3/\3/\3/\3/\3/\3")
        buf.write("/\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3")
        buf.write("\61\3\61\3\61\3\61\3\62\3\62\3\62\3\62\3\62\3\62\3\63")
        buf.write("\3\63\3\63\3\64\3\64\7\64\u017b\n\64\f\64\16\64\u017e")
        buf.write("\13\64\3\65\3\65\3\65\3\65\7\65\u0184\n\65\f\65\16\65")
        buf.write("\u0187\13\65\3\65\3\65\3\65\3\65\3\65\3\66\3\66\7\66\u0190")
        buf.write("\n\66\f\66\16\66\u0193\13\66\3\66\3\66\3\66\3\66\3\67")
        buf.write("\3\67\3\67\3\67\7\67\u019d\n\67\f\67\16\67\u01a0\13\67")
        buf.write("\3\67\3\67\38\38\38\39\39\3:\3:\3;\3;\3<\3<\3=\3=\3=\3")
        buf.write("=\3>\3>\3>\3>\3?\3?\3@\3@\3A\3A\3A\3B\3B\3C\3C\3C\3D\3")
        buf.write("D\3D\3D\3E\3E\3E\3F\3F\3F\3G\3G\3G\3G\3H\3H\3I\3I\3I\3")
        buf.write("J\3J\3K\3K\3L\3L\3M\3M\3N\3N\3O\3O\3P\3P\3Q\3Q\3R\6R\u01e7")
        buf.write("\nR\rR\16R\u01e8\3S\6S\u01ec\nS\rS\16S\u01ed\3T\5T\u01f1")
        buf.write("\nT\3T\5T\u01f4\nT\3T\6T\u01f7\nT\rT\16T\u01f8\3U\3U\3")
        buf.write("U\3U\3U\3U\3U\3U\5U\u0203\nU\3U\3U\3U\7U\u0208\nU\fU\16")
        buf.write("U\u020b\13U\3U\5U\u020e\nU\3U\3U\3U\5U\u0213\nU\3V\3V")
        buf.write("\3V\3V\3V\3V\3V\3V\3V\3V\3V\5V\u0220\nV\3W\6W\u0223\n")
        buf.write("W\rW\16W\u0224\3W\3W\3X\3X\3X\3Y\3Y\3Y\3Y\7Y\u0230\nY")
        buf.write("\fY\16Y\u0233\13Y\3Y\3Y\3Y\3Z\3Z\3Z\3Z\7Z\u023c\nZ\fZ")
        buf.write("\16Z\u023f\13Z\3Z\3Z\3Z\3Z\3Z\3[\3[\3[\5\u0185\u0191\u023d")
        buf.write("\2\\\3\2\5\2\7\2\t\2\13\2\r\2\17\2\21\2\23\2\25\2\27\2")
        buf.write("\31\2\33\2\35\2\37\2!\2#\2%\2\'\2)\2+\2-\2/\2\61\2\63")
        buf.write("\2\65\3\67\49\5;\6=\7?\bA\tC\nE\13G\fI\rK\16M\17O\20Q")
        buf.write("\21S\22U\23W\24Y\25[\26]\27_\30a\31c\32e\33g\34i\35k\36")
        buf.write("m\37o q!s\"u#w$y%{&}\'\177(\u0081)\u0083*\u0085+\u0087")
        buf.write(",\u0089-\u008b.\u008d/\u008f\60\u0091\61\u0093\62\u0095")
        buf.write("\63\u0097\64\u0099\65\u009b\66\u009d\67\u009f8\u00a19")
        buf.write("\u00a3\2\u00a5:\u00a7\2\u00a9;\u00ab<\u00ad=\u00af>\u00b1")
        buf.write("?\u00b3@\u00b5A\3\2$\4\2CCcc\4\2DDdd\4\2EEee\4\2FFff\4")
        buf.write("\2GGgg\4\2HHhh\4\2IIii\4\2JJjj\4\2KKkk\4\2MMmm\4\2NNn")
        buf.write("n\4\2OOoo\4\2PPpp\4\2QQqq\4\2RRrr\4\2SSss\4\2TTtt\4\2")
        buf.write("UUuu\4\2VVvv\4\2WWww\4\2XXxx\4\2YYyy\4\2ZZzz\4\2[[{{\4")
        buf.write("\2\\\\||\5\2C\\aac|\6\2\62;C\\aac|\4\2\f\f\17\17\3\2\62")
        buf.write(";\5\2\13\f\16\17\"\"\n\2$$))^^ddhhppttvv\b\2\f\f\17\17")
        buf.write("$$GHQQ^^\4\2$$^^\3\2^^\2\u0241\2\65\3\2\2\2\2\67\3\2\2")
        buf.write("\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2")
        buf.write("\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3")
        buf.write("\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U")
        buf.write("\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2")
        buf.write("_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2")
        buf.write("\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2")
        buf.write("\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2")
        buf.write("\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083")
        buf.write("\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2")
        buf.write("\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091")
        buf.write("\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2")
        buf.write("\2\2\u0099\3\2\2\2\2\u009b\3\2\2\2\2\u009d\3\2\2\2\2\u009f")
        buf.write("\3\2\2\2\2\u00a1\3\2\2\2\2\u00a5\3\2\2\2\2\u00a9\3\2\2")
        buf.write("\2\2\u00ab\3\2\2\2\2\u00ad\3\2\2\2\2\u00af\3\2\2\2\2\u00b1")
        buf.write("\3\2\2\2\2\u00b3\3\2\2\2\2\u00b5\3\2\2\2\3\u00b7\3\2\2")
        buf.write("\2\5\u00b9\3\2\2\2\7\u00bb\3\2\2\2\t\u00bd\3\2\2\2\13")
        buf.write("\u00bf\3\2\2\2\r\u00c1\3\2\2\2\17\u00c3\3\2\2\2\21\u00c5")
        buf.write("\3\2\2\2\23\u00c7\3\2\2\2\25\u00c9\3\2\2\2\27\u00cb\3")
        buf.write("\2\2\2\31\u00cd\3\2\2\2\33\u00cf\3\2\2\2\35\u00d1\3\2")
        buf.write("\2\2\37\u00d3\3\2\2\2!\u00d5\3\2\2\2#\u00d7\3\2\2\2%\u00d9")
        buf.write("\3\2\2\2\'\u00db\3\2\2\2)\u00dd\3\2\2\2+\u00df\3\2\2\2")
        buf.write("-\u00e1\3\2\2\2/\u00e3\3\2\2\2\61\u00e5\3\2\2\2\63\u00e7")
        buf.write("\3\2\2\2\65\u00e9\3\2\2\2\67\u00f1\3\2\2\29\u00f7\3\2")
        buf.write("\2\2;\u0100\3\2\2\2=\u0105\3\2\2\2?\u0109\3\2\2\2A\u010e")
        buf.write("\3\2\2\2C\u0111\3\2\2\2E\u0119\3\2\2\2G\u0120\3\2\2\2")
        buf.write("I\u0125\3\2\2\2K\u0128\3\2\2\2M\u012e\3\2\2\2O\u0133\3")
        buf.write("\2\2\2Q\u013a\3\2\2\2S\u013f\3\2\2\2U\u0142\3\2\2\2W\u0149")
        buf.write("\3\2\2\2Y\u014e\3\2\2\2[\u0154\3\2\2\2]\u0158\3\2\2\2")
        buf.write("_\u0161\3\2\2\2a\u016b\3\2\2\2c\u016f\3\2\2\2e\u0175\3")
        buf.write("\2\2\2g\u0178\3\2\2\2i\u017f\3\2\2\2k\u018d\3\2\2\2m\u0198")
        buf.write("\3\2\2\2o\u01a3\3\2\2\2q\u01a6\3\2\2\2s\u01a8\3\2\2\2")
        buf.write("u\u01aa\3\2\2\2w\u01ac\3\2\2\2y\u01ae\3\2\2\2{\u01b2\3")
        buf.write("\2\2\2}\u01b6\3\2\2\2\177\u01b8\3\2\2\2\u0081\u01ba\3")
        buf.write("\2\2\2\u0083\u01bd\3\2\2\2\u0085\u01bf\3\2\2\2\u0087\u01c2")
        buf.write("\3\2\2\2\u0089\u01c6\3\2\2\2\u008b\u01c9\3\2\2\2\u008d")
        buf.write("\u01cc\3\2\2\2\u008f\u01d0\3\2\2\2\u0091\u01d2\3\2\2\2")
        buf.write("\u0093\u01d5\3\2\2\2\u0095\u01d7\3\2\2\2\u0097\u01d9\3")
        buf.write("\2\2\2\u0099\u01db\3\2\2\2\u009b\u01dd\3\2\2\2\u009d\u01df")
        buf.write("\3\2\2\2\u009f\u01e1\3\2\2\2\u00a1\u01e3\3\2\2\2\u00a3")
        buf.write("\u01e6\3\2\2\2\u00a5\u01eb\3\2\2\2\u00a7\u01f0\3\2\2\2")
        buf.write("\u00a9\u0212\3\2\2\2\u00ab\u021f\3\2\2\2\u00ad\u0222\3")
        buf.write("\2\2\2\u00af\u0228\3\2\2\2\u00b1\u022b\3\2\2\2\u00b3\u0237")
        buf.write("\3\2\2\2\u00b5\u0245\3\2\2\2\u00b7\u00b8\t\2\2\2\u00b8")
        buf.write("\4\3\2\2\2\u00b9\u00ba\t\3\2\2\u00ba\6\3\2\2\2\u00bb\u00bc")
        buf.write("\t\4\2\2\u00bc\b\3\2\2\2\u00bd\u00be\t\5\2\2\u00be\n\3")
        buf.write("\2\2\2\u00bf\u00c0\t\6\2\2\u00c0\f\3\2\2\2\u00c1\u00c2")
        buf.write("\t\7\2\2\u00c2\16\3\2\2\2\u00c3\u00c4\t\b\2\2\u00c4\20")
        buf.write("\3\2\2\2\u00c5\u00c6\t\t\2\2\u00c6\22\3\2\2\2\u00c7\u00c8")
        buf.write("\t\n\2\2\u00c8\24\3\2\2\2\u00c9\u00ca\t\13\2\2\u00ca\26")
        buf.write("\3\2\2\2\u00cb\u00cc\t\f\2\2\u00cc\30\3\2\2\2\u00cd\u00ce")
        buf.write("\t\r\2\2\u00ce\32\3\2\2\2\u00cf\u00d0\t\16\2\2\u00d0\34")
        buf.write("\3\2\2\2\u00d1\u00d2\t\17\2\2\u00d2\36\3\2\2\2\u00d3\u00d4")
        buf.write("\t\20\2\2\u00d4 \3\2\2\2\u00d5\u00d6\t\21\2\2\u00d6\"")
        buf.write("\3\2\2\2\u00d7\u00d8\t\22\2\2\u00d8$\3\2\2\2\u00d9\u00da")
        buf.write("\t\23\2\2\u00da&\3\2\2\2\u00db\u00dc\t\24\2\2\u00dc(\3")
        buf.write("\2\2\2\u00dd\u00de\t\25\2\2\u00de*\3\2\2\2\u00df\u00e0")
        buf.write("\t\26\2\2\u00e0,\3\2\2\2\u00e1\u00e2\t\27\2\2\u00e2.\3")
        buf.write("\2\2\2\u00e3\u00e4\t\30\2\2\u00e4\60\3\2\2\2\u00e5\u00e6")
        buf.write("\t\31\2\2\u00e6\62\3\2\2\2\u00e7\u00e8\t\32\2\2\u00e8")
        buf.write("\64\3\2\2\2\u00e9\u00ea\5\5\3\2\u00ea\u00eb\5\35\17\2")
        buf.write("\u00eb\u00ec\5\35\17\2\u00ec\u00ed\5\27\f\2\u00ed\u00ee")
        buf.write("\5\13\6\2\u00ee\u00ef\5\3\2\2\u00ef\u00f0\5\33\16\2\u00f0")
        buf.write("\66\3\2\2\2\u00f1\u00f2\5\5\3\2\u00f2\u00f3\5#\22\2\u00f3")
        buf.write("\u00f4\5\13\6\2\u00f4\u00f5\5\3\2\2\u00f5\u00f6\5\25\13")
        buf.write("\2\u00f68\3\2\2\2\u00f7\u00f8\5\7\4\2\u00f8\u00f9\5\35")
        buf.write("\17\2\u00f9\u00fa\5\33\16\2\u00fa\u00fb\5\'\24\2\u00fb")
        buf.write("\u00fc\5\23\n\2\u00fc\u00fd\5\33\16\2\u00fd\u00fe\5)\25")
        buf.write("\2\u00fe\u00ff\5\13\6\2\u00ff:\3\2\2\2\u0100\u0101\5\13")
        buf.write("\6\2\u0101\u0102\5\27\f\2\u0102\u0103\5%\23\2\u0103\u0104")
        buf.write("\5\13\6\2\u0104<\3\2\2\2\u0105\u0106\5\r\7\2\u0106\u0107")
        buf.write("\5\35\17\2\u0107\u0108\5#\22\2\u0108>\3\2\2\2\u0109\u010a")
        buf.write("\5#\22\2\u010a\u010b\5\13\6\2\u010b\u010c\5\3\2\2\u010c")
        buf.write("\u010d\5\27\f\2\u010d@\3\2\2\2\u010e\u010f\5\23\n\2\u010f")
        buf.write("\u0110\5\r\7\2\u0110B\3\2\2\2\u0111\u0112\5\23\n\2\u0112")
        buf.write("\u0113\5\33\16\2\u0113\u0114\5\'\24\2\u0114\u0115\5\13")
        buf.write("\6\2\u0115\u0116\5\17\b\2\u0116\u0117\5\13\6\2\u0117\u0118")
        buf.write("\5#\22\2\u0118D\3\2\2\2\u0119\u011a\5#\22\2\u011a\u011b")
        buf.write("\5\13\6\2\u011b\u011c\5\'\24\2\u011c\u011d\5)\25\2\u011d")
        buf.write("\u011e\5#\22\2\u011e\u011f\5\33\16\2\u011fF\3\2\2\2\u0120")
        buf.write("\u0121\5+\26\2\u0121\u0122\5\35\17\2\u0122\u0123\5\23")
        buf.write("\n\2\u0123\u0124\5\t\5\2\u0124H\3\2\2\2\u0125\u0126\5")
        buf.write("\t\5\2\u0126\u0127\5\35\17\2\u0127J\3\2\2\2\u0128\u0129")
        buf.write("\5-\27\2\u0129\u012a\5\21\t\2\u012a\u012b\5\23\n\2\u012b")
        buf.write("\u012c\5\27\f\2\u012c\u012d\5\13\6\2\u012dL\3\2\2\2\u012e")
        buf.write("\u012f\5\31\r\2\u012f\u0130\5\3\2\2\u0130\u0131\5\23\n")
        buf.write("\2\u0131\u0132\5\33\16\2\u0132N\3\2\2\2\u0133\u0134\5")
        buf.write("%\23\2\u0134\u0135\5\'\24\2\u0135\u0136\5#\22\2\u0136")
        buf.write("\u0137\5\23\n\2\u0137\u0138\5\33\16\2\u0138\u0139\5\17")
        buf.write("\b\2\u0139P\3\2\2\2\u013a\u013b\5-\27\2\u013b\u013c\5")
        buf.write("\23\n\2\u013c\u013d\5\'\24\2\u013d\u013e\5\21\t\2\u013e")
        buf.write("R\3\2\2\2\u013f\u0140\5\'\24\2\u0140\u0141\5\35\17\2\u0141")
        buf.write("T\3\2\2\2\u0142\u0143\5\t\5\2\u0143\u0144\5\35\17\2\u0144")
        buf.write("\u0145\5-\27\2\u0145\u0146\5\33\16\2\u0146\u0147\5\'\24")
        buf.write("\2\u0147\u0148\5\35\17\2\u0148V\3\2\2\2\u0149\u014a\5")
        buf.write("\'\24\2\u014a\u014b\5\21\t\2\u014b\u014c\5\13\6\2\u014c")
        buf.write("\u014d\5\33\16\2\u014dX\3\2\2\2\u014e\u014f\5\5\3\2\u014f")
        buf.write("\u0150\5\13\6\2\u0150\u0151\5\17\b\2\u0151\u0152\5\23")
        buf.write("\n\2\u0152\u0153\5\33\16\2\u0153Z\3\2\2\2\u0154\u0155")
        buf.write("\5\13\6\2\u0155\u0156\5\33\16\2\u0156\u0157\5\t\5\2\u0157")
        buf.write("\\\3\2\2\2\u0158\u0159\5\r\7\2\u0159\u015a\5)\25\2\u015a")
        buf.write("\u015b\5\33\16\2\u015b\u015c\5\7\4\2\u015c\u015d\5\'\24")
        buf.write("\2\u015d\u015e\5\23\n\2\u015e\u015f\5\35\17\2\u015f\u0160")
        buf.write("\5\33\16\2\u0160^\3\2\2\2\u0161\u0162\5\37\20\2\u0162")
        buf.write("\u0163\5#\22\2\u0163\u0164\5\35\17\2\u0164\u0165\5\7\4")
        buf.write("\2\u0165\u0166\5\13\6\2\u0166\u0167\5\t\5\2\u0167\u0168")
        buf.write("\5)\25\2\u0168\u0169\5#\22\2\u0169\u016a\5\13\6\2\u016a")
        buf.write("`\3\2\2\2\u016b\u016c\5+\26\2\u016c\u016d\5\3\2\2\u016d")
        buf.write("\u016e\5#\22\2\u016eb\3\2\2\2\u016f\u0170\5\3\2\2\u0170")
        buf.write("\u0171\5#\22\2\u0171\u0172\5#\22\2\u0172\u0173\5\3\2\2")
        buf.write("\u0173\u0174\5\61\31\2\u0174d\3\2\2\2\u0175\u0176\5\35")
        buf.write("\17\2\u0176\u0177\5\r\7\2\u0177f\3\2\2\2\u0178\u017c\t")
        buf.write("\33\2\2\u0179\u017b\t\34\2\2\u017a\u0179\3\2\2\2\u017b")
        buf.write("\u017e\3\2\2\2\u017c\u017a\3\2\2\2\u017c\u017d\3\2\2\2")
        buf.write("\u017dh\3\2\2\2\u017e\u017c\3\2\2\2\u017f\u0180\7*\2\2")
        buf.write("\u0180\u0181\7,\2\2\u0181\u0185\3\2\2\2\u0182\u0184\13")
        buf.write("\2\2\2\u0183\u0182\3\2\2\2\u0184\u0187\3\2\2\2\u0185\u0186")
        buf.write("\3\2\2\2\u0185\u0183\3\2\2\2\u0186\u0188\3\2\2\2\u0187")
        buf.write("\u0185\3\2\2\2\u0188\u0189\7,\2\2\u0189\u018a\7+\2\2\u018a")
        buf.write("\u018b\3\2\2\2\u018b\u018c\b\65\2\2\u018cj\3\2\2\2\u018d")
        buf.write("\u0191\5\u009fP\2\u018e\u0190\13\2\2\2\u018f\u018e\3\2")
        buf.write("\2\2\u0190\u0193\3\2\2\2\u0191\u0192\3\2\2\2\u0191\u018f")
        buf.write("\3\2\2\2\u0192\u0194\3\2\2\2\u0193\u0191\3\2\2\2\u0194")
        buf.write("\u0195\5\u00a1Q\2\u0195\u0196\3\2\2\2\u0196\u0197\b\66")
        buf.write("\2\2\u0197l\3\2\2\2\u0198\u0199\7\61\2\2\u0199\u019a\7")
        buf.write("\61\2\2\u019a\u019e\3\2\2\2\u019b\u019d\n\35\2\2\u019c")
        buf.write("\u019b\3\2\2\2\u019d\u01a0\3\2\2\2\u019e\u019c\3\2\2\2")
        buf.write("\u019e\u019f\3\2\2\2\u019f\u01a1\3\2\2\2\u01a0\u019e\3")
        buf.write("\2\2\2\u01a1\u01a2\b\67\2\2\u01a2n\3\2\2\2\u01a3\u01a4")
        buf.write("\7<\2\2\u01a4\u01a5\7?\2\2\u01a5p\3\2\2\2\u01a6\u01a7")
        buf.write("\7-\2\2\u01a7r\3\2\2\2\u01a8\u01a9\7/\2\2\u01a9t\3\2\2")
        buf.write("\2\u01aa\u01ab\7,\2\2\u01abv\3\2\2\2\u01ac\u01ad\7\61")
        buf.write("\2\2\u01adx\3\2\2\2\u01ae\u01af\5\t\5\2\u01af\u01b0\5")
        buf.write("\23\n\2\u01b0\u01b1\5+\26\2\u01b1z\3\2\2\2\u01b2\u01b3")
        buf.write("\5\31\r\2\u01b3\u01b4\5\35\17\2\u01b4\u01b5\5\t\5\2\u01b5")
        buf.write("|\3\2\2\2\u01b6\u01b7\7?\2\2\u01b7~\3\2\2\2\u01b8\u01b9")
        buf.write("\7@\2\2\u01b9\u0080\3\2\2\2\u01ba\u01bb\7@\2\2\u01bb\u01bc")
        buf.write("\7?\2\2\u01bc\u0082\3\2\2\2\u01bd\u01be\7>\2\2\u01be\u0084")
        buf.write("\3\2\2\2\u01bf\u01c0\7>\2\2\u01c0\u01c1\7?\2\2\u01c1\u0086")
        buf.write("\3\2\2\2\u01c2\u01c3\5\3\2\2\u01c3\u01c4\5\33\16\2\u01c4")
        buf.write("\u01c5\5\t\5\2\u01c5\u0088\3\2\2\2\u01c6\u01c7\5\35\17")
        buf.write("\2\u01c7\u01c8\5#\22\2\u01c8\u008a\3\2\2\2\u01c9\u01ca")
        buf.write("\7>\2\2\u01ca\u01cb\7@\2\2\u01cb\u008c\3\2\2\2\u01cc\u01cd")
        buf.write("\5\33\16\2\u01cd\u01ce\5\35\17\2\u01ce\u01cf\5\'\24\2")
        buf.write("\u01cf\u008e\3\2\2\2\u01d0\u01d1\7.\2\2\u01d1\u0090\3")
        buf.write("\2\2\2\u01d2\u01d3\7\60\2\2\u01d3\u01d4\7\60\2\2\u01d4")
        buf.write("\u0092\3\2\2\2\u01d5\u01d6\7<\2\2\u01d6\u0094\3\2\2\2")
        buf.write("\u01d7\u01d8\7=\2\2\u01d8\u0096\3\2\2\2\u01d9\u01da\7")
        buf.write("]\2\2\u01da\u0098\3\2\2\2\u01db\u01dc\7_\2\2\u01dc\u009a")
        buf.write("\3\2\2\2\u01dd\u01de\7*\2\2\u01de\u009c\3\2\2\2\u01df")
        buf.write("\u01e0\7+\2\2\u01e0\u009e\3\2\2\2\u01e1\u01e2\7}\2\2\u01e2")
        buf.write("\u00a0\3\2\2\2\u01e3\u01e4\7\177\2\2\u01e4\u00a2\3\2\2")
        buf.write("\2\u01e5\u01e7\t\36\2\2\u01e6\u01e5\3\2\2\2\u01e7\u01e8")
        buf.write("\3\2\2\2\u01e8\u01e6\3\2\2\2\u01e8\u01e9\3\2\2\2\u01e9")
        buf.write("\u00a4\3\2\2\2\u01ea\u01ec\t\36\2\2\u01eb\u01ea\3\2\2")
        buf.write("\2\u01ec\u01ed\3\2\2\2\u01ed\u01eb\3\2\2\2\u01ed\u01ee")
        buf.write("\3\2\2\2\u01ee\u00a6\3\2\2\2\u01ef\u01f1\t\6\2\2\u01f0")
        buf.write("\u01ef\3\2\2\2\u01f1\u01f3\3\2\2\2\u01f2\u01f4\7/\2\2")
        buf.write("\u01f3\u01f2\3\2\2\2\u01f3\u01f4\3\2\2\2\u01f4\u01f6\3")
        buf.write("\2\2\2\u01f5\u01f7\t\36\2\2\u01f6\u01f5\3\2\2\2\u01f7")
        buf.write("\u01f8\3\2\2\2\u01f8\u01f6\3\2\2\2\u01f8\u01f9\3\2\2\2")
        buf.write("\u01f9\u00a8\3\2\2\2\u01fa\u01fb\5\u00a3R\2\u01fb\u01fc")
        buf.write("\7\60\2\2\u01fc\u0213\3\2\2\2\u01fd\u01fe\7\60\2\2\u01fe")
        buf.write("\u0213\5\u00a3R\2\u01ff\u0200\7\60\2\2\u0200\u0202\5\u00a3")
        buf.write("R\2\u0201\u0203\5\u00a7T\2\u0202\u0201\3\2\2\2\u0202\u0203")
        buf.write("\3\2\2\2\u0203\u0213\3\2\2\2\u0204\u0205\5\u00a3R\2\u0205")
        buf.write("\u0209\7\60\2\2\u0206\u0208\t\36\2\2\u0207\u0206\3\2\2")
        buf.write("\2\u0208\u020b\3\2\2\2\u0209\u0207\3\2\2\2\u0209\u020a")
        buf.write("\3\2\2\2\u020a\u020d\3\2\2\2\u020b\u0209\3\2\2\2\u020c")
        buf.write("\u020e\5\u00a7T\2\u020d\u020c\3\2\2\2\u020d\u020e\3\2")
        buf.write("\2\2\u020e\u0213\3\2\2\2\u020f\u0210\5\u00a3R\2\u0210")
        buf.write("\u0211\5\u00a7T\2\u0211\u0213\3\2\2\2\u0212\u01fa\3\2")
        buf.write("\2\2\u0212\u01fd\3\2\2\2\u0212\u01ff\3\2\2\2\u0212\u0204")
        buf.write("\3\2\2\2\u0212\u020f\3\2\2\2\u0213\u00aa\3\2\2\2\u0214")
        buf.write("\u0215\5\'\24\2\u0215\u0216\5#\22\2\u0216\u0217\5)\25")
        buf.write("\2\u0217\u0218\5\13\6\2\u0218\u0220\3\2\2\2\u0219\u021a")
        buf.write("\5\r\7\2\u021a\u021b\5\3\2\2\u021b\u021c\5\27\f\2\u021c")
        buf.write("\u021d\5%\23\2\u021d\u021e\5\13\6\2\u021e\u0220\3\2\2")
        buf.write("\2\u021f\u0214\3\2\2\2\u021f\u0219\3\2\2\2\u0220\u00ac")
        buf.write("\3\2\2\2\u0221\u0223\t\37\2\2\u0222\u0221\3\2\2\2\u0223")
        buf.write("\u0224\3\2\2\2\u0224\u0222\3\2\2\2\u0224\u0225\3\2\2\2")
        buf.write("\u0225\u0226\3\2\2\2\u0226\u0227\bW\2\2\u0227\u00ae\3")
        buf.write("\2\2\2\u0228\u0229\13\2\2\2\u0229\u022a\bX\3\2\u022a\u00b0")
        buf.write("\3\2\2\2\u022b\u0231\7$\2\2\u022c\u022d\7^\2\2\u022d\u0230")
        buf.write("\t \2\2\u022e\u0230\n!\2\2\u022f\u022c\3\2\2\2\u022f\u022e")
        buf.write("\3\2\2\2\u0230\u0233\3\2\2\2\u0231\u022f\3\2\2\2\u0231")
        buf.write("\u0232\3\2\2\2\u0232\u0234\3\2\2\2\u0233\u0231\3\2\2\2")
        buf.write("\u0234\u0235\7$\2\2\u0235\u0236\bY\4\2\u0236\u00b2\3\2")
        buf.write("\2\2\u0237\u023d\7$\2\2\u0238\u0239\7^\2\2\u0239\u023c")
        buf.write("\t \2\2\u023a\u023c\n\"\2\2\u023b\u0238\3\2\2\2\u023b")
        buf.write("\u023a\3\2\2\2\u023c\u023f\3\2\2\2\u023d\u023e\3\2\2\2")
        buf.write("\u023d\u023b\3\2\2\2\u023e\u0240\3\2\2\2\u023f\u023d\3")
        buf.write("\2\2\2\u0240\u0241\t#\2\2\u0241\u0242\n \2\2\u0242\u0243")
        buf.write("\3\2\2\2\u0243\u0244\bZ\5\2\u0244\u00b4\3\2\2\2\u0245")
        buf.write("\u0246\7$\2\2\u0246\u0247\b[\6\2\u0247\u00b6\3\2\2\2\26")
        buf.write("\2\u017c\u0185\u0191\u019e\u01e8\u01ed\u01f0\u01f3\u01f8")
        buf.write("\u0202\u0209\u020d\u0212\u021f\u0224\u022f\u0231\u023b")
        buf.write("\u023d\7\b\2\2\3X\2\3Y\3\3Z\4\3[\5")
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
    MAIN = 13
    STRING = 14
    WITH = 15
    TO = 16
    DOWNTO = 17
    THEN = 18
    BEGIN = 19
    END = 20
    FUNCTION = 21
    PROCEDURE = 22
    VAR = 23
    ARRAY = 24
    OF = 25
    ID = 26
    TRADBLOCK = 27
    BLOCK = 28
    LINE = 29
    ASSIOP = 30
    ADDOP = 31
    SUBOP = 32
    MULOP = 33
    DIVOP = 34
    DIVINOP = 35
    MODOP = 36
    EQUOP = 37
    GTOP = 38
    GTEOP = 39
    LTOP = 40
    LTEOP = 41
    ANDOP = 42
    OROP = 43
    NEOP = 44
    NOTOP = 45
    COMMA = 46
    DOUDOT = 47
    COLON = 48
    SEMI = 49
    LSB = 50
    RSB = 51
    LB = 52
    RB = 53
    LP = 54
    RP = 55
    INTLIT = 56
    REALLIT = 57
    BOOLLIT = 58
    WS = 59
    ERROR_CHAR = 60
    STRINGLIT = 61
    ILLEGAL_ESCAPE = 62
    UNCLOSE_STRING = 63

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "':='", "'+'", "'-'", "'*'", "'/'", "'='", "'>'", "'>='", "'<'", 
            "'<='", "'<>'", "','", "'..'", "':'", "';'", "'['", "']'", "'('", 
            "')'", "'{'", "'}'", "'\"'" ]

    symbolicNames = [ "<INVALID>",
            "BOOLEAN", "BREAK", "CONTINUE", "ELSE", "FOR", "REAL", "IF", 
            "INTEGER", "RETURN", "VOIDTYPE", "DO", "WHILE", "MAIN", "STRING", 
            "WITH", "TO", "DOWNTO", "THEN", "BEGIN", "END", "FUNCTION", 
            "PROCEDURE", "VAR", "ARRAY", "OF", "ID", "TRADBLOCK", "BLOCK", 
            "LINE", "ASSIOP", "ADDOP", "SUBOP", "MULOP", "DIVOP", "DIVINOP", 
            "MODOP", "EQUOP", "GTOP", "GTEOP", "LTOP", "LTEOP", "ANDOP", 
            "OROP", "NEOP", "NOTOP", "COMMA", "DOUDOT", "COLON", "SEMI", 
            "LSB", "RSB", "LB", "RB", "LP", "RP", "INTLIT", "REALLIT", "BOOLLIT", 
            "WS", "ERROR_CHAR", "STRINGLIT", "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

    ruleNames = [ "Ca", "Cb", "Cc", "Cd", "Ce", "Cf", "Cg", "Ch", "Ci", 
                  "Ck", "Cl", "Cm", "Cn", "Co", "Cp", "Cq", "Cr", "Cs", 
                  "Ct", "Cu", "Cv", "Cw", "Cx", "Cy", "Cz", "BOOLEAN", "BREAK", 
                  "CONTINUE", "ELSE", "FOR", "REAL", "IF", "INTEGER", "RETURN", 
                  "VOIDTYPE", "DO", "WHILE", "MAIN", "STRING", "WITH", "TO", 
                  "DOWNTO", "THEN", "BEGIN", "END", "FUNCTION", "PROCEDURE", 
                  "VAR", "ARRAY", "OF", "ID", "TRADBLOCK", "BLOCK", "LINE", 
                  "ASSIOP", "ADDOP", "SUBOP", "MULOP", "DIVOP", "DIVINOP", 
                  "MODOP", "EQUOP", "GTOP", "GTEOP", "LTOP", "LTEOP", "ANDOP", 
                  "OROP", "NEOP", "NOTOP", "COMMA", "DOUDOT", "COLON", "SEMI", 
                  "LSB", "RSB", "LB", "RB", "LP", "RP", "DIGIT", "INTLIT", 
                  "EXPONENT", "REALLIT", "BOOLLIT", "WS", "ERROR_CHAR", 
                  "STRINGLIT", "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

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
            actions[86] = self.ERROR_CHAR_action 
            actions[87] = self.STRINGLIT_action 
            actions[88] = self.ILLEGAL_ESCAPE_action 
            actions[89] = self.UNCLOSE_STRING_action 
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
                    
     


