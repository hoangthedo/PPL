import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """var x:integer;
        procedure main();
        begin
            a:= a+b or c;
            b:= a or b +c; 
        end"""
        expect = str(Program([
            VarDecl(Id(x),IntType),
            FuncDecl(Id(main),[],VoidType(),[],
                [
                AssignStmt(Id(a),BinaryOp(or,BinaryOp(+,Id(a),Id(b)),Id(c))),

                AssignStmt(Id(b),BinaryOp(+,BinaryOp(or,Id(a),Id(b)),Id(c)))])]))
        self.assertTrue(TestAST.test(input,expect,300))


    '''def test_simple_function(self):
        """More complex program"""
        input = """var x,y:boolean;"""
        expect = str(Program([
            VarDecl(Id("x"),BoolType()),
            VarDecl(Id("y"),BoolType())]))
        self.assertTrue(TestAST.test(input,expect,301))
    def test_simple_function_2(self):
        """More complex program"""
        input = """var x,y:boolean;t,z:real;"""
        expect = str(Program([
            VarDecl(Id("x"),BoolType()),
            VarDecl(Id("y"),BoolType()),
            VarDecl(Id("t"),FloatType()),
            VarDecl(Id("z"),FloatType())]))
        self.assertTrue(TestAST.test(input,expect,302))
    def test_simple_function_3(self):
        """More complex program"""
        input = """var x,y:boolean;var t,z:real;"""
        expect = str(Program([
            VarDecl(Id("x"),BoolType()),
            VarDecl(Id("y"),BoolType()),
            VarDecl(Id("t"),FloatType()),
            VarDecl(Id("z"),FloatType())]))
        self.assertTrue(TestAST.test(input,expect,303))
    def test_simple_function_4(self):
        """More complex program"""
        input = """var x:array[1 .. 2] of integer;"""
        expect = str(Program([VarDecl(Id("x"),ArrayType(1,2,IntType()))]))
        self.assertTrue(TestAST.test(input,expect,304))
    def test_simple_function_5(self):
        """More complex program"""
        input = """
        function main(x,y:integer):integer;
        var a:real;
        begin 
        end"""
        expect = ""
        expect = str(Program([
            FuncDecl(
                Id("main"),
                [VarDecl(Id("x"),IntType()),VarDecl(Id("y"),IntType())]    
                ,[VarDecl(Id("a"),FloatType())]
                ,[]
                ,IntType())]))
        self.assertTrue(TestAST.test(input,expect,305))
    def test_simple_function_6(self):
        input = """
        function main(x,y:integer):integer;
        var a:real;
        begin
            putInt(); 
        end"""
        expect = ""
        expect = str(Program([
            FuncDecl(
                Id("main"),
                [VarDecl(Id("x"),IntType()),VarDecl(Id("y"),IntType())]
                ,[VarDecl(Id("a"),FloatType())]
                ,
                [
                CallStmt(Id("putInt"),[])
                ]
                ,IntType())]))
        self.assertTrue(TestAST.test(input,expect,306))
    def test_simple_function_7(self):
        input = """
        function main(x,y:integer):integer;
        var a:real;
        begin
            putInt(x+5); 
        end"""
        expect = ""
        expect = str(Program([
            FuncDecl(
                Id("main"),
                [VarDecl(Id("x"),IntType()),VarDecl(Id("y"),IntType())]
                ,[VarDecl(Id("a"),FloatType())]
                ,[CallStmt(Id("putInt"),[BinaryOp("+",Id("x"),IntLiteral(5))])]
                ,IntType())]))
        self.assertTrue(TestAST.test(input,expect,307))
    def test_simple_function_8(self):
        input = """
        function main(x,y:integer):integer;
        var a:real;
        begin
            putInt(x+5,x*x);
        end"""
        expect = ""
        expect = str(Program([
            FuncDecl(
                Id("main"),
                [VarDecl(Id("x"),IntType()),VarDecl(Id("y"),IntType())]
                ,[VarDecl(Id("a"),FloatType())],
                [
                CallStmt(Id("putInt"),[BinaryOp("+",Id("x"),IntLiteral(5)),BinaryOp("*",Id("x"),Id("x"))])
                ]
                ,IntType())]))
        self.assertTrue(TestAST.test(input,expect,308))
    def test_simple_function_9(self):
        input = """
        function main(x,y:integer):integer;
        var a:real;
        begin
            putInt(x+5,x*x);
            putInt(-x);
        end"""
        expect = ""
        expect = str(Program([
            FuncDecl(
                Id("main"),
                [VarDecl(Id("x"),IntType()),VarDecl(Id("y"),IntType())]
                ,[VarDecl(Id("a"),FloatType())]
                ,
                [
                CallStmt(Id("putInt"),[BinaryOp("+",Id("x"),IntLiteral(5)),BinaryOp("*",Id("x"),Id("x"))]),
                CallStmt(Id("putInt"),[UnaryOp("-",Id("x"))])
                ]
                
                ,IntType())]))
        self.assertTrue(TestAST.test(input,expect,309))
    def test_simple_function_10(self):
        input = """
        function main(x,y:integer):integer;
        var a:real;
        begin
            BREAK;
            COntinue;
        end"""
        expect = ""
        expect = str(Program([
            FuncDecl(
                Id("main"),
                [VarDecl(Id("x"),IntType()),VarDecl(Id("y"),IntType())]
                ,[VarDecl(Id("a"),FloatType())]
                ,
                [
                Break(),
                Continue()
                ]
                
                ,IntType())]))
        self.assertTrue(TestAST.test(input,expect,310))
    def test_simple_function_11(self):
        input = """
        function main(x,y:integer):integer;
        var a:real;
        begin
            print(a and b);
            print(x or y);
            print(a div c);
            print(a mod b);
            print(not c);
        end"""
        expect = str(Program([
            FuncDecl(
                Id("main"),
                [VarDecl(Id("x"),IntType()),VarDecl(Id("y"),IntType())]
                ,[VarDecl(Id("a"),FloatType())],
                [
                CallStmt(Id("print"),[BinaryOp("and",Id("a"),Id("b"))]),
                CallStmt(Id("print"),[BinaryOp("or",Id("x"),Id("y"))]),
                CallStmt(Id("print"),[BinaryOp("div",Id("a"),Id("c"))]),
                CallStmt(Id("print"),[BinaryOp("mod",Id("a"),Id("b"))]),
                CallStmt(Id("print"),[UnaryOp("not",Id("c"))])
                ]
                
                ,IntType())]))
        self.assertTrue(TestAST.test(input,expect,311))
    def test_simple_function_12(self):
        input = """
        function main(x,y:integer):integer;
        var a:real;
        begin
            while x>y do putInt(5);
        end"""
        expect = str(Program([
            FuncDecl(
                Id("main"),
                [VarDecl(Id("x"),IntType()),VarDecl(Id("y"),IntType())]
                ,[VarDecl(Id("a"),FloatType())]
                ,
                [
                While(BinaryOp(">",Id("x"),Id("y")),
                    [CallStmt(Id("putInt"),[IntLiteral(5)])])
                ]
                ,IntType())]))
        self.assertTrue(TestAST.test(input,expect,312))
    def test_simple_function_13(self):
        input = """
        function main(x,y:integer):integer;
        var a:real;
        begin
            while arr1[1]>5 do 
            begin
                putInt(5);
                putInt(10);
            end
        end"""
        expect = str(Program([
            FuncDecl(
                Id("main"),
                [VarDecl(Id("x"),IntType()),VarDecl(Id("y"),IntType())]
                ,[VarDecl(Id("a"),FloatType())],
                [
                While(
                    BinaryOp(">",ArrayCell(Id("arr1"),IntLiteral(1)),
                        IntLiteral(5))
                    ,[
                    CallStmt(Id("putInt"),[IntLiteral(5)])
                    ,CallStmt(Id("putInt"),[IntLiteral(10)])
                    ])
                ]
                ,IntType())]))
        self.assertTrue(TestAST.test(input,expect,313))
    def test_simple_function_14(self):
        input = """
        function main(x,y:integer):integer;
        var a:real;
        begin
            for i:=1 to n do
            begin
                putInt(5);
                putInt(10);
            end
        end"""
        expect = str(Program([
            FuncDecl(
                Id("main"),
                [VarDecl(Id("x"),IntType()),VarDecl(Id("y"),IntType())]
                ,[VarDecl(Id("a"),FloatType())]
                ,
                [
                For(Id("i"),
                    IntLiteral(1),
                    Id("n"),
                    True,
                    [
                    CallStmt(Id("putInt"),[IntLiteral(5)]),
                    CallStmt(Id("putInt"),[IntLiteral(10)])
                    ])
                ]  
                ,IntType())]))
        self.assertTrue(TestAST.test(input,expect,314))
    def test_simple_function_15(self):
        input = """
        function main(x,y:integer):integer;
        var a:real;
        begin
            a:=b;
        end"""
        expect = str(Program([
            FuncDecl(
                Id("main"),
                [VarDecl(Id("x"),IntType()),VarDecl(Id("y"),IntType())]
                ,[VarDecl(Id("a"),FloatType())]
                ,
                [Assign(Id("a"),Id("b"))]
                ,IntType())]))
        self.assertTrue(TestAST.test(input,expect,315))
    def test_simple_function_16(self):
        input = """
        function main(x,y:integer):integer;
        var a:real;
        begin
            a := b := c := d := e ;
        end"""
        expect = str(Program([
            FuncDecl(
                Id("main"),
                [VarDecl(Id("x"),IntType()),VarDecl(Id("y"),IntType())]
                ,[VarDecl(Id("a"),FloatType())]
                ,
                [
                Assign(Id("d"),Id("e")),
                Assign(Id("c"),Id("d")),
                Assign(Id("b"),Id("c")),
                Assign(Id("a"),Id("b"))
                ]
                ,IntType())]))
        self.assertTrue(TestAST.test(input,expect,316))
    def test_simple_function_17(self):
        input = """
        function main(x,y:integer):integer;
        var a:real;
        begin
            a := b[1] := c[x+1] := d := x*x+2 ;
        end"""
        expect = str(Program([
            FuncDecl(
                Id("main"),
                [VarDecl(Id("x"),IntType()),VarDecl(Id("y"),IntType())]
                ,[VarDecl(Id("a"),FloatType())]
                ,
                [
                Assign(Id("d"),BinaryOp("+",BinaryOp("*",Id("x"),Id("x")),IntLiteral(2))),
                Assign(ArrayCell(Id("c"),BinaryOp("+",Id("x"),IntLiteral(1))),Id("d")),
                Assign(ArrayCell(Id("b"),IntLiteral(1)),ArrayCell(Id("c"),BinaryOp("+",Id("x"),IntLiteral(1)))),
                Assign(Id("a"),ArrayCell(Id("b"),IntLiteral(1)))
                ]   
                ,IntType())]))
        self.assertTrue(TestAST.test(input,expect,317))
    def test_simple_function_18(self):
        input = """
        function main(x,y:integer):integer;
        var a:real;
        begin
            with a:integer;b: array [1 .. 2] of real;do
                begin
                    a:=2;
                    b:= function1();
                end
        end"""
        expect = str(Program([
            FuncDecl(
                Id("main"),
                [VarDecl(Id("x"),IntType()),VarDecl(Id("y"),IntType())]
                ,[VarDecl(Id("a"),FloatType())]
                ,
                [
                With([
                    VarDecl(Id("a"),IntType()),
                    VarDecl(Id("b"),ArrayType(1,2,FloatType()))
                    ],
                    [
                    Assign(Id("a"),IntLiteral(2)),
                    Assign(Id("b"),CallExpr(Id("function1"),[]))
                    ])
                ]
                
                ,IntType())]))
        self.assertTrue(TestAST.test(input,expect,318))
    def test_simple_function_19(self):
        input = """
        function giaithua(n:integer):integer;
        var gt:integer;
        begin
            gt:=1;
            for i:=1 to n do
            begin
                gt:= gt*i;
            end
            return gt;
        end
        Procedure main();
        begin
            putIntLn(giaithua(5));
        end
        """
        expect = str(Program([
            FuncDecl(
                Id("giaithua"),
                [VarDecl(Id("n"),IntType())]
                ,[VarDecl(Id("gt"),IntType())]
                ,
                [
                Assign(Id("gt"),IntLiteral(1)),
                For(Id("i"),IntLiteral(1),Id("n"),True,
                    [Assign(Id("gt"),BinaryOp("*",Id("gt"),Id("i")))])
                ,Return(Id("gt"))
                ]
                
                ,IntType()),
            FuncDecl(
                Id("main"),
                [],[],
                [CallStmt(Id("putIntLn"),[CallExpr(Id("giaithua"),[IntLiteral(5)])])]
                ,
                VoidType())]))
        self.assertTrue(TestAST.test(input,expect,319))
    def test_simple_function_20(self):
        input = """ 
        Procedure main();
        begin
            a:=b:=c:= abc()[5];
        end"""
        expect = str(Program([
            FuncDecl(Id("main"),
                [],[],
                [Assign(Id("c"),ArrayCell(CallExpr(Id("abc"),[]),IntLiteral(5))),
                Assign(Id("b"),Id("c")),
                Assign(Id("a"),Id("b"))]
                ,VoidType())]))
        self.assertTrue(TestAST.test(input,expect,320))
    def test_simple_function_21(self):
        input = """ 
        Procedure main();
        begin
            a:=b:=c:= abc()+dfc();
        end"""
        expect = str(Program([
            FuncDecl(Id("main"),
                [],[],
                [
                Assign(Id("c"),BinaryOp("+",CallExpr(Id("abc"),[]),CallExpr(Id("dfc"),[]))),
                Assign(Id("b"),Id("c")),
                Assign(Id("a"),Id("b"))]
                ,VoidType())]))
        self.assertTrue(TestAST.test(input,expect,321))
    def test_simple_function_22(self):
        input = """ 
        Procedure main();
        begin
            if a>b then
             a := 5;
        end"""
        expect = str(Program([
            FuncDecl(Id("main"),
                [],[],
                [
                If(BinaryOp(">",Id("a"),Id("b")),
                    [Assign(Id("a"),IntLiteral(5))],[])
                ]
                ,VoidType())]))
        self.assertTrue(TestAST.test(input,expect,322)) 
    def test_simple_function_23(self):
        input = """ 
        Procedure main();
        begin
            if a>b then
                a:=b;
            else
                b:=a;
        end"""
        expect = str(Program([
            FuncDecl(Id("main"),
                [],
                [],
                [
                If(BinaryOp(">",Id("a"),Id("b")),
                    [Assign(Id("a"),Id("b"))],
                    [Assign(Id("b"),Id("a"))])
                ],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,323))
    def test_simple_function_24(self):
        input = """ 
        Procedure main();
        begin
            if a>b then
                if a>5 then
                    a:=b;
            else b:=a;
        end"""
        expect = str(Program([
            FuncDecl(Id("main"),
                [],
                [],
                [
                If(BinaryOp(">",Id("a"),Id("b")),
                    [If(
                        BinaryOp(">",Id("a"),IntLiteral(5)),
                        [Assign(Id("a"),Id("b"))],
                        [Assign(Id("b"),Id("a"))])],[])
                ],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,324))
    def test_simple_function_25(self):
        input = """ 
        Procedure main();
        begin
            if a>b then
                if a>5 then
                    a:=b;
                else
                    if a>3 then
                        a:=3;
                    else
                        a:=0;
            else
                b:=a;
        end"""
        expect = str(Program([
            FuncDecl(Id("main"),
                [],
                [],
                [
                If(
                    BinaryOp(">",Id("a"),Id("b")),
                    [If(
                        BinaryOp(">",Id("a"),IntLiteral(5)),
                        [Assign(Id("a"),Id("b"))],
                        [If(
                            BinaryOp(">",Id("a"),IntLiteral(3)),
                            [Assign(Id("a"),IntLiteral(3))],
                            [Assign(Id("a"),IntLiteral(0))])])
                    ],
                    [Assign(Id("b"),Id("a"))])
                ],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,325))    

    def test_simple_function_26(self):
        input = """ 
        Procedure main();
        begin
            n:=2;
            while n<10 do
                n:=n*n;
        end"""
        expect = str(Program([
            FuncDecl(Id("main"),
                [],
                [],
                [
                Assign(Id("n"),IntLiteral(2)),
                While(
                    BinaryOp("<",Id("n"),IntLiteral(10)),
                    [Assign(Id("n"),BinaryOp("*",Id("n"),Id("n")))])
                ],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,326))
    def test_simple_function_27(self):
        input = """ 
        Procedure main();
        begin
            n:=2;
            while ((n<10) and (a>b)) do
                n:=n*n;
        end"""
        expect = str(Program([
            FuncDecl(Id("main"),
                [],
                [],
                [
                Assign(Id("n"),IntLiteral(2)),
                While(
                    BinaryOp("and",
                        BinaryOp("<",Id("n"),IntLiteral(10)),
                        BinaryOp(">",Id("a"),Id("b"))),
                    [Assign(Id("n"),BinaryOp("*",Id("n"),Id("n")))])
                ],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,327))
    def test_simple_function_28(self):
        input = """ 
        Procedure main();
        begin
            n:= a or b;
        end"""
        expect = str(Program([
            FuncDecl(Id("main"),
                [],
                [],
                [
                Assign(Id("n"),BinaryOp("or",Id("a"),Id("b")))
                ],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,328))
    def test_simple_function_29(self):
        input = """ 
        Procedure main();
        begin
            n:= a or b or c and d;
        end"""
        expect = str(Program([
            FuncDecl(Id("main"),
                [],
                [],
                [
                Assign(Id("n"),
                    BinaryOp("or",
                        BinaryOp("or",Id("a"),Id("b")),
                        BinaryOp("and",Id("c"),Id("d"))))
                ],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,329))
    def test_simple_function_30(self):
        input = """ 
        Procedure main();
        begin
            n:= a or b or c and d or e and f and g;
        end"""
        expect = str(Program([
            FuncDecl(Id("main"),
                [],
                [],
                [
                Assign(Id("n"),
                    BinaryOp("or",
                        BinaryOp("or",
                            BinaryOp("or",Id("a"),Id("b")),
                            BinaryOp("and",Id("c"),Id("d"))),
                        BinaryOp("and",
                            BinaryOp("and",Id("e"),Id("f")),
                            Id("g"))))
                ],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,330))
    def test_simple_function_31(self):
        input = """ 
        Procedure main();
        begin
            n:= 5>=a;
            m:= 6<=5;
            q:= 5<>2;
        end"""
        expect = str(Program([
            FuncDecl(Id("main"),
                [],
                [],
                [
                Assign(Id("n"),BinaryOp(">=",IntLiteral(5),Id("a"))),
                Assign(Id("m"),BinaryOp("<=",IntLiteral(6),IntLiteral(5))),
                Assign(Id("q"),BinaryOp("<>",IntLiteral(5),IntLiteral(2)))
                ],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,331))
    def test_simple_function_32(self):
        input = """ 
        Procedure main();
        begin
            n:= true;
            m:= False;
            q:= False;
        end"""
        expect = str(Program([
            FuncDecl(Id("main"),
                [],
                [],
                [
                Assign(Id("n"),BooleanLiteral(True)),
                Assign(Id("m"),BooleanLiteral(False)),
                Assign(Id("q"),BooleanLiteral(False))
                ],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,332))
    def test_simple_function_33(self):
        input = """ 
        Procedure main();
        begin
            n:= not a;
            m:= a+-c;
        end"""
        expect = str(Program([
            FuncDecl(Id("main"),
                [],
                [],
                [
                Assign(Id("n"),UnaryOp("not",Id("a"))),
                Assign(Id("m"),BinaryOp("+",Id("a"),UnaryOp("-",Id("c"))))
                ],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,333))
    def test_simple_function_34(self):
        input = """ 
        Procedure main();
        begin
            n:= not not a;
            //m:= - (-c);
            m:= --c;
        end"""
        expect = str(Program([
            FuncDecl(Id("main"),
                [],
                [],
                [
                Assign(Id("n"),UnaryOp("not",UnaryOp('not',Id('a')))),
                Assign(Id('m'),UnaryOp('-',UnaryOp('-',Id('c'))))
                ],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,334))
    def test_simple_function_35(self):
        input = """ 
        Procedure main();
        begin
            n:= 1.25;
            m:= 1.2e5;
            q:= 1. ;
            p:= .1 ;
        end"""
        expect = str(Program([
            FuncDecl(Id("main"),
                [],
                [],
                [
                Assign(Id("n"),FloatLiteral(1.25)),
                Assign(Id("m"),FloatLiteral(120000.0)),
                Assign(Id("q"),FloatLiteral(1.0)),
                Assign(Id("p"),FloatLiteral(0.1))
                ],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,335))
    def test_simple_function_36(self):
        input = """ 
        Procedure main();
        begin
            a:=a+5;
            b:=a-5;
            c:=5/2;
            d:=6*5;
            e:=g mod 5;
            g:=h div 5;
        end"""
        expect = str(Program([
            FuncDecl(Id("main"),
                [],
                [],
                [
                Assign(Id('a'),BinaryOp('+',Id('a'),IntLiteral(5))),
                Assign(Id('b'),BinaryOp('-',Id('a'),IntLiteral(5))),
                Assign(Id('c'),BinaryOp('/',IntLiteral(5),IntLiteral(2))),
                Assign(Id('d'),BinaryOp('*',IntLiteral(6),IntLiteral(5))),
                Assign(Id('e'),BinaryOp('mod',Id('g'),IntLiteral(5))),
                Assign(Id('g'),BinaryOp('div',Id('h'),IntLiteral(5)))]
                ,VoidType())]))
        self.assertTrue(TestAST.test(input,expect,336))
    def test_simple_function_37(self):
        input = """ 
        Procedure main();
        begin
            a:= a and b and not c and d;
        end"""
        expect = str(Program([
            FuncDecl(Id("main"),
                [],
                [],
                [
                Assign(Id("a"),
                    BinaryOp("and",
                        BinaryOp("and",
                            BinaryOp("and",Id("a"),Id("b")),
                            UnaryOp("not",Id("c"))),
                        Id("d")))
                ],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,337))
    def test_simple_function_38(self):
        input = """ 
        Procedure main();
        begin
            a:= 5+bcd()+edf()[1];
        end"""
        expect = str(Program([
            FuncDecl(Id("main"),
                [],
                [],
                [
                Assign(Id('a'),
                    BinaryOp('+',
                        BinaryOp('+',
                            IntLiteral(5),
                            CallExpr(Id('bcd'),[])),
                        ArrayCell(CallExpr(Id('edf'),[]),IntLiteral(1))))
                ],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,338))
    def test_simple_function_39(self):
        input = """ 
        Procedure main();
        begin
            a:= c/5/5-3+2--2*123+b;
        end"""
        expect = str(Program([
            FuncDecl(Id("main"),
                [],
                [],
                [
                Assign(Id('a'),
                    BinaryOp('+',
                        BinaryOp('-',
                            BinaryOp('+',
                                BinaryOp('-',
                                    BinaryOp('/',
                                        BinaryOp('/',
                                            Id('c'),
                                            IntLiteral(5))
                                        ,IntLiteral(5)),
                                    IntLiteral(3)),
                                IntLiteral(2)),
                            BinaryOp('*',
                                UnaryOp('-',
                                    IntLiteral(2)),
                                IntLiteral(123))),
                        Id('b')))]
                ,VoidType())]))
        self.assertTrue(TestAST.test(input,expect,339))
    def test_simple_function_40(self):
        input = """ 
        Procedure main();
        begin
            n:= a(1,2)[b(123+5)[c(174.145)]];
        end"""
        expect = str(Program([
            FuncDecl(Id("main"),
                [],
                [],
                [
                Assign(Id('n'),
                    ArrayCell(CallExpr(Id('a'),
                        [IntLiteral(1),IntLiteral(2)]),
                    ArrayCell(CallExpr(Id('b'),
                        [BinaryOp('+',IntLiteral(123),
                            IntLiteral(5))]),
                    CallExpr(Id('c'),
                        [FloatLiteral(174.145)]))))]
                ,VoidType())]))
        self.assertTrue(TestAST.test(input,expect,340))
    def test_simple_function_41(self):
        input = """ 
        Procedure main();
        begin
            n:=1;
            S:=0;
            while n<10 do
            begin
                S:=S+n;
                n:=n+1;
            end
        end"""
        expect = str(Program([
            FuncDecl(Id("main"),
                [],
                [], 
                [
                Assign(Id('n'),
                    IntLiteral(1)),
                Assign(Id('S'),IntLiteral(0)),
                While(BinaryOp('<',Id('n'),IntLiteral(10)),
                    [
                    Assign(Id('S'),BinaryOp('+',Id('S'),Id('n'))),
                    Assign(Id('n'),BinaryOp('+',Id('n'),IntLiteral(1)))
                    ])
                ],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,341))
    def test_simple_function_42(self):
        input = """ 
        Procedure main();
        begin
            n:=1;
            S:=0;
            while (n<10) and (s<20) do
            begin
                S:=S+n;
                n:=n+1;
            end
        end"""
        expect = str(Program([
            FuncDecl(Id("main"),
                [],
                [],
                [
                Assign(Id('n'),IntLiteral(1)),
                Assign(Id('S'),IntLiteral(0)),
                While(
                    BinaryOp('and',
                        BinaryOp('<',Id('n'),IntLiteral(10)),
                        BinaryOp('<',Id('s'),IntLiteral(20))),
                    [
                    Assign(Id('S'),BinaryOp('+',Id('S'),Id('n'))),
                    Assign(Id('n'),
                        BinaryOp('+',Id('n'),IntLiteral(1)))
                    ])
                ],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,342))
    def test_simple_function_43(self):
        input = """ 
        Procedure main();
        begin
            n:=10;
            S:=1;
            for i:=1 to n do
            begin
                S:=S*i;
                if(S>20) then
                    break;
            end
        end"""
        expect = str(Program([
            FuncDecl(Id("main"),
                [],
                [],
                [
                Assign(Id('n'),IntLiteral(10)),
                Assign(Id('S'),IntLiteral(1)),
                For(Id('i'),IntLiteral(1),
                    Id('n'),True,
                    [
                    Assign(Id('S'),
                        BinaryOp('*',Id('S'),Id('i'))),
                    If(BinaryOp('>',Id('S'),IntLiteral(20)),
                        [Break()],[])
                    ])
                ],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,343))
    def test_simple_function_44(self):
        input = """ 
        Procedure main();
        begin
            n:=10;
            S:=1;
            for i:=1 to n do
                S:=S*i;
        end"""
        expect = str(Program([
            FuncDecl(Id("main"),
                [],
                [],
                [
                Assign(Id('n'),IntLiteral(10)),
                Assign(Id('S'),IntLiteral(1)),
                For(Id('i'),IntLiteral(1),
                    Id('n'),True,
                    [
                    Assign(Id('S'),
                        BinaryOp('*',Id('S'),Id('i')))])
                ],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,344))

    def test_simple_function_45(self):
        input = """ 
        Procedure main();
        begin
            n:=1;
            S:=0;
            while (n<10) and (s<20) do
                n:=n+1;
        end"""
        expect = str(Program([
            FuncDecl(Id("main"),
                [],
                [],
                [
                Assign(Id('n'),IntLiteral(1)),
                Assign(Id('S'),IntLiteral(0)),
                While(
                    BinaryOp('and',
                        BinaryOp('<',Id('n'),IntLiteral(10)),
                        BinaryOp('<',Id('s'),IntLiteral(20))),
                    [
                    Assign(Id('n'),
                        BinaryOp('+',Id('n'),IntLiteral(1)))
                    ])
                ],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,345))
    def test_simple_function_46(self):
        input = """ 
        Procedure main();
        begin
            while 1<2 do begin
            end
                b := c[a]+b;
        end"""
        expect = str(Program([
            FuncDecl(Id("main"),
                [],
                [],
                [
                While(
                    BinaryOp('<',IntLiteral(1),IntLiteral(2)),
                    []),
                Assign(Id('b'),BinaryOp('+',ArrayCell(Id('c'),Id('a')),Id('b')))
                ],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,346))
    def test_simple_function_47(self):
        input = """ 
        Procedure main();
        begin
            with a:integer;b: array [1 .. 2] of real;do
                begin
                    a:=2;
                    b:= function1();
                end
        end"""
        expect = str(Program([
            FuncDecl(Id("main"),
                [],
                [],
                [
                With(
                    [
                    VarDecl(Id('a'),IntType()),
                    VarDecl(Id('b'),ArrayType(1,2,FloatType()))
                    ]
                    ,[
                    Assign(Id('a'),IntLiteral(2)),
                    Assign(Id('b'),CallExpr(Id('function1'),[]))])
                ],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,347))
    def test_simple_function_48(self):
        input = """ 
        Procedure main();
        begin
            n:= fucntion1(a,b,c);
        end"""
        expect = str(Program([
            FuncDecl(Id("main"),
                [],
                [],
                [Assign(Id('n'),
                    CallExpr(Id('fucntion1'),[Id('a'),Id('b'),Id('c')]))
                ],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,348))
    def test_simple_function_49(self):
        input = """ 
        //var a:array[1-2..5] ;
        Procedure main();
        begin
            k:=5+--5--5;
            n:=--5;
            m:=not not a;
            if 5<-15 then
            a:=5;
        end"""
        expect = str(Program([
            FuncDecl(Id("main"),
                [],
                [],
                [
                Assign(Id('k'),
                    BinaryOp('-',BinaryOp('+',IntLiteral(5),UnaryOp('-',UnaryOp('-',IntLiteral(5)))),
                    UnaryOp('-',IntLiteral(5)))),
                Assign(Id('n'),UnaryOp('-',UnaryOp('-',IntLiteral(5)))),
                Assign(Id('m'),UnaryOp('not',UnaryOp('not',Id('a')))),
                If(BinaryOp('<',IntLiteral(5),UnaryOp('-',IntLiteral(15))),
                    [
                    Assign(Id('a'),IntLiteral(5))
                    ],[])
                ],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,349))
    def test_simple_function_50(self):
        input = """ 
        Procedure main();
        var a,b,c,x,y,z:integer;
        begin
            if(y<5)and(z<10)then
            begin
            end
        end"""
        expect = str(Program([
            FuncDecl(Id("main"),
                [],
                [
                VarDecl(Id('a'),IntType()),
                VarDecl(Id('b'),IntType()),
                VarDecl(Id('c'),IntType()),
                VarDecl(Id('x'),IntType()),
                VarDecl(Id('y'),IntType()),
                VarDecl(Id('z'),IntType())
                ],
                [
                If(BinaryOp('and',BinaryOp('<',Id('y'),IntLiteral(5)),
                    BinaryOp('<',Id('z'),IntLiteral(10))),
                []
                ,[])
                ],
                VoidType())]))
        self.assertTrue(TestAST.test(input,expect,350))
    def test_simple_function_51(self):
        input = """ 
        var x:integer;
        var y:real;
        Procedure main();
        var a,b:integer;
        begin
            if(y<5)and(y<10)then
            begin
                x:=a;
                y:=b;
                putIntLn( x );
                putIntLn( y );
            end
        end"""
        expect = str(Program([
            VarDecl(Id('x'),IntType()),
            VarDecl(Id('y'),FloatType()),
            FuncDecl(Id("main"),
                [],
                [VarDecl(Id('a'),IntType()),
                VarDecl(Id('b'),IntType())],
                [
                If(BinaryOp('and',BinaryOp('<',Id('y'),IntLiteral(5)),
                    BinaryOp('<',Id('y'),IntLiteral(10))),
                [
                Assign(Id('x'),Id('a')),
                Assign(Id('y'),Id('b')),
                CallStmt(Id('putIntLn'),[Id('x')]),
                CallStmt(Id('putIntLn'),[Id('y')])],[])]
                ,VoidType())]))
        self.assertTrue(TestAST.test(input,expect,351))
    def test_simple_function_52(self):
        input = """ 
        var x:integer;
        var y:real;
        function increase(x:integer):integer;
        begin
            return x+1;
        end
        Procedure main();
        var a,b:integer;
        begin
            putIntLn(increase(x));
            putIntLn(increase(y));
        end"""
        expect = str(Program([
            VarDecl(Id('x'),IntType()),
            VarDecl(Id('y'),FloatType()),
            FuncDecl(Id('increase'),[VarDecl(Id('x'),IntType())],[],
                [
                Return(BinaryOp('+',Id('x'),IntLiteral(1)))
                ]
                ,IntType()),
            FuncDecl(Id('main'),[],
                [
                VarDecl(Id('a'),IntType()),
                VarDecl(Id('b'),IntType())
                ],
                [
                CallStmt(Id('putIntLn'),
                    [CallExpr(Id('increase'),
                        [Id('x')])]),
                CallStmt(Id('putIntLn'),
                    [CallExpr(Id('increase'),[Id('y')])])]
                ,VoidType())
            ]))
        self.assertTrue(TestAST.test(input,expect,352))
    def test_simple_function_53(self):
        input = """ 
        Procedure main();
        begin
            putIntLn("Hello Word!!!");
        end"""
        expect = str(Program([
            FuncDecl(Id("main"),
                [],
                [],
                [CallStmt(Id("putIntLn"),[StringLiteral("Hello Word!!!")])]
,
                VoidType())]))
        self.assertTrue(TestAST.test(input,expect,353))
    def test_simple_function_54(self):
        input = """ 
        function giaithua(n:integer):integer;
        var gt:integer;
        begin
            gt:=1;
            for i:=1 to n do
            begin
                gt:= gt*i;
            end
            return gt;
        end
        Procedure main();
        begin
            putIntLn(giaithua(5));
        end"""
        expect = str(Program([
        FuncDecl(
            Id('giaithua'),
            [VarDecl(Id('n'),IntType())],[VarDecl(Id('gt'),IntType())],
            [
            Assign(Id('gt'),IntLiteral(1)),
            For(Id('i'),IntLiteral(1),
                Id('n'),True,
                [
                Assign(Id('gt'),BinaryOp('*',Id('gt'),Id('i')))
                ]),
            Return(Id('gt'))
            ]
            ,IntType()),
        FuncDecl(Id('main'),[],[]
            ,
            [
            CallStmt(Id('putIntLn'),
                [CallExpr(Id('giaithua'),[IntLiteral(5)])]
                )]
            ,VoidType())]))
        self.assertTrue(TestAST.test(input,expect,354))
    def test_simple_function_55(self):
        input = """ 
        function tong_array(arr:array[1 .. 10] of integer):integer;
        var tong_:integer;
        begin
            tong_:=0;
            for i:=1 to 10 do
            begin
                tong_ := tong_+arr[i];
            end
            return tong_;
        end
        Procedure main();
        var k: array[1 .. 10] of integer;
        begin
            putIntLn(tong_array(k));
        end"""
        expect = str(Program([
        FuncDecl(
            Id('tong_array'),
            [VarDecl(Id('arr'),ArrayType(1,10,IntType()))]
            ,
            [VarDecl(Id('tong_'),IntType())]
            ,
            [
            Assign(Id('tong_'),IntLiteral(0)),
            For(Id('i'),IntLiteral(1),IntLiteral(10),True,
                [
                Assign(Id('tong_'),
                    BinaryOp('+',Id('tong_'),ArrayCell(Id('arr'),Id('i'))))]),
            Return(Id('tong_'))
            ],IntType()),
        FuncDecl(Id('main'),[],
            [VarDecl(Id('k'),ArrayType(1,10,IntType()))],
            [
            CallStmt(Id('putIntLn'),[CallExpr(Id('tong_array'),[Id('k')])])]
            ,VoidType())]))
        self.assertTrue(TestAST.test(input,expect,355))
    def test_simple_function_56(self):
        input = """ 
        Procedure main();
        begin
            putIntLn("Hello Word!!!\\n");
            putIntLn("Hello Word!!!\\n");
            putIntLn("Hello Word!!!\\n");
        end"""
        expect = str(Program([
            FuncDecl(Id('main'),[],[],
                [
                CallStmt(Id('putIntLn'),[StringLiteral('Hello Word!!!\\n')]),
                CallStmt(Id('putIntLn'),[StringLiteral('Hello Word!!!\\n')]),
                CallStmt(Id('putIntLn'),[StringLiteral('Hello Word!!!\\n')])]
                ,VoidType())]))
        self.assertTrue(TestAST.test(input,expect,356))
    def test_simple_function_57(self):
        input = """ 
        function sum_2_int(a,b:integer):integer;
        begin
            return a+b;
        end
        Procedure main();
        begin
            putIntLn(sum_2_int(1,2));
        end"""
        expect = str(Program([
            FuncDecl(Id('sum_2_int'),
                [VarDecl(Id('a'),IntType()),
                VarDecl(Id('b'),IntType())],[],
                [
                Return(BinaryOp('+',Id('a'),Id('b')))],IntType()),
            FuncDecl(Id('main'),
                [],[],[
                CallStmt(Id('putIntLn'),
                    [
                    CallExpr(Id('sum_2_int'),[IntLiteral(1),IntLiteral(2)])]
                    )
                ],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,357))

    def test_simple_function_58(self):
        input = """ 
        function div_2_int(a,b:integer):integer;
        begin
            return a/b;
        end
        Procedure main();
        begin
            putIntLn(div_2_int(1,2));
        end"""
        expect = str(Program([
            FuncDecl(Id('div_2_int'),
                [VarDecl(Id('a'),IntType()),
                VarDecl(Id('b'),IntType())],[],
                [
                Return(BinaryOp('/',Id('a'),Id('b')))],IntType()),
            FuncDecl(Id('main'),
                [],[],[
                CallStmt(Id('putIntLn'),
                    [
                    CallExpr(Id('div_2_int'),[IntLiteral(1),IntLiteral(2)])]
                    )
                ],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,358))
    def test_simple_function_59(self):
        input = """ 
        function mul_2_int(a,b:integer):integer;
        begin
            return a*b;
        end
        Procedure main();
        begin
            putIntLn(mul_2_int(1,2));
        end"""
        expect = str(Program([
            FuncDecl(Id('mul_2_int'),
                [VarDecl(Id('a'),IntType()),
                VarDecl(Id('b'),IntType())],[],
                [
                Return(BinaryOp('*',Id('a'),Id('b')))],IntType()),
            FuncDecl(Id('main'),
                [],[],[
                CallStmt(Id('putIntLn'),
                    [
                    CallExpr(Id('mul_2_int'),[IntLiteral(1),IntLiteral(2)])]
                    )
                ],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,359))
    def test_simple_function_60(self):
        input = """ 
        function sub_2_int(a,b:integer):integer;
        begin
            return a-b;
        end
        Procedure main();
        begin
            putIntLn(sub_2_int(1,2));
        end"""
        expect = str(Program([
            FuncDecl(Id('sub_2_int'),
                [VarDecl(Id('a'),IntType()),
                VarDecl(Id('b'),IntType())],[],
                [
                Return(BinaryOp('-',Id('a'),Id('b')))],IntType()),
            FuncDecl(Id('main'),
                [],[],[
                CallStmt(Id('putIntLn'),
                    [
                    CallExpr(Id('sub_2_int'),[IntLiteral(1),IntLiteral(2)])]
                    )
                ],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,360))
    def test_simple_function_61(self):
        input = """ 
        function mod_2_int(a,b:integer):integer;
        begin
            return a mod b;
        end
        Procedure main();
        begin
            putIntLn(mod_2_int(1,2));
        end"""
        expect = str(Program([
            FuncDecl(Id('mod_2_int'),
                [VarDecl(Id('a'),IntType()),
                VarDecl(Id('b'),IntType())],[],
                [
                Return(BinaryOp('mod',Id('a'),Id('b')))
                ],IntType()),
            FuncDecl(Id('main'),
                [],[],
                [
                CallStmt(Id('putIntLn'),
                    [
                    CallExpr(Id('mod_2_int'),[IntLiteral(1),IntLiteral(2)])]
                    )
                ]
                ,VoidType())]))
        self.assertTrue(TestAST.test(input,expect,361))
    def test_simple_function_62(self):
        input = """ 
        Function kt(n:integer):boolean;
        var i,d:integer;
        begin
            kt:=false;
            d:=0;
            For i:=1 to n do
                if n mod i=0 then inc(d);
            if d=2 then kt:=true;
        end"""
        expect = str(Program([
            FuncDecl(Id('kt'),
                [VarDecl(Id('n'),IntType())],
                [VarDecl(Id('i'),IntType()),VarDecl(Id('d'),IntType())],
                [
                Assign(Id('kt'),BooleanLiteral(False)),
                Assign(Id('d'),IntLiteral(0)),
                For(Id('i'),IntLiteral(1),Id('n'),True,
                    [
                    If(BinaryOp('=',BinaryOp('mod',Id('n'),Id('i')),IntLiteral(0)),
                        [CallStmt(Id('inc'),[Id('d')])],[])]),
                If(BinaryOp('=',Id('d'),IntLiteral(2)),
                    [Assign(Id('kt'),BooleanLiteral(True))],[])],BoolType())]))
        self.assertTrue(TestAST.test(input,expect,362))
    def test_simple_function_63(self):
        input = """ 
        Procedure main();
        var n: integer;
            m,tong,i: integer;
        BEGIN
            write("Nhap n:"); readln(n);
            write("Nhap m: "); readln(m);
            for i:=1 to m do
            begin
                tong:=tong+(n mod 10);
                n:=n div 10;
            end
        END"""
        expect = str(Program([
            FuncDecl(Id('main'),[],
                [VarDecl(Id('n'),IntType()),VarDecl(Id('m'),IntType()),
                VarDecl(Id('tong'),IntType()),VarDecl(Id('i'),IntType())],
                [
                CallStmt(Id('write'),[StringLiteral('Nhap n:')]),
                CallStmt(Id('readln'),[Id('n')]),
                CallStmt(Id('write'),[StringLiteral('Nhap m: ')]),
                CallStmt(Id('readln'),[Id('m')]),
                For(Id('i'),IntLiteral(1),Id('m'),True,
                    [
                    Assign(Id('tong'),BinaryOp('+',Id('tong'),BinaryOp('mod',Id('n'),IntLiteral(10)))),
                    Assign(Id('n'),BinaryOp('div',Id('n'),IntLiteral(10)))]
                    )]
                ,VoidType())]))
    def test_simple_function_64(self):
        input = """ 
        function factorial(n:integer):integer;
        var i:integer;
            prod:integer;
        begin
            prod:=1;
            for i:=1 to n do prod:=prod*i;
            factorial:=prod;
        end"""
        expect = str(Program([
            FuncDecl(Id('factorial'),
                [VarDecl(Id('n'),IntType())],
                [
                VarDecl(Id('i'),IntType()),
                VarDecl(Id('prod'),IntType())],
                [
                Assign(Id('prod'),IntLiteral(1)),
                For(Id('i'),IntLiteral(1),Id('n'),True,
                    [
                    Assign(Id('prod'),BinaryOp('*',Id('prod'),Id('i')))
                    ]),
                Assign(Id('factorial'),Id('prod'))
                ],IntType())]))
    def test_simple_function_65(self):
        input = """ 
        function power(x:real;y:integer):real;
        var p:real;
            i:integer;
        begin
            p:=1;
            for i:=1 to y do p:=p*x;
            power:=p;
        end
        procedure main();
        var x:real;
            y:integer;
        begin
            putIntLn("aaa : ",power(x,y));
        end"""
        expect = str(Program([
            FuncDecl(Id('power'),
                [VarDecl(Id('x'),FloatType()),
                VarDecl(Id('y'),IntType())],
                [
                VarDecl(Id('p'),FloatType()),
                VarDecl(Id('i'),IntType())],
                [
                Assign(Id('p'),IntLiteral(1)),
                For(Id('i'),IntLiteral(1),Id('y'),True,
                    [
                    Assign(Id('p'),BinaryOp('*',Id('p'),Id('x')))]),
                Assign(Id('power'),Id('p'))
                ],FloatType()),
            FuncDecl(Id('main'),[],
                [
                VarDecl(Id('x'),FloatType()),
                VarDecl(Id('y'),IntType())],
                [
                CallStmt(Id('putIntLn'),[StringLiteral('aaa : '),
                    CallExpr(Id('power'),[Id('x'),Id('y')])])
                ],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,365))
    def test_simple_function_66(self):
        input = """ 
        procedure main();
        var sum,i:integer;
        begin
            sum:=0;
            for i:=1 to 10 do sum:=sum+i;
            writeln(sum);
        end"""
        expect = str(Program([
            FuncDecl(Id('main'),[],
                [VarDecl(Id('sum'),IntType()),
                VarDecl(Id('i'),IntType())],
                [
                Assign(Id('sum'),IntLiteral(0)),
                For(Id('i'),IntLiteral(1),IntLiteral(10),True,
                    [
                    Assign(Id('sum'),BinaryOp('+',Id('sum'),Id('i')))]),
                CallStmt(Id('writeln'),[Id('sum')])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,366))
    def test_simple_function_67(self):
        input = """ 
        procedure main(n:integer);
        begin
            if(a>b)then a:=b;
            else
            begin
                a:=-b;
            end
        end"""
        expect = str(Program([
            FuncDecl(Id('main'),[VarDecl(Id('n'),IntType())],[],        
                [
                If(BinaryOp('>',Id('a'),Id('b')),
                    [
                    Assign(Id('a'),Id('b'))
                    ],
                    [
                    Assign(Id('a'),UnaryOp('-',Id('b')))
                    ])
                ]
                ,VoidType())]))
        self.assertTrue(TestAST.test(input,expect,367))
    def test_simple_function_68(self):
        input = """ 
        function factorial(n:integer):integer;
        var i:integer;
            prod:integer;
        begin
            prod:=1;
            for i:=1 to n do prod:=prod*i;
            factorial:=prod;
        end"""
        expect = str(Program([
            FuncDecl(Id('factorial'),
                [VarDecl(Id('n'),IntType())],
                [VarDecl(Id('i'),IntType()),
                VarDecl(Id('prod'),IntType())],
                [
                Assign(Id('prod'),IntLiteral(1)),
                For(Id('i'),IntLiteral(1),Id('n'),True,
                    [
                    Assign(Id('prod'),
                        BinaryOp('*',Id('prod'),Id('i')))]),
                Assign(Id('factorial'),Id('prod'))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,368))
    def test_simple_function_69(self):
        input = """ 
        procedure main();
        var n: string;
            m,i,a,tong: integer;
        BEGIN
           write("Nhap so n: "); readln(n);
           write("Nhap m: "); readln(m);
           for i:= length(n) downto length(n)-m+1 do
             begin
                 val(n[i],a);
                 tong:=tong+a;
             end
           write(tong);
        END"""
        expect = str(Program([
            FuncDecl(Id('main'),[],
                [VarDecl(Id('n'),StringType()),
                VarDecl(Id('m'),IntType()),
                VarDecl(Id('i'),IntType()),
                VarDecl(Id('a'),IntType()),
                VarDecl(Id('tong'),IntType())],
                [
                CallStmt(Id('write'),[StringLiteral('Nhap so n: ')]),
                CallStmt(Id('readln'),[Id('n')]),
                CallStmt(Id('write'),[StringLiteral('Nhap m: ')]),
                CallStmt(Id('readln'),[Id('m')]),
                For(Id('i'),CallExpr(Id('length'),[Id('n')]),
                    BinaryOp('+',BinaryOp('-',CallExpr(Id('length'),[Id('n')])
                        ,Id('m')),IntLiteral(1)),False,
                    [
                    CallStmt(Id('val'),[ArrayCell(Id('n'),Id('i')),Id('a')]),
                    Assign(Id('tong'),BinaryOp('+',Id('tong'),Id('a')))]),
                CallStmt(Id('write'),[Id('tong')])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,369))
    def test_simple_function_70(self):
        input = """ 
        procedure main();
        var n, i, j, count: integer;
        begin
            write("Nhap N (N>=1): "); readln(n);
            for i:=1 to n do
            begin
                j:=i;
                while j mod 5 = 0 do
                begin
                    j:=j div 5;
                    count:=count+1;
                end
            end
            write(" So chu so 0 cuoi cua ",n,"! la: ",count);
        end"""
        expect = str(Program([
            FuncDecl(Id('main'),[],
                [VarDecl(Id('n'),IntType()),
                VarDecl(Id('i'),IntType()),
                VarDecl(Id('j'),IntType()),
                VarDecl(Id('count'),IntType())
                ],
                [
                CallStmt(Id('write'),[StringLiteral('Nhap N (N>=1): ')]),
                CallStmt(Id('readln'),[Id('n')]),
                For(Id('i'),IntLiteral(1),Id('n'),True,
                    [
                    Assign(Id('j'),Id('i')),
                    While(BinaryOp('=',BinaryOp('mod',Id('j'),IntLiteral(5)),
                        IntLiteral(0)),
                    [
                    Assign(Id('j'),BinaryOp('div',Id('j'),IntLiteral(5))),
                    Assign(Id('count'),BinaryOp('+',Id('count'),IntLiteral(1)))])]),
                CallStmt(Id('write'),[StringLiteral(' So chu so 0 cuoi cua '),Id('n'),StringLiteral('! la: '),Id('count')])]
                ,VoidType())]))
        self.assertTrue(TestAST.test(input,expect,370))
    def test_simple_function_71(self):
        input = """ 
        procedure main();
        Var    St:String;
               dem: Array[1 .. 10] Of string;
               i:string;
               ch:string;
        Begin
            Write("Nhap xau St: "); Readln(St);
            For ch:="A" To "Z" Do dem[ch]:=0;
           
            For ch:="A" To "Z" Do 
                If dem[ch]>0 Then Writeln(ch," : ",dem[ch]);
        End"""
        expect = str(Program([
            FuncDecl(Id('main'),[],
                [
                VarDecl(Id('St'),StringType()),
                VarDecl(Id('dem'),ArrayType(1,10,StringType())),
                VarDecl(Id('i'),StringType()),
                VarDecl(Id('ch'),StringType())],
                [
                CallStmt(Id('Write'),[StringLiteral('Nhap xau St: ')]),
                CallStmt(Id('Readln'),[Id('St')]),
                For(Id('ch'),StringLiteral('A'),StringLiteral('Z'),True,
                    [
                    Assign(ArrayCell(Id('dem'),Id('ch')),IntLiteral(0))]),
                For(Id('ch'),StringLiteral('A'),StringLiteral('Z'),True,
                    [If(BinaryOp('>',ArrayCell(Id('dem'),Id('ch')),IntLiteral(0)),
                        [CallStmt(Id('Writeln'),[Id('ch'),StringLiteral(' : '),
                            ArrayCell(Id('dem'),Id('ch'))])],
                        [])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,371))
    def test_simple_function_72(self):
        input = """ 
                procedure main();
        Var a,b,c : integer;
        Begin
            Write("Nhap vao 3 so : ");Readln(a,b,c);
            If a>b then
            Begin
                a := a + b;
                b := a - b;
                a := a - b;
            End
            If b>c then
            Begin
                b := b + c;
                c := b - c;
                b := b - c;
            End
            If a>b then
            Begin
                a := a + b;
                b := a - b;
                a := a - b;
            End
            Writeln("Min = ",a);
            Writeln("Max = ",c);
        End"""
        expect = str(Program([
            FuncDecl(Id('main'),[],
                [
                VarDecl(Id('a'),IntType()),
                VarDecl(Id('b'),IntType()),
                VarDecl(Id('c'),IntType())],
                [
                CallStmt(Id('Write'),[StringLiteral('Nhap vao 3 so : ')]),
                CallStmt(Id('Readln'),[Id('a'),Id('b'),Id('c')]),
                If(BinaryOp('>',Id('a'),Id('b')),
                    [
                    Assign(Id('a'),BinaryOp('+',Id('a'),Id('b'))),
                    Assign(Id('b'),BinaryOp('-',Id('a'),Id('b'))),
                    Assign(Id('a'),BinaryOp('-',Id('a'),Id('b')))
                    ],[]),
                If(BinaryOp('>',Id('b'),Id('c')),
                    [
                    Assign(Id('b'),BinaryOp('+',Id('b'),Id('c'))),
                    Assign(Id('c'),BinaryOp('-',Id('b'),Id('c'))),
                    Assign(Id('b'),BinaryOp('-',Id('b'),Id('c')))],[]),
                If(BinaryOp('>',Id('a'),Id('b')),
                    [
                    Assign(Id('a'),BinaryOp('+',Id('a'),Id('b'))),
                    Assign(Id('b'),BinaryOp('-',Id('a'),Id('b'))),
                    Assign(Id('a'),BinaryOp('-',Id('a'),Id('b')))],[]),
                CallStmt(Id('Writeln'),[StringLiteral('Min = '),Id('a')]),
                CallStmt(Id('Writeln'),[StringLiteral('Max = '),Id('c')])]
                ,VoidType())]))
    def test_simple_function_73(self):
        input = """ 
        procedure main();
        VAR i,n :INTEGER;
        BEGIN
            Write ("Nhap n:");
            Readln(n);
            Write (n,"=");
            i:=2;
            While n<>1 do 
            Begin
                WHILE n MOD i <> 0 DO
                    i:=i+1;
                Write(i);
                n:=n DIV i;
                IF n > 1 THEN
                    write ("*");
            end
        END"""
        expect = str(Program([
            FuncDecl(Id('main'),[],
                [VarDecl(Id('i'),IntType()),VarDecl(Id('n'),IntType())],
                [
                CallStmt(Id('Write'),[StringLiteral('Nhap n:')]),
                CallStmt(Id('Readln'),[Id('n')]),
                CallStmt(Id('Write'),[Id('n'),StringLiteral('=')]),
                Assign(Id('i'),IntLiteral(2)),
                While(BinaryOp('<>',Id('n'),IntLiteral(1)),
                    [
                    While(BinaryOp('<>',BinaryOp('MOD',Id('n'),Id('i')),
                        IntLiteral(0)),
                    [
                    Assign(Id('i'),BinaryOp('+',Id('i'),IntLiteral(1)))
                    ]),
                    CallStmt(Id('Write'),[Id('i')]),
                    Assign(Id('n'),BinaryOp('DIV',Id('n'),Id('i'))),
                    If(BinaryOp('>',Id('n'),IntLiteral(1)),
                        [CallStmt(Id('write'),[StringLiteral('*')])],[])])]
                ,VoidType())]))
        self.assertTrue(TestAST.test(input,expect,373))

    def test_simple_function_74(self):
        input = """ 
        procedure main();
        var tcha,tcon,nam,kq:string;
        begin
            write("nhap tuoi con");
            readln(tcon);
            write();readln(tcha);
            while tcha<>2*tcon do
            begin
                nam:=nam+1;
                tcon:=tcon+1;
                tcha:=tcha+1;
            end
        end"""
        expect = str(Program([
            FuncDecl(Id('main'),[],
                [
                VarDecl(Id('tcha'),StringType()),
                VarDecl(Id('tcon'),StringType()),
                VarDecl(Id('nam'),StringType()),
                VarDecl(Id('kq'),StringType())],
                [
                CallStmt(Id('write'),[StringLiteral('nhap tuoi con')]),
                CallStmt(Id('readln'),[Id('tcon')]),
                CallStmt(Id('write'),[]),
                CallStmt(Id('readln'),[Id('tcha')]),
                While(BinaryOp('<>',Id('tcha'),BinaryOp('*',IntLiteral(2),Id('tcon'))),
                    [
                    Assign(Id('nam'),BinaryOp('+',Id('nam'),IntLiteral(1))),
                    Assign(Id('tcon'),BinaryOp('+',Id('tcon'),IntLiteral(1))),
                    Assign(Id('tcha'),BinaryOp('+',Id('tcha'),IntLiteral(1)))])]
                ,VoidType())]))
        self.assertTrue(TestAST.test(input,expect,374))

    def test_simple_function_75(self):
        input = """ 
        procedure main();
        Var a:array[1 .. 100] of integer;
            n,i:integer;
        Begin
          write("Do dai cua mang can nhap?");
          readln(n);
          For i:=1 to n do 
          begin
            write("Phan tu thu ",i,"=?");
            readln(a[i]);
          end
          writeln("Mang dao nguoc la :");
          For i:=n downto 1 do write(a[i]);
        End"""
        expect = str(Program([
            FuncDecl(Id('main'),[],
                [
                VarDecl(Id('a'),ArrayType(1,100,IntType())),
                VarDecl(Id('n'),IntType()),
                VarDecl(Id('i'),IntType())],
                [
                CallStmt(Id('write'),[StringLiteral('Do dai cua mang can nhap?')]),
                CallStmt(Id('readln'),[Id('n')]),
                For(Id('i'),IntLiteral(1),Id('n'),True,
                    [
                    CallStmt(Id('write'),[StringLiteral('Phan tu thu '),Id('i'),StringLiteral('=?')]),
                    CallStmt(Id('readln'),[ArrayCell(Id('a'),Id('i'))])]),
                CallStmt(Id('writeln'),[StringLiteral('Mang dao nguoc la :')]),
                For(Id('i'),Id('n'),IntLiteral(1),False,
                    [
                    CallStmt(Id('write'),[ArrayCell(Id('a'),Id('i'))])])]
                ,VoidType())]))
        self.assertTrue(TestAST.test(input,expect,375))
    def test_simple_function_76(self):
        input = """ 
        function abc():array [1 .. 3] of string;
        var a,b,c,d:integer;
            x,y:array [1 .. 3] of string;
        begin
            a:=5;
            c:=b-5;
        end
        Procedure main();
        begin
        end"""
        expect = str(Program([
            FuncDecl(Id('abc'),[],
                [
                VarDecl(Id('a'),IntType()),
                VarDecl(Id('b'),IntType()),
                VarDecl(Id('c'),IntType()),
                VarDecl(Id('d'),IntType()),
                VarDecl(Id('x'),ArrayType(1,3,StringType())),
                VarDecl(Id('y'),ArrayType(1,3,StringType()))
                ]
                ,
                [
                Assign(Id('a'),IntLiteral(5)),
                Assign(Id('c'),BinaryOp('-',Id('b'),IntLiteral(5)))
                ]
                ,ArrayType(1,3,StringType())),
            FuncDecl(Id('main'),[],[],[],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,376))
    def test_simple_function_77(self):
        input = """ 
        Procedure abc();
        var a,b,c,d:integer;
            x,y:array [1 .. 3] of string;
        begin

        end
        Procedure main();
        begin
        end"""
        expect = str(Program([
            FuncDecl(Id('abc'),[],
                [
                VarDecl(Id('a'),IntType()),
                VarDecl(Id('b'),IntType()),
                VarDecl(Id('c'),IntType()),
                VarDecl(Id('d'),IntType()),
                VarDecl(Id('x'),ArrayType(1,3,StringType())),
                VarDecl(Id('y'),ArrayType(1,3,StringType()))
                ],
                [
                ],VoidType()
                ),
            FuncDecl(Id('main'),[],[],[],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,377))
    def test_simple_function_78(self):
        input = """ 
        Procedure main();
        begin
            n:= not a;
            m:= a+-c;
        end"""
        expect = str(Program([
            FuncDecl(Id("main"),
                [],
                [],
                [
                Assign(Id("n"),UnaryOp("not",Id("a"))),
                Assign(Id("m"),BinaryOp("+",Id("a"),UnaryOp("-",Id("c"))))
                ],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,378))
    def test_simple_function_79(self):
        input = """ 
        Procedure main();
        begin
            a:=b:=c:= abc()+foo1();
        end"""
        expect = str(Program([
            FuncDecl(Id("main"),
                [],
                [],
                [
                Assign(Id("c"),BinaryOp("+",CallExpr(Id("abc"),[]),CallExpr(Id("foo1"),[]))),
                Assign(Id("b"),Id("c")),
                Assign(Id("a"),Id("b"))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,379))
    def test_simple_function_80(self):
        input = """ 
        Procedure main();
        begin
            if a>b then
                if a>5 then
                    a:=b;
                else
                    if a>3 then
                        a:=3;
            else
                b:=a;
        end"""
        expect = str(Program([
            FuncDecl(Id("main"),
                [],
                [],
                [
                If(
                    BinaryOp(">",Id("a"),Id("b")),
                    [If(
                        BinaryOp(">",Id("a"),IntLiteral(5)),
                        [Assign(Id("a"),Id("b"))],
                        [If(
                            BinaryOp(">",Id("a"),IntLiteral(3)),
                            [Assign(Id("a"),IntLiteral(3))],
                            [Assign(Id("b"),Id("a"))])])
                    ],
                    [])
                ],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,380)) 
    def test_simple_function_81(self):
        input = """ 
        Procedure main();
        begin
            n:= a or b or c and f;
        end"""
        expect = str(Program([
            FuncDecl(Id("main"),
                [],
                [],
                [
                Assign(Id("n"),
                    BinaryOp("or",
                        BinaryOp("or",Id("a"),Id("b")),
                        BinaryOp("and",Id("c"),Id("f"))))
                ],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,381))
    def test_simple_function_82(self):
        input = """ 
        var x:integer;
        var y:real;
        Procedure main();
        var a,b:integer;
        begin
            if(y<5)and(y<10)then
            begin
                x:=a;
                y:=b;
                putIntLn( x );
            end
        end"""
        expect = str(Program([
            VarDecl(Id('x'),IntType()),
            VarDecl(Id('y'),FloatType()),
            FuncDecl(Id("main"),
                [],
                [VarDecl(Id('a'),IntType()),
                VarDecl(Id('b'),IntType())],
                [
                If(BinaryOp('and',BinaryOp('<',Id('y'),IntLiteral(5)),
                    BinaryOp('<',Id('y'),IntLiteral(10))),
                [
                Assign(Id('x'),Id('a')),
                Assign(Id('y'),Id('b')),
                CallStmt(Id('putIntLn'),[Id('x')])],[])]
                ,VoidType())]))
        self.assertTrue(TestAST.test(input,expect,382))
    def test_simple_function_83(self):
        input = """ 
        Procedure main();
        begin
            result:= func1(a,b,c);
        end"""
        expect = str(Program([
            FuncDecl(Id("main"),
                [],
                [],
                [Assign(Id('result'),
                    CallExpr(Id('func1'),[Id('a'),Id('b'),Id('c')]))
                ],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,383))
    def test_simple_function_84(self):
        input = """ 
        Function kt(n:integer):boolean;
        var i,d:integer;
        begin
            kt:=false;
            d:=0;
            For i:=1 to n do
                if n mod i=0 then inc(d);
        end"""
        expect = str(Program([
            FuncDecl(Id('kt'),
                [VarDecl(Id('n'),IntType())],
                [VarDecl(Id('i'),IntType()),VarDecl(Id('d'),IntType())],
                [
                Assign(Id('kt'),BooleanLiteral(False)),
                Assign(Id('d'),IntLiteral(0)),
                For(Id('i'),IntLiteral(1),Id('n'),True,
                    [
                    If(BinaryOp('=',BinaryOp('mod',Id('n'),Id('i')),IntLiteral(0)),
                        [CallStmt(Id('inc'),[Id('d')])],[])])]
                ,BoolType())]))
        self.assertTrue(TestAST.test(input,expect,384))
    def test_simple_function_85(self):
        input = """ 
        Procedure main();
        begin
            n:=1;
            S:=0;
            while (n<10) and (s<20) do
            begin
                S:=S+n;
                n:=n+1;
            end
        end"""
        expect = str(Program([
            FuncDecl(Id("main"),
                [],
                [],
                [
                Assign(Id('n'),IntLiteral(1)),
                Assign(Id('S'),IntLiteral(0)),
                While(
                    BinaryOp('and',
                        BinaryOp('<',Id('n'),IntLiteral(10)),
                        BinaryOp('<',Id('s'),IntLiteral(20))),
                    [
                    Assign(Id('S'),BinaryOp('+',Id('S'),Id('n'))),
                    Assign(Id('n'),
                        BinaryOp('+',Id('n'),IntLiteral(1)))
                    ])
                ],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,385))
    def test_simple_function_86(self):
        input = """ 
        Procedure main();
        begin
            with a:integer;b: array [1 .. 2] of real;do
                begin
                    b:= function1();
                    a:=b;
                end
        end"""
        expect = str(Program([
            FuncDecl(Id("main"),
                [],
                [],
                [
                With(
                    [
                    VarDecl(Id('a'),IntType()),
                    VarDecl(Id('b'),ArrayType(1,2,FloatType()))
                    ]
                    ,[
                    Assign(Id('b'),CallExpr(Id('function1'),[])),
                    Assign(Id('a'),Id('b'))
                    ])
                ],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,386))
    def test_simple_function_87(self):
        input = """ 
        Procedure main();
        begin
            if a>b then
                if a>5 then
                    b:=a;
            else a:=b;
        end"""
        expect = str(Program([
            FuncDecl(Id("main"),
                [],
                [],
                [
                If(BinaryOp(">",Id("a"),Id("b")),
                    [If(
                        BinaryOp(">",Id("a"),IntLiteral(5)),
                        [Assign(Id("b"),Id("a"))],
                        [Assign(Id("a"),Id("b"))])],[])
                ],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,387))
    def test_simple_function_88(self):
        input = """ 
        Procedure main();
        begin
            n:=15;
            S:=0;
            while (n<10) and (s<20) do
                n:=n-1;
        end"""
        expect = str(Program([
            FuncDecl(Id("main"),
                [],
                [],
                [
                Assign(Id('n'),IntLiteral(15)),
                Assign(Id('S'),IntLiteral(0)),
                While(
                    BinaryOp('and',
                        BinaryOp('<',Id('n'),IntLiteral(10)),
                        BinaryOp('<',Id('s'),IntLiteral(20))),
                    [
                    Assign(Id('n'),
                        BinaryOp('-',Id('n'),IntLiteral(1)))
                    ])
                ],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,388))
    def test_simple_function_89(self):
        input = """ 
        Procedure main();
        begin
            while 1<2 do begin
            end
                a := c[a]+a;
        end"""
        expect = str(Program([
            FuncDecl(Id("main"),
                [],
                [],
                [
                While(
                    BinaryOp('<',IntLiteral(1),IntLiteral(2)),
                    []),
                Assign(Id('a'),BinaryOp('+',ArrayCell(Id('c'),Id('a')),Id('a')))
                ],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,389))
    def test_simple_function_90(self):
        input = """ 
        var x,y:array[-1 .. 2]of integer;"""
        expect = str(Program([
            VarDecl(Id("x"),ArrayType(-1,2,IntType())),
            VarDecl(Id("y"),ArrayType(-1,2,IntType()))]))
        self.assertTrue(TestAST.test(input,expect,390))
    def test_simple_function_91(self):
        input = """ 
        Procedure main();
        begin
            while 1<2 do 
            begin
                begin
                    begin if a > 0 then
                    	begin
                    	end
                    	a:=b;
                    end
                end
                begin
                end
            end
        end
        """
        expect = str(Program(
        	[FuncDecl(Id("main"),[],[],
        		[While(
        			BinaryOp("<",IntLiteral(1),IntLiteral(2)),
        			[If(
        				BinaryOp(">",Id("a"),IntLiteral(0)),
        				[],
        				[]),
        			Assign(Id("a"),Id("b"))
        			])
        		],
        		VoidType())
        	]))
        self.assertTrue(TestAST.test(input,expect,391))
    def test_simple_function_92(self):
        input = """ 
        Procedure main();
        begin
            while 1<2 do 
            x:= a=5 And Then a=10;
        end
        """
        expect = str(Program([
            FuncDecl(Id('main'),[],[],
                [
                While(BinaryOp('<',IntLiteral(1),IntLiteral(2)),
                    [Assign(Id('x'),
                        BinaryOp('andthen',
                            BinaryOp('=',Id('a'),IntLiteral(5)),
                            BinaryOp('=',Id('a'),IntLiteral(10))))
                    ])
                ],VoidType()
                )]))
        self.assertTrue(TestAST.test(input,expect,392))
    def test_simple_function_93(self):
        input = """ 
        Procedure main();
        begin
            while 1<2 OR ELSE 2>10 do 
            x:= 5;
        end
        """
        expect = str(Program([
            FuncDecl(Id('main'),[],[],
                [
                While(BinaryOp('orelse',
                    BinaryOp('<',IntLiteral(1),IntLiteral(2)),
                    BinaryOp('>',IntLiteral(2),IntLiteral(10))),
                [Assign(Id('x'),IntLiteral(5))])
                ],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,393))
    def test_simple_function_94(self):
        input = """ 
        Procedure main();
        begin
            if a>b then 
                begin
                end
            else
                begin
                end
        end
        """
        expect = str(Program([
            FuncDecl(Id('main'),[],[],
                [If(BinaryOp('>',Id('a'),Id('b')),[],[])]
                ,VoidType()
                )]))
        self.assertTrue(TestAST.test(input,expect,394))
    def test_simple_function_95(self):
        input = """ 
        Procedure main();
        begin
            x := (foo2())[5];
        end
        """
        expect = str(Program([
            FuncDecl(Id('main'),[],[],
                [
                Assign(Id('x'),
                    ArrayCell(CallExpr(Id('foo2'),[]),IntLiteral(5)))
                ],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,395))
    def test_simple_function_96(self):
        input = """ 
        Procedure main();
        begin
            // arr is an array
            x := (((arr)))[5];
        end
        """
        expect = str(Program([
            FuncDecl(Id('main'),[],[],
                [
                Assign(Id('x'),
                    ArrayCell(Id('arr'),IntLiteral(5)))
                ],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,396))
    def test_simple_function_97(self):
        input = """ 
        Procedure main();
        begin
            // arr is an array
            x := ((arr))[foo2(5*10)[0]];
        end
        """
        expect = str(Program([
            FuncDecl(Id('main'),[],[],
                [
                Assign(Id('x'),
                    ArrayCell(Id('arr'),
                        ArrayCell(
                            CallExpr(Id('foo2'),
                                [BinaryOp('*',IntLiteral(5),IntLiteral(10))])
                            ,IntLiteral(0))))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,397))
    def test_simple_function_98(self):
        input = """ 
        Procedure main();
        begin
            x := -((a()))[2]+5;
        end
        """
        expect = str(Program([
            FuncDecl(Id('main'),[],[],
                [
                Assign(Id('x'),
                    BinaryOp('+',
                        UnaryOp('-',ArrayCell(CallExpr(Id('a'),[]),IntLiteral(2))),
                        IntLiteral(5)))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,398))
    def test_simple_function_99(self):
        input = """ 
        Procedure main();
        begin
            x := -((a()))[2] and then abc(arr[1]) + 5 - 10 and not b;
        end
        """
        expect = str(Program([
            FuncDecl(Id('main'),[],[],
                [
                Assign(Id('x'),
                    BinaryOp('andthen',
                        UnaryOp('-',ArrayCell(CallExpr(Id('a'),[]),IntLiteral(2))),
                        BinaryOp('-',
                            BinaryOp('+',CallExpr(Id('abc'),[ArrayCell(Id('arr'),IntLiteral(1))]),
                                IntLiteral(5)),BinaryOp('and',IntLiteral(10),UnaryOp('not',Id('b'))))))]
                ,VoidType())]))
        self.assertTrue(TestAST.test(input,expect,399))'''