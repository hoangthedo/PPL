// Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class MPParser extends Parser {
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
	public static final int
		RULE_program = 0, RULE_vardec = 1, RULE_var1 = 2, RULE_vartype = 3;
	public static final String[] ruleNames = {
		"program", "vardec", "var1", "vartype"
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

	@Override
	public String getGrammarFileName() { return "MP.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public MPParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}
	public static class ProgramContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(MPParser.EOF, 0); }
		public List<VardecContext> vardec() {
			return getRuleContexts(VardecContext.class);
		}
		public VardecContext vardec(int i) {
			return getRuleContext(VardecContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof MPVisitor ) return ((MPVisitor<? extends T>)visitor).visitProgram(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(9); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(8);
				vardec();
				}
				}
				setState(11); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==INTTYPE || _la==FLOAT );
			setState(13);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class VardecContext extends ParserRuleContext {
		public VartypeContext vartype() {
			return getRuleContext(VartypeContext.class,0);
		}
		public List<Var1Context> var1() {
			return getRuleContexts(Var1Context.class);
		}
		public Var1Context var1(int i) {
			return getRuleContext(Var1Context.class,i);
		}
		public TerminalNode SEMI() { return getToken(MPParser.SEMI, 0); }
		public List<TerminalNode> COMMA() { return getTokens(MPParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(MPParser.COMMA, i);
		}
		public VardecContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_vardec; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof MPVisitor ) return ((MPVisitor<? extends T>)visitor).visitVardec(this);
			else return visitor.visitChildren(this);
		}
	}

	public final VardecContext vardec() throws RecognitionException {
		VardecContext _localctx = new VardecContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_vardec);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(15);
			vartype();
			setState(21);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,1,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(16);
					var1();
					setState(17);
					match(COMMA);
					}
					} 
				}
				setState(23);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,1,_ctx);
			}
			setState(24);
			var1();
			setState(25);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Var1Context extends ParserRuleContext {
		public TerminalNode ID() { return getToken(MPParser.ID, 0); }
		public TerminalNode LSB() { return getToken(MPParser.LSB, 0); }
		public TerminalNode INTLIT() { return getToken(MPParser.INTLIT, 0); }
		public TerminalNode RSB() { return getToken(MPParser.RSB, 0); }
		public Var1Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_var1; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof MPVisitor ) return ((MPVisitor<? extends T>)visitor).visitVar1(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Var1Context var1() throws RecognitionException {
		Var1Context _localctx = new Var1Context(_ctx, getState());
		enterRule(_localctx, 4, RULE_var1);
		try {
			setState(32);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(27);
				match(ID);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(28);
				match(ID);
				setState(29);
				match(LSB);
				setState(30);
				match(INTLIT);
				setState(31);
				match(RSB);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class VartypeContext extends ParserRuleContext {
		public TerminalNode INTTYPE() { return getToken(MPParser.INTTYPE, 0); }
		public TerminalNode FLOAT() { return getToken(MPParser.FLOAT, 0); }
		public VartypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_vartype; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof MPVisitor ) return ((MPVisitor<? extends T>)visitor).visitVartype(this);
			else return visitor.visitChildren(this);
		}
	}

	public final VartypeContext vartype() throws RecognitionException {
		VartypeContext _localctx = new VartypeContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_vartype);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(34);
			_la = _input.LA(1);
			if ( !(_la==INTTYPE || _la==FLOAT) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3<\'\4\2\t\2\4\3\t"+
		"\3\4\4\t\4\4\5\t\5\3\2\6\2\f\n\2\r\2\16\2\r\3\2\3\2\3\3\3\3\3\3\3\3\7"+
		"\3\26\n\3\f\3\16\3\31\13\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\5\4#\n\4\3"+
		"\5\3\5\3\5\2\2\6\2\4\6\b\2\3\4\2\3\3\5\5\2%\2\13\3\2\2\2\4\21\3\2\2\2"+
		"\6\"\3\2\2\2\b$\3\2\2\2\n\f\5\4\3\2\13\n\3\2\2\2\f\r\3\2\2\2\r\13\3\2"+
		"\2\2\r\16\3\2\2\2\16\17\3\2\2\2\17\20\7\2\2\3\20\3\3\2\2\2\21\27\5\b\5"+
		"\2\22\23\5\6\4\2\23\24\7\35\2\2\24\26\3\2\2\2\25\22\3\2\2\2\26\31\3\2"+
		"\2\2\27\25\3\2\2\2\27\30\3\2\2\2\30\32\3\2\2\2\31\27\3\2\2\2\32\33\5\6"+
		"\4\2\33\34\7 \2\2\34\5\3\2\2\2\35#\7\32\2\2\36\37\7\32\2\2\37 \7!\2\2"+
		" !\7\65\2\2!#\7\"\2\2\"\35\3\2\2\2\"\36\3\2\2\2#\7\3\2\2\2$%\t\2\2\2%"+
		"\t\3\2\2\2\5\r\27\"";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}