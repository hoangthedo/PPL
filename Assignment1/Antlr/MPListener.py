# Generated from MP.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MPParser import MPParser
else:
    from MPParser import MPParser

# This class defines a complete listener for a parse tree produced by MPParser.
class MPListener(ParseTreeListener):

    # Enter a parse tree produced by MPParser#program.
    def enterProgram(self, ctx:MPParser.ProgramContext):
        pass

    # Exit a parse tree produced by MPParser#program.
    def exitProgram(self, ctx:MPParser.ProgramContext):
        pass


    # Enter a parse tree produced by MPParser#manydec.
    def enterManydec(self, ctx:MPParser.ManydecContext):
        pass

    # Exit a parse tree produced by MPParser#manydec.
    def exitManydec(self, ctx:MPParser.ManydecContext):
        pass


    # Enter a parse tree produced by MPParser#onedec.
    def enterOnedec(self, ctx:MPParser.OnedecContext):
        pass

    # Exit a parse tree produced by MPParser#onedec.
    def exitOnedec(self, ctx:MPParser.OnedecContext):
        pass


    # Enter a parse tree produced by MPParser#vardec.
    def enterVardec(self, ctx:MPParser.VardecContext):
        pass

    # Exit a parse tree produced by MPParser#vardec.
    def exitVardec(self, ctx:MPParser.VardecContext):
        pass


    # Enter a parse tree produced by MPParser#varlist.
    def enterVarlist(self, ctx:MPParser.VarlistContext):
        pass

    # Exit a parse tree produced by MPParser#varlist.
    def exitVarlist(self, ctx:MPParser.VarlistContext):
        pass


    # Enter a parse tree produced by MPParser#vartypelist.
    def enterVartypelist(self, ctx:MPParser.VartypelistContext):
        pass

    # Exit a parse tree produced by MPParser#vartypelist.
    def exitVartypelist(self, ctx:MPParser.VartypelistContext):
        pass


    # Enter a parse tree produced by MPParser#vartype.
    def enterVartype(self, ctx:MPParser.VartypeContext):
        pass

    # Exit a parse tree produced by MPParser#vartype.
    def exitVartype(self, ctx:MPParser.VartypeContext):
        pass


    # Enter a parse tree produced by MPParser#vartypebasic.
    def enterVartypebasic(self, ctx:MPParser.VartypebasicContext):
        pass

    # Exit a parse tree produced by MPParser#vartypebasic.
    def exitVartypebasic(self, ctx:MPParser.VartypebasicContext):
        pass


    # Enter a parse tree produced by MPParser#funcdec.
    def enterFuncdec(self, ctx:MPParser.FuncdecContext):
        pass

    # Exit a parse tree produced by MPParser#funcdec.
    def exitFuncdec(self, ctx:MPParser.FuncdecContext):
        pass


    # Enter a parse tree produced by MPParser#paramlist.
    def enterParamlist(self, ctx:MPParser.ParamlistContext):
        pass

    # Exit a parse tree produced by MPParser#paramlist.
    def exitParamlist(self, ctx:MPParser.ParamlistContext):
        pass


    # Enter a parse tree produced by MPParser#paramsingle.
    def enterParamsingle(self, ctx:MPParser.ParamsingleContext):
        pass

    # Exit a parse tree produced by MPParser#paramsingle.
    def exitParamsingle(self, ctx:MPParser.ParamsingleContext):
        pass


    # Enter a parse tree produced by MPParser#returntype.
    def enterReturntype(self, ctx:MPParser.ReturntypeContext):
        pass

    # Exit a parse tree produced by MPParser#returntype.
    def exitReturntype(self, ctx:MPParser.ReturntypeContext):
        pass


    # Enter a parse tree produced by MPParser#compoundstmt.
    def enterCompoundstmt(self, ctx:MPParser.CompoundstmtContext):
        pass

    # Exit a parse tree produced by MPParser#compoundstmt.
    def exitCompoundstmt(self, ctx:MPParser.CompoundstmtContext):
        pass


    # Enter a parse tree produced by MPParser#stmt.
    def enterStmt(self, ctx:MPParser.StmtContext):
        pass

    # Exit a parse tree produced by MPParser#stmt.
    def exitStmt(self, ctx:MPParser.StmtContext):
        pass


    # Enter a parse tree produced by MPParser#assignstmt.
    def enterAssignstmt(self, ctx:MPParser.AssignstmtContext):
        pass

    # Exit a parse tree produced by MPParser#assignstmt.
    def exitAssignstmt(self, ctx:MPParser.AssignstmtContext):
        pass


    # Enter a parse tree produced by MPParser#assignlist.
    def enterAssignlist(self, ctx:MPParser.AssignlistContext):
        pass

    # Exit a parse tree produced by MPParser#assignlist.
    def exitAssignlist(self, ctx:MPParser.AssignlistContext):
        pass


    # Enter a parse tree produced by MPParser#arrayvar.
    def enterArrayvar(self, ctx:MPParser.ArrayvarContext):
        pass

    # Exit a parse tree produced by MPParser#arrayvar.
    def exitArrayvar(self, ctx:MPParser.ArrayvarContext):
        pass


    # Enter a parse tree produced by MPParser#funcstmt.
    def enterFuncstmt(self, ctx:MPParser.FuncstmtContext):
        pass

    # Exit a parse tree produced by MPParser#funcstmt.
    def exitFuncstmt(self, ctx:MPParser.FuncstmtContext):
        pass


    # Enter a parse tree produced by MPParser#ifstmt.
    def enterIfstmt(self, ctx:MPParser.IfstmtContext):
        pass

    # Exit a parse tree produced by MPParser#ifstmt.
    def exitIfstmt(self, ctx:MPParser.IfstmtContext):
        pass


    # Enter a parse tree produced by MPParser#ifexp.
    def enterIfexp(self, ctx:MPParser.IfexpContext):
        pass

    # Exit a parse tree produced by MPParser#ifexp.
    def exitIfexp(self, ctx:MPParser.IfexpContext):
        pass


    # Enter a parse tree produced by MPParser#ifbody.
    def enterIfbody(self, ctx:MPParser.IfbodyContext):
        pass

    # Exit a parse tree produced by MPParser#ifbody.
    def exitIfbody(self, ctx:MPParser.IfbodyContext):
        pass


    # Enter a parse tree produced by MPParser#whilestmt.
    def enterWhilestmt(self, ctx:MPParser.WhilestmtContext):
        pass

    # Exit a parse tree produced by MPParser#whilestmt.
    def exitWhilestmt(self, ctx:MPParser.WhilestmtContext):
        pass


    # Enter a parse tree produced by MPParser#whileexp.
    def enterWhileexp(self, ctx:MPParser.WhileexpContext):
        pass

    # Exit a parse tree produced by MPParser#whileexp.
    def exitWhileexp(self, ctx:MPParser.WhileexpContext):
        pass


    # Enter a parse tree produced by MPParser#whilebody.
    def enterWhilebody(self, ctx:MPParser.WhilebodyContext):
        pass

    # Exit a parse tree produced by MPParser#whilebody.
    def exitWhilebody(self, ctx:MPParser.WhilebodyContext):
        pass


    # Enter a parse tree produced by MPParser#forstmt.
    def enterForstmt(self, ctx:MPParser.ForstmtContext):
        pass

    # Exit a parse tree produced by MPParser#forstmt.
    def exitForstmt(self, ctx:MPParser.ForstmtContext):
        pass


    # Enter a parse tree produced by MPParser#forbody.
    def enterForbody(self, ctx:MPParser.ForbodyContext):
        pass

    # Exit a parse tree produced by MPParser#forbody.
    def exitForbody(self, ctx:MPParser.ForbodyContext):
        pass


    # Enter a parse tree produced by MPParser#breakstmt.
    def enterBreakstmt(self, ctx:MPParser.BreakstmtContext):
        pass

    # Exit a parse tree produced by MPParser#breakstmt.
    def exitBreakstmt(self, ctx:MPParser.BreakstmtContext):
        pass


    # Enter a parse tree produced by MPParser#continuestmt.
    def enterContinuestmt(self, ctx:MPParser.ContinuestmtContext):
        pass

    # Exit a parse tree produced by MPParser#continuestmt.
    def exitContinuestmt(self, ctx:MPParser.ContinuestmtContext):
        pass


    # Enter a parse tree produced by MPParser#returnstmt.
    def enterReturnstmt(self, ctx:MPParser.ReturnstmtContext):
        pass

    # Exit a parse tree produced by MPParser#returnstmt.
    def exitReturnstmt(self, ctx:MPParser.ReturnstmtContext):
        pass


    # Enter a parse tree produced by MPParser#returnbody.
    def enterReturnbody(self, ctx:MPParser.ReturnbodyContext):
        pass

    # Exit a parse tree produced by MPParser#returnbody.
    def exitReturnbody(self, ctx:MPParser.ReturnbodyContext):
        pass


    # Enter a parse tree produced by MPParser#withstmt.
    def enterWithstmt(self, ctx:MPParser.WithstmtContext):
        pass

    # Exit a parse tree produced by MPParser#withstmt.
    def exitWithstmt(self, ctx:MPParser.WithstmtContext):
        pass


    # Enter a parse tree produced by MPParser#funcall.
    def enterFuncall(self, ctx:MPParser.FuncallContext):
        pass

    # Exit a parse tree produced by MPParser#funcall.
    def exitFuncall(self, ctx:MPParser.FuncallContext):
        pass


    # Enter a parse tree produced by MPParser#calllist.
    def enterCalllist(self, ctx:MPParser.CalllistContext):
        pass

    # Exit a parse tree produced by MPParser#calllist.
    def exitCalllist(self, ctx:MPParser.CalllistContext):
        pass


    # Enter a parse tree produced by MPParser#procdec.
    def enterProcdec(self, ctx:MPParser.ProcdecContext):
        pass

    # Exit a parse tree produced by MPParser#procdec.
    def exitProcdec(self, ctx:MPParser.ProcdecContext):
        pass


    # Enter a parse tree produced by MPParser#procmain.
    def enterProcmain(self, ctx:MPParser.ProcmainContext):
        pass

    # Exit a parse tree produced by MPParser#procmain.
    def exitProcmain(self, ctx:MPParser.ProcmainContext):
        pass


    # Enter a parse tree produced by MPParser#procbasic.
    def enterProcbasic(self, ctx:MPParser.ProcbasicContext):
        pass

    # Exit a parse tree produced by MPParser#procbasic.
    def exitProcbasic(self, ctx:MPParser.ProcbasicContext):
        pass


    # Enter a parse tree produced by MPParser#expstmt.
    def enterExpstmt(self, ctx:MPParser.ExpstmtContext):
        pass

    # Exit a parse tree produced by MPParser#expstmt.
    def exitExpstmt(self, ctx:MPParser.ExpstmtContext):
        pass


    # Enter a parse tree produced by MPParser#exp.
    def enterExp(self, ctx:MPParser.ExpContext):
        pass

    # Exit a parse tree produced by MPParser#exp.
    def exitExp(self, ctx:MPParser.ExpContext):
        pass


    # Enter a parse tree produced by MPParser#exp1.
    def enterExp1(self, ctx:MPParser.Exp1Context):
        pass

    # Exit a parse tree produced by MPParser#exp1.
    def exitExp1(self, ctx:MPParser.Exp1Context):
        pass


    # Enter a parse tree produced by MPParser#exp2.
    def enterExp2(self, ctx:MPParser.Exp2Context):
        pass

    # Exit a parse tree produced by MPParser#exp2.
    def exitExp2(self, ctx:MPParser.Exp2Context):
        pass


    # Enter a parse tree produced by MPParser#exp3.
    def enterExp3(self, ctx:MPParser.Exp3Context):
        pass

    # Exit a parse tree produced by MPParser#exp3.
    def exitExp3(self, ctx:MPParser.Exp3Context):
        pass


    # Enter a parse tree produced by MPParser#exp4.
    def enterExp4(self, ctx:MPParser.Exp4Context):
        pass

    # Exit a parse tree produced by MPParser#exp4.
    def exitExp4(self, ctx:MPParser.Exp4Context):
        pass


    # Enter a parse tree produced by MPParser#exp5.
    def enterExp5(self, ctx:MPParser.Exp5Context):
        pass

    # Exit a parse tree produced by MPParser#exp5.
    def exitExp5(self, ctx:MPParser.Exp5Context):
        pass


    # Enter a parse tree produced by MPParser#literals.
    def enterLiterals(self, ctx:MPParser.LiteralsContext):
        pass

    # Exit a parse tree produced by MPParser#literals.
    def exitLiterals(self, ctx:MPParser.LiteralsContext):
        pass


