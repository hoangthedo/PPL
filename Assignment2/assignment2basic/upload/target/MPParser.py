# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\f")
        buf.write("\63\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\6\2\16")
        buf.write("\n\2\r\2\16\2\17\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\7\4\32")
        buf.write("\n\4\f\4\16\4\35\13\4\3\5\3\5\3\5\3\5\3\5\3\5\7\5%\n\5")
        buf.write("\f\5\16\5(\13\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6\61\n\6")
        buf.write("\3\6\2\3\b\7\2\4\6\b\n\2\2\2\63\2\r\3\2\2\2\4\21\3\2\2")
        buf.write("\2\6\26\3\2\2\2\b\36\3\2\2\2\n\60\3\2\2\2\f\16\5\4\3\2")
        buf.write("\r\f\3\2\2\2\16\17\3\2\2\2\17\r\3\2\2\2\17\20\3\2\2\2")
        buf.write("\20\3\3\2\2\2\21\22\7\13\2\2\22\23\7\3\2\2\23\24\5\6\4")
        buf.write("\2\24\25\7\4\2\2\25\5\3\2\2\2\26\33\5\b\5\2\27\30\7\t")
        buf.write("\2\2\30\32\5\b\5\2\31\27\3\2\2\2\32\35\3\2\2\2\33\31\3")
        buf.write("\2\2\2\33\34\3\2\2\2\34\7\3\2\2\2\35\33\3\2\2\2\36\37")
        buf.write("\b\5\1\2\37 \5\n\6\2 &\3\2\2\2!\"\f\4\2\2\"#\7\n\2\2#")
        buf.write("%\5\n\6\2$!\3\2\2\2%(\3\2\2\2&$\3\2\2\2&\'\3\2\2\2\'\t")
        buf.write("\3\2\2\2(&\3\2\2\2)\61\7\13\2\2*\61\7\7\2\2+\61\7\b\2")
        buf.write("\2,-\7\5\2\2-.\5\6\4\2./\7\6\2\2/\61\3\2\2\2\60)\3\2\2")
        buf.write("\2\60*\3\2\2\2\60+\3\2\2\2\60,\3\2\2\2\61\13\3\2\2\2\6")
        buf.write("\17\33&\60")
        return buf.getvalue()


class MPParser ( Parser ):

    grammarFileName = "MP.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "';'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "INTLIT", "FLOATLIT", "ADDOP", "MULOP", 
                      "ID", "ERROR_CHAR" ]

    RULE_prog = 0
    RULE_stmt = 1
    RULE_exp = 2
    RULE_term = 3
    RULE_fact = 4

    ruleNames =  [ "prog", "stmt", "exp", "term", "fact" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    INTLIT=5
    FLOATLIT=6
    ADDOP=7
    MULOP=8
    ID=9
    ERROR_CHAR=10

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MPParser.StmtContext)
            else:
                return self.getTypedRuleContext(MPParser.StmtContext,i)


        def getRuleIndex(self):
            return MPParser.RULE_prog

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = MPParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 10
                self.stmt()
                self.state = 13 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MPParser.ID):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MPParser.ID, 0)

        def exp(self):
            return self.getTypedRuleContext(MPParser.ExpContext,0)


        def getRuleIndex(self):
            return MPParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = MPParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self.match(MPParser.ID)
            self.state = 16
            self.match(MPParser.T__0)
            self.state = 17
            self.exp()
            self.state = 18
            self.match(MPParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MPParser.TermContext)
            else:
                return self.getTypedRuleContext(MPParser.TermContext,i)


        def ADDOP(self, i:int=None):
            if i is None:
                return self.getTokens(MPParser.ADDOP)
            else:
                return self.getToken(MPParser.ADDOP, i)

        def getRuleIndex(self):
            return MPParser.RULE_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = MPParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_exp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.term(0)
            self.state = 25
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MPParser.ADDOP:
                self.state = 21
                self.match(MPParser.ADDOP)
                self.state = 22
                self.term(0)
                self.state = 27
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TermContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fact(self):
            return self.getTypedRuleContext(MPParser.FactContext,0)


        def term(self):
            return self.getTypedRuleContext(MPParser.TermContext,0)


        def MULOP(self):
            return self.getToken(MPParser.MULOP, 0)

        def getRuleIndex(self):
            return MPParser.RULE_term

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)



    def term(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MPParser.TermContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_term, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self.fact()
            self._ctx.stop = self._input.LT(-1)
            self.state = 36
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MPParser.TermContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                    self.state = 31
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 32
                    self.match(MPParser.MULOP)
                    self.state = 33
                    self.fact() 
                self.state = 38
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class FactContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MPParser.ID, 0)

        def INTLIT(self):
            return self.getToken(MPParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(MPParser.FLOATLIT, 0)

        def exp(self):
            return self.getTypedRuleContext(MPParser.ExpContext,0)


        def getRuleIndex(self):
            return MPParser.RULE_fact

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFact" ):
                return visitor.visitFact(self)
            else:
                return visitor.visitChildren(self)




    def fact(self):

        localctx = MPParser.FactContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_fact)
        try:
            self.state = 46
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MPParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 39
                self.match(MPParser.ID)
                pass
            elif token in [MPParser.INTLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 40
                self.match(MPParser.INTLIT)
                pass
            elif token in [MPParser.FLOATLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 41
                self.match(MPParser.FLOATLIT)
                pass
            elif token in [MPParser.T__2]:
                self.enterOuterAlt(localctx, 4)
                self.state = 42
                self.match(MPParser.T__2)
                self.state = 43
                self.exp()
                self.state = 44
                self.match(MPParser.T__3)
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.term_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def term_sempred(self, localctx:TermContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         




