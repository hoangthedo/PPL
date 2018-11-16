
"""
 * @author nhphung
"""
from AST import * 
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce
class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value
        
def checkOp(lef,rig):
    if (type(lef),type(rig)) == (IntType,IntType) or\
        (type(lef),type(rig)) == (FloatType,FloatType) or\
        (type(lef),type(rig)) == (IntType,FloatType) or\
        (type(lef),type(rig)) == (FloatType,IntType) or\
        (type(lef),type(rig)) == (BoolType,BoolType):
        return FloatType() if type(lef) == FloatType or type(rig) == FloatType else lef
    return False

def raiseNextast(pre,astnext,c):
    if type(pre) is Break or type(pre) is Continue or type(pre) is Return or c:
        raise UnreachableStatement(astnext)
    return True
class StaticChecker(BaseVisitor,Utils):

    global_envi = [Symbol("getInt",MType([],IntType())),
                    Symbol("putInt",MType([IntType()],VoidType())),
                    Symbol("putIntLn",MType([IntType()],VoidType())),
                    Symbol("getFloat",MType([],FloatType())),
                    Symbol("putFloat",MType([FloatType()],VoidType())),
                    Symbol("putFloatLn",MType([FloatType()],VoidType())),
                    Symbol("putBool",MType([BoolType()],VoidType())),
                    Symbol("putBoolLn",MType([BoolType()],VoidType())),
                    Symbol("putString",MType([StringType()],VoidType())),
                    Symbol("putStringLn",MType([StringType()],VoidType())),
                    Symbol("putLn",MType([StringType()],VoidType()))
                    ]
    def __init__(self,ast):
        self.ast = ast

    def check(self):
        # duyet node ast program
        return self.visit(self.ast,StaticChecker.global_envi)

    def visitProgram(self,ast, c):
        envi_pro = []
        lstfunc = []
        countfunc = 0
        hasMain = False
        for i in ast.decl:
            envi_pro = [self.visit(i,(envi_pro+c,"traverse"))] + envi_pro 
            if type(i) is FuncDecl and i.name.name.lower() == "main" and type(i.returnType) is VoidType and i.param == []:
                hasMain = True
            else:
                if type(i) is not VarDecl and i.returnType:
                    lstfunc.append((i.name.name,i.returnType))
                    countfunc = countfunc + 1
        if hasMain:
            list(map(lambda x: self.visit(x,(envi_pro+c,lstfunc)),ast.decl))
            #print(lstfunc)
            if len(lstfunc) != 0 and countfunc != 0:
                if type(lstfunc[0][1]) is VoidType:
                    raise Unreachable(Procedure(),lstfunc[0][0])
                else:
                    raise Unreachable(Function(),lstfunc[0][0])
        raise NoEntryPoint()            

    def visitVarDecl(self,ast,c):
        #check body of funcdecl
        if type(c) is tuple:
            if c[1] == "param" or c[1] == "local" or c[1] == "traverse":
                if self.lookup(ast.variable.name,c[0],lambda x: x.name) is None :
                    return Symbol(ast.variable.name,ast.varType)
                if c[1] == "param":
                    raise Redeclared(Parameter(),ast.variable.name)
                raise Redeclared(Variable(),ast.variable.name)
            else:
                return Symbol(ast.variable.name,ast.varType)
        else:   
            return Symbol(ast.variable.name,ast.varType)  

    def visitFuncDecl(self,ast, c):
        #if type(c) is tuple: 
        if c[1] == "traverse":
            if self.lookup(ast.name.name,c[0],lambda x: x.name) is None:
                return Symbol(ast.name.name,MType(list(map(lambda x: x.varType,ast.param)),ast.returnType))
            else:
                raise Redeclared(Procedure(),ast.name.name) if type(ast.returnType) is VoidType else Redeclared(Function(),ast.name.name)
        else:
            _sym_func = Symbol(ast.name.name,MType(list(map(lambda x: x.varType,ast.param)),ast.returnType))
            #enviroment reference of param funcdecl
            lst_param_envi = reduce(lambda x,y: [self.visit(y,(x,"param"))] + x ,ast.param,[])
            #enviroment reference of local funcdecl
            lst_local_envi = reduce(lambda x,y: [self.visit(y,(x + lst_param_envi,"local"))] + x,ast.local,[])
            #enviroment reference of funcdecl
            lst_local_envi = lst_local_envi + lst_param_envi + [_sym_func] + c[0]
            #enviroment reference of body funcdecl
            inloop = False
            _return = [False]
            #recursive is unreachable function
            [c[1].remove((_sym_func.name,_sym_func.mtype.rettype)) if x == (_sym_func.name,_sym_func.mtype.rettype) else [] for x in c[1]]
            lst_body = reduce(lambda x,y: self.visit(y,(lst_local_envi,ast.returnType,inloop,_return,c[1])) if raiseNextast(x,y,_return[0]) else [],ast.body,[])
            #has funcdecl returnstmt?
            c[1].append((_sym_func.name,_sym_func.mtype.rettype))if _sym_func.name.lower() != "main" else []
            
            if not _return[0] and type(ast.returnType) is not VoidType:
                raise FunctionNotReturn(_sym_func.name)
            return _sym_func            
       
    def visitAssign(self,ast,c):
        # c is tuple
        lef = self.visit(ast.lhs,c)
        rig = self.visit(ast.exp,c)
        #print((type(lef),type(rig)))
        if (type(lef),type(rig)) == (IntType,IntType) or\
            (type(lef),type(rig)) == (FloatType,FloatType) or\
            (type(lef),type(rig)) == (FloatType,IntType) or \
            (type(lef),type(rig)) == (BoolType,BoolType):
            return FloatType() if type(lef) or type(rig) == FloatType else lef
        raise TypeMismatchInStatement(ast)

    def visitCallExpr(self,ast,c):
        # c is tuple
        _callexpr_param = [self.visit(x,c) for x in ast.param]
        _callexpr = self.lookup(ast.method.name,c[0],lambda x: x.name)
        if _callexpr is not None and type(_callexpr.mtype) is MType:
            if len(_callexpr.mtype.partype) == len(_callexpr_param):
                for x,y in zip(_callexpr.mtype.partype,_callexpr_param):
                    if type(x) != type(y):
                        raise TypeMismatchInExpression(ast)
                [c[4].remove((_callexpr.name,_callexpr.mtype.rettype)) if x == (_callexpr.name,_callexpr.mtype.rettype) else [] for x in c[4]]
                
                return _callexpr.mtype.rettype
            else:
                raise TypeMismatchInExpression(ast)
        else:
            raise Undeclared(Function(),ast.method.name)

    def visitId(self,ast,c):
        # c is tuple
        _id =  self.lookup(ast.name,c[0],lambda x: x.name)
        if _id is not None:
            return _id.mtype
        raise Undeclared(Identifier(),ast.name)

    def visitCallStmt(self, ast, c): 
        # c is tuple
        at = [self.visit(x,(c[0],False)) for x in ast.param]
        res = self.lookup(ast.method.name,c[0],lambda x: x.name)
        if res is None or not type(res.mtype) is MType or not type(res.mtype.rettype) is VoidType:
            raise Undeclared(Procedure(),ast.method.name)
        elif len(res.mtype.partype) != len(at):
            raise TypeMismatchInStatement(ast)            
        else:
            for x,y in zip(res.mtype.partype,at):
                if type(x) is ArrayType and type(y) is ArrayType:
                    if x.lower != y.lower or x.upper != y.upper or (x.eleType,y.eleType) != (FloatType,IntType):
                        raise TypeMismatchInStatement(ast)
                if type(x) != type(y):
                    raise TypeMismatchInStatement(ast)
            [c[4].remove((res.name,res.mtype.rettype)) if x == (res.name,res.mtype.rettype) else [] for x in c[4]]
            return res.mtype.rettype

    def visitIf(self,ast,c):
        if type(self.visit(ast.expr,c)) is not BoolType:
            raise TypeMismatchInStatement(ast)
        else:
            _returnThen = (c[0],c[1],c[2],[False],c[4])
            _returnElse = (c[0],c[1],c[2],[False],c[4])
            _thenStmt = reduce(lambda x,y: self.visit(y,_returnThen) if raiseNextast(x,y,c[3][0]) else [],ast.thenStmt,[])
            _elseStmt = reduce(lambda x,y: self.visit(y,_returnElse) if raiseNextast(x,y,c[3][0]) else [],ast.elseStmt,[])
            if _returnThen[3][0] and _returnElse[3][0]:
                c[3][0] = True
            else:
                c[3][0] = False

    def visitFor(self,ast,c):
        _idtype = self.visit(ast.id,c)
        _exprtype1 = self.visit(ast.expr1,c)
        _exprtype2 = self.visit(ast.expr2,c)
        if type(_idtype) is IntType and type(_exprtype1) is IntType and type(_exprtype2) is IntType:
            inloop = True
            _forbody = reduce(lambda x,y: self.visit(y,(c[0],c[1],inloop,c[3],c[4])) if raiseNextast(x,y,c[3][0]) else [],ast.loop,[])
            c[3][0] = False
        else:
            raise TypeMismatchInStatement(ast)
        #[self.visit(x,c) for x in ast.loop]

    def visitWhile(self,ast,c):
        _expr = self.visit(ast.exp,c)
        if type(_expr) is BoolType:
            inloop = True
            _whileBody = reduce(lambda x,y: self.visit(y,(c[0],c[1],inloop,c[3],c[4])) if raiseNextast(x,y,c[3][0]) else [],ast.sl,[])
            c[3][0] = False
        else:
            raise TypeMismatchInStatement(ast)

    def visitWith(self,ast,c):
        _expr = reduce(lambda x,y: [self.visit(y,x)] + x ,ast.decl,[])
        _expr = _expr + c[0]
        _withbody = reduce(lambda x,y: self.visit(y,(_expr,c[1],c[2],c[3],c[4])) if raiseNextast(x,y,c[3][0]) else [],ast.stmt,[])

    def visitReturn(self,ast,c):
        c[3][0] = True
        if type(c[1]) is VoidType:
            if ast.expr is not None:
                raise TypeMismatchInStatement(ast)
        else:
            if ast.expr is not None:
                _expr = self.visit(ast.expr,c)
                if type(_expr) is ArrayType and type(c[1]) is ArrayType: # ArrayType
                    if type(self.visit(c[1],c)) is not type(self.visit(_expr,c)) or\
                             _expr.lower != c[1].lower or\
                            _expr.upper != c[1].upper:
                        if  (type(self.visit(c[1],c)),type((self.visit(_expr,c)))) != (FloatType,IntType):
                            raise TypeMismatchInStatement(ast)
                else:
                    if type(c[1]) is not type(_expr):
                        if  (type(c[1]),type(_expr)) != (FloatType,IntType):
                            raise TypeMismatchInStatement(ast)
            else:
                raise TypeMismatchInStatement(ast)
        return Return()

    def visitBinaryOp(self,ast,c):
        _op = ast.op.lower()
        _left = self.visit(ast.left,c)
        _right = self.visit(ast.right,c)
        #print(_left,_right)
        _return = checkOp(_left,_right)
        #print(_return)
        if _return:
            if _op == ">" or _op == "<" or\
                _op == "=" or _op == "<>" or\
                _op == "<=" or _op == ">=" or\
                _op == "andthen" or _op == "orelse" or\
                _op == "or" or _op == "and":
                return BoolType()
            elif _op == "+" or _op == "-" or\
                _op == "*" or _op == "/":
                if type(_return) is BoolType:
                    raise TypeMismatchInExpression(ast)
                return _return
            else:
                return IntType()
        raise TypeMismatchInExpression(ast)

    def visitUnaryOp(self,ast,c):
        _op = ast.op.lower()
        _return = self.visit(ast.body,c)
        if _op == "not":
            if type(_return) is BoolType:
                return BoolType()
            raise TypeMismatchInExpression(ast)
        else:
            if type(_return) is BoolType:
                raise TypeMismatchInExpression(ast) 
            return _return

    def visitArrayCell(self,ast,c):
        _exprID = self.visit(ast.arr,c)
        _exprIdx = self.visit(ast.idx,c)
        if type(_exprID) is ArrayType and type(_exprIdx) is IntType:
            return _exprID.eleType
        raise TypeMismatchInExpression(ast)

    def visitBreak(self,ast,c):
        if c[2]:
            return Break()
        raise BreakNotInLoop()

    def visitContinue(self,ast,c):
        if c[2]:
            return Continue()
        raise ContinueNotInLoop()

    def visitIntLiteral(self,ast, c): 
        return IntType()

    def visitFloatLiteral(self,ast,c):
        return FloatType()

    def visitStringLiteral(self,ast,c):
        return StringType()

    def visitBooleanLiteral(self,ast,c):
        return BoolType()

    def visitIntType(self,ast,c):
        return IntType()    

    def visitFloatType(self,ast,c):
        return FloatType()

    def visitBoolType(self,ast,c):
        return BoolType()

    def visitStringType(self,ast,c):
        return StringType()

    def visitVoidType(self,ast,c):
        return VoidType()

    def visitArrayType(self,ast,c):
        return ast.eleType
