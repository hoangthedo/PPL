# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MPParser import MPParser
else:
    from MPParser import MPParser

# This class defines a complete generic visitor for a parse tree produced by MPParser.

class MPVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MPParser#program.
    def visitProgram(self, ctx:MPParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#vardec.
    def visitVardec(self, ctx:MPParser.VardecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#varlist.
    def visitVarlist(self, ctx:MPParser.VarlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#vartype.
    def visitVartype(self, ctx:MPParser.VartypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#paramarr.
    def visitParamarr(self, ctx:MPParser.ParamarrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#vartypebasic.
    def visitVartypebasic(self, ctx:MPParser.VartypebasicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#funcdec.
    def visitFuncdec(self, ctx:MPParser.FuncdecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#paramlist.
    def visitParamlist(self, ctx:MPParser.ParamlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#paramsingle.
    def visitParamsingle(self, ctx:MPParser.ParamsingleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#returntype.
    def visitReturntype(self, ctx:MPParser.ReturntypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#stmt.
    def visitStmt(self, ctx:MPParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#stmtsingle.
    def visitStmtsingle(self, ctx:MPParser.StmtsingleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#matchstmt.
    def visitMatchstmt(self, ctx:MPParser.MatchstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#ortherstmt.
    def visitOrtherstmt(self, ctx:MPParser.OrtherstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#unmatchstmt.
    def visitUnmatchstmt(self, ctx:MPParser.UnmatchstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#assignstmt.
    def visitAssignstmt(self, ctx:MPParser.AssignstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#assignvar.
    def visitAssignvar(self, ctx:MPParser.AssignvarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#arrayvar.
    def visitArrayvar(self, ctx:MPParser.ArrayvarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#indexexp.
    def visitIndexexp(self, ctx:MPParser.IndexexpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#whilestmt.
    def visitWhilestmt(self, ctx:MPParser.WhilestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#whilebody.
    def visitWhilebody(self, ctx:MPParser.WhilebodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#forstmt.
    def visitForstmt(self, ctx:MPParser.ForstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#forbody.
    def visitForbody(self, ctx:MPParser.ForbodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#breakstmt.
    def visitBreakstmt(self, ctx:MPParser.BreakstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#continuestmt.
    def visitContinuestmt(self, ctx:MPParser.ContinuestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#compoundstmt.
    def visitCompoundstmt(self, ctx:MPParser.CompoundstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#returnstmt.
    def visitReturnstmt(self, ctx:MPParser.ReturnstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#returnbody.
    def visitReturnbody(self, ctx:MPParser.ReturnbodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#withstmt.
    def visitWithstmt(self, ctx:MPParser.WithstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#funcall.
    def visitFuncall(self, ctx:MPParser.FuncallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#calllist.
    def visitCalllist(self, ctx:MPParser.CalllistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#callnosemi.
    def visitCallnosemi(self, ctx:MPParser.CallnosemiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#procdec.
    def visitProcdec(self, ctx:MPParser.ProcdecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#expstmt.
    def visitExpstmt(self, ctx:MPParser.ExpstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#expr.
    def visitExpr(self, ctx:MPParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp0.
    def visitExp0(self, ctx:MPParser.Exp0Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp1.
    def visitExp1(self, ctx:MPParser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp2.
    def visitExp2(self, ctx:MPParser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp3.
    def visitExp3(self, ctx:MPParser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp4.
    def visitExp4(self, ctx:MPParser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp5.
    def visitExp5(self, ctx:MPParser.Exp5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#literals.
    def visitLiterals(self, ctx:MPParser.LiteralsContext):
        return self.visitChildren(ctx)



del MPParser