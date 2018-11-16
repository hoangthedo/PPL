from MPVisitor import MPVisitor
from MPParser import MPParser
from AST import *

class ASTGeneration(MPVisitor):
    
    def visitProgram(self,ctx:MPParser.ProgramContext):
        lst=[]
        vlst = list(map(self.visit,ctx.vardec()))
        flst = list(map(self.visit,ctx.funcdec()))
        plst = list(map(self.visit,ctx.procdec()))
        for i in range(0,ctx.getChildCount()):
            if isinstance(ctx.getChild(i),MPParser.VardecContext) and vlst:
                lst+=vlst.pop(0)
            elif isinstance(ctx.getChild(i),MPParser.FuncdecContext) and flst:
                lst.append(flst.pop(0))
            elif isinstance(ctx.getChild(i),MPParser.ProcdecContext) and plst:
                lst.append(plst.pop(0))
        return Program(lst)

# Phan Vardec

    def visitVardec(self,ctx:MPParser.VardecContext):
        lst = []
        for x in ctx.varlist():
            sublst = self.visit(x)
            lst += sublst
        return lst

    def visitVarlist(self,ctx:MPParser.VarlistContext):
        lst = []
        for x in ctx.ID():
            lst.append(VarDecl(Id(x.getText()),self.visit(ctx.vartype())))
        return lst

    def visitVartype(self,ctx:MPParser.VartypeContext):
        if ctx.ARRAY():
            intl,intr = self.visit(ctx.paramarr())
            return ArrayType(int(intl),int(intr),self.visit(ctx.vartypebasic()))
        elif ctx.vartypebasic():
            return self.visit(ctx.vartypebasic())   
    
    def visitParamarr(self,ctx:MPParser.ParamarrContext):
        intl = []
        count = 0
        for x in ctx.SUBOP():
            count = count + 1
        sub = []
        for x in ctx.INTLIT():
            intl.append(x.getText())#intl.append(IntLiteral(x.getText()))
            sub.append(x.getText())
        if count == 2:
            intl[0] = "-" + sub[0]#UnaryOp("-",intl[0]) #"-"+ intl[0]
            intl[1] = "-" + sub[1]#UnaryOp("-",intl[1]) #"-"+ intl[1]
        elif count == 1:
            if ctx.getChild(1).getText() == "-":
                intl[0] = "-" + sub[0]#UnaryOp("-",intl[0]) #"-" + intl[0]
            else:
                intl[1] = "-" + sub[1]#UnaryOp("-",intl[1]) #"-" + intl[1]
        return intl[0],intl[1]

    def visitVartypebasic(self,ctx:MPParser.VartypebasicContext):
        if ctx.INTEGER():
            return IntType();
        elif ctx.BOOLEAN():
            return BoolType();
        elif ctx.STRING():
            return StringType();
        elif ctx.REAL():
            return FloatType();
                
        
# Phan funcdec
    def visitProcdec(self,ctx:MPParser.ProcdecContext):
        #name: Id
        #param: list(VarDecl)
        #returnType: Type => VoidType for Procedure
        #local:list(VarDecl)
        #body: list(Stmt)
        # __init__(self, name, param, local, body, returnType=VoidType())
        return FuncDecl(Id(ctx.ID().getText()),
            self.visit(ctx.paramlist()) if ctx.paramlist() else [],
            self.visit(ctx.vardec()) if ctx.vardec() else [],
            self.visit(ctx.compoundstmt())
            )

    def visitFuncdec(self,ctx:MPParser.FuncdecContext):
        #name: Id
        #param: list(VarDecl)
        #returnType: Type => VoidType for Procedure
        #local:list(VarDecl)
        #body: list(Stmt)
        # __init__(self, name, param, local, body, returnType=VoidType())
        return FuncDecl(Id(ctx.ID().getText()),
            self.visit(ctx.paramlist()) if ctx.paramlist() else [],
            self.visit(ctx.vardec()) if ctx.vardec() else [],
            self.visit(ctx.compoundstmt()),
            self.visit(ctx.returntype())
            )

    def visitParamlist(self,ctx:MPParser.ParamlistContext):
        lst=[]
        sublst = []
        for x in ctx.paramsingle():
            sublst = self.visit(x)
            lst += sublst
        return lst

    def visitParamsingle(self,ctx:MPParser.ParamsingleContext):
        lst = []
        for x in ctx.ID():
            lst.append(VarDecl(Id(x.getText()),self.visit(ctx.vartype())))
        return lst

    def visitReturntype(self,ctx:MPParser.ReturntypeContext):
        return self.visit(ctx.vartype())

    def visitStmt(self,ctx:MPParser.StmtContext):
        stmt = []
        for x in ctx.stmtsingle():
            x = self.visit(x)
            #Kiểm tra x có phải list không
            if isinstance(x,list):
                for i in x:
                    stmt.append(i)
            else:
                stmt.append(x)
        return stmt #[self.visit(x) for x in ctx.stmtsingle()]#list(map(self.visit,ctx.stmtsingle()))

    def visitStmtsingle(self,ctx:MPParser.StmtsingleContext):
        return [self.visit(ctx.getChild(0))] if not isinstance(self.visit(ctx.getChild(0)),list) else self.visit(ctx.getChild(0))
    
    def visitMatchstmt(self,ctx:MPParser.MatchstmtContext):
        #IF
        #expr:Expr
        #thenStmt:list(Stmt)
        #elseStmt:list(Stmt)
        #__init__(self, expr, thenStmt, elseStmt=[]):
        if ctx.ortherstmt():
            return self.visit(ctx.ortherstmt())
        else:
            #Do có thể trả lại 2 loại list hoặc [list]
            thenStmt_ = self.visit(ctx.getChild(3))
            elseStmt_ = self.visit(ctx.getChild(5))
            if not isinstance(thenStmt_,list):
                thenStmt_ = [thenStmt_]
            if not isinstance(elseStmt_,list):
                elseStmt_ = [elseStmt_]
            return If(self.visit(ctx.expr()),thenStmt_,elseStmt_)

    def visitOrtherstmt(self,ctx:MPParser.OrtherstmtContext):
        return self.visit(ctx.getChild(0))

    def visitUnmatchstmt(self,ctx:MPParser.UnmatchstmtContext):
        if ctx.getChildCount() == 4:
            thenStmt_ = self.visit(ctx.getChild(3))
            if not isinstance(thenStmt_,list):
                thenStmt_ = [thenStmt_]
            return If(self.visit(ctx.expr()),thenStmt_ ,[])
                #[self.visit(ctx.stmtsingle())] if ctx.stmtsingle() else self.visit(ctx.compoundstmt()))
        else:
            thenStmt_ = self.visit(ctx.getChild(3))
            elseStmt_ = self.visit(ctx.getChild(5))
            if not isinstance(thenStmt_,list):
                thenStmt_ = [thenStmt_]
            if not isinstance(elseStmt_,list):
                elseStmt_ = [elseStmt_]
            return If(self.visit(ctx.expr()), thenStmt_ , elseStmt_)
                #[self.visit(ctx.matchstmt())] if ctx.matchstmt() else self.visit.compoundstmt(0),
                #[self.visit(ctx.unmatchstmt())] if ctx.unmatchstmt() else self.visit.compoundstmt(1)

    
    

    def visitAssignstmt(self,ctx:MPParser.AssignstmtContext):
        lst = []
        sub=[]
        for x in range(0,ctx.getChildCount()-2):
            if ctx.getChild(x).getText() != ":=":
                lst.append(Assign(self.visit(ctx.getChild(x)),self.visit(ctx.getChild(x+2))))
        for x in range(len(lst)-1, -1, -1):
            sub.append(lst[x])
        return sub

    def visitAssignvar(self,ctx:MPParser.AssignvarContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        else:
            return self.visit(ctx.getChild(0)) # ctx.arrayvar

    def visitArrayvar(self,ctx:MPParser.ArrayvarContext):
        if ctx.indexexp():
            return self.visit(ctx.indexexp())
        else:
            return ArrayCell(Id(ctx.ID().getText()),self.visit(ctx.expr()))

    def visitIndexexp(self,ctx:MPParser.IndexexpContext):
        if ctx.ID():
            return ArrayCell(
                CallExpr(
                    Id(ctx.ID().getText()),
                    (self.visit(ctx.calllist()) if ctx.calllist() else [])
                    ),
                self.visit(ctx.getChild(5)) if ctx.calllist() else self.visit(ctx.getChild(4)))
        else:
            return ArrayCell(self.visit(ctx.expr(0)),self.visit(ctx.expr(1)))

    def visitWhilestmt(self,ctx:MPParser.WhilestmtContext):
        #sl:list(Stmt)
        #exp: Expr
        #def __init__(self, exp,sl):
        return While(self.visit(ctx.expr()),self.visit(ctx.whilebody()))

    def visitWhilebody(self,ctx:MPParser.WhilebodyContext):
        return self.visit(ctx.stmtsingle()) if ctx.stmtsingle() else self.visit(ctx.compoundstmt())

    def visitForstmt(self,ctx:MPParser.ForstmtContext):
        #id:Id
        #expr1,expr2:Expr
        #loop:list(Stmt)
        #up:Boolean #True => increase; False => decrease
        #def __init__(self, id, expr1, expr2,up,loop):
        forStmt_ = self.visit(ctx.forbody())
        dynamic = "False"
        if ctx.TO():
            dynamic = "True"
        if not isinstance(forStmt_,list):
            forStmt_ = [forStmt_]
        return For(Id(ctx.ID().getText()),
                    self.visit(ctx.expr(0)),
                    self.visit(ctx.expr(1)),
                    dynamic,
                    forStmt_)

    def visitForbody(self,ctx:MPParser.ForbodyContext):
        return self.visit(ctx.getChild(0))

    def visitBreakstmt(self,ctx:MPParser.BreakstmtContext):
        return Break();

    def visitContinuestmt(self,ctx:MPParser.ContinuestmtContext):
        return Continue();

    def visitCompoundstmt(self,ctx:MPParser.CompoundstmtContext):
        return self.visit(ctx.stmt())

    def visitReturnstmt(self,ctx:MPParser.ReturnstmtContext):
        return Return(self.visit(ctx.returnbody()) if ctx.returnbody() else None)

    def visitReturnbody(self,ctx:MPParser.ReturnbodyContext):
        return self.visit(ctx.getChild(0))

    def visitWithstmt(self,ctx:MPParser.WithstmtContext):
        #decl:list(VarDecl)
        #stmt:list(Stmt)
        #def __init__(self, decl, stmt):
        return With(self.visit(ctx.paramlist()),
            self.visit(ctx.stmtsingle()) if ctx.stmtsingle() else self.visit(ctx.compoundstmt()))

    def visitFuncall(self,ctx:MPParser.FuncallContext):
        #method:Id
        #param:list(Expr)
        #def __init__(self, method, param):
        return CallStmt(Id(ctx.ID().getText()),(self.visit(ctx.calllist()) if ctx.calllist() else []))

    def visitCalllist(self,ctx:MPParser.CalllistContext):
        return [self.visit(x) for x in ctx.expr()]

    def visitCallnosemi(self,ctx:MPParser.CallnosemiContext):
        return CallExpr(Id(ctx.ID().getText()),(self.visit(ctx.calllist()) if ctx.calllist() else []))
        
    def visitExpstmt(self,ctx:MPParser.ExpstmtContext):
        return list(self.visit(x) for x in ctx.expr())

    def visitExpr(self,ctx:MPParser.ExprContext):
        #BinaryOp
        #op:string: AND THEN => andthen; OR ELSE => orelse; other => keep it
        #left:Expr
        #right:Expr
        #def __init__(self, op, left, right):
        pass
        if ctx.getChildCount() == 4:
            if ctx.ANDOP() and ctx.THEN():
                return BinaryOp("andthen",
                                self.visit(ctx.expr()),
                                self.visit(ctx.exp0()))
            elif ctx.OROP() and ctx.ELSE():
                return BinaryOp("orelse",
                                self.visit(ctx.expr()),
                                self.visit(ctx.exp0()))
        else: 
            return self.visit(ctx.exp0())

    def visitExp0(self,ctx:MPParser.Exp0Context):
        if ctx.getChildCount() == 3:
            if ctx.EQUOP():
                return BinaryOp(ctx.EQUOP().getText(),
                                self.visit(ctx.exp1(0)),
                                self.visit(ctx.exp1(1)))
            elif ctx.NEOP():
                return BinaryOp(ctx.NEOP().getText(),
                                self.visit(ctx.exp1(0)),
                                self.visit(ctx.exp1(1)))
            elif ctx.GTOP():
                return BinaryOp(ctx.GTOP().getText(),
                                self.visit(ctx.exp1(0)),
                                self.visit(ctx.exp1(1)))
            elif ctx.GTEOP():
                return BinaryOp(ctx.GTEOP().getText(),
                                self.visit(ctx.exp1(0)),
                                self.visit(ctx.exp1(1)))
            elif ctx.LTOP():
                return BinaryOp(ctx.LTOP().getText(),
                                self.visit(ctx.exp1(0)),
                                self.visit(ctx.exp1(1)))
            elif ctx.LTEOP():
                return BinaryOp(ctx.LTEOP().getText(),
                                self.visit(ctx.exp1(0)),
                                self.visit(ctx.exp1(1)))
        else: 
            return self.visit(ctx.exp1(0))

    def visitExp1(self,ctx:MPParser.Exp1Context):
        #exp1 ADDOP exp2| exp1 OROP exp2  | exp2;

        # if ctx.ADDOP():
        #     return BinaryOp(ctx.ADDOP().getText(),
        #                     self.visit(ctx.exp1()),
        #                     self.visit(ctx.exp2()))
        # elif ctx.OROP():
        #     return BinaryOp(ctx.OROP().getText(),
        #                     self.visit(ctx.exp1()),
        #                     self.visit(ctx.exp2()))
        # else: 
        #     return self.visit(ctx.exp2())    
        if ctx.getChildCount() == 3:
            if ctx.ADDOP():
                return BinaryOp(ctx.ADDOP().getText(),
                                self.visit(ctx.exp1()),
                                self.visit(ctx.exp2()))
            elif ctx.SUBOP():
                return BinaryOp(ctx.SUBOP().getText(),
                                self.visit(ctx.exp1()),
                                self.visit(ctx.exp2()))
            elif ctx.OROP():
                return BinaryOp(ctx.OROP().getText(),
                                self.visit(ctx.exp1()),
                                self.visit(ctx.exp2()))
        else: 
            return self.visit(ctx.exp2())

    def visitExp2(self,ctx:MPParser.Exp2Context):
        if ctx.getChildCount() == 3:
            if ctx.MULOP():
                return BinaryOp(ctx.MULOP().getText(),
                                self.visit(ctx.exp2()),
                                self.visit(ctx.exp3()))
            elif ctx.DIVOP():
                return BinaryOp(ctx.DIVOP().getText(),
                                self.visit(ctx.exp2()),
                                self.visit(ctx.exp3()))
            elif ctx.DIVINOP():
                return BinaryOp(ctx.DIVINOP().getText(),
                                self.visit(ctx.exp2()),
                                self.visit(ctx.exp3()))
            elif ctx.MODOP():
                return BinaryOp(ctx.MODOP().getText(),
                                self.visit(ctx.exp2()),
                                self.visit(ctx.exp3()))
            elif ctx.ANDOP():
                return BinaryOp(ctx.ANDOP().getText(),
                                self.visit(ctx.exp2()),
                                self.visit(ctx.exp3()))                
        else: 
            return self.visit(ctx.exp3())

    def visitExp3(self,ctx:MPParser.Exp3Context):
        if ctx.getChildCount()==2:
            return UnaryOp(ctx.getChild(0).getText(),self.visit(ctx.exp3()))
        else:
            return self.visit(ctx.exp4())

    def visitExp4(self,ctx:MPParser.Exp4Context):
        if ctx.expr():
            return self.visit(ctx.expr())
        else:
            return self.visit(ctx.exp5())

    def visitExp5(self,ctx:MPParser.Exp5Context):
        if ctx.literals():
            return self.visit(ctx.literals())
        elif ctx.arrayvar():
            return self.visit(ctx.arrayvar())
        elif ctx.callnosemi():
            return self.visit(ctx.callnosemi())
        elif ctx.ID():
            return Id(ctx.ID().getText())

    def visitLiterals(self,ctx:MPParser.LiteralsContext):
        if ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.BOOLLIT():
            bl= 0
            if ctx.BOOLLIT().getText()[0] is 't' or ctx.BOOLLIT().getText()[0] is 'T':
                bl = 1
            elif ctx.BOOLLIT().getText()[0] is 'f' or ctx.BOOLLIT().getText()[0] is 'F':
                bl = 0
            return BooleanLiteral(bool(bl))
        elif ctx.REALLIT():
            return FloatLiteral(float(ctx.REALLIT().getText()))
        elif ctx.STRINGLIT():
            return StringLiteral(str(ctx.STRINGLIT().getText()))
        