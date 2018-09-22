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
                lst+=flst.pop(0)
            elif isinstance(ctx.getChild(i),MPParser.ProcdecContext) and plst:
                lst+=plst.pop(0)
        
        return Program(lst)

# Phan Vardec

    def visitVardec(self,ctx:MPParser.VardecContext):
        lst = []
        for x in ctx.varlist():
            sublst = self.visit(x)
            lst += sublst
        #print(str(lst[0]))
        return lst

    def visitVarlist(self,ctx:MPParser.VarlistContext):
        lst = []
        for x in ctx.ID():
            lst.append(VarDecl(Id(x.getText()),self.visit(ctx.vartype())))
        return lst

    def visitVartype(self,ctx:MPParser.VartypeContext):
        if ctx.ARRAY():
            intl,intr = self.visit(ctx.paramarr())
            return ArrayType(intl,intr,self.visit(ctx.vartypebasic()))
        elif ctx.vartypebasic():
            return self.visit(ctx.vartypebasic())   
    
    def visitParamarr(self,ctx:MPParser.ParamarrContext):
        intl = []
        for x in ctx.INTLIT():
            intl.append(IntLiteral(x.getText()))
        return intl[0],intl[1]

    def visitVartypebasic(self,ctx:MPParser.VartypebasicContext):
        if ctx.INTEGER():
            return IntType();
        elif ctx.BOOLLEAN():
            return BoolType();
        elif ctx.STRING():
            return StrType();
        elif ctx.REAL():
            return RealType();
                
        
# Phan funcdec
    def visitFuncdec(self,ctx:MPParser.FuncdecContext):
        #name: Id
        #param: list(VarDecl)
        #returnType: Type => VoidType for Procedure
        #local:list(VarDecl)
        #body: list(Stmt)
        # __init__(self, name, param, local, body, returnType=VoidType())
        return FuncDecl(Id(ctx.ID().getText()),
            (self.visit(ctx.paramlist()) if ctx.paramlist() else []),
            self.visit(ctx.returntype()),
            (self.visit(ctx.vardec()) if ctx.vardec() else []),
            self.visit(ctx.compoundstmt()),
            self.visit(ctx.returntype()))

    def visitParamlist(self,ctx:MPParser.ParamarrContext):
        return [self.visit(x) for x in ctx.paramsingle()]

    def visitParamsingle(self,ctx:MPParser.ParamsingleContext):
        lst = []
        for x in ctx.ID():
            lst.append(VarDecl(Id(x.getText()),self.visit(ctx.vartype())))
        return lst

    def visitReturntype(self,ctx:MPParser.ReturntypeContext):
        return visitVartype(self,ctx)

    def visitCompoundstmt(self,ctx:MPParser.CompoundstmtContext):
        return self.visit(ctx.stmt())

    def visitStmt(self,ctx:MPParser.StmtContext):
        lst = []
        mlst = list(map(self.visit,ctx.matchstmt()))
        ulst = list(map(self.visit,ctx.unmatchstmt()))
        for i in range(0,ctx.getChildCount()):
            if isinstance(ctx.getChild(i),MPParser.MatchstmtContext) and mlst:
                lst+=mlst.pop(0)
            elif isinstance(ctx.getChild(i),MPParser.UnmatchstmtContext) and ulst:
                lst+=ulst.pop(0)
        return lst

    def visitMatchstmt(self,ctx:MPParser.MatchstmtContext):
        #IF
        #expr:Expr
        #thenStmt:list(Stmt)
        #elseStmt:list(Stmt)
        #__init__(self, expr, thenStmt, elseStmt=[]):
        if ctx.ortherstmt():
            return self.visit(ctx.ortherstmt())
        else:
            return If(self.visit(ctx.exp()),
                [self.visit(ctx.matchstmt(0))] if ctx.matchstmt(0) else [self.visit(ctx.compoundstmt(0))],
                [self.visit(ctx.matchstmt(1))] if ctx.matchstmt(1) else [self.visit(ctx.compoundstmt(1))]
                )

    def visitUnmatchstmt(self,ctx:MPParser.UnmatchstmtContext):
        if ctx.getChildCount() == 4:
            return If(self.visit(ctx.exp()), 
                [self.visit(ctx.stmtsingle())] if ctx.stmtsingle() else[self.visit.compoundstmt()])
        else: 
            return If(self.visit(ctx.exp()), 
                [self.visit(ctx.matchstmt())] if ctx.matchstmt() else[self.visit.compoundstmt(0)],
                [self.visit(ctx.unmatchstmt())] if ctx.unmatchstmt() else[self.visit.compoundstmt(1)]
                )

    def visitOrtherstmt(self,ctx:MPParser.OrtherstmtContext):
        return self.visit(ctx.getChild(0))

    def visitAssignstmt(self,ctx:MPParser.AssignstmtContext):
        lst = []
        for x in range(1,ctx.getChildCount()):
            lst += Assign(self.visit(ctx.getChild(x-1)).getText(),self.visit(ctx.getChild(x)).getText())