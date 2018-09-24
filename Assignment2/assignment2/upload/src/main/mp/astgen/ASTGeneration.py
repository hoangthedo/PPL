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
               
