# Generated from /Users/labtop/PyCharm/BioScript/grammar/grammar/BSParser.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

#/* parser/listener/visitor header section */

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\u00b7")
        buf.write("\u01b1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\3\2\6\2`\n\2\r\2\16\2a\3\2\5\2e\n\2\3\2\3\2\3\2\7")
        buf.write("\2j\n\2\f\2\16\2m\13\2\3\2\3\2\3\3\3\3\3\3\5\3t\n\3\3")
        buf.write("\4\3\4\3\4\3\5\5\5z\n\5\3\5\3\5\3\5\3\6\5\6\u0080\n\6")
        buf.write("\3\6\3\6\3\6\3\7\3\7\3\7\6\7\u0088\n\7\r\7\16\7\u0089")
        buf.write("\3\b\3\b\3\b\3\b\5\b\u0090\n\b\3\b\3\b\7\b\u0094\n\b\f")
        buf.write("\b\16\b\u0097\13\b\3\b\3\b\3\b\3\t\3\t\5\t\u009e\n\t\3")
        buf.write("\t\3\t\3\n\3\n\3\n\7\n\u00a5\n\n\f\n\16\n\u00a8\13\n\3")
        buf.write("\13\5\13\u00ab\n\13\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3\r")
        buf.write("\3\r\5\r\u00b6\n\r\3\16\3\16\7\16\u00ba\n\16\f\16\16\16")
        buf.write("\u00bd\13\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\5\17\u00d0")
        buf.write("\n\17\3\20\3\20\3\20\3\20\3\20\5\20\u00d7\n\20\3\21\3")
        buf.write("\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\23\5\23\u00e3")
        buf.write("\n\23\3\23\3\23\3\23\3\23\3\23\3\23\5\23\u00eb\n\23\3")
        buf.write("\23\3\23\5\23\u00ef\n\23\3\24\3\24\3\24\3\24\5\24\u00f5")
        buf.write("\n\24\3\25\5\25\u00f8\n\25\3\25\3\25\3\25\5\25\u00fd\n")
        buf.write("\25\3\25\3\25\3\25\5\25\u0102\n\25\3\25\3\25\3\25\5\25")
        buf.write("\u0107\n\25\3\25\3\25\5\25\u010b\n\25\3\25\3\25\5\25\u010f")
        buf.write("\n\25\3\26\3\26\3\26\5\26\u0114\n\26\3\26\3\26\3\27\3")
        buf.write("\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\5\30")
        buf.write("\u0123\n\30\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3")
        buf.write("\32\5\32\u012e\n\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\35")
        buf.write("\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\5\36\u014e\n\36\3\37\3\37\3\37\3\37\3\37\3\37\3")
        buf.write("\37\3\37\5\37\u0158\n\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\5\37\u0164\n\37\3 \3 \3 \3 \7 \u016a")
        buf.write("\n \f \16 \u016d\13 \3 \3 \3!\3!\3!\3\"\3\"\3\"\5\"\u0177")
        buf.write("\n\"\3\"\3\"\3#\3#\3#\7#\u017e\n#\f#\16#\u0181\13#\3$")
        buf.write("\3$\5$\u0185\n$\3%\3%\3%\3%\3&\3&\3&\7&\u018e\n&\f&\16")
        buf.write("&\u0191\13&\3\'\5\'\u0194\n\'\3\'\3\'\3\'\3(\3(\3(\3(")
        buf.write("\5(\u019d\n(\3)\3)\5)\u01a1\n)\3*\3*\3+\3+\3,\3,\3-\3")
        buf.write("-\3.\3.\3/\3/\3/\3/\3/\2\2\60\2\4\6\b\n\f\16\20\22\24")
        buf.write("\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVX")
        buf.write("Z\\\2\13\3\2#(\4\2OPTT\3\2MN\4\2?@FG\4\2EEHH\3\2IJ\3\2")
        buf.write(".\61\3\2),\4\2\61\61m\u00b4\2\u01ba\2_\3\2\2\2\4s\3\2")
        buf.write("\2\2\6u\3\2\2\2\by\3\2\2\2\n\177\3\2\2\2\f\u0084\3\2\2")
        buf.write("\2\16\u008b\3\2\2\2\20\u009b\3\2\2\2\22\u00a1\3\2\2\2")
        buf.write("\24\u00aa\3\2\2\2\26\u00ae\3\2\2\2\30\u00b5\3\2\2\2\32")
        buf.write("\u00b7\3\2\2\2\34\u00cf\3\2\2\2\36\u00d1\3\2\2\2 \u00d8")
        buf.write("\3\2\2\2\"\u00dc\3\2\2\2$\u00e2\3\2\2\2&\u00f4\3\2\2\2")
        buf.write("(\u00f7\3\2\2\2*\u0110\3\2\2\2,\u0117\3\2\2\2.\u011b\3")
        buf.write("\2\2\2\60\u0124\3\2\2\2\62\u012a\3\2\2\2\64\u0131\3\2")
        buf.write("\2\2\66\u013d\3\2\2\28\u0140\3\2\2\2:\u014d\3\2\2\2<\u0163")
        buf.write("\3\2\2\2>\u0165\3\2\2\2@\u0170\3\2\2\2B\u0173\3\2\2\2")
        buf.write("D\u017a\3\2\2\2F\u0184\3\2\2\2H\u0186\3\2\2\2J\u018a\3")
        buf.write("\2\2\2L\u0193\3\2\2\2N\u0198\3\2\2\2P\u01a0\3\2\2\2R\u01a2")
        buf.write("\3\2\2\2T\u01a4\3\2\2\2V\u01a6\3\2\2\2X\u01a8\3\2\2\2")
        buf.write("Z\u01aa\3\2\2\2\\\u01ac\3\2\2\2^`\5\4\3\2_^\3\2\2\2`a")
        buf.write("\3\2\2\2a_\3\2\2\2ab\3\2\2\2bd\3\2\2\2ce\5\f\7\2dc\3\2")
        buf.write("\2\2de\3\2\2\2ef\3\2\2\2fg\7\r\2\2gk\7D\2\2hj\5\34\17")
        buf.write("\2ih\3\2\2\2jm\3\2\2\2ki\3\2\2\2kl\3\2\2\2ln\3\2\2\2m")
        buf.write("k\3\2\2\2no\7\2\2\3o\3\3\2\2\2pt\5\6\4\2qt\5\b\5\2rt\5")
        buf.write("\n\6\2sp\3\2\2\2sq\3\2\2\2sr\3\2\2\2t\5\3\2\2\2uv\7\n")
        buf.write("\2\2vw\7-\2\2w\7\3\2\2\2xz\5H%\2yx\3\2\2\2yz\3\2\2\2z")
        buf.write("{\3\2\2\2{|\7\t\2\2|}\7-\2\2}\t\3\2\2\2~\u0080\5H%\2\177")
        buf.write("~\3\2\2\2\177\u0080\3\2\2\2\u0080\u0081\3\2\2\2\u0081")
        buf.write("\u0082\7\13\2\2\u0082\u0083\7-\2\2\u0083\13\3\2\2\2\u0084")
        buf.write("\u0085\7\f\2\2\u0085\u0087\7D\2\2\u0086\u0088\5\16\b\2")
        buf.write("\u0087\u0086\3\2\2\2\u0088\u0089\3\2\2\2\u0089\u0087\3")
        buf.write("\2\2\2\u0089\u008a\3\2\2\2\u008a\r\3\2\2\2\u008b\u008c")
        buf.write("\7\7\2\2\u008c\u008d\7-\2\2\u008d\u008f\5\20\t\2\u008e")
        buf.write("\u0090\5\26\f\2\u008f\u008e\3\2\2\2\u008f\u0090\3\2\2")
        buf.write("\2\u0090\u0091\3\2\2\2\u0091\u0095\7\67\2\2\u0092\u0094")
        buf.write("\5\34\17\2\u0093\u0092\3\2\2\2\u0094\u0097\3\2\2\2\u0095")
        buf.write("\u0093\3\2\2\2\u0095\u0096\3\2\2\2\u0096\u0098\3\2\2\2")
        buf.write("\u0097\u0095\3\2\2\2\u0098\u0099\5\30\r\2\u0099\u009a")
        buf.write("\78\2\2\u009a\17\3\2\2\2\u009b\u009d\7\65\2\2\u009c\u009e")
        buf.write("\5\22\n\2\u009d\u009c\3\2\2\2\u009d\u009e\3\2\2\2\u009e")
        buf.write("\u009f\3\2\2\2\u009f\u00a0\7\66\2\2\u00a0\21\3\2\2\2\u00a1")
        buf.write("\u00a6\5\24\13\2\u00a2\u00a3\7<\2\2\u00a3\u00a5\5\24\13")
        buf.write("\2\u00a4\u00a2\3\2\2\2\u00a5\u00a8\3\2\2\2\u00a6\u00a4")
        buf.write("\3\2\2\2\u00a6\u00a7\3\2\2\2\u00a7\23\3\2\2\2\u00a8\u00a6")
        buf.write("\3\2\2\2\u00a9\u00ab\5H%\2\u00aa\u00a9\3\2\2\2\u00aa\u00ab")
        buf.write("\3\2\2\2\u00ab\u00ac\3\2\2\2\u00ac\u00ad\7-\2\2\u00ad")
        buf.write("\25\3\2\2\2\u00ae\u00af\7D\2\2\u00af\u00b0\5H%\2\u00b0")
        buf.write("\27\3\2\2\2\u00b1\u00b2\7\b\2\2\u00b2\u00b6\5P)\2\u00b3")
        buf.write("\u00b4\7\b\2\2\u00b4\u00b6\5B\"\2\u00b5\u00b1\3\2\2\2")
        buf.write("\u00b5\u00b3\3\2\2\2\u00b6\31\3\2\2\2\u00b7\u00bb\7\67")
        buf.write("\2\2\u00b8\u00ba\5\34\17\2\u00b9\u00b8\3\2\2\2\u00ba\u00bd")
        buf.write("\3\2\2\2\u00bb\u00b9\3\2\2\2\u00bb\u00bc\3\2\2\2\u00bc")
        buf.write("\u00be\3\2\2\2\u00bd\u00bb\3\2\2\2\u00be\u00bf\78\2\2")
        buf.write("\u00bf\33\3\2\2\2\u00c0\u00d0\5\36\20\2\u00c1\u00d0\5")
        buf.write(" \21\2\u00c2\u00d0\5L\'\2\u00c3\u00d0\5\"\22\2\u00c4\u00d0")
        buf.write("\5$\23\2\u00c5\u00d0\5&\24\2\u00c6\u00d0\5(\25\2\u00c7")
        buf.write("\u00d0\5\62\32\2\u00c8\u00d0\5\60\31\2\u00c9\u00d0\5@")
        buf.write("!\2\u00ca\u00d0\5\64\33\2\u00cb\u00d0\5.\30\2\u00cc\u00d0")
        buf.write("\5\66\34\2\u00cd\u00d0\5:\36\2\u00ce\u00d0\58\35\2\u00cf")
        buf.write("\u00c0\3\2\2\2\u00cf\u00c1\3\2\2\2\u00cf\u00c2\3\2\2\2")
        buf.write("\u00cf\u00c3\3\2\2\2\u00cf\u00c4\3\2\2\2\u00cf\u00c5\3")
        buf.write("\2\2\2\u00cf\u00c6\3\2\2\2\u00cf\u00c7\3\2\2\2\u00cf\u00c8")
        buf.write("\3\2\2\2\u00cf\u00c9\3\2\2\2\u00cf\u00ca\3\2\2\2\u00cf")
        buf.write("\u00cb\3\2\2\2\u00cf\u00cc\3\2\2\2\u00cf\u00cd\3\2\2\2")
        buf.write("\u00cf\u00ce\3\2\2\2\u00d0\35\3\2\2\2\u00d1\u00d2\7\3")
        buf.write("\2\2\u00d2\u00d3\5> \2\u00d3\u00d6\5\32\16\2\u00d4\u00d5")
        buf.write("\7\4\2\2\u00d5\u00d7\5\32\16\2\u00d6\u00d4\3\2\2\2\u00d6")
        buf.write("\u00d7\3\2\2\2\u00d7\37\3\2\2\2\u00d8\u00d9\7\6\2\2\u00d9")
        buf.write("\u00da\5> \2\u00da\u00db\5\32\16\2\u00db!\3\2\2\2\u00dc")
        buf.write("\u00dd\7\5\2\2\u00dd\u00de\7\61\2\2\u00de\u00df\7\35\2")
        buf.write("\2\u00df\u00e0\5\32\16\2\u00e0#\3\2\2\2\u00e1\u00e3\5")
        buf.write("*\26\2\u00e2\u00e1\3\2\2\2\u00e2\u00e3\3\2\2\2\u00e3\u00e4")
        buf.write("\3\2\2\2\u00e4\u00e5\7\22\2\2\u00e5\u00e6\5N(\2\u00e6")
        buf.write("\u00e7\7\31\2\2\u00e7\u00ea\5Z.\2\u00e8\u00e9\7\36\2\2")
        buf.write("\u00e9\u00eb\5N(\2\u00ea\u00e8\3\2\2\2\u00ea\u00eb\3\2")
        buf.write("\2\2\u00eb\u00ee\3\2\2\2\u00ec\u00ed\7\33\2\2\u00ed\u00ef")
        buf.write("\5X-\2\u00ee\u00ec\3\2\2\2\u00ee\u00ef\3\2\2\2\u00ef%")
        buf.write("\3\2\2\2\u00f0\u00f1\7\23\2\2\u00f1\u00f5\5N(\2\u00f2")
        buf.write("\u00f3\7\25\2\2\u00f3\u00f5\5N(\2\u00f4\u00f0\3\2\2\2")
        buf.write("\u00f4\u00f2\3\2\2\2\u00f5\'\3\2\2\2\u00f6\u00f8\5*\26")
        buf.write("\2\u00f7\u00f6\3\2\2\2\u00f7\u00f8\3\2\2\2\u00f8\u00f9")
        buf.write("\3\2\2\2\u00f9\u00fa\5L\'\2\u00fa\u00fc\7\17\2\2\u00fb")
        buf.write("\u00fd\5\\/\2\u00fc\u00fb\3\2\2\2\u00fc\u00fd\3\2\2\2")
        buf.write("\u00fd\u00fe\3\2\2\2\u00fe\u010a\5N(\2\u00ff\u0101\7\32")
        buf.write("\2\2\u0100\u0102\5\\/\2\u0101\u0100\3\2\2\2\u0101\u0102")
        buf.write("\3\2\2\2\u0102\u0103\3\2\2\2\u0103\u0106\5N(\2\u0104\u0105")
        buf.write("\7\36\2\2\u0105\u0107\5N(\2\u0106\u0104\3\2\2\2\u0106")
        buf.write("\u0107\3\2\2\2\u0107\u010b\3\2\2\2\u0108\u0109\7\36\2")
        buf.write("\2\u0109\u010b\5N(\2\u010a\u00ff\3\2\2\2\u010a\u0108\3")
        buf.write("\2\2\2\u010b\u010e\3\2\2\2\u010c\u010d\7\33\2\2\u010d")
        buf.write("\u010f\5X-\2\u010e\u010c\3\2\2\2\u010e\u010f\3\2\2\2\u010f")
        buf.write(")\3\2\2\2\u0110\u0111\7V\2\2\u0111\u0113\7\"\2\2\u0112")
        buf.write("\u0114\5,\27\2\u0113\u0112\3\2\2\2\u0113\u0114\3\2\2\2")
        buf.write("\u0114\u0115\3\2\2\2\u0115\u0116\5X-\2\u0116+\3\2\2\2")
        buf.write("\u0117\u0118\7\65\2\2\u0118\u0119\t\2\2\2\u0119\u011a")
        buf.write("\7\66\2\2\u011a-\3\2\2\2\u011b\u011c\5L\'\2\u011c\u011d")
        buf.write("\7\16\2\2\u011d\u011e\7-\2\2\u011e\u011f\7\36\2\2\u011f")
        buf.write("\u0122\5N(\2\u0120\u0121\7\33\2\2\u0121\u0123\5X-\2\u0122")
        buf.write("\u0120\3\2\2\2\u0122\u0123\3\2\2\2\u0123/\3\2\2\2\u0124")
        buf.write("\u0125\5L\'\2\u0125\u0126\7\21\2\2\u0126\u0127\5N(\2\u0127")
        buf.write("\u0128\7\34\2\2\u0128\u0129\7\61\2\2\u0129\61\3\2\2\2")
        buf.write("\u012a\u012b\5L\'\2\u012b\u012d\7\24\2\2\u012c\u012e\5")
        buf.write("\\/\2\u012d\u012c\3\2\2\2\u012d\u012e\3\2\2\2\u012e\u012f")
        buf.write("\3\2\2\2\u012f\u0130\7-\2\2\u0130\63\3\2\2\2\u0131\u0132")
        buf.write("\5L\'\2\u0132\u0133\7\26\2\2\u0133\u0134\5N(\2\u0134\u0135")
        buf.write("\7\32\2\2\u0135\u0136\5N(\2\u0136\u0137\7\30\2\2\u0137")
        buf.write("\u0138\7\60\2\2\u0138\u0139\7<\2\2\u0139\u013a\7\60\2")
        buf.write("\2\u013a\u013b\7\31\2\2\u013b\u013c\7\60\2\2\u013c\65")
        buf.write("\3\2\2\2\u013d\u013e\7\27\2\2\u013e\u013f\5N(\2\u013f")
        buf.write("\67\3\2\2\2\u0140\u0141\5L\'\2\u0141\u0142\5R*\2\u0142")
        buf.write("9\3\2\2\2\u0143\u0144\5L\'\2\u0144\u0145\5P)\2\u0145\u0146")
        buf.write("\t\3\2\2\u0146\u0147\5P)\2\u0147\u014e\3\2\2\2\u0148\u0149")
        buf.write("\5L\'\2\u0149\u014a\5P)\2\u014a\u014b\t\4\2\2\u014b\u014c")
        buf.write("\5P)\2\u014c\u014e\3\2\2\2\u014d\u0143\3\2\2\2\u014d\u0148")
        buf.write("\3\2\2\2\u014e;\3\2\2\2\u014f\u0157\5P)\2\u0150\u0151")
        buf.write("\7@\2\2\u0151\u0158\7@\2\2\u0152\u0153\7?\2\2\u0153\u0154")
        buf.write("\7?\2\2\u0154\u0158\7?\2\2\u0155\u0156\7?\2\2\u0156\u0158")
        buf.write("\7?\2\2\u0157\u0150\3\2\2\2\u0157\u0152\3\2\2\2\u0157")
        buf.write("\u0155\3\2\2\2\u0158\u0159\3\2\2\2\u0159\u015a\5P)\2\u015a")
        buf.write("\u0164\3\2\2\2\u015b\u015c\5P)\2\u015c\u015d\t\5\2\2\u015d")
        buf.write("\u015e\5P)\2\u015e\u0164\3\2\2\2\u015f\u0160\5P)\2\u0160")
        buf.write("\u0161\t\6\2\2\u0161\u0162\5P)\2\u0162\u0164\3\2\2\2\u0163")
        buf.write("\u014f\3\2\2\2\u0163\u015b\3\2\2\2\u0163\u015f\3\2\2\2")
        buf.write("\u0164=\3\2\2\2\u0165\u0166\7\65\2\2\u0166\u016b\5<\37")
        buf.write("\2\u0167\u0168\t\7\2\2\u0168\u016a\5<\37\2\u0169\u0167")
        buf.write("\3\2\2\2\u016a\u016d\3\2\2\2\u016b\u0169\3\2\2\2\u016b")
        buf.write("\u016c\3\2\2\2\u016c\u016e\3\2\2\2\u016d\u016b\3\2\2\2")
        buf.write("\u016e\u016f\7\66\2\2\u016f?\3\2\2\2\u0170\u0171\5L\'")
        buf.write("\2\u0171\u0172\5B\"\2\u0172A\3\2\2\2\u0173\u0174\7-\2")
        buf.write("\2\u0174\u0176\7\65\2\2\u0175\u0177\5D#\2\u0176\u0175")
        buf.write("\3\2\2\2\u0176\u0177\3\2\2\2\u0177\u0178\3\2\2\2\u0178")
        buf.write("\u0179\7\66\2\2\u0179C\3\2\2\2\u017a\u017f\5P)\2\u017b")
        buf.write("\u017c\7<\2\2\u017c\u017e\5P)\2\u017d\u017b\3\2\2\2\u017e")
        buf.write("\u0181\3\2\2\2\u017f\u017d\3\2\2\2\u017f\u0180\3\2\2\2")
        buf.write("\u0180E\3\2\2\2\u0181\u017f\3\2\2\2\u0182\u0185\5T+\2")
        buf.write("\u0183\u0185\5V,\2\u0184\u0182\3\2\2\2\u0184\u0183\3\2")
        buf.write("\2\2\u0185G\3\2\2\2\u0186\u0187\79\2\2\u0187\u0188\5J")
        buf.write("&\2\u0188\u0189\7:\2\2\u0189I\3\2\2\2\u018a\u018f\5F$")
        buf.write("\2\u018b\u018c\7;\2\2\u018c\u018e\5F$\2\u018d\u018b\3")
        buf.write("\2\2\2\u018e\u0191\3\2\2\2\u018f\u018d\3\2\2\2\u018f\u0190")
        buf.write("\3\2\2\2\u0190K\3\2\2\2\u0191\u018f\3\2\2\2\u0192\u0194")
        buf.write("\5H%\2\u0193\u0192\3\2\2\2\u0193\u0194\3\2\2\2\u0194\u0195")
        buf.write("\3\2\2\2\u0195\u0196\5N(\2\u0196\u0197\7>\2\2\u0197M\3")
        buf.write("\2\2\2\u0198\u019c\7-\2\2\u0199\u019a\79\2\2\u019a\u019b")
        buf.write("\7\61\2\2\u019b\u019d\7:\2\2\u019c\u0199\3\2\2\2\u019c")
        buf.write("\u019d\3\2\2\2\u019dO\3\2\2\2\u019e\u01a1\5R*\2\u019f")
        buf.write("\u01a1\5N(\2\u01a0\u019e\3\2\2\2\u01a0\u019f\3\2\2\2\u01a1")
        buf.write("Q\3\2\2\2\u01a2\u01a3\t\b\2\2\u01a3S\3\2\2\2\u01a4\u01a5")
        buf.write("\t\t\2\2\u01a5U\3\2\2\2\u01a6\u01a7\t\n\2\2\u01a7W\3\2")
        buf.write("\2\2\u01a8\u01a9\7\62\2\2\u01a9Y\3\2\2\2\u01aa\u01ab\7")
        buf.write("\64\2\2\u01ab[\3\2\2\2\u01ac\u01ad\7\61\2\2\u01ad\u01ae")
        buf.write("\7!\2\2\u01ae\u01af\7 \2\2\u01af]\3\2\2\2*adksy\177\u0089")
        buf.write("\u008f\u0095\u009d\u00a6\u00aa\u00b5\u00bb\u00cf\u00d6")
        buf.write("\u00e2\u00ea\u00ee\u00f4\u00f7\u00fc\u0101\u0106\u010a")
        buf.write("\u010e\u0113\u0122\u012d\u014d\u0157\u0163\u016b\u0176")
        buf.write("\u017f\u0184\u018f\u0193\u019c\u01a0")
        return buf.getvalue()


class BSParser ( Parser ):

    grammarFileName = "BSParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'else'", "'repeat'", "'while'", 
                     "'function'", "'return'", "'manifest'", "'module'", 
                     "'stationary'", "'functions'", "'instructions'", "'detect'", 
                     "'mix'", "'send'", "'split'", "'heat'", "'drain'", 
                     "'dispense'", "'dispose'", "'gradient'", "'store'", 
                     "'range'", "'at'", "'with'", "'for'", "'into'", "'times'", 
                     "'on'", "'to'", "'of'", "'units'", "'usein'", "'start <='", 
                     "'start'", "'start >='", "'finish <='", "'finish'", 
                     "'finish >='", "'nat'", "'real'", "'mat'", "'bool'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'('", "')'", "'{'", "'}'", "'['", "']'", "';'", "','", 
                     "'.'", "'='", "'>'", "'<'", "'!'", "'~'", "'?'", "':'", 
                     "'=='", "'<='", "'>='", "'!='", "'&&'", "'||'", "'++'", 
                     "'--'", "'+'", "'-'", "'*'", "'/'", "'&'", "'|'", "'^'", 
                     "'%'", "'_'", "'@'", "'ns'", "'us'", "'ms'", "'cs'", 
                     "'ds'", "'s'", "'m'", "'h'", "'d'", "'w'", "'mo'", 
                     "'y'", "'nL'", "'uL'", "'mL'", "'cL'", "'dL'", "'L'", 
                     "'daL'", "'c'", "'f'", "'k'", "'1'", "'2'", "'3'", 
                     "'4'", "'5'", "'6'", "'7'", "'8'", "'9'", "'10'", "'11'", 
                     "'12'", "'13'", "'14'", "'15'", "'16'", "'17'", "'18'", 
                     "'19'", "'20'", "'21'", "'22'", "'23'", "'24'", "'25'", 
                     "'26'", "'27'", "'28'", "'29'", "'30'", "'31'", "'32'", 
                     "'33'", "'34'", "'35'", "'37'", "'38'", "'39'", "'40'", 
                     "'42'", "'44'", "'45'", "'46'", "'47'", "'48'", "'49'", 
                     "'50'", "'51'", "'55'", "'58'", "'59'", "'60'", "'61'", 
                     "'62'", "'63'", "'64'", "'65'", "'66'", "'68'", "'69'", 
                     "'70'", "'71'", "'72'", "'73'", "'74'", "'75'", "'76'", 
                     "'98'", "'99'", "'100'", "'134'", "'-1'" ]

    symbolicNames = [ "<INVALID>", "IF", "ELSE", "REPEAT", "WHILE", "FUNCTION", 
                      "RETURN", "MANIFEST", "MODULE", "STATIONARY", "FUNCTIONS", 
                      "INSTRUCTIONS", "DETECT", "MIX", "SEND", "SPLIT", 
                      "HEAT", "DRAIN", "DISPENSE", "DISPOSE", "GRADIENT", 
                      "STORE", "RANGE", "AT", "WITH", "FOR", "INTO", "TIMES", 
                      "ON", "TO", "OF", "UNITS", "USEIN", "SLE", "SEQ", 
                      "SGE", "FLE", "FEQ", "FGE", "NAT", "REAL", "MAT", 
                      "BOOL", "IDENTIFIER", "STRING_LITERAL", "BOOL_LITERAL", 
                      "FLOAT_LITERAL", "INTEGER_LITERAL", "TIME_NUMBER", 
                      "VOLUME_NUMBER", "TEMP_NUMBER", "LPAREN", "RPAREN", 
                      "LBRACE", "RBRACE", "LBRACKET", "RBRACKET", "SEMICOLON", 
                      "COMMA", "DOT", "ASSIGN", "GT", "LT", "BANG", "TILDE", 
                      "QUESTION", "COLON", "EQUALITY", "LTE", "GTE", "NOTEQUAL", 
                      "AND", "OR", "INC", "DEC", "ADDITION", "SUBTRACT", 
                      "MULTIPLY", "DIVIDE", "BITAND", "BITOR", "CARET", 
                      "MOD", "UNDERSCORE", "ATSIGN", "NANOSECOND", "MICROSECOND", 
                      "MILLISECOND", "CENTISECOND", "DECISECOND", "SECOND", 
                      "MINUTE", "HOUR", "DAY", "WEEK", "MONTH", "YEAR", 
                      "NANOLITRE", "MICROLITRE", "MILLILITRE", "CENTILITRE", 
                      "DECILITRE", "LITRE", "DECALITRE", "CELSIUS", "FAHRENHEIT", 
                      "KELVIN", "ACIDS_STRONG_NON_OXIDIZING", "ACIDS_STRONG_OXIDIZING", 
                      "ACIDS_CARBOXYLIC", "ALCOHOLS_AND_POLYOLS", "ALDEHYDES", 
                      "AMIDES_AND_IMIDES", "AMINES_PHOSPHINES_AND_PYRIDINES", 
                      "AZO_DIAZO_AZIDO_HYDRAZINE_AND_AZIDE_COMPOUNDS", "CARBAMATES", 
                      "BASES_STRONG", "CYANIDES_INORGANIC", "THIOCARBAMATE_ESTERS_AND_SALTS_DITHIOCARBAMATE_ESTERS_AND_SALTS", 
                      "ESTERS_SULFATE_ESTERS_PHOSPHATE_ESTERS_THIOPHOSPHATE_ESTERS_AND_BORATE_ESTERS", 
                      "ETHERS", "FLUORIDES_INORGANIC", "HYDROCARBONS_AROMATIC", 
                      "HALOGENATED_ORGANIC_COMPOUNDS", "ISOCYANATES_AND_ISOTHIOCYANATES", 
                      "KETONES", "SULFIDES_ORGANIC", "METALS_ALKALI_VERY_ACTIVE", 
                      "METALS_ELEMENTAL_AND_POWDER_ACTIVE", "METALS_LESS_REACTIVE", 
                      "METALS_AND_METAL_COMPOUNDS_TOXIC", "DIAZONIUM_SALTS", 
                      "NITRILES", "NITRO_NITROSO_NITRATE_AND_NITRITE_COMPOUNDS_ORGANIC", 
                      "HYDROCARBONS_ALIPHATIC_UNSATURATED", "HYDROCARBONS_ALIPHATIC_SATURATED", 
                      "PEROXIDES_ORGANIC", "PHENOLS_AND_CRESOLS", "SULFONATES_PHOSPHONATES_AND_THIOPHOSPHONATES_ORGANIC", 
                      "SULFIDES_INORGANIC", "EPOXIDES", "METAL_HYDRIDES_METAL_ALKYLS_METAL_ARYLS_AND_SILANES", 
                      "ANHYDRIDES", "SALTS_ACIDIC", "SALTS_BASIC", "ACYL_HALIDES_SULFONYL_HALIDES_AND_CHLOROFORMATES", 
                      "ORGANOMETALLICS", "OXIDIZING_AGENTS_STRONG", "REDUCING_AGENTS_STRONG", 
                      "NON_REDOX_ACTIVE_INORGANIC_COMPOUNDS", "FLUORINATED_ORGANIC_COMPOUNDS", 
                      "FLUORIDE_SALTS_SOLUBLE", "OXIDIZING_AGENTS_WEAK", 
                      "REDUCING_AGENTS_WEAK", "NITRIDES_PHOSPHIDES_CARBIDES_AND_SILICIDES", 
                      "CHLOROSILANES", "SILOXANES", "HALOGENATING_AGENTS", 
                      "ACIDS_WEAK", "BASES_WEAK", "CARBONATE_SALTS", "ALKYNES_WITH_ACETYLENIC_HYDROGEN", 
                      "ALKYNES_WITH_NO_ACETYLENIC_HYDROGEN", "CONJUGATED_DIENES", 
                      "ARYL_HALIDES", "AMINES_AROMATIC", "NITRATE_AND_NITRITE_COMPOUNDS_INORGANIC", 
                      "ACETALS_KETALS_HEMIACETALS_AND_HEMIKETALS", "ACRYLATES_AND_ACRYLIC_ACIDS", 
                      "PHENOLIC_SALTS", "QUATERNARY_AMMONIUM_AND_PHOSPHONIUM_SALTS", 
                      "SULFITE_AND_THIOSULFATE_SALTS", "OXIMES", "POLYMERIZABLE_COMPOUNDS", 
                      "NOT_CHEMICALLY_REACTIVE", "INSUFFICIENT_INFORMATION_FOR_CLASSIFICATION", 
                      "WATER_AND_AQUEOUS_SOLUTIONS", "NULL", "UNKNOWN", 
                      "WS", "COMMENT", "LINE_COMMENT" ]

    RULE_program = 0
    RULE_globalDeclarations = 1
    RULE_moduleDeclaration = 2
    RULE_manifestDeclaration = 3
    RULE_stationaryDeclaration = 4
    RULE_functions = 5
    RULE_functionDeclaration = 6
    RULE_formalParameters = 7
    RULE_formalParameterList = 8
    RULE_formalParameter = 9
    RULE_functionTyping = 10
    RULE_returnStatement = 11
    RULE_blockStatement = 12
    RULE_statements = 13
    RULE_ifStatement = 14
    RULE_whileStatement = 15
    RULE_repeat = 16
    RULE_heat = 17
    RULE_dispose = 18
    RULE_mix = 19
    RULE_usein = 20
    RULE_useinType = 21
    RULE_detect = 22
    RULE_split = 23
    RULE_dispense = 24
    RULE_gradient = 25
    RULE_store = 26
    RULE_numberAssignment = 27
    RULE_math = 28
    RULE_binops = 29
    RULE_parExpression = 30
    RULE_methodInvocation = 31
    RULE_methodCall = 32
    RULE_expressionList = 33
    RULE_typeType = 34
    RULE_unionType = 35
    RULE_typesList = 36
    RULE_variableDefinition = 37
    RULE_variable = 38
    RULE_primary = 39
    RULE_literal = 40
    RULE_primitiveType = 41
    RULE_chemicalType = 42
    RULE_timeIdentifier = 43
    RULE_temperatureIdentifier = 44
    RULE_unitTracker = 45

    ruleNames =  [ "program", "globalDeclarations", "moduleDeclaration", 
                   "manifestDeclaration", "stationaryDeclaration", "functions", 
                   "functionDeclaration", "formalParameters", "formalParameterList", 
                   "formalParameter", "functionTyping", "returnStatement", 
                   "blockStatement", "statements", "ifStatement", "whileStatement", 
                   "repeat", "heat", "dispose", "mix", "usein", "useinType", 
                   "detect", "split", "dispense", "gradient", "store", "numberAssignment", 
                   "math", "binops", "parExpression", "methodInvocation", 
                   "methodCall", "expressionList", "typeType", "unionType", 
                   "typesList", "variableDefinition", "variable", "primary", 
                   "literal", "primitiveType", "chemicalType", "timeIdentifier", 
                   "temperatureIdentifier", "unitTracker" ]

    EOF = Token.EOF
    IF=1
    ELSE=2
    REPEAT=3
    WHILE=4
    FUNCTION=5
    RETURN=6
    MANIFEST=7
    MODULE=8
    STATIONARY=9
    FUNCTIONS=10
    INSTRUCTIONS=11
    DETECT=12
    MIX=13
    SEND=14
    SPLIT=15
    HEAT=16
    DRAIN=17
    DISPENSE=18
    DISPOSE=19
    GRADIENT=20
    STORE=21
    RANGE=22
    AT=23
    WITH=24
    FOR=25
    INTO=26
    TIMES=27
    ON=28
    TO=29
    OF=30
    UNITS=31
    USEIN=32
    SLE=33
    SEQ=34
    SGE=35
    FLE=36
    FEQ=37
    FGE=38
    NAT=39
    REAL=40
    MAT=41
    BOOL=42
    IDENTIFIER=43
    STRING_LITERAL=44
    BOOL_LITERAL=45
    FLOAT_LITERAL=46
    INTEGER_LITERAL=47
    TIME_NUMBER=48
    VOLUME_NUMBER=49
    TEMP_NUMBER=50
    LPAREN=51
    RPAREN=52
    LBRACE=53
    RBRACE=54
    LBRACKET=55
    RBRACKET=56
    SEMICOLON=57
    COMMA=58
    DOT=59
    ASSIGN=60
    GT=61
    LT=62
    BANG=63
    TILDE=64
    QUESTION=65
    COLON=66
    EQUALITY=67
    LTE=68
    GTE=69
    NOTEQUAL=70
    AND=71
    OR=72
    INC=73
    DEC=74
    ADDITION=75
    SUBTRACT=76
    MULTIPLY=77
    DIVIDE=78
    BITAND=79
    BITOR=80
    CARET=81
    MOD=82
    UNDERSCORE=83
    ATSIGN=84
    NANOSECOND=85
    MICROSECOND=86
    MILLISECOND=87
    CENTISECOND=88
    DECISECOND=89
    SECOND=90
    MINUTE=91
    HOUR=92
    DAY=93
    WEEK=94
    MONTH=95
    YEAR=96
    NANOLITRE=97
    MICROLITRE=98
    MILLILITRE=99
    CENTILITRE=100
    DECILITRE=101
    LITRE=102
    DECALITRE=103
    CELSIUS=104
    FAHRENHEIT=105
    KELVIN=106
    ACIDS_STRONG_NON_OXIDIZING=107
    ACIDS_STRONG_OXIDIZING=108
    ACIDS_CARBOXYLIC=109
    ALCOHOLS_AND_POLYOLS=110
    ALDEHYDES=111
    AMIDES_AND_IMIDES=112
    AMINES_PHOSPHINES_AND_PYRIDINES=113
    AZO_DIAZO_AZIDO_HYDRAZINE_AND_AZIDE_COMPOUNDS=114
    CARBAMATES=115
    BASES_STRONG=116
    CYANIDES_INORGANIC=117
    THIOCARBAMATE_ESTERS_AND_SALTS_DITHIOCARBAMATE_ESTERS_AND_SALTS=118
    ESTERS_SULFATE_ESTERS_PHOSPHATE_ESTERS_THIOPHOSPHATE_ESTERS_AND_BORATE_ESTERS=119
    ETHERS=120
    FLUORIDES_INORGANIC=121
    HYDROCARBONS_AROMATIC=122
    HALOGENATED_ORGANIC_COMPOUNDS=123
    ISOCYANATES_AND_ISOTHIOCYANATES=124
    KETONES=125
    SULFIDES_ORGANIC=126
    METALS_ALKALI_VERY_ACTIVE=127
    METALS_ELEMENTAL_AND_POWDER_ACTIVE=128
    METALS_LESS_REACTIVE=129
    METALS_AND_METAL_COMPOUNDS_TOXIC=130
    DIAZONIUM_SALTS=131
    NITRILES=132
    NITRO_NITROSO_NITRATE_AND_NITRITE_COMPOUNDS_ORGANIC=133
    HYDROCARBONS_ALIPHATIC_UNSATURATED=134
    HYDROCARBONS_ALIPHATIC_SATURATED=135
    PEROXIDES_ORGANIC=136
    PHENOLS_AND_CRESOLS=137
    SULFONATES_PHOSPHONATES_AND_THIOPHOSPHONATES_ORGANIC=138
    SULFIDES_INORGANIC=139
    EPOXIDES=140
    METAL_HYDRIDES_METAL_ALKYLS_METAL_ARYLS_AND_SILANES=141
    ANHYDRIDES=142
    SALTS_ACIDIC=143
    SALTS_BASIC=144
    ACYL_HALIDES_SULFONYL_HALIDES_AND_CHLOROFORMATES=145
    ORGANOMETALLICS=146
    OXIDIZING_AGENTS_STRONG=147
    REDUCING_AGENTS_STRONG=148
    NON_REDOX_ACTIVE_INORGANIC_COMPOUNDS=149
    FLUORINATED_ORGANIC_COMPOUNDS=150
    FLUORIDE_SALTS_SOLUBLE=151
    OXIDIZING_AGENTS_WEAK=152
    REDUCING_AGENTS_WEAK=153
    NITRIDES_PHOSPHIDES_CARBIDES_AND_SILICIDES=154
    CHLOROSILANES=155
    SILOXANES=156
    HALOGENATING_AGENTS=157
    ACIDS_WEAK=158
    BASES_WEAK=159
    CARBONATE_SALTS=160
    ALKYNES_WITH_ACETYLENIC_HYDROGEN=161
    ALKYNES_WITH_NO_ACETYLENIC_HYDROGEN=162
    CONJUGATED_DIENES=163
    ARYL_HALIDES=164
    AMINES_AROMATIC=165
    NITRATE_AND_NITRITE_COMPOUNDS_INORGANIC=166
    ACETALS_KETALS_HEMIACETALS_AND_HEMIKETALS=167
    ACRYLATES_AND_ACRYLIC_ACIDS=168
    PHENOLIC_SALTS=169
    QUATERNARY_AMMONIUM_AND_PHOSPHONIUM_SALTS=170
    SULFITE_AND_THIOSULFATE_SALTS=171
    OXIMES=172
    POLYMERIZABLE_COMPOUNDS=173
    NOT_CHEMICALLY_REACTIVE=174
    INSUFFICIENT_INFORMATION_FOR_CLASSIFICATION=175
    WATER_AND_AQUEOUS_SOLUTIONS=176
    NULL=177
    UNKNOWN=178
    WS=179
    COMMENT=180
    LINE_COMMENT=181

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INSTRUCTIONS(self):
            return self.getToken(BSParser.INSTRUCTIONS, 0)

        def COLON(self):
            return self.getToken(BSParser.COLON, 0)

        def EOF(self):
            return self.getToken(BSParser.EOF, 0)

        def globalDeclarations(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BSParser.GlobalDeclarationsContext)
            else:
                return self.getTypedRuleContext(BSParser.GlobalDeclarationsContext,i)


        def functions(self):
            return self.getTypedRuleContext(BSParser.FunctionsContext,0)


        def statements(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BSParser.StatementsContext)
            else:
                return self.getTypedRuleContext(BSParser.StatementsContext,i)


        def getRuleIndex(self):
            return BSParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = BSParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 92
                self.globalDeclarations()
                self.state = 95 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BSParser.MANIFEST) | (1 << BSParser.MODULE) | (1 << BSParser.STATIONARY) | (1 << BSParser.LBRACKET))) != 0)):
                    break

            self.state = 98
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.FUNCTIONS:
                self.state = 97
                self.functions()


            self.state = 100
            self.match(BSParser.INSTRUCTIONS)
            self.state = 101
            self.match(BSParser.COLON)
            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BSParser.IF) | (1 << BSParser.REPEAT) | (1 << BSParser.WHILE) | (1 << BSParser.HEAT) | (1 << BSParser.DRAIN) | (1 << BSParser.DISPOSE) | (1 << BSParser.STORE) | (1 << BSParser.IDENTIFIER) | (1 << BSParser.LBRACKET))) != 0) or _la==BSParser.ATSIGN:
                self.state = 102
                self.statements()
                self.state = 107
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 108
            self.match(BSParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GlobalDeclarationsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def moduleDeclaration(self):
            return self.getTypedRuleContext(BSParser.ModuleDeclarationContext,0)


        def manifestDeclaration(self):
            return self.getTypedRuleContext(BSParser.ManifestDeclarationContext,0)


        def stationaryDeclaration(self):
            return self.getTypedRuleContext(BSParser.StationaryDeclarationContext,0)


        def getRuleIndex(self):
            return BSParser.RULE_globalDeclarations

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGlobalDeclarations" ):
                listener.enterGlobalDeclarations(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGlobalDeclarations" ):
                listener.exitGlobalDeclarations(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGlobalDeclarations" ):
                return visitor.visitGlobalDeclarations(self)
            else:
                return visitor.visitChildren(self)




    def globalDeclarations(self):

        localctx = BSParser.GlobalDeclarationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_globalDeclarations)
        try:
            self.state = 113
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 110
                self.moduleDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 111
                self.manifestDeclaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 112
                self.stationaryDeclaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ModuleDeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MODULE(self):
            return self.getToken(BSParser.MODULE, 0)

        def IDENTIFIER(self):
            return self.getToken(BSParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return BSParser.RULE_moduleDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModuleDeclaration" ):
                listener.enterModuleDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModuleDeclaration" ):
                listener.exitModuleDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModuleDeclaration" ):
                return visitor.visitModuleDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def moduleDeclaration(self):

        localctx = BSParser.ModuleDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_moduleDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.match(BSParser.MODULE)
            self.state = 116
            self.match(BSParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ManifestDeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MANIFEST(self):
            return self.getToken(BSParser.MANIFEST, 0)

        def IDENTIFIER(self):
            return self.getToken(BSParser.IDENTIFIER, 0)

        def unionType(self):
            return self.getTypedRuleContext(BSParser.UnionTypeContext,0)


        def getRuleIndex(self):
            return BSParser.RULE_manifestDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterManifestDeclaration" ):
                listener.enterManifestDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitManifestDeclaration" ):
                listener.exitManifestDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitManifestDeclaration" ):
                return visitor.visitManifestDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def manifestDeclaration(self):

        localctx = BSParser.ManifestDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_manifestDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.LBRACKET:
                self.state = 118
                self.unionType()


            self.state = 121
            self.match(BSParser.MANIFEST)
            self.state = 122
            self.match(BSParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StationaryDeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STATIONARY(self):
            return self.getToken(BSParser.STATIONARY, 0)

        def IDENTIFIER(self):
            return self.getToken(BSParser.IDENTIFIER, 0)

        def unionType(self):
            return self.getTypedRuleContext(BSParser.UnionTypeContext,0)


        def getRuleIndex(self):
            return BSParser.RULE_stationaryDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStationaryDeclaration" ):
                listener.enterStationaryDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStationaryDeclaration" ):
                listener.exitStationaryDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStationaryDeclaration" ):
                return visitor.visitStationaryDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def stationaryDeclaration(self):

        localctx = BSParser.StationaryDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_stationaryDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.LBRACKET:
                self.state = 124
                self.unionType()


            self.state = 127
            self.match(BSParser.STATIONARY)
            self.state = 128
            self.match(BSParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTIONS(self):
            return self.getToken(BSParser.FUNCTIONS, 0)

        def COLON(self):
            return self.getToken(BSParser.COLON, 0)

        def functionDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BSParser.FunctionDeclarationContext)
            else:
                return self.getTypedRuleContext(BSParser.FunctionDeclarationContext,i)


        def getRuleIndex(self):
            return BSParser.RULE_functions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctions" ):
                listener.enterFunctions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctions" ):
                listener.exitFunctions(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctions" ):
                return visitor.visitFunctions(self)
            else:
                return visitor.visitChildren(self)




    def functions(self):

        localctx = BSParser.FunctionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_functions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.match(BSParser.FUNCTIONS)
            self.state = 131
            self.match(BSParser.COLON)
            self.state = 133 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 132
                self.functionDeclaration()
                self.state = 135 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==BSParser.FUNCTION):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(BSParser.FUNCTION, 0)

        def IDENTIFIER(self):
            return self.getToken(BSParser.IDENTIFIER, 0)

        def formalParameters(self):
            return self.getTypedRuleContext(BSParser.FormalParametersContext,0)


        def LBRACE(self):
            return self.getToken(BSParser.LBRACE, 0)

        def returnStatement(self):
            return self.getTypedRuleContext(BSParser.ReturnStatementContext,0)


        def RBRACE(self):
            return self.getToken(BSParser.RBRACE, 0)

        def functionTyping(self):
            return self.getTypedRuleContext(BSParser.FunctionTypingContext,0)


        def statements(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BSParser.StatementsContext)
            else:
                return self.getTypedRuleContext(BSParser.StatementsContext,i)


        def getRuleIndex(self):
            return BSParser.RULE_functionDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDeclaration" ):
                listener.enterFunctionDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDeclaration" ):
                listener.exitFunctionDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDeclaration" ):
                return visitor.visitFunctionDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def functionDeclaration(self):

        localctx = BSParser.FunctionDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_functionDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.match(BSParser.FUNCTION)
            self.state = 138
            self.match(BSParser.IDENTIFIER)
            self.state = 139
            self.formalParameters()
            self.state = 141
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.COLON:
                self.state = 140
                self.functionTyping()


            self.state = 143
            self.match(BSParser.LBRACE)
            self.state = 147
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BSParser.IF) | (1 << BSParser.REPEAT) | (1 << BSParser.WHILE) | (1 << BSParser.HEAT) | (1 << BSParser.DRAIN) | (1 << BSParser.DISPOSE) | (1 << BSParser.STORE) | (1 << BSParser.IDENTIFIER) | (1 << BSParser.LBRACKET))) != 0) or _la==BSParser.ATSIGN:
                self.state = 144
                self.statements()
                self.state = 149
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 150
            self.returnStatement()
            self.state = 151
            self.match(BSParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FormalParametersContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(BSParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(BSParser.RPAREN, 0)

        def formalParameterList(self):
            return self.getTypedRuleContext(BSParser.FormalParameterListContext,0)


        def getRuleIndex(self):
            return BSParser.RULE_formalParameters

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFormalParameters" ):
                listener.enterFormalParameters(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFormalParameters" ):
                listener.exitFormalParameters(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFormalParameters" ):
                return visitor.visitFormalParameters(self)
            else:
                return visitor.visitChildren(self)




    def formalParameters(self):

        localctx = BSParser.FormalParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_formalParameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.match(BSParser.LPAREN)
            self.state = 155
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.IDENTIFIER or _la==BSParser.LBRACKET:
                self.state = 154
                self.formalParameterList()


            self.state = 157
            self.match(BSParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FormalParameterListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def formalParameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BSParser.FormalParameterContext)
            else:
                return self.getTypedRuleContext(BSParser.FormalParameterContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BSParser.COMMA)
            else:
                return self.getToken(BSParser.COMMA, i)

        def getRuleIndex(self):
            return BSParser.RULE_formalParameterList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFormalParameterList" ):
                listener.enterFormalParameterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFormalParameterList" ):
                listener.exitFormalParameterList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFormalParameterList" ):
                return visitor.visitFormalParameterList(self)
            else:
                return visitor.visitChildren(self)




    def formalParameterList(self):

        localctx = BSParser.FormalParameterListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_formalParameterList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.formalParameter()
            self.state = 164
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BSParser.COMMA:
                self.state = 160
                self.match(BSParser.COMMA)
                self.state = 161
                self.formalParameter()
                self.state = 166
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FormalParameterContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(BSParser.IDENTIFIER, 0)

        def unionType(self):
            return self.getTypedRuleContext(BSParser.UnionTypeContext,0)


        def getRuleIndex(self):
            return BSParser.RULE_formalParameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFormalParameter" ):
                listener.enterFormalParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFormalParameter" ):
                listener.exitFormalParameter(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFormalParameter" ):
                return visitor.visitFormalParameter(self)
            else:
                return visitor.visitChildren(self)




    def formalParameter(self):

        localctx = BSParser.FormalParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_formalParameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.LBRACKET:
                self.state = 167
                self.unionType()


            self.state = 170
            self.match(BSParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionTypingContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self):
            return self.getToken(BSParser.COLON, 0)

        def unionType(self):
            return self.getTypedRuleContext(BSParser.UnionTypeContext,0)


        def getRuleIndex(self):
            return BSParser.RULE_functionTyping

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionTyping" ):
                listener.enterFunctionTyping(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionTyping" ):
                listener.exitFunctionTyping(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionTyping" ):
                return visitor.visitFunctionTyping(self)
            else:
                return visitor.visitChildren(self)




    def functionTyping(self):

        localctx = BSParser.FunctionTypingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_functionTyping)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.match(BSParser.COLON)
            self.state = 173
            self.unionType()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(BSParser.RETURN, 0)

        def primary(self):
            return self.getTypedRuleContext(BSParser.PrimaryContext,0)


        def methodCall(self):
            return self.getTypedRuleContext(BSParser.MethodCallContext,0)


        def getRuleIndex(self):
            return BSParser.RULE_returnStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStatement" ):
                listener.enterReturnStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStatement" ):
                listener.exitReturnStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStatement" ):
                return visitor.visitReturnStatement(self)
            else:
                return visitor.visitChildren(self)




    def returnStatement(self):

        localctx = BSParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_returnStatement)
        try:
            self.state = 179
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 175
                self.match(BSParser.RETURN)
                self.state = 176
                self.primary()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 177
                self.match(BSParser.RETURN)
                self.state = 178
                self.methodCall()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(BSParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(BSParser.RBRACE, 0)

        def statements(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BSParser.StatementsContext)
            else:
                return self.getTypedRuleContext(BSParser.StatementsContext,i)


        def getRuleIndex(self):
            return BSParser.RULE_blockStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlockStatement" ):
                listener.enterBlockStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlockStatement" ):
                listener.exitBlockStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockStatement" ):
                return visitor.visitBlockStatement(self)
            else:
                return visitor.visitChildren(self)




    def blockStatement(self):

        localctx = BSParser.BlockStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_blockStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.match(BSParser.LBRACE)
            self.state = 185
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BSParser.IF) | (1 << BSParser.REPEAT) | (1 << BSParser.WHILE) | (1 << BSParser.HEAT) | (1 << BSParser.DRAIN) | (1 << BSParser.DISPOSE) | (1 << BSParser.STORE) | (1 << BSParser.IDENTIFIER) | (1 << BSParser.LBRACKET))) != 0) or _la==BSParser.ATSIGN:
                self.state = 182
                self.statements()
                self.state = 187
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 188
            self.match(BSParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ifStatement(self):
            return self.getTypedRuleContext(BSParser.IfStatementContext,0)


        def whileStatement(self):
            return self.getTypedRuleContext(BSParser.WhileStatementContext,0)


        def variableDefinition(self):
            return self.getTypedRuleContext(BSParser.VariableDefinitionContext,0)


        def repeat(self):
            return self.getTypedRuleContext(BSParser.RepeatContext,0)


        def heat(self):
            return self.getTypedRuleContext(BSParser.HeatContext,0)


        def dispose(self):
            return self.getTypedRuleContext(BSParser.DisposeContext,0)


        def mix(self):
            return self.getTypedRuleContext(BSParser.MixContext,0)


        def dispense(self):
            return self.getTypedRuleContext(BSParser.DispenseContext,0)


        def split(self):
            return self.getTypedRuleContext(BSParser.SplitContext,0)


        def methodInvocation(self):
            return self.getTypedRuleContext(BSParser.MethodInvocationContext,0)


        def gradient(self):
            return self.getTypedRuleContext(BSParser.GradientContext,0)


        def detect(self):
            return self.getTypedRuleContext(BSParser.DetectContext,0)


        def store(self):
            return self.getTypedRuleContext(BSParser.StoreContext,0)


        def math(self):
            return self.getTypedRuleContext(BSParser.MathContext,0)


        def numberAssignment(self):
            return self.getTypedRuleContext(BSParser.NumberAssignmentContext,0)


        def getRuleIndex(self):
            return BSParser.RULE_statements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatements" ):
                listener.enterStatements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatements" ):
                listener.exitStatements(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatements" ):
                return visitor.visitStatements(self)
            else:
                return visitor.visitChildren(self)




    def statements(self):

        localctx = BSParser.StatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_statements)
        try:
            self.state = 205
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 190
                self.ifStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 191
                self.whileStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 192
                self.variableDefinition()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 193
                self.repeat()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 194
                self.heat()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 195
                self.dispose()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 196
                self.mix()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 197
                self.dispense()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 198
                self.split()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 199
                self.methodInvocation()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 200
                self.gradient()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 201
                self.detect()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 202
                self.store()
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 203
                self.math()
                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 204
                self.numberAssignment()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(BSParser.IF, 0)

        def parExpression(self):
            return self.getTypedRuleContext(BSParser.ParExpressionContext,0)


        def blockStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BSParser.BlockStatementContext)
            else:
                return self.getTypedRuleContext(BSParser.BlockStatementContext,i)


        def ELSE(self):
            return self.getToken(BSParser.ELSE, 0)

        def getRuleIndex(self):
            return BSParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = BSParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.match(BSParser.IF)
            self.state = 208
            self.parExpression()
            self.state = 209
            self.blockStatement()
            self.state = 212
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.ELSE:
                self.state = 210
                self.match(BSParser.ELSE)
                self.state = 211
                self.blockStatement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(BSParser.WHILE, 0)

        def parExpression(self):
            return self.getTypedRuleContext(BSParser.ParExpressionContext,0)


        def blockStatement(self):
            return self.getTypedRuleContext(BSParser.BlockStatementContext,0)


        def getRuleIndex(self):
            return BSParser.RULE_whileStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStatement" ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStatement" ):
                listener.exitWhileStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStatement" ):
                return visitor.visitWhileStatement(self)
            else:
                return visitor.visitChildren(self)




    def whileStatement(self):

        localctx = BSParser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.match(BSParser.WHILE)
            self.state = 215
            self.parExpression()
            self.state = 216
            self.blockStatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RepeatContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REPEAT(self):
            return self.getToken(BSParser.REPEAT, 0)

        def INTEGER_LITERAL(self):
            return self.getToken(BSParser.INTEGER_LITERAL, 0)

        def TIMES(self):
            return self.getToken(BSParser.TIMES, 0)

        def blockStatement(self):
            return self.getTypedRuleContext(BSParser.BlockStatementContext,0)


        def getRuleIndex(self):
            return BSParser.RULE_repeat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRepeat" ):
                listener.enterRepeat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRepeat" ):
                listener.exitRepeat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRepeat" ):
                return visitor.visitRepeat(self)
            else:
                return visitor.visitChildren(self)




    def repeat(self):

        localctx = BSParser.RepeatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_repeat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            self.match(BSParser.REPEAT)
            self.state = 219
            self.match(BSParser.INTEGER_LITERAL)
            self.state = 220
            self.match(BSParser.TIMES)
            self.state = 221
            self.blockStatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HeatContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def HEAT(self):
            return self.getToken(BSParser.HEAT, 0)

        def variable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BSParser.VariableContext)
            else:
                return self.getTypedRuleContext(BSParser.VariableContext,i)


        def AT(self):
            return self.getToken(BSParser.AT, 0)

        def temperatureIdentifier(self):
            return self.getTypedRuleContext(BSParser.TemperatureIdentifierContext,0)


        def usein(self):
            return self.getTypedRuleContext(BSParser.UseinContext,0)


        def ON(self):
            return self.getToken(BSParser.ON, 0)

        def FOR(self):
            return self.getToken(BSParser.FOR, 0)

        def timeIdentifier(self):
            return self.getTypedRuleContext(BSParser.TimeIdentifierContext,0)


        def getRuleIndex(self):
            return BSParser.RULE_heat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHeat" ):
                listener.enterHeat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHeat" ):
                listener.exitHeat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHeat" ):
                return visitor.visitHeat(self)
            else:
                return visitor.visitChildren(self)




    def heat(self):

        localctx = BSParser.HeatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_heat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.ATSIGN:
                self.state = 223
                self.usein()


            self.state = 226
            self.match(BSParser.HEAT)
            self.state = 227
            self.variable()
            self.state = 228
            self.match(BSParser.AT)
            self.state = 229
            self.temperatureIdentifier()
            self.state = 232
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.ON:
                self.state = 230
                self.match(BSParser.ON)
                self.state = 231
                self.variable()


            self.state = 236
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.FOR:
                self.state = 234
                self.match(BSParser.FOR)
                self.state = 235
                self.timeIdentifier()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DisposeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DRAIN(self):
            return self.getToken(BSParser.DRAIN, 0)

        def variable(self):
            return self.getTypedRuleContext(BSParser.VariableContext,0)


        def DISPOSE(self):
            return self.getToken(BSParser.DISPOSE, 0)

        def getRuleIndex(self):
            return BSParser.RULE_dispose

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDispose" ):
                listener.enterDispose(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDispose" ):
                listener.exitDispose(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDispose" ):
                return visitor.visitDispose(self)
            else:
                return visitor.visitChildren(self)




    def dispose(self):

        localctx = BSParser.DisposeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_dispose)
        try:
            self.state = 242
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BSParser.DRAIN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 238
                self.match(BSParser.DRAIN)
                self.state = 239
                self.variable()
                pass
            elif token in [BSParser.DISPOSE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 240
                self.match(BSParser.DISPOSE)
                self.state = 241
                self.variable()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MixContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableDefinition(self):
            return self.getTypedRuleContext(BSParser.VariableDefinitionContext,0)


        def MIX(self):
            return self.getToken(BSParser.MIX, 0)

        def variable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BSParser.VariableContext)
            else:
                return self.getTypedRuleContext(BSParser.VariableContext,i)


        def WITH(self):
            return self.getToken(BSParser.WITH, 0)

        def ON(self):
            return self.getToken(BSParser.ON, 0)

        def usein(self):
            return self.getTypedRuleContext(BSParser.UseinContext,0)


        def unitTracker(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BSParser.UnitTrackerContext)
            else:
                return self.getTypedRuleContext(BSParser.UnitTrackerContext,i)


        def FOR(self):
            return self.getToken(BSParser.FOR, 0)

        def timeIdentifier(self):
            return self.getTypedRuleContext(BSParser.TimeIdentifierContext,0)


        def getRuleIndex(self):
            return BSParser.RULE_mix

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMix" ):
                listener.enterMix(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMix" ):
                listener.exitMix(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMix" ):
                return visitor.visitMix(self)
            else:
                return visitor.visitChildren(self)




    def mix(self):

        localctx = BSParser.MixContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_mix)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.ATSIGN:
                self.state = 244
                self.usein()


            self.state = 247
            self.variableDefinition()
            self.state = 248
            self.match(BSParser.MIX)
            self.state = 250
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.INTEGER_LITERAL:
                self.state = 249
                self.unitTracker()


            self.state = 252
            self.variable()
            self.state = 264
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BSParser.WITH]:
                self.state = 253
                self.match(BSParser.WITH)
                self.state = 255
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BSParser.INTEGER_LITERAL:
                    self.state = 254
                    self.unitTracker()


                self.state = 257
                self.variable()
                self.state = 260
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BSParser.ON:
                    self.state = 258
                    self.match(BSParser.ON)
                    self.state = 259
                    self.variable()


                pass
            elif token in [BSParser.ON]:
                self.state = 262
                self.match(BSParser.ON)
                self.state = 263
                self.variable()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 268
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.FOR:
                self.state = 266
                self.match(BSParser.FOR)
                self.state = 267
                self.timeIdentifier()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UseinContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ATSIGN(self):
            return self.getToken(BSParser.ATSIGN, 0)

        def USEIN(self):
            return self.getToken(BSParser.USEIN, 0)

        def timeIdentifier(self):
            return self.getTypedRuleContext(BSParser.TimeIdentifierContext,0)


        def useinType(self):
            return self.getTypedRuleContext(BSParser.UseinTypeContext,0)


        def getRuleIndex(self):
            return BSParser.RULE_usein

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUsein" ):
                listener.enterUsein(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUsein" ):
                listener.exitUsein(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUsein" ):
                return visitor.visitUsein(self)
            else:
                return visitor.visitChildren(self)




    def usein(self):

        localctx = BSParser.UseinContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_usein)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            self.match(BSParser.ATSIGN)
            self.state = 271
            self.match(BSParser.USEIN)
            self.state = 273
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.LPAREN:
                self.state = 272
                self.useinType()


            self.state = 275
            self.timeIdentifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UseinTypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(BSParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(BSParser.RPAREN, 0)

        def SLE(self):
            return self.getToken(BSParser.SLE, 0)

        def SEQ(self):
            return self.getToken(BSParser.SEQ, 0)

        def SGE(self):
            return self.getToken(BSParser.SGE, 0)

        def FLE(self):
            return self.getToken(BSParser.FLE, 0)

        def FEQ(self):
            return self.getToken(BSParser.FEQ, 0)

        def FGE(self):
            return self.getToken(BSParser.FGE, 0)

        def getRuleIndex(self):
            return BSParser.RULE_useinType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUseinType" ):
                listener.enterUseinType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUseinType" ):
                listener.exitUseinType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUseinType" ):
                return visitor.visitUseinType(self)
            else:
                return visitor.visitChildren(self)




    def useinType(self):

        localctx = BSParser.UseinTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_useinType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
            self.match(BSParser.LPAREN)
            self.state = 278
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BSParser.SLE) | (1 << BSParser.SEQ) | (1 << BSParser.SGE) | (1 << BSParser.FLE) | (1 << BSParser.FEQ) | (1 << BSParser.FGE))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 279
            self.match(BSParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DetectContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableDefinition(self):
            return self.getTypedRuleContext(BSParser.VariableDefinitionContext,0)


        def DETECT(self):
            return self.getToken(BSParser.DETECT, 0)

        def IDENTIFIER(self):
            return self.getToken(BSParser.IDENTIFIER, 0)

        def ON(self):
            return self.getToken(BSParser.ON, 0)

        def variable(self):
            return self.getTypedRuleContext(BSParser.VariableContext,0)


        def FOR(self):
            return self.getToken(BSParser.FOR, 0)

        def timeIdentifier(self):
            return self.getTypedRuleContext(BSParser.TimeIdentifierContext,0)


        def getRuleIndex(self):
            return BSParser.RULE_detect

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDetect" ):
                listener.enterDetect(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDetect" ):
                listener.exitDetect(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDetect" ):
                return visitor.visitDetect(self)
            else:
                return visitor.visitChildren(self)




    def detect(self):

        localctx = BSParser.DetectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_detect)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            self.variableDefinition()
            self.state = 282
            self.match(BSParser.DETECT)
            self.state = 283
            self.match(BSParser.IDENTIFIER)
            self.state = 284
            self.match(BSParser.ON)
            self.state = 285
            self.variable()
            self.state = 288
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.FOR:
                self.state = 286
                self.match(BSParser.FOR)
                self.state = 287
                self.timeIdentifier()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SplitContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableDefinition(self):
            return self.getTypedRuleContext(BSParser.VariableDefinitionContext,0)


        def SPLIT(self):
            return self.getToken(BSParser.SPLIT, 0)

        def variable(self):
            return self.getTypedRuleContext(BSParser.VariableContext,0)


        def INTO(self):
            return self.getToken(BSParser.INTO, 0)

        def INTEGER_LITERAL(self):
            return self.getToken(BSParser.INTEGER_LITERAL, 0)

        def getRuleIndex(self):
            return BSParser.RULE_split

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSplit" ):
                listener.enterSplit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSplit" ):
                listener.exitSplit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSplit" ):
                return visitor.visitSplit(self)
            else:
                return visitor.visitChildren(self)




    def split(self):

        localctx = BSParser.SplitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_split)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 290
            self.variableDefinition()
            self.state = 291
            self.match(BSParser.SPLIT)
            self.state = 292
            self.variable()
            self.state = 293
            self.match(BSParser.INTO)
            self.state = 294
            self.match(BSParser.INTEGER_LITERAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DispenseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableDefinition(self):
            return self.getTypedRuleContext(BSParser.VariableDefinitionContext,0)


        def DISPENSE(self):
            return self.getToken(BSParser.DISPENSE, 0)

        def IDENTIFIER(self):
            return self.getToken(BSParser.IDENTIFIER, 0)

        def unitTracker(self):
            return self.getTypedRuleContext(BSParser.UnitTrackerContext,0)


        def getRuleIndex(self):
            return BSParser.RULE_dispense

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDispense" ):
                listener.enterDispense(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDispense" ):
                listener.exitDispense(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDispense" ):
                return visitor.visitDispense(self)
            else:
                return visitor.visitChildren(self)




    def dispense(self):

        localctx = BSParser.DispenseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_dispense)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 296
            self.variableDefinition()
            self.state = 297
            self.match(BSParser.DISPENSE)
            self.state = 299
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.INTEGER_LITERAL:
                self.state = 298
                self.unitTracker()


            self.state = 301
            self.match(BSParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GradientContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableDefinition(self):
            return self.getTypedRuleContext(BSParser.VariableDefinitionContext,0)


        def GRADIENT(self):
            return self.getToken(BSParser.GRADIENT, 0)

        def variable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BSParser.VariableContext)
            else:
                return self.getTypedRuleContext(BSParser.VariableContext,i)


        def WITH(self):
            return self.getToken(BSParser.WITH, 0)

        def RANGE(self):
            return self.getToken(BSParser.RANGE, 0)

        def FLOAT_LITERAL(self, i:int=None):
            if i is None:
                return self.getTokens(BSParser.FLOAT_LITERAL)
            else:
                return self.getToken(BSParser.FLOAT_LITERAL, i)

        def COMMA(self):
            return self.getToken(BSParser.COMMA, 0)

        def AT(self):
            return self.getToken(BSParser.AT, 0)

        def getRuleIndex(self):
            return BSParser.RULE_gradient

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGradient" ):
                listener.enterGradient(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGradient" ):
                listener.exitGradient(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGradient" ):
                return visitor.visitGradient(self)
            else:
                return visitor.visitChildren(self)




    def gradient(self):

        localctx = BSParser.GradientContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_gradient)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            self.variableDefinition()
            self.state = 304
            self.match(BSParser.GRADIENT)
            self.state = 305
            self.variable()
            self.state = 306
            self.match(BSParser.WITH)
            self.state = 307
            self.variable()
            self.state = 308
            self.match(BSParser.RANGE)
            self.state = 309
            self.match(BSParser.FLOAT_LITERAL)
            self.state = 310
            self.match(BSParser.COMMA)
            self.state = 311
            self.match(BSParser.FLOAT_LITERAL)
            self.state = 312
            self.match(BSParser.AT)
            self.state = 313
            self.match(BSParser.FLOAT_LITERAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StoreContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STORE(self):
            return self.getToken(BSParser.STORE, 0)

        def variable(self):
            return self.getTypedRuleContext(BSParser.VariableContext,0)


        def getRuleIndex(self):
            return BSParser.RULE_store

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStore" ):
                listener.enterStore(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStore" ):
                listener.exitStore(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStore" ):
                return visitor.visitStore(self)
            else:
                return visitor.visitChildren(self)




    def store(self):

        localctx = BSParser.StoreContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_store)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 315
            self.match(BSParser.STORE)
            self.state = 316
            self.variable()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumberAssignmentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableDefinition(self):
            return self.getTypedRuleContext(BSParser.VariableDefinitionContext,0)


        def literal(self):
            return self.getTypedRuleContext(BSParser.LiteralContext,0)


        def getRuleIndex(self):
            return BSParser.RULE_numberAssignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumberAssignment" ):
                listener.enterNumberAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumberAssignment" ):
                listener.exitNumberAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumberAssignment" ):
                return visitor.visitNumberAssignment(self)
            else:
                return visitor.visitChildren(self)




    def numberAssignment(self):

        localctx = BSParser.NumberAssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_numberAssignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 318
            self.variableDefinition()
            self.state = 319
            self.literal()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MathContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.bop = None # Token

        def variableDefinition(self):
            return self.getTypedRuleContext(BSParser.VariableDefinitionContext,0)


        def primary(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BSParser.PrimaryContext)
            else:
                return self.getTypedRuleContext(BSParser.PrimaryContext,i)


        def MULTIPLY(self):
            return self.getToken(BSParser.MULTIPLY, 0)

        def DIVIDE(self):
            return self.getToken(BSParser.DIVIDE, 0)

        def MOD(self):
            return self.getToken(BSParser.MOD, 0)

        def ADDITION(self):
            return self.getToken(BSParser.ADDITION, 0)

        def SUBTRACT(self):
            return self.getToken(BSParser.SUBTRACT, 0)

        def getRuleIndex(self):
            return BSParser.RULE_math

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMath" ):
                listener.enterMath(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMath" ):
                listener.exitMath(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMath" ):
                return visitor.visitMath(self)
            else:
                return visitor.visitChildren(self)




    def math(self):

        localctx = BSParser.MathContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_math)
        self._la = 0 # Token type
        try:
            self.state = 331
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 321
                self.variableDefinition()
                self.state = 322
                self.primary()
                self.state = 323
                localctx.bop = self._input.LT(1)
                _la = self._input.LA(1)
                if not(((((_la - 77)) & ~0x3f) == 0 and ((1 << (_la - 77)) & ((1 << (BSParser.MULTIPLY - 77)) | (1 << (BSParser.DIVIDE - 77)) | (1 << (BSParser.MOD - 77)))) != 0)):
                    localctx.bop = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 324
                self.primary()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 326
                self.variableDefinition()
                self.state = 327
                self.primary()
                self.state = 328
                localctx.bop = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==BSParser.ADDITION or _la==BSParser.SUBTRACT):
                    localctx.bop = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 329
                self.primary()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BinopsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.bop = None # Token

        def primary(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BSParser.PrimaryContext)
            else:
                return self.getTypedRuleContext(BSParser.PrimaryContext,i)


        def LT(self, i:int=None):
            if i is None:
                return self.getTokens(BSParser.LT)
            else:
                return self.getToken(BSParser.LT, i)

        def GT(self, i:int=None):
            if i is None:
                return self.getTokens(BSParser.GT)
            else:
                return self.getToken(BSParser.GT, i)

        def LTE(self):
            return self.getToken(BSParser.LTE, 0)

        def GTE(self):
            return self.getToken(BSParser.GTE, 0)

        def EQUALITY(self):
            return self.getToken(BSParser.EQUALITY, 0)

        def NOTEQUAL(self):
            return self.getToken(BSParser.NOTEQUAL, 0)

        def getRuleIndex(self):
            return BSParser.RULE_binops

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinops" ):
                listener.enterBinops(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinops" ):
                listener.exitBinops(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinops" ):
                return visitor.visitBinops(self)
            else:
                return visitor.visitChildren(self)




    def binops(self):

        localctx = BSParser.BinopsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_binops)
        self._la = 0 # Token type
        try:
            self.state = 353
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 333
                self.primary()
                self.state = 341
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
                if la_ == 1:
                    self.state = 334
                    self.match(BSParser.LT)
                    self.state = 335
                    self.match(BSParser.LT)
                    pass

                elif la_ == 2:
                    self.state = 336
                    self.match(BSParser.GT)
                    self.state = 337
                    self.match(BSParser.GT)
                    self.state = 338
                    self.match(BSParser.GT)
                    pass

                elif la_ == 3:
                    self.state = 339
                    self.match(BSParser.GT)
                    self.state = 340
                    self.match(BSParser.GT)
                    pass


                self.state = 343
                self.primary()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 345
                self.primary()
                self.state = 346
                localctx.bop = self._input.LT(1)
                _la = self._input.LA(1)
                if not(((((_la - 61)) & ~0x3f) == 0 and ((1 << (_la - 61)) & ((1 << (BSParser.GT - 61)) | (1 << (BSParser.LT - 61)) | (1 << (BSParser.LTE - 61)) | (1 << (BSParser.GTE - 61)))) != 0)):
                    localctx.bop = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 347
                self.primary()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 349
                self.primary()
                self.state = 350
                localctx.bop = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==BSParser.EQUALITY or _la==BSParser.NOTEQUAL):
                    localctx.bop = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 351
                self.primary()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(BSParser.LPAREN, 0)

        def binops(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BSParser.BinopsContext)
            else:
                return self.getTypedRuleContext(BSParser.BinopsContext,i)


        def RPAREN(self):
            return self.getToken(BSParser.RPAREN, 0)

        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(BSParser.AND)
            else:
                return self.getToken(BSParser.AND, i)

        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(BSParser.OR)
            else:
                return self.getToken(BSParser.OR, i)

        def getRuleIndex(self):
            return BSParser.RULE_parExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParExpression" ):
                listener.enterParExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParExpression" ):
                listener.exitParExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParExpression" ):
                return visitor.visitParExpression(self)
            else:
                return visitor.visitChildren(self)




    def parExpression(self):

        localctx = BSParser.ParExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_parExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 355
            self.match(BSParser.LPAREN)
            self.state = 356
            self.binops()
            self.state = 361
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BSParser.AND or _la==BSParser.OR:
                self.state = 357
                _la = self._input.LA(1)
                if not(_la==BSParser.AND or _la==BSParser.OR):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 358
                self.binops()
                self.state = 363
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 364
            self.match(BSParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodInvocationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableDefinition(self):
            return self.getTypedRuleContext(BSParser.VariableDefinitionContext,0)


        def methodCall(self):
            return self.getTypedRuleContext(BSParser.MethodCallContext,0)


        def getRuleIndex(self):
            return BSParser.RULE_methodInvocation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodInvocation" ):
                listener.enterMethodInvocation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodInvocation" ):
                listener.exitMethodInvocation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodInvocation" ):
                return visitor.visitMethodInvocation(self)
            else:
                return visitor.visitChildren(self)




    def methodInvocation(self):

        localctx = BSParser.MethodInvocationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_methodInvocation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 366
            self.variableDefinition()
            self.state = 367
            self.methodCall()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodCallContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(BSParser.IDENTIFIER, 0)

        def LPAREN(self):
            return self.getToken(BSParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(BSParser.RPAREN, 0)

        def expressionList(self):
            return self.getTypedRuleContext(BSParser.ExpressionListContext,0)


        def getRuleIndex(self):
            return BSParser.RULE_methodCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodCall" ):
                listener.enterMethodCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodCall" ):
                listener.exitMethodCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodCall" ):
                return visitor.visitMethodCall(self)
            else:
                return visitor.visitChildren(self)




    def methodCall(self):

        localctx = BSParser.MethodCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_methodCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 369
            self.match(BSParser.IDENTIFIER)
            self.state = 370
            self.match(BSParser.LPAREN)
            self.state = 372
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BSParser.IDENTIFIER) | (1 << BSParser.STRING_LITERAL) | (1 << BSParser.BOOL_LITERAL) | (1 << BSParser.FLOAT_LITERAL) | (1 << BSParser.INTEGER_LITERAL))) != 0):
                self.state = 371
                self.expressionList()


            self.state = 374
            self.match(BSParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primary(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BSParser.PrimaryContext)
            else:
                return self.getTypedRuleContext(BSParser.PrimaryContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BSParser.COMMA)
            else:
                return self.getToken(BSParser.COMMA, i)

        def getRuleIndex(self):
            return BSParser.RULE_expressionList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionList" ):
                listener.enterExpressionList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionList" ):
                listener.exitExpressionList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionList" ):
                return visitor.visitExpressionList(self)
            else:
                return visitor.visitChildren(self)




    def expressionList(self):

        localctx = BSParser.ExpressionListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_expressionList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 376
            self.primary()
            self.state = 381
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BSParser.COMMA:
                self.state = 377
                self.match(BSParser.COMMA)
                self.state = 378
                self.primary()
                self.state = 383
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeTypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitiveType(self):
            return self.getTypedRuleContext(BSParser.PrimitiveTypeContext,0)


        def chemicalType(self):
            return self.getTypedRuleContext(BSParser.ChemicalTypeContext,0)


        def getRuleIndex(self):
            return BSParser.RULE_typeType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeType" ):
                listener.enterTypeType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeType" ):
                listener.exitTypeType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeType" ):
                return visitor.visitTypeType(self)
            else:
                return visitor.visitChildren(self)




    def typeType(self):

        localctx = BSParser.TypeTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_typeType)
        try:
            self.state = 386
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BSParser.NAT, BSParser.REAL, BSParser.MAT, BSParser.BOOL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 384
                self.primitiveType()
                pass
            elif token in [BSParser.INTEGER_LITERAL, BSParser.ACIDS_STRONG_NON_OXIDIZING, BSParser.ACIDS_STRONG_OXIDIZING, BSParser.ACIDS_CARBOXYLIC, BSParser.ALCOHOLS_AND_POLYOLS, BSParser.ALDEHYDES, BSParser.AMIDES_AND_IMIDES, BSParser.AMINES_PHOSPHINES_AND_PYRIDINES, BSParser.AZO_DIAZO_AZIDO_HYDRAZINE_AND_AZIDE_COMPOUNDS, BSParser.CARBAMATES, BSParser.BASES_STRONG, BSParser.CYANIDES_INORGANIC, BSParser.THIOCARBAMATE_ESTERS_AND_SALTS_DITHIOCARBAMATE_ESTERS_AND_SALTS, BSParser.ESTERS_SULFATE_ESTERS_PHOSPHATE_ESTERS_THIOPHOSPHATE_ESTERS_AND_BORATE_ESTERS, BSParser.ETHERS, BSParser.FLUORIDES_INORGANIC, BSParser.HYDROCARBONS_AROMATIC, BSParser.HALOGENATED_ORGANIC_COMPOUNDS, BSParser.ISOCYANATES_AND_ISOTHIOCYANATES, BSParser.KETONES, BSParser.SULFIDES_ORGANIC, BSParser.METALS_ALKALI_VERY_ACTIVE, BSParser.METALS_ELEMENTAL_AND_POWDER_ACTIVE, BSParser.METALS_LESS_REACTIVE, BSParser.METALS_AND_METAL_COMPOUNDS_TOXIC, BSParser.DIAZONIUM_SALTS, BSParser.NITRILES, BSParser.NITRO_NITROSO_NITRATE_AND_NITRITE_COMPOUNDS_ORGANIC, BSParser.HYDROCARBONS_ALIPHATIC_UNSATURATED, BSParser.HYDROCARBONS_ALIPHATIC_SATURATED, BSParser.PEROXIDES_ORGANIC, BSParser.PHENOLS_AND_CRESOLS, BSParser.SULFONATES_PHOSPHONATES_AND_THIOPHOSPHONATES_ORGANIC, BSParser.SULFIDES_INORGANIC, BSParser.EPOXIDES, BSParser.METAL_HYDRIDES_METAL_ALKYLS_METAL_ARYLS_AND_SILANES, BSParser.ANHYDRIDES, BSParser.SALTS_ACIDIC, BSParser.SALTS_BASIC, BSParser.ACYL_HALIDES_SULFONYL_HALIDES_AND_CHLOROFORMATES, BSParser.ORGANOMETALLICS, BSParser.OXIDIZING_AGENTS_STRONG, BSParser.REDUCING_AGENTS_STRONG, BSParser.NON_REDOX_ACTIVE_INORGANIC_COMPOUNDS, BSParser.FLUORINATED_ORGANIC_COMPOUNDS, BSParser.FLUORIDE_SALTS_SOLUBLE, BSParser.OXIDIZING_AGENTS_WEAK, BSParser.REDUCING_AGENTS_WEAK, BSParser.NITRIDES_PHOSPHIDES_CARBIDES_AND_SILICIDES, BSParser.CHLOROSILANES, BSParser.SILOXANES, BSParser.HALOGENATING_AGENTS, BSParser.ACIDS_WEAK, BSParser.BASES_WEAK, BSParser.CARBONATE_SALTS, BSParser.ALKYNES_WITH_ACETYLENIC_HYDROGEN, BSParser.ALKYNES_WITH_NO_ACETYLENIC_HYDROGEN, BSParser.CONJUGATED_DIENES, BSParser.ARYL_HALIDES, BSParser.AMINES_AROMATIC, BSParser.NITRATE_AND_NITRITE_COMPOUNDS_INORGANIC, BSParser.ACETALS_KETALS_HEMIACETALS_AND_HEMIKETALS, BSParser.ACRYLATES_AND_ACRYLIC_ACIDS, BSParser.PHENOLIC_SALTS, BSParser.QUATERNARY_AMMONIUM_AND_PHOSPHONIUM_SALTS, BSParser.SULFITE_AND_THIOSULFATE_SALTS, BSParser.OXIMES, BSParser.POLYMERIZABLE_COMPOUNDS, BSParser.NOT_CHEMICALLY_REACTIVE, BSParser.INSUFFICIENT_INFORMATION_FOR_CLASSIFICATION, BSParser.WATER_AND_AQUEOUS_SOLUTIONS, BSParser.NULL, BSParser.UNKNOWN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 385
                self.chemicalType()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnionTypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACKET(self):
            return self.getToken(BSParser.LBRACKET, 0)

        def typesList(self):
            return self.getTypedRuleContext(BSParser.TypesListContext,0)


        def RBRACKET(self):
            return self.getToken(BSParser.RBRACKET, 0)

        def getRuleIndex(self):
            return BSParser.RULE_unionType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnionType" ):
                listener.enterUnionType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnionType" ):
                listener.exitUnionType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnionType" ):
                return visitor.visitUnionType(self)
            else:
                return visitor.visitChildren(self)




    def unionType(self):

        localctx = BSParser.UnionTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_unionType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 388
            self.match(BSParser.LBRACKET)
            self.state = 389
            self.typesList()
            self.state = 390
            self.match(BSParser.RBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypesListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeType(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BSParser.TypeTypeContext)
            else:
                return self.getTypedRuleContext(BSParser.TypeTypeContext,i)


        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(BSParser.SEMICOLON)
            else:
                return self.getToken(BSParser.SEMICOLON, i)

        def getRuleIndex(self):
            return BSParser.RULE_typesList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypesList" ):
                listener.enterTypesList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypesList" ):
                listener.exitTypesList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypesList" ):
                return visitor.visitTypesList(self)
            else:
                return visitor.visitChildren(self)




    def typesList(self):

        localctx = BSParser.TypesListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_typesList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 392
            self.typeType()
            self.state = 397
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BSParser.SEMICOLON:
                self.state = 393
                self.match(BSParser.SEMICOLON)
                self.state = 394
                self.typeType()
                self.state = 399
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDefinitionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(BSParser.VariableContext,0)


        def ASSIGN(self):
            return self.getToken(BSParser.ASSIGN, 0)

        def unionType(self):
            return self.getTypedRuleContext(BSParser.UnionTypeContext,0)


        def getRuleIndex(self):
            return BSParser.RULE_variableDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDefinition" ):
                listener.enterVariableDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDefinition" ):
                listener.exitVariableDefinition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableDefinition" ):
                return visitor.visitVariableDefinition(self)
            else:
                return visitor.visitChildren(self)




    def variableDefinition(self):

        localctx = BSParser.VariableDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_variableDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 401
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BSParser.LBRACKET:
                self.state = 400
                self.unionType()


            self.state = 403
            self.variable()
            self.state = 404
            self.match(BSParser.ASSIGN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(BSParser.IDENTIFIER, 0)

        def LBRACKET(self):
            return self.getToken(BSParser.LBRACKET, 0)

        def INTEGER_LITERAL(self):
            return self.getToken(BSParser.INTEGER_LITERAL, 0)

        def RBRACKET(self):
            return self.getToken(BSParser.RBRACKET, 0)

        def getRuleIndex(self):
            return BSParser.RULE_variable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)




    def variable(self):

        localctx = BSParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 406
            self.match(BSParser.IDENTIFIER)
            self.state = 410
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.state = 407
                self.match(BSParser.LBRACKET)
                self.state = 408
                self.match(BSParser.INTEGER_LITERAL)
                self.state = 409
                self.match(BSParser.RBRACKET)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(BSParser.LiteralContext,0)


        def variable(self):
            return self.getTypedRuleContext(BSParser.VariableContext,0)


        def getRuleIndex(self):
            return BSParser.RULE_primary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimary" ):
                listener.enterPrimary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimary" ):
                listener.exitPrimary(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimary" ):
                return visitor.visitPrimary(self)
            else:
                return visitor.visitChildren(self)




    def primary(self):

        localctx = BSParser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_primary)
        try:
            self.state = 414
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BSParser.STRING_LITERAL, BSParser.BOOL_LITERAL, BSParser.FLOAT_LITERAL, BSParser.INTEGER_LITERAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 412
                self.literal()
                pass
            elif token in [BSParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 413
                self.variable()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER_LITERAL(self):
            return self.getToken(BSParser.INTEGER_LITERAL, 0)

        def FLOAT_LITERAL(self):
            return self.getToken(BSParser.FLOAT_LITERAL, 0)

        def BOOL_LITERAL(self):
            return self.getToken(BSParser.BOOL_LITERAL, 0)

        def STRING_LITERAL(self):
            return self.getToken(BSParser.STRING_LITERAL, 0)

        def getRuleIndex(self):
            return BSParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = BSParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 416
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BSParser.STRING_LITERAL) | (1 << BSParser.BOOL_LITERAL) | (1 << BSParser.FLOAT_LITERAL) | (1 << BSParser.INTEGER_LITERAL))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimitiveTypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOL(self):
            return self.getToken(BSParser.BOOL, 0)

        def NAT(self):
            return self.getToken(BSParser.NAT, 0)

        def REAL(self):
            return self.getToken(BSParser.REAL, 0)

        def MAT(self):
            return self.getToken(BSParser.MAT, 0)

        def getRuleIndex(self):
            return BSParser.RULE_primitiveType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimitiveType" ):
                listener.enterPrimitiveType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimitiveType" ):
                listener.exitPrimitiveType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitiveType" ):
                return visitor.visitPrimitiveType(self)
            else:
                return visitor.visitChildren(self)




    def primitiveType(self):

        localctx = BSParser.PrimitiveTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_primitiveType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 418
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BSParser.NAT) | (1 << BSParser.REAL) | (1 << BSParser.MAT) | (1 << BSParser.BOOL))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ChemicalTypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER_LITERAL(self):
            return self.getToken(BSParser.INTEGER_LITERAL, 0)

        def ACIDS_STRONG_NON_OXIDIZING(self):
            return self.getToken(BSParser.ACIDS_STRONG_NON_OXIDIZING, 0)

        def ACIDS_STRONG_OXIDIZING(self):
            return self.getToken(BSParser.ACIDS_STRONG_OXIDIZING, 0)

        def ACIDS_CARBOXYLIC(self):
            return self.getToken(BSParser.ACIDS_CARBOXYLIC, 0)

        def ALCOHOLS_AND_POLYOLS(self):
            return self.getToken(BSParser.ALCOHOLS_AND_POLYOLS, 0)

        def ALDEHYDES(self):
            return self.getToken(BSParser.ALDEHYDES, 0)

        def AMIDES_AND_IMIDES(self):
            return self.getToken(BSParser.AMIDES_AND_IMIDES, 0)

        def AMINES_PHOSPHINES_AND_PYRIDINES(self):
            return self.getToken(BSParser.AMINES_PHOSPHINES_AND_PYRIDINES, 0)

        def AZO_DIAZO_AZIDO_HYDRAZINE_AND_AZIDE_COMPOUNDS(self):
            return self.getToken(BSParser.AZO_DIAZO_AZIDO_HYDRAZINE_AND_AZIDE_COMPOUNDS, 0)

        def CARBAMATES(self):
            return self.getToken(BSParser.CARBAMATES, 0)

        def BASES_STRONG(self):
            return self.getToken(BSParser.BASES_STRONG, 0)

        def CYANIDES_INORGANIC(self):
            return self.getToken(BSParser.CYANIDES_INORGANIC, 0)

        def THIOCARBAMATE_ESTERS_AND_SALTS_DITHIOCARBAMATE_ESTERS_AND_SALTS(self):
            return self.getToken(BSParser.THIOCARBAMATE_ESTERS_AND_SALTS_DITHIOCARBAMATE_ESTERS_AND_SALTS, 0)

        def ESTERS_SULFATE_ESTERS_PHOSPHATE_ESTERS_THIOPHOSPHATE_ESTERS_AND_BORATE_ESTERS(self):
            return self.getToken(BSParser.ESTERS_SULFATE_ESTERS_PHOSPHATE_ESTERS_THIOPHOSPHATE_ESTERS_AND_BORATE_ESTERS, 0)

        def ETHERS(self):
            return self.getToken(BSParser.ETHERS, 0)

        def FLUORIDES_INORGANIC(self):
            return self.getToken(BSParser.FLUORIDES_INORGANIC, 0)

        def HYDROCARBONS_AROMATIC(self):
            return self.getToken(BSParser.HYDROCARBONS_AROMATIC, 0)

        def HALOGENATED_ORGANIC_COMPOUNDS(self):
            return self.getToken(BSParser.HALOGENATED_ORGANIC_COMPOUNDS, 0)

        def ISOCYANATES_AND_ISOTHIOCYANATES(self):
            return self.getToken(BSParser.ISOCYANATES_AND_ISOTHIOCYANATES, 0)

        def KETONES(self):
            return self.getToken(BSParser.KETONES, 0)

        def SULFIDES_ORGANIC(self):
            return self.getToken(BSParser.SULFIDES_ORGANIC, 0)

        def METALS_ALKALI_VERY_ACTIVE(self):
            return self.getToken(BSParser.METALS_ALKALI_VERY_ACTIVE, 0)

        def METALS_ELEMENTAL_AND_POWDER_ACTIVE(self):
            return self.getToken(BSParser.METALS_ELEMENTAL_AND_POWDER_ACTIVE, 0)

        def METALS_LESS_REACTIVE(self):
            return self.getToken(BSParser.METALS_LESS_REACTIVE, 0)

        def METALS_AND_METAL_COMPOUNDS_TOXIC(self):
            return self.getToken(BSParser.METALS_AND_METAL_COMPOUNDS_TOXIC, 0)

        def DIAZONIUM_SALTS(self):
            return self.getToken(BSParser.DIAZONIUM_SALTS, 0)

        def NITRILES(self):
            return self.getToken(BSParser.NITRILES, 0)

        def NITRO_NITROSO_NITRATE_AND_NITRITE_COMPOUNDS_ORGANIC(self):
            return self.getToken(BSParser.NITRO_NITROSO_NITRATE_AND_NITRITE_COMPOUNDS_ORGANIC, 0)

        def HYDROCARBONS_ALIPHATIC_UNSATURATED(self):
            return self.getToken(BSParser.HYDROCARBONS_ALIPHATIC_UNSATURATED, 0)

        def HYDROCARBONS_ALIPHATIC_SATURATED(self):
            return self.getToken(BSParser.HYDROCARBONS_ALIPHATIC_SATURATED, 0)

        def PEROXIDES_ORGANIC(self):
            return self.getToken(BSParser.PEROXIDES_ORGANIC, 0)

        def PHENOLS_AND_CRESOLS(self):
            return self.getToken(BSParser.PHENOLS_AND_CRESOLS, 0)

        def SULFONATES_PHOSPHONATES_AND_THIOPHOSPHONATES_ORGANIC(self):
            return self.getToken(BSParser.SULFONATES_PHOSPHONATES_AND_THIOPHOSPHONATES_ORGANIC, 0)

        def SULFIDES_INORGANIC(self):
            return self.getToken(BSParser.SULFIDES_INORGANIC, 0)

        def EPOXIDES(self):
            return self.getToken(BSParser.EPOXIDES, 0)

        def METAL_HYDRIDES_METAL_ALKYLS_METAL_ARYLS_AND_SILANES(self):
            return self.getToken(BSParser.METAL_HYDRIDES_METAL_ALKYLS_METAL_ARYLS_AND_SILANES, 0)

        def ANHYDRIDES(self):
            return self.getToken(BSParser.ANHYDRIDES, 0)

        def SALTS_ACIDIC(self):
            return self.getToken(BSParser.SALTS_ACIDIC, 0)

        def SALTS_BASIC(self):
            return self.getToken(BSParser.SALTS_BASIC, 0)

        def ACYL_HALIDES_SULFONYL_HALIDES_AND_CHLOROFORMATES(self):
            return self.getToken(BSParser.ACYL_HALIDES_SULFONYL_HALIDES_AND_CHLOROFORMATES, 0)

        def ORGANOMETALLICS(self):
            return self.getToken(BSParser.ORGANOMETALLICS, 0)

        def OXIDIZING_AGENTS_STRONG(self):
            return self.getToken(BSParser.OXIDIZING_AGENTS_STRONG, 0)

        def REDUCING_AGENTS_STRONG(self):
            return self.getToken(BSParser.REDUCING_AGENTS_STRONG, 0)

        def NON_REDOX_ACTIVE_INORGANIC_COMPOUNDS(self):
            return self.getToken(BSParser.NON_REDOX_ACTIVE_INORGANIC_COMPOUNDS, 0)

        def FLUORINATED_ORGANIC_COMPOUNDS(self):
            return self.getToken(BSParser.FLUORINATED_ORGANIC_COMPOUNDS, 0)

        def FLUORIDE_SALTS_SOLUBLE(self):
            return self.getToken(BSParser.FLUORIDE_SALTS_SOLUBLE, 0)

        def OXIDIZING_AGENTS_WEAK(self):
            return self.getToken(BSParser.OXIDIZING_AGENTS_WEAK, 0)

        def REDUCING_AGENTS_WEAK(self):
            return self.getToken(BSParser.REDUCING_AGENTS_WEAK, 0)

        def NITRIDES_PHOSPHIDES_CARBIDES_AND_SILICIDES(self):
            return self.getToken(BSParser.NITRIDES_PHOSPHIDES_CARBIDES_AND_SILICIDES, 0)

        def CHLOROSILANES(self):
            return self.getToken(BSParser.CHLOROSILANES, 0)

        def SILOXANES(self):
            return self.getToken(BSParser.SILOXANES, 0)

        def HALOGENATING_AGENTS(self):
            return self.getToken(BSParser.HALOGENATING_AGENTS, 0)

        def ACIDS_WEAK(self):
            return self.getToken(BSParser.ACIDS_WEAK, 0)

        def BASES_WEAK(self):
            return self.getToken(BSParser.BASES_WEAK, 0)

        def CARBONATE_SALTS(self):
            return self.getToken(BSParser.CARBONATE_SALTS, 0)

        def ALKYNES_WITH_ACETYLENIC_HYDROGEN(self):
            return self.getToken(BSParser.ALKYNES_WITH_ACETYLENIC_HYDROGEN, 0)

        def ALKYNES_WITH_NO_ACETYLENIC_HYDROGEN(self):
            return self.getToken(BSParser.ALKYNES_WITH_NO_ACETYLENIC_HYDROGEN, 0)

        def CONJUGATED_DIENES(self):
            return self.getToken(BSParser.CONJUGATED_DIENES, 0)

        def ARYL_HALIDES(self):
            return self.getToken(BSParser.ARYL_HALIDES, 0)

        def AMINES_AROMATIC(self):
            return self.getToken(BSParser.AMINES_AROMATIC, 0)

        def NITRATE_AND_NITRITE_COMPOUNDS_INORGANIC(self):
            return self.getToken(BSParser.NITRATE_AND_NITRITE_COMPOUNDS_INORGANIC, 0)

        def ACETALS_KETALS_HEMIACETALS_AND_HEMIKETALS(self):
            return self.getToken(BSParser.ACETALS_KETALS_HEMIACETALS_AND_HEMIKETALS, 0)

        def ACRYLATES_AND_ACRYLIC_ACIDS(self):
            return self.getToken(BSParser.ACRYLATES_AND_ACRYLIC_ACIDS, 0)

        def PHENOLIC_SALTS(self):
            return self.getToken(BSParser.PHENOLIC_SALTS, 0)

        def QUATERNARY_AMMONIUM_AND_PHOSPHONIUM_SALTS(self):
            return self.getToken(BSParser.QUATERNARY_AMMONIUM_AND_PHOSPHONIUM_SALTS, 0)

        def SULFITE_AND_THIOSULFATE_SALTS(self):
            return self.getToken(BSParser.SULFITE_AND_THIOSULFATE_SALTS, 0)

        def OXIMES(self):
            return self.getToken(BSParser.OXIMES, 0)

        def POLYMERIZABLE_COMPOUNDS(self):
            return self.getToken(BSParser.POLYMERIZABLE_COMPOUNDS, 0)

        def NOT_CHEMICALLY_REACTIVE(self):
            return self.getToken(BSParser.NOT_CHEMICALLY_REACTIVE, 0)

        def INSUFFICIENT_INFORMATION_FOR_CLASSIFICATION(self):
            return self.getToken(BSParser.INSUFFICIENT_INFORMATION_FOR_CLASSIFICATION, 0)

        def WATER_AND_AQUEOUS_SOLUTIONS(self):
            return self.getToken(BSParser.WATER_AND_AQUEOUS_SOLUTIONS, 0)

        def NULL(self):
            return self.getToken(BSParser.NULL, 0)

        def UNKNOWN(self):
            return self.getToken(BSParser.UNKNOWN, 0)

        def getRuleIndex(self):
            return BSParser.RULE_chemicalType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterChemicalType" ):
                listener.enterChemicalType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitChemicalType" ):
                listener.exitChemicalType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitChemicalType" ):
                return visitor.visitChemicalType(self)
            else:
                return visitor.visitChildren(self)




    def chemicalType(self):

        localctx = BSParser.ChemicalTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_chemicalType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 420
            _la = self._input.LA(1)
            if not(_la==BSParser.INTEGER_LITERAL or ((((_la - 107)) & ~0x3f) == 0 and ((1 << (_la - 107)) & ((1 << (BSParser.ACIDS_STRONG_NON_OXIDIZING - 107)) | (1 << (BSParser.ACIDS_STRONG_OXIDIZING - 107)) | (1 << (BSParser.ACIDS_CARBOXYLIC - 107)) | (1 << (BSParser.ALCOHOLS_AND_POLYOLS - 107)) | (1 << (BSParser.ALDEHYDES - 107)) | (1 << (BSParser.AMIDES_AND_IMIDES - 107)) | (1 << (BSParser.AMINES_PHOSPHINES_AND_PYRIDINES - 107)) | (1 << (BSParser.AZO_DIAZO_AZIDO_HYDRAZINE_AND_AZIDE_COMPOUNDS - 107)) | (1 << (BSParser.CARBAMATES - 107)) | (1 << (BSParser.BASES_STRONG - 107)) | (1 << (BSParser.CYANIDES_INORGANIC - 107)) | (1 << (BSParser.THIOCARBAMATE_ESTERS_AND_SALTS_DITHIOCARBAMATE_ESTERS_AND_SALTS - 107)) | (1 << (BSParser.ESTERS_SULFATE_ESTERS_PHOSPHATE_ESTERS_THIOPHOSPHATE_ESTERS_AND_BORATE_ESTERS - 107)) | (1 << (BSParser.ETHERS - 107)) | (1 << (BSParser.FLUORIDES_INORGANIC - 107)) | (1 << (BSParser.HYDROCARBONS_AROMATIC - 107)) | (1 << (BSParser.HALOGENATED_ORGANIC_COMPOUNDS - 107)) | (1 << (BSParser.ISOCYANATES_AND_ISOTHIOCYANATES - 107)) | (1 << (BSParser.KETONES - 107)) | (1 << (BSParser.SULFIDES_ORGANIC - 107)) | (1 << (BSParser.METALS_ALKALI_VERY_ACTIVE - 107)) | (1 << (BSParser.METALS_ELEMENTAL_AND_POWDER_ACTIVE - 107)) | (1 << (BSParser.METALS_LESS_REACTIVE - 107)) | (1 << (BSParser.METALS_AND_METAL_COMPOUNDS_TOXIC - 107)) | (1 << (BSParser.DIAZONIUM_SALTS - 107)) | (1 << (BSParser.NITRILES - 107)) | (1 << (BSParser.NITRO_NITROSO_NITRATE_AND_NITRITE_COMPOUNDS_ORGANIC - 107)) | (1 << (BSParser.HYDROCARBONS_ALIPHATIC_UNSATURATED - 107)) | (1 << (BSParser.HYDROCARBONS_ALIPHATIC_SATURATED - 107)) | (1 << (BSParser.PEROXIDES_ORGANIC - 107)) | (1 << (BSParser.PHENOLS_AND_CRESOLS - 107)) | (1 << (BSParser.SULFONATES_PHOSPHONATES_AND_THIOPHOSPHONATES_ORGANIC - 107)) | (1 << (BSParser.SULFIDES_INORGANIC - 107)) | (1 << (BSParser.EPOXIDES - 107)) | (1 << (BSParser.METAL_HYDRIDES_METAL_ALKYLS_METAL_ARYLS_AND_SILANES - 107)) | (1 << (BSParser.ANHYDRIDES - 107)) | (1 << (BSParser.SALTS_ACIDIC - 107)) | (1 << (BSParser.SALTS_BASIC - 107)) | (1 << (BSParser.ACYL_HALIDES_SULFONYL_HALIDES_AND_CHLOROFORMATES - 107)) | (1 << (BSParser.ORGANOMETALLICS - 107)) | (1 << (BSParser.OXIDIZING_AGENTS_STRONG - 107)) | (1 << (BSParser.REDUCING_AGENTS_STRONG - 107)) | (1 << (BSParser.NON_REDOX_ACTIVE_INORGANIC_COMPOUNDS - 107)) | (1 << (BSParser.FLUORINATED_ORGANIC_COMPOUNDS - 107)) | (1 << (BSParser.FLUORIDE_SALTS_SOLUBLE - 107)) | (1 << (BSParser.OXIDIZING_AGENTS_WEAK - 107)) | (1 << (BSParser.REDUCING_AGENTS_WEAK - 107)) | (1 << (BSParser.NITRIDES_PHOSPHIDES_CARBIDES_AND_SILICIDES - 107)) | (1 << (BSParser.CHLOROSILANES - 107)) | (1 << (BSParser.SILOXANES - 107)) | (1 << (BSParser.HALOGENATING_AGENTS - 107)) | (1 << (BSParser.ACIDS_WEAK - 107)) | (1 << (BSParser.BASES_WEAK - 107)) | (1 << (BSParser.CARBONATE_SALTS - 107)) | (1 << (BSParser.ALKYNES_WITH_ACETYLENIC_HYDROGEN - 107)) | (1 << (BSParser.ALKYNES_WITH_NO_ACETYLENIC_HYDROGEN - 107)) | (1 << (BSParser.CONJUGATED_DIENES - 107)) | (1 << (BSParser.ARYL_HALIDES - 107)) | (1 << (BSParser.AMINES_AROMATIC - 107)) | (1 << (BSParser.NITRATE_AND_NITRITE_COMPOUNDS_INORGANIC - 107)) | (1 << (BSParser.ACETALS_KETALS_HEMIACETALS_AND_HEMIKETALS - 107)) | (1 << (BSParser.ACRYLATES_AND_ACRYLIC_ACIDS - 107)) | (1 << (BSParser.PHENOLIC_SALTS - 107)) | (1 << (BSParser.QUATERNARY_AMMONIUM_AND_PHOSPHONIUM_SALTS - 107)))) != 0) or ((((_la - 171)) & ~0x3f) == 0 and ((1 << (_la - 171)) & ((1 << (BSParser.SULFITE_AND_THIOSULFATE_SALTS - 171)) | (1 << (BSParser.OXIMES - 171)) | (1 << (BSParser.POLYMERIZABLE_COMPOUNDS - 171)) | (1 << (BSParser.NOT_CHEMICALLY_REACTIVE - 171)) | (1 << (BSParser.INSUFFICIENT_INFORMATION_FOR_CLASSIFICATION - 171)) | (1 << (BSParser.WATER_AND_AQUEOUS_SOLUTIONS - 171)) | (1 << (BSParser.NULL - 171)) | (1 << (BSParser.UNKNOWN - 171)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TimeIdentifierContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TIME_NUMBER(self):
            return self.getToken(BSParser.TIME_NUMBER, 0)

        def getRuleIndex(self):
            return BSParser.RULE_timeIdentifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTimeIdentifier" ):
                listener.enterTimeIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTimeIdentifier" ):
                listener.exitTimeIdentifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTimeIdentifier" ):
                return visitor.visitTimeIdentifier(self)
            else:
                return visitor.visitChildren(self)




    def timeIdentifier(self):

        localctx = BSParser.TimeIdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_timeIdentifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 422
            self.match(BSParser.TIME_NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TemperatureIdentifierContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEMP_NUMBER(self):
            return self.getToken(BSParser.TEMP_NUMBER, 0)

        def getRuleIndex(self):
            return BSParser.RULE_temperatureIdentifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTemperatureIdentifier" ):
                listener.enterTemperatureIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTemperatureIdentifier" ):
                listener.exitTemperatureIdentifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTemperatureIdentifier" ):
                return visitor.visitTemperatureIdentifier(self)
            else:
                return visitor.visitChildren(self)




    def temperatureIdentifier(self):

        localctx = BSParser.TemperatureIdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_temperatureIdentifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 424
            self.match(BSParser.TEMP_NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnitTrackerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER_LITERAL(self):
            return self.getToken(BSParser.INTEGER_LITERAL, 0)

        def UNITS(self):
            return self.getToken(BSParser.UNITS, 0)

        def OF(self):
            return self.getToken(BSParser.OF, 0)

        def getRuleIndex(self):
            return BSParser.RULE_unitTracker

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnitTracker" ):
                listener.enterUnitTracker(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnitTracker" ):
                listener.exitUnitTracker(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnitTracker" ):
                return visitor.visitUnitTracker(self)
            else:
                return visitor.visitChildren(self)




    def unitTracker(self):

        localctx = BSParser.UnitTrackerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_unitTracker)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 426
            self.match(BSParser.INTEGER_LITERAL)
            self.state = 427
            self.match(BSParser.UNITS)
            self.state = 428
            self.match(BSParser.OF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





