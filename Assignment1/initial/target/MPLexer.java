// Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class MPLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.7.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		INTTYPE=1, VOIDTYPE=2, FLOAT=3, STRINGTYPE=4, BOOLLEAN=5, BREAK=6, CONTINUE=7, 
		FOR=8, DO=9, WHILE=10, IF=11, ELSE=12, RETURN=13, TO=14, DOWNTO=15, THEN=16, 
		BEGIN=17, END=18, FUNCTION=19, PROCEDURE=20, VAR=21, ARRAY=22, OF=23, 
		ID=24, BLOCK=25, LINE=26, COMMA=27, DOUDOT=28, COLON=29, SEMI=30, LSB=31, 
		RSB=32, LB=33, RB=34, LP=35, RP=36, ADDOP=37, SUBOP=38, MULOP=39, DIVOP=40, 
		MODOP=41, EQUOP=42, MTOP=43, MTEOP=44, LTOP=45, LTEOP=46, ANDOP=47, OROP=48, 
		NEOP=49, NOTOP=50, INTLIT=51, FLOATLIT=52, BOOLLIT=53, WS=54, ERROR_CHAR=55, 
		STRINGLIT=56, ILLEGAL_ESCAPE=57, UNCLOSE_STRING=58;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	public static final String[] ruleNames = {
		"Char_a", "Char_b", "Char_c", "Char_d", "Char_e", "Char_f", "Char_g", 
		"Char_h", "Char_i", "Char_k", "Char_l", "Char_m", "Char_n", "Char_t", 
		"INTTYPE", "VOIDTYPE", "FLOAT", "STRINGTYPE", "BOOLLEAN", "BREAK", "CONTINUE", 
		"FOR", "DO", "WHILE", "IF", "ELSE", "RETURN", "TO", "DOWNTO", "THEN", 
		"BEGIN", "END", "FUNCTION", "PROCEDURE", "VAR", "ARRAY", "OF", "ID", "BLOCK", 
		"LINE", "COMMA", "DOUDOT", "COLON", "SEMI", "LSB", "RSB", "LB", "RB", 
		"LP", "RP", "ADDOP", "SUBOP", "MULOP", "DIVOP", "MODOP", "EQUOP", "MTOP", 
		"MTEOP", "LTOP", "LTEOP", "ANDOP", "OROP", "NEOP", "NOTOP", "DIGIT", "INTLIT", 
		"EXPONENT", "FLOATLIT", "BOOLLIT", "WS", "ESC", "ERROR_CHAR", "STRINGLIT", 
		"ILLEGAL_ESCAPE", "UNCLOSE_STRING"
	};

	private static final String[] _LITERAL_NAMES = {
		null, null, null, null, "'string'", "'bool'", "'break'", "'continue'", 
		"'for'", "'do'", "'while'", "'if'", "'else'", "'return'", "'to'", "'downto'", 
		"'then'", "'begin'", "'end'", "'function'", "'procedure'", "'var'", "'array'", 
		"'of'", null, null, null, "','", "'..'", "':'", "';'", "'['", "']'", "'('", 
		"')'", "'{'", "'}'", "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", "'>'", 
		"'>='", "'<'", "'<='", "'&&'", "'||'", "'!='", "'not'"
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, "INTTYPE", "VOIDTYPE", "FLOAT", "STRINGTYPE", "BOOLLEAN", "BREAK", 
		"CONTINUE", "FOR", "DO", "WHILE", "IF", "ELSE", "RETURN", "TO", "DOWNTO", 
		"THEN", "BEGIN", "END", "FUNCTION", "PROCEDURE", "VAR", "ARRAY", "OF", 
		"ID", "BLOCK", "LINE", "COMMA", "DOUDOT", "COLON", "SEMI", "LSB", "RSB", 
		"LB", "RB", "LP", "RP", "ADDOP", "SUBOP", "MULOP", "DIVOP", "MODOP", "EQUOP", 
		"MTOP", "MTEOP", "LTOP", "LTEOP", "ANDOP", "OROP", "NEOP", "NOTOP", "INTLIT", 
		"FLOATLIT", "BOOLLIT", "WS", "ERROR_CHAR", "STRINGLIT", "ILLEGAL_ESCAPE", 
		"UNCLOSE_STRING"
	};
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public MPLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "MP.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	@Override
	public void action(RuleContext _localctx, int ruleIndex, int actionIndex) {
		switch (ruleIndex) {
		case 71:
			ERROR_CHAR_action((RuleContext)_localctx, actionIndex);
			break;
		case 72:
			STRINGLIT_action((RuleContext)_localctx, actionIndex);
			break;
		case 73:
			ILLEGAL_ESCAPE_action((RuleContext)_localctx, actionIndex);
			break;
		case 74:
			UNCLOSE_STRING_action((RuleContext)_localctx, actionIndex);
			break;
		}
	}
	private void ERROR_CHAR_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 0:
			 
			            raise ErrorToken(self.text) 
			        
			break;
		}
	}
	private void STRINGLIT_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 1:

			            s=self.text[1:-1]
			            self.text=s
			        
			break;
		}
	}
	private void ILLEGAL_ESCAPE_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 2:

			           raise IllegalEscape(self.text[1:])
			        
			break;
		}
	}
	private void UNCLOSE_STRING_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 3:

			            if self.text[-1]=='\n':
			                 raise UncloseString(self.text[1:-1])
			            else:
			                raise UncloseString(self.text[1:])
			        
			break;
		}
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2<\u01f7\b\1\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4"+
		",\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t"+
		"\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t;\4<\t<\4=\t="+
		"\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I"+
		"\tI\4J\tJ\4K\tK\4L\tL\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7"+
		"\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17"+
		"\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22"+
		"\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\25"+
		"\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26"+
		"\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\32"+
		"\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34"+
		"\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37"+
		"\3\37\3 \3 \3 \3 \3 \3 \3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3"+
		"\"\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3$\3$\3$\3$\3%\3%\3%\3%\3%\3%\3&\3&\3"+
		"&\3\'\3\'\6\'\u0137\n\'\r\'\16\'\u0138\3(\3(\3(\3(\7(\u013f\n(\f(\16("+
		"\u0142\13(\3(\3(\3(\3(\3(\3)\3)\3)\3)\7)\u014d\n)\f)\16)\u0150\13)\3)"+
		"\3)\3*\3*\3+\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3"+
		"\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38\38\39\39\39\3"+
		":\3:\3;\3;\3;\3<\3<\3=\3=\3=\3>\3>\3>\3?\3?\3?\3@\3@\3@\3A\3A\3A\3A\3"+
		"B\6B\u018e\nB\rB\16B\u018f\3C\6C\u0193\nC\rC\16C\u0194\3D\3D\3D\5D\u019a"+
		"\nD\3D\6D\u019d\nD\rD\16D\u019e\5D\u01a1\nD\3E\3E\3E\5E\u01a6\nE\3E\3"+
		"E\3E\7E\u01ab\nE\fE\16E\u01ae\13E\3E\5E\u01b1\nE\3E\3E\3E\5E\u01b6\nE"+
		"\3F\3F\3F\3F\3F\3F\3F\3F\3F\5F\u01c1\nF\3G\6G\u01c4\nG\rG\16G\u01c5\3"+
		"G\3G\3H\3H\3H\3I\3I\3I\3J\3J\3J\7J\u01d3\nJ\fJ\16J\u01d6\13J\3J\3J\3J"+
		"\3K\3K\3K\7K\u01de\nK\fK\16K\u01e1\13K\3K\3K\3K\3K\3K\3L\3L\3L\3L\3L\3"+
		"L\7L\u01ee\nL\fL\16L\u01f1\13L\3L\5L\u01f4\nL\3L\3L\4\u0140\u01df\2M\3"+
		"\2\5\2\7\2\t\2\13\2\r\2\17\2\21\2\23\2\25\2\27\2\31\2\33\2\35\2\37\3!"+
		"\4#\5%\6\'\7)\b+\t-\n/\13\61\f\63\r\65\16\67\179\20;\21=\22?\23A\24C\25"+
		"E\26G\27I\30K\31M\32O\33Q\34S\35U\36W\37Y [!]\"_#a$c%e&g\'i(k)m*o+q,s"+
		"-u.w/y\60{\61}\62\177\63\u0081\64\u0083\2\u0085\65\u0087\2\u0089\66\u008b"+
		"\67\u008d8\u008f\2\u00919\u0093:\u0095;\u0097<\3\2\35\4\2CCcc\4\2DDdd"+
		"\4\2EEee\4\2FFff\4\2GGgg\4\2HHhh\4\2IIii\4\2JJjj\4\2KKkk\4\2MMmm\4\2N"+
		"Nnn\4\2OOoo\4\2PPpp\4\2VVvv\4\2XXxx\4\2QQqq\5\2C\\aac|\6\2\62;C\\aac|"+
		"\4\2\f\f\17\17\3\2\62;\5\2\13\f\16\17\"\"\n\2$$))^^ddhhppttvv\b\2\f\f"+
		"\17\17$$GHQQ^^\4\2$$^^\3\2^^\5\2\f\f\17\17$$\3\3\f\f\2\u01fb\2\37\3\2"+
		"\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2"+
		"\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3"+
		"\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2"+
		"\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2"+
		"Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3"+
		"\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2"+
		"\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2"+
		"w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2"+
		"\2\2\u0085\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u0091"+
		"\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2\3\u0099\3\2\2"+
		"\2\5\u009b\3\2\2\2\7\u009d\3\2\2\2\t\u009f\3\2\2\2\13\u00a1\3\2\2\2\r"+
		"\u00a3\3\2\2\2\17\u00a5\3\2\2\2\21\u00a7\3\2\2\2\23\u00a9\3\2\2\2\25\u00ab"+
		"\3\2\2\2\27\u00ad\3\2\2\2\31\u00af\3\2\2\2\33\u00b1\3\2\2\2\35\u00b3\3"+
		"\2\2\2\37\u00b5\3\2\2\2!\u00b9\3\2\2\2#\u00be\3\2\2\2%\u00c4\3\2\2\2\'"+
		"\u00cb\3\2\2\2)\u00d0\3\2\2\2+\u00d6\3\2\2\2-\u00df\3\2\2\2/\u00e3\3\2"+
		"\2\2\61\u00e6\3\2\2\2\63\u00ec\3\2\2\2\65\u00ef\3\2\2\2\67\u00f4\3\2\2"+
		"\29\u00fb\3\2\2\2;\u00fe\3\2\2\2=\u0105\3\2\2\2?\u010a\3\2\2\2A\u0110"+
		"\3\2\2\2C\u0114\3\2\2\2E\u011d\3\2\2\2G\u0127\3\2\2\2I\u012b\3\2\2\2K"+
		"\u0131\3\2\2\2M\u0134\3\2\2\2O\u013a\3\2\2\2Q\u0148\3\2\2\2S\u0153\3\2"+
		"\2\2U\u0155\3\2\2\2W\u0158\3\2\2\2Y\u015a\3\2\2\2[\u015c\3\2\2\2]\u015e"+
		"\3\2\2\2_\u0160\3\2\2\2a\u0162\3\2\2\2c\u0164\3\2\2\2e\u0166\3\2\2\2g"+
		"\u0168\3\2\2\2i\u016a\3\2\2\2k\u016c\3\2\2\2m\u016e\3\2\2\2o\u0170\3\2"+
		"\2\2q\u0172\3\2\2\2s\u0175\3\2\2\2u\u0177\3\2\2\2w\u017a\3\2\2\2y\u017c"+
		"\3\2\2\2{\u017f\3\2\2\2}\u0182\3\2\2\2\177\u0185\3\2\2\2\u0081\u0188\3"+
		"\2\2\2\u0083\u018d\3\2\2\2\u0085\u0192\3\2\2\2\u0087\u01a0\3\2\2\2\u0089"+
		"\u01b5\3\2\2\2\u008b\u01c0\3\2\2\2\u008d\u01c3\3\2\2\2\u008f\u01c9\3\2"+
		"\2\2\u0091\u01cc\3\2\2\2\u0093\u01cf\3\2\2\2\u0095\u01da\3\2\2\2\u0097"+
		"\u01e7\3\2\2\2\u0099\u009a\t\2\2\2\u009a\4\3\2\2\2\u009b\u009c\t\3\2\2"+
		"\u009c\6\3\2\2\2\u009d\u009e\t\4\2\2\u009e\b\3\2\2\2\u009f\u00a0\t\5\2"+
		"\2\u00a0\n\3\2\2\2\u00a1\u00a2\t\6\2\2\u00a2\f\3\2\2\2\u00a3\u00a4\t\7"+
		"\2\2\u00a4\16\3\2\2\2\u00a5\u00a6\t\b\2\2\u00a6\20\3\2\2\2\u00a7\u00a8"+
		"\t\t\2\2\u00a8\22\3\2\2\2\u00a9\u00aa\t\n\2\2\u00aa\24\3\2\2\2\u00ab\u00ac"+
		"\t\13\2\2\u00ac\26\3\2\2\2\u00ad\u00ae\t\f\2\2\u00ae\30\3\2\2\2\u00af"+
		"\u00b0\t\r\2\2\u00b0\32\3\2\2\2\u00b1\u00b2\t\16\2\2\u00b2\34\3\2\2\2"+
		"\u00b3\u00b4\t\17\2\2\u00b4\36\3\2\2\2\u00b5\u00b6\5\23\n\2\u00b6\u00b7"+
		"\5\33\16\2\u00b7\u00b8\5\35\17\2\u00b8 \3\2\2\2\u00b9\u00ba\t\20\2\2\u00ba"+
		"\u00bb\t\21\2\2\u00bb\u00bc\t\n\2\2\u00bc\u00bd\t\5\2\2\u00bd\"\3\2\2"+
		"\2\u00be\u00bf\t\7\2\2\u00bf\u00c0\t\f\2\2\u00c0\u00c1\t\21\2\2\u00c1"+
		"\u00c2\t\2\2\2\u00c2\u00c3\t\17\2\2\u00c3$\3\2\2\2\u00c4\u00c5\7u\2\2"+
		"\u00c5\u00c6\7v\2\2\u00c6\u00c7\7t\2\2\u00c7\u00c8\7k\2\2\u00c8\u00c9"+
		"\7p\2\2\u00c9\u00ca\7i\2\2\u00ca&\3\2\2\2\u00cb\u00cc\7d\2\2\u00cc\u00cd"+
		"\7q\2\2\u00cd\u00ce\7q\2\2\u00ce\u00cf\7n\2\2\u00cf(\3\2\2\2\u00d0\u00d1"+
		"\7d\2\2\u00d1\u00d2\7t\2\2\u00d2\u00d3\7g\2\2\u00d3\u00d4\7c\2\2\u00d4"+
		"\u00d5\7m\2\2\u00d5*\3\2\2\2\u00d6\u00d7\7e\2\2\u00d7\u00d8\7q\2\2\u00d8"+
		"\u00d9\7p\2\2\u00d9\u00da\7v\2\2\u00da\u00db\7k\2\2\u00db\u00dc\7p\2\2"+
		"\u00dc\u00dd\7w\2\2\u00dd\u00de\7g\2\2\u00de,\3\2\2\2\u00df\u00e0\7h\2"+
		"\2\u00e0\u00e1\7q\2\2\u00e1\u00e2\7t\2\2\u00e2.\3\2\2\2\u00e3\u00e4\7"+
		"f\2\2\u00e4\u00e5\7q\2\2\u00e5\60\3\2\2\2\u00e6\u00e7\7y\2\2\u00e7\u00e8"+
		"\7j\2\2\u00e8\u00e9\7k\2\2\u00e9\u00ea\7n\2\2\u00ea\u00eb\7g\2\2\u00eb"+
		"\62\3\2\2\2\u00ec\u00ed\7k\2\2\u00ed\u00ee\7h\2\2\u00ee\64\3\2\2\2\u00ef"+
		"\u00f0\7g\2\2\u00f0\u00f1\7n\2\2\u00f1\u00f2\7u\2\2\u00f2\u00f3\7g\2\2"+
		"\u00f3\66\3\2\2\2\u00f4\u00f5\7t\2\2\u00f5\u00f6\7g\2\2\u00f6\u00f7\7"+
		"v\2\2\u00f7\u00f8\7w\2\2\u00f8\u00f9\7t\2\2\u00f9\u00fa\7p\2\2\u00fa8"+
		"\3\2\2\2\u00fb\u00fc\7v\2\2\u00fc\u00fd\7q\2\2\u00fd:\3\2\2\2\u00fe\u00ff"+
		"\7f\2\2\u00ff\u0100\7q\2\2\u0100\u0101\7y\2\2\u0101\u0102\7p\2\2\u0102"+
		"\u0103\7v\2\2\u0103\u0104\7q\2\2\u0104<\3\2\2\2\u0105\u0106\7v\2\2\u0106"+
		"\u0107\7j\2\2\u0107\u0108\7g\2\2\u0108\u0109\7p\2\2\u0109>\3\2\2\2\u010a"+
		"\u010b\7d\2\2\u010b\u010c\7g\2\2\u010c\u010d\7i\2\2\u010d\u010e\7k\2\2"+
		"\u010e\u010f\7p\2\2\u010f@\3\2\2\2\u0110\u0111\7g\2\2\u0111\u0112\7p\2"+
		"\2\u0112\u0113\7f\2\2\u0113B\3\2\2\2\u0114\u0115\7h\2\2\u0115\u0116\7"+
		"w\2\2\u0116\u0117\7p\2\2\u0117\u0118\7e\2\2\u0118\u0119\7v\2\2\u0119\u011a"+
		"\7k\2\2\u011a\u011b\7q\2\2\u011b\u011c\7p\2\2\u011cD\3\2\2\2\u011d\u011e"+
		"\7r\2\2\u011e\u011f\7t\2\2\u011f\u0120\7q\2\2\u0120\u0121\7e\2\2\u0121"+
		"\u0122\7g\2\2\u0122\u0123\7f\2\2\u0123\u0124\7w\2\2\u0124\u0125\7t\2\2"+
		"\u0125\u0126\7g\2\2\u0126F\3\2\2\2\u0127\u0128\7x\2\2\u0128\u0129\7c\2"+
		"\2\u0129\u012a\7t\2\2\u012aH\3\2\2\2\u012b\u012c\7c\2\2\u012c\u012d\7"+
		"t\2\2\u012d\u012e\7t\2\2\u012e\u012f\7c\2\2\u012f\u0130\7{\2\2\u0130J"+
		"\3\2\2\2\u0131\u0132\7q\2\2\u0132\u0133\7h\2\2\u0133L\3\2\2\2\u0134\u0136"+
		"\t\22\2\2\u0135\u0137\t\23\2\2\u0136\u0135\3\2\2\2\u0137\u0138\3\2\2\2"+
		"\u0138\u0136\3\2\2\2\u0138\u0139\3\2\2\2\u0139N\3\2\2\2\u013a\u013b\7"+
		"\61\2\2\u013b\u013c\7,\2\2\u013c\u0140\3\2\2\2\u013d\u013f\13\2\2\2\u013e"+
		"\u013d\3\2\2\2\u013f\u0142\3\2\2\2\u0140\u0141\3\2\2\2\u0140\u013e\3\2"+
		"\2\2\u0141\u0143\3\2\2\2\u0142\u0140\3\2\2\2\u0143\u0144\7,\2\2\u0144"+
		"\u0145\7\61\2\2\u0145\u0146\3\2\2\2\u0146\u0147\b(\2\2\u0147P\3\2\2\2"+
		"\u0148\u0149\7\61\2\2\u0149\u014a\7\61\2\2\u014a\u014e\3\2\2\2\u014b\u014d"+
		"\n\24\2\2\u014c\u014b\3\2\2\2\u014d\u0150\3\2\2\2\u014e\u014c\3\2\2\2"+
		"\u014e\u014f\3\2\2\2\u014f\u0151\3\2\2\2\u0150\u014e\3\2\2\2\u0151\u0152"+
		"\b)\2\2\u0152R\3\2\2\2\u0153\u0154\7.\2\2\u0154T\3\2\2\2\u0155\u0156\7"+
		"\60\2\2\u0156\u0157\7\60\2\2\u0157V\3\2\2\2\u0158\u0159\7<\2\2\u0159X"+
		"\3\2\2\2\u015a\u015b\7=\2\2\u015bZ\3\2\2\2\u015c\u015d\7]\2\2\u015d\\"+
		"\3\2\2\2\u015e\u015f\7_\2\2\u015f^\3\2\2\2\u0160\u0161\7*\2\2\u0161`\3"+
		"\2\2\2\u0162\u0163\7+\2\2\u0163b\3\2\2\2\u0164\u0165\7}\2\2\u0165d\3\2"+
		"\2\2\u0166\u0167\7\177\2\2\u0167f\3\2\2\2\u0168\u0169\7-\2\2\u0169h\3"+
		"\2\2\2\u016a\u016b\7/\2\2\u016bj\3\2\2\2\u016c\u016d\7,\2\2\u016dl\3\2"+
		"\2\2\u016e\u016f\7\61\2\2\u016fn\3\2\2\2\u0170\u0171\7\'\2\2\u0171p\3"+
		"\2\2\2\u0172\u0173\7?\2\2\u0173\u0174\7?\2\2\u0174r\3\2\2\2\u0175\u0176"+
		"\7@\2\2\u0176t\3\2\2\2\u0177\u0178\7@\2\2\u0178\u0179\7?\2\2\u0179v\3"+
		"\2\2\2\u017a\u017b\7>\2\2\u017bx\3\2\2\2\u017c\u017d\7>\2\2\u017d\u017e"+
		"\7?\2\2\u017ez\3\2\2\2\u017f\u0180\7(\2\2\u0180\u0181\7(\2\2\u0181|\3"+
		"\2\2\2\u0182\u0183\7~\2\2\u0183\u0184\7~\2\2\u0184~\3\2\2\2\u0185\u0186"+
		"\7#\2\2\u0186\u0187\7?\2\2\u0187\u0080\3\2\2\2\u0188\u0189\7p\2\2\u0189"+
		"\u018a\7q\2\2\u018a\u018b\7v\2\2\u018b\u0082\3\2\2\2\u018c\u018e\t\25"+
		"\2\2\u018d\u018c\3\2\2\2\u018e\u018f\3\2\2\2\u018f\u018d\3\2\2\2\u018f"+
		"\u0190\3\2\2\2\u0190\u0084\3\2\2\2\u0191\u0193\t\25\2\2\u0192\u0191\3"+
		"\2\2\2\u0193\u0194\3\2\2\2\u0194\u0192\3\2\2\2\u0194\u0195\3\2\2\2\u0195"+
		"\u0086\3\2\2\2\u0196\u01a1\7g\2\2\u0197\u0199\7G\2\2\u0198\u019a\7/\2"+
		"\2\u0199\u0198\3\2\2\2\u0199\u019a\3\2\2\2\u019a\u019c\3\2\2\2\u019b\u019d"+
		"\t\25\2\2\u019c\u019b\3\2\2\2\u019d\u019e\3\2\2\2\u019e\u019c\3\2\2\2"+
		"\u019e\u019f\3\2\2\2\u019f\u01a1\3\2\2\2\u01a0\u0196\3\2\2\2\u01a0\u0197"+
		"\3\2\2\2\u01a1\u0088\3\2\2\2\u01a2\u01a3\7\60\2\2\u01a3\u01a5\5\u0083"+
		"B\2\u01a4\u01a6\5\u0087D\2\u01a5\u01a4\3\2\2\2\u01a5\u01a6\3\2\2\2\u01a6"+
		"\u01b6\3\2\2\2\u01a7\u01a8\5\u0083B\2\u01a8\u01ac\7\60\2\2\u01a9\u01ab"+
		"\t\25\2\2\u01aa\u01a9\3\2\2\2\u01ab\u01ae\3\2\2\2\u01ac\u01aa\3\2\2\2"+
		"\u01ac\u01ad\3\2\2\2\u01ad\u01b0\3\2\2\2\u01ae\u01ac\3\2\2\2\u01af\u01b1"+
		"\5\u0087D\2\u01b0\u01af\3\2\2\2\u01b0\u01b1\3\2\2\2\u01b1\u01b6\3\2\2"+
		"\2\u01b2\u01b3\5\u0083B\2\u01b3\u01b4\5\u0087D\2\u01b4\u01b6\3\2\2\2\u01b5"+
		"\u01a2\3\2\2\2\u01b5\u01a7\3\2\2\2\u01b5\u01b2\3\2\2\2\u01b6\u008a\3\2"+
		"\2\2\u01b7\u01b8\7v\2\2\u01b8\u01b9\7t\2\2\u01b9\u01ba\7w\2\2\u01ba\u01c1"+
		"\7g\2\2\u01bb\u01bc\7h\2\2\u01bc\u01bd\7c\2\2\u01bd\u01be\7n\2\2\u01be"+
		"\u01bf\7u\2\2\u01bf\u01c1\7g\2\2\u01c0\u01b7\3\2\2\2\u01c0\u01bb\3\2\2"+
		"\2\u01c1\u008c\3\2\2\2\u01c2\u01c4\t\26\2\2\u01c3\u01c2\3\2\2\2\u01c4"+
		"\u01c5\3\2\2\2\u01c5\u01c3\3\2\2\2\u01c5\u01c6\3\2\2\2\u01c6\u01c7\3\2"+
		"\2\2\u01c7\u01c8\bG\2\2\u01c8\u008e\3\2\2\2\u01c9\u01ca\7^\2\2\u01ca\u01cb"+
		"\t\27\2\2\u01cb\u0090\3\2\2\2\u01cc\u01cd\13\2\2\2\u01cd\u01ce\bI\3\2"+
		"\u01ce\u0092\3\2\2\2\u01cf\u01d4\7$\2\2\u01d0\u01d3\5\u008fH\2\u01d1\u01d3"+
		"\n\30\2\2\u01d2\u01d0\3\2\2\2\u01d2\u01d1\3\2\2\2\u01d3\u01d6\3\2\2\2"+
		"\u01d4\u01d2\3\2\2\2\u01d4\u01d5\3\2\2\2\u01d5\u01d7\3\2\2\2\u01d6\u01d4"+
		"\3\2\2\2\u01d7\u01d8\7$\2\2\u01d8\u01d9\bJ\4\2\u01d9\u0094\3\2\2\2\u01da"+
		"\u01df\7$\2\2\u01db\u01de\5\u008fH\2\u01dc\u01de\n\31\2\2\u01dd\u01db"+
		"\3\2\2\2\u01dd\u01dc\3\2\2\2\u01de\u01e1\3\2\2\2\u01df\u01e0\3\2\2\2\u01df"+
		"\u01dd\3\2\2\2\u01e0\u01e2\3\2\2\2\u01e1\u01df\3\2\2\2\u01e2\u01e3\t\32"+
		"\2\2\u01e3\u01e4\n\27\2\2\u01e4\u01e5\3\2\2\2\u01e5\u01e6\bK\5\2\u01e6"+
		"\u0096\3\2\2\2\u01e7\u01ef\7$\2\2\u01e8\u01ee\5\u008fH\2\u01e9\u01ee\n"+
		"\33\2\2\u01ea\u01eb\n\32\2\2\u01eb\u01ec\7^\2\2\u01ec\u01ee\7$\2\2\u01ed"+
		"\u01e8\3\2\2\2\u01ed\u01e9\3\2\2\2\u01ed\u01ea\3\2\2\2\u01ee\u01f1\3\2"+
		"\2\2\u01ef\u01ed\3\2\2\2\u01ef\u01f0\3\2\2\2\u01f0\u01f3\3\2\2\2\u01f1"+
		"\u01ef\3\2\2\2\u01f2\u01f4\t\34\2\2\u01f3\u01f2\3\2\2\2\u01f4\u01f5\3"+
		"\2\2\2\u01f5\u01f6\bL\6\2\u01f6\u0098\3\2\2\2\30\2\u0138\u0140\u014e\u018f"+
		"\u0194\u0199\u019e\u01a0\u01a5\u01ac\u01b0\u01b5\u01c0\u01c5\u01d2\u01d4"+
		"\u01dd\u01df\u01ed\u01ef\u01f3\7\b\2\2\3I\2\3J\3\3K\4\3L\5";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}