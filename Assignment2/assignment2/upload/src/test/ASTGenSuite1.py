import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """var a,b,c:array[1 .. 2] of integer;
                        a,b,c:integer;"""
        expect = str(Program([
            VarDecl(Id("a"),ArrayType("1","2",IntType())),
            VarDecl(Id("b"),ArrayType("1","2",IntType())),
            VarDecl(Id("c"),ArrayType("1","2",IntType())),
            VarDecl(Id("a"),IntType()),
            VarDecl(Id("b"),IntType()),
            VarDecl(Id("c"),IntType())
            ]))
        self.assertTrue(TestAST.test(input,expect,300))

    def test_simple_function1(self):
        """More complex program"""
        input = """function foo ():INTEGER; begin
        end"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[],IntType())]))
        self.assertTrue(TestAST.test(input,expect,301))

    def test_simple_function2(self):
        """More complex program"""
        input = """function foo ():INTEGER; begin
            putIntLn(4);
        end"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[CallStmt(Id("putIntLn"),[IntLiteral(4)])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,302))

    def test_simple_function3(self):
        """More complex program"""
        input = """function foo (a:real):INTEGER;
        begin
            putIntLn(4);
        end"""
        expect = str(Program([
            FuncDecl(Id("foo"),[VarDecl(Id("a"),FloatType())],[],[CallStmt(Id("putIntLn"),[IntLiteral(4)])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,303))

    def test_simple_function4(self):
        """More complex program"""
        input = """function foo (a:real):INTEGER;
        var a:real;
        begin
            putIntLn(4);
        end"""
        expect = str(Program([
            FuncDecl(Id("foo"),[VarDecl(Id("a"),FloatType())],[VarDecl(Id("a"),FloatType())],[CallStmt(Id("putIntLn"),[IntLiteral(4)])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,304))

    def test_simple_function5(self):
        """More complex program"""
        input = """function foo (a:real; b:integer):INTEGER;
        var a:real;
        begin
            putIntLn(4);
        end"""
        expect = str(Program([
            FuncDecl(
                Id("foo"),
                [VarDecl(Id("a"),FloatType()),VarDecl(Id("b"),IntType())],
                [VarDecl(Id("a"),FloatType())],
                [CallStmt(Id("putIntLn"),[IntLiteral(4)])],
                IntType())]))
        self.assertTrue(TestAST.test(input,expect,305))

    def test_simple_function6(self):
        """More complex program"""
        input = """function foo (a:real; b:integer):INTEGER;
        var a,b:real;
        begin
            putIntLn(4);
        end"""
        expect = str(Program([
            FuncDecl(Id("foo"),
                [VarDecl(Id("a"),FloatType()),VarDecl(Id("b"),IntType())],
                [VarDecl(Id("a"),FloatType()),VarDecl(Id("b"),FloatType())],
                [CallStmt(Id("putIntLn"),[IntLiteral(4)])],
                IntType())]))
        self.assertTrue(TestAST.test(input,expect,306))

    def test_simple_function7(self):
        """More complex program"""
        input = """function foo (a:real; b:integer):INTEGER;
        var a,b:real;
        begin
            putIntLn(4);
        end"""
        expect = str(Program([
            FuncDecl(Id("foo"),
                [VarDecl(Id("a"),FloatType()),VarDecl(Id("b"),IntType())],
                [VarDecl(Id("a"),FloatType()),VarDecl(Id("b"),FloatType())],
                [CallStmt(Id("putIntLn"),[IntLiteral(4)])],
                IntType()
                )]))
        self.assertTrue(TestAST.test(input,expect,307))

    def test_simple_function8(self):
        """More complex program"""
        input = """function foo (a:real; b:integer):INTEGER;
        begin
            while a > 0 do begin
            end
        end"""
        expect = str(Program([
            FuncDecl(Id("foo"),
                [VarDecl(Id("a"),FloatType()),VarDecl(Id("b"),IntType())],
                [],
                [While(BinaryOp(">",Id("a"),IntLiteral("0")),[])],
                IntType()
                )]))
        self.assertTrue(TestAST.test(input,expect,308))

    def test_simple_function9(self):
        """More complex program"""
        input = """function foo (a:real; b:integer):INTEGER;
        begin
            while a > 0 do begin
                break;
            end
        end"""
        expect = str(Program([
            FuncDecl(
                Id("foo"),
                [VarDecl(Id("a"),FloatType()),VarDecl(Id("b"),IntType())],
                [],
                [While(
                    BinaryOp(">",Id("a"),IntLiteral("0")),
                    ["Break"])],
                IntType()
                )]))
        self.assertTrue(TestAST.test(input,expect,309))

    def test_simple_function10(self):
        """More complex program"""
        input = """function foo (a:real; b:integer):INTEGER;
        begin
            while a > 0 do begin
            end
            while a >0 do begin
            end
        end"""
        expect = str(Program([
            FuncDecl(
                Id("foo"),
                [VarDecl(Id("a"),FloatType()),VarDecl(Id("b"),IntType())],
                [],
                [While(
                    BinaryOp(">",Id("a"),IntLiteral("0")),
                    []),
                While(
                    BinaryOp(">",Id("a"),IntLiteral("0")),
                    []),],
                IntType()
                )]))
        self.assertTrue(TestAST.test(input,expect,310))

    def test_simple_function11(self):
        """More complex program"""
        input = """function foo (a:real; b:integer):INTEGER;
        begin
            while a > 0 do begin
                putIntLn(4);
            end
        end"""
        expect = str(Program([
            FuncDecl(
                Id("foo"),
                [VarDecl(Id("a"),FloatType()),VarDecl(Id("b"),IntType())],
                [],
                [While(
                    BinaryOp(">",Id("a"),IntLiteral("0")),
                    [CallStmt(Id("putIntLn"),[IntLiteral(4)])])],
                IntType()
                )]))
        self.assertTrue(TestAST.test(input,expect,311))

    def test_simple_function12(self):
        """More complex program"""
        input = """function foo (a:real; b:integer):INTEGER;
        begin
            while a > 0 do begin
                while a > 0 do begin
                    putIntLn(4);
                end
            end
        end"""
        expect = str(Program([
            FuncDecl(
                Id("foo"),
                [VarDecl(Id("a"),FloatType()),VarDecl(Id("b"),IntType())],
                [],
                [While(
                    BinaryOp(">",Id("a"),IntLiteral("0")),
                    [While(
                    BinaryOp(">",Id("a"),IntLiteral("0")),
                    [CallStmt(Id("putIntLn"),[IntLiteral(4)])])])],
                IntType()
                )]))
        self.assertTrue(TestAST.test(input,expect,312))

    def test_simple_function13(self):
        """More complex program"""
        input = """function foo (a:real; b:integer):INTEGER;
        begin
            while a > 0 do begin
                while a > 0 do begin
                    putIntLn(4);
                    putIntLn(4);
                end
            end
        end"""
        expect = str(Program([
            FuncDecl(
                Id("foo"),
                [VarDecl(Id("a"),FloatType()),VarDecl(Id("b"),IntType())],
                [],
                [While(
                    BinaryOp(">",Id("a"),IntLiteral("0")),
                    [While(
                    BinaryOp(">",Id("a"),IntLiteral("0")),
                    [CallStmt(Id("putIntLn"),[IntLiteral(4)]),CallStmt(Id("putIntLn"),[IntLiteral(4)])])])],
                IntType()
                )]))
        self.assertTrue(TestAST.test(input,expect,313))

    def test_simple_function14(self):
        """More complex program"""
        input = """function foo (a:real; b:integer):INTEGER;
        begin
            if a > 0 then 
                putIntLn(4);
        end"""
        expect = str(Program([
            FuncDecl(
                Id("foo"),
                [VarDecl(Id("a"),FloatType()),VarDecl(Id("b"),IntType())],
                [],
                [If(BinaryOp(">",Id("a"),IntLiteral(0)),[CallStmt(Id("putIntLn"),[IntLiteral(4)])])],
                IntType()
                )]))
        self.assertTrue(TestAST.test(input,expect,314))

    def test_simple_function15(self):
        """More complex program"""
        input = """function foo (a:real; b:integer):INTEGER;
        begin
            if a > 0 then 
                putIntLn(4);
            else 
                putIntLn(4);
        end"""
        expect = str(Program([
            FuncDecl(
                Id("foo"),
                [VarDecl(Id("a"),FloatType()),VarDecl(Id("b"),IntType())],
                [],
                [If(BinaryOp(">",Id("a"),IntLiteral(0)),[CallStmt(Id("putIntLn"),[IntLiteral(4)])],[CallStmt(Id("putIntLn"),[IntLiteral(4)])])],
                IntType()
                )]))
        self.assertTrue(TestAST.test(input,expect,315))

    def test_simple_function16(self):
        """More complex program"""
        input = """function foo (a:real; b:integer):INTEGER;
        begin
            if a > 0 then begin
                while a > 0 do begin
                    putIntLn(4);
                    putIntLn(4);
                end
            end
        end"""
        expect = str(Program([
            FuncDecl(
                Id("foo"),
                [VarDecl(Id("a"),FloatType()),VarDecl(Id("b"),IntType())],
                [],
                [If(BinaryOp(">",Id("a"),IntLiteral(0)),
                    [While(
                    BinaryOp(">",Id("a"),IntLiteral("0")),
                    [CallStmt(Id("putIntLn"),[IntLiteral(4)]),CallStmt(Id("putIntLn"),[IntLiteral(4)])])])],
                IntType()
                )]))
        self.assertTrue(TestAST.test(input,expect,316))

    def test_simple_function17(self):
        """More complex program"""
        input = """function foo (a:real; b:integer):INTEGER;
        begin
            a:=b:=c:=1;
        end"""
        expect = str(Program([
            FuncDecl(
                Id("foo"),
                [VarDecl(Id("a"),FloatType()),VarDecl(Id("b"),IntType())],
                [],
                [Assign(Id("c"),IntLiteral(1)),
                Assign(Id("b"),Id("c")),
                Assign(Id("a"),Id("b"))],
                IntType()
                )]))
        self.assertTrue(TestAST.test(input,expect,317))

    def test_simple_function18(self):
        """More complex program"""
        input = """function foo (a:real; b:integer):INTEGER;
        begin
            for a:= 0 downto 10 do putIntLn(4);
        end"""
        expect = str(Program([
            FuncDecl(
                Id("foo"),
                [VarDecl(Id("a"),FloatType()),VarDecl(Id("b"),IntType())],
                [],[For(Id("a"),IntLiteral(0),IntLiteral(10),"False",[CallStmt(Id("putIntLn"),[IntLiteral(4)])])],
                IntType()
                )]))
        self.assertTrue(TestAST.test(input,expect,318))

    def test_simple_function19(self):
        """More complex program"""
        input = """function foo (a:real; b:integer):INTEGER;
        begin
            for a:= 0 downto 10 do begin 
            putIntLn(4);
            end
        end"""
        expect = str(Program([
            FuncDecl(
                Id("foo"),
                [VarDecl(Id("a"),FloatType()),VarDecl(Id("b"),IntType())],
                [],[For(Id("a"),IntLiteral(0),IntLiteral(10),"False",[CallStmt(Id("putIntLn"),[IntLiteral(4)])])],
                IntType()
                )]))
        self.assertTrue(TestAST.test(input,expect,319))

    def test_simple_function20(self):
        """More complex program"""
        input = """function foo (a:real; b:integer):INTEGER;
        begin
            b := True;
            c := False;
        end"""
        expect = str(Program([
            FuncDecl(
                Id("foo"),
                [VarDecl(Id("a"),FloatType()),VarDecl(Id("b"),IntType())],
                [],[Assign(Id("b"),BooleanLiteral(True)),Assign(Id("c"),BooleanLiteral(False))],
                IntType()
                )]))
        self.assertTrue(TestAST.test(input,expect,320))

    def test_simple_function21(self):
        """More complex program"""
        input = """function foo (a:real; b:integer): Integer;
        begin
            b := true;
            c := false;
            a := 2.0;
            d := 2e10;
            g := 1.;
            h := .1;
            a := 1.2E-2;
            a := .2E-2;
            a := 123e1;  
        end"""
        expect = str(Program([
            FuncDecl(
                Id("foo"),
                [VarDecl(Id("a"),FloatType()),VarDecl(Id("b"),IntType())],
                [],[Assign(Id("b"),BooleanLiteral(True)),Assign(Id("c"),BooleanLiteral(False)),
                    Assign(Id("a"),FloatLiteral(2.0)),Assign(Id("d"),FloatLiteral(2e10)),
                    Assign(Id("g"),FloatLiteral(1.)),Assign(Id("h"),FloatLiteral(.1)),
                    Assign(Id("a"),FloatLiteral(1.2E-2)),Assign(Id("a"),FloatLiteral(.2E-2)),
                    Assign(Id("a"),FloatLiteral(123e1))
                    ],
                IntType()
                )]))
        self.assertTrue(TestAST.test(input,expect,321))
    def test_simple_function22(self):
        """More complex program"""
        input = """procedure main (); begin
            getIntLn();
        end
        function foo ():INTEGER; begin
            putIntLn(4);
        end"""
        expect = str(Program([
                FuncDecl(Id("main"),[],[],[CallStmt(Id("getIntLn"),[])],VoidType()),
                FuncDecl(Id("foo"),[],[],[CallStmt(Id("putIntLn"),[IntLiteral(4)])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,322))
    
    def test_simple_function23(self):
        """More complex program"""
        input = """procedure proc();
        begin
            if a > 3 then
            begin
                if a < 7 then 
                    b := b + 2;
                else 
                    b := 123;
            end
        end"""
        expect = str(Program([
                FuncDecl(Id("proc"),[],[],
                    [If(BinaryOp(">",Id("a"),IntLiteral(3)),
                        [If(BinaryOp("<",Id("a"),IntLiteral(7)),
                            [Assign(Id("b"),BinaryOp("+",Id("b"),IntLiteral(2)))],
                            [Assign(Id("b"),IntLiteral(123))])],[])],
                    VoidType())]))
        
        self.assertTrue(TestAST.test(input,expect,323))

    def test_simple_function24(self):
        """More complex program"""
        input = """procedure main (); begin
                with a,b:integer; Do 
                    putIntLn(4);
        end"""
        expect = str(Program([
                FuncDecl(Id("main"),[],[],
                    [With(
                        [VarDecl(Id("a"),IntType()),
                            VarDecl(Id("b"),IntType())],
                        [CallStmt(Id("putIntLn"),[IntLiteral(4)])])
                    ],
                    VoidType())]))
        self.assertTrue(TestAST.test(input,expect,324))

    def test_simple_function25(self):
        """More complex program"""
        input = """procedure main (); begin
            
        end"""
        expect = str(Program([
                FuncDecl(Id("main"),[],[],[],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,325))
    
    def test_simple_function26(self):
        """More complex program"""
        input = """procedure proc();
        begin
            a:= a and not c;
        end"""
        expect = str(Program([
                FuncDecl(Id("proc"),[],[],
                    [Assign(Id("a"),
                        BinaryOp("and",
                            Id("a"),
                                UnaryOp("not",Id("c"))))
                    ],
                    VoidType())]))
        
        self.assertTrue(TestAST.test(input,expect,326))

    def test_simple_function27(self):
        """More complex program"""
        input = """procedure proc();
        begin
            a:= a and b and not c and d;
        end"""
        expect = str(Program([
                FuncDecl(Id("proc"),[],[],
                    [Assign(Id("a"),
                        BinaryOp("and",
                            BinaryOp("and",
                                BinaryOp("and",Id("a"),Id("b")),
                                    UnaryOp("not",Id("c"))),
                        Id("d"))
                        )
                    ],
                    VoidType())]))
        
        self.assertTrue(TestAST.test(input,expect,327))

    def test_simple_function28(self):
        """More complex program"""
        input = """procedure proc();
        begin
            a:= foo(a,b,a+b)[1];
        end"""
        expect = str(Program(
            [FuncDecl(
                Id("proc"),[],[],
                [Assign(Id("a"),
                    ArrayCell(
                        CallExpr(Id("foo"),
                            [Id("a"),Id("b"),BinaryOp("+",Id("a"),Id("b"))]),IntLiteral(1)))],
                VoidType())]))
        
        self.assertTrue(TestAST.test(input,expect,328))

    def test_simple_function29(self):
        """More complex program"""
        input = """procedure proc();
        begin
            a:= a > b + c;
        end"""
        expect = str(Program(
            [FuncDecl(
                Id("proc"),[],[],
                [Assign(Id("a"),BinaryOp(">",Id("a"),
                    BinaryOp("+",Id("b"),Id("c"))))],
                VoidType())]))
        
        self.assertTrue(TestAST.test(input,expect,329))

    def test_simple_function30(self):
        """More complex program"""
        input = """procedure proc();
        begin
            a:= a + b > c;
        end"""
        expect = str(Program(
            [FuncDecl(
                Id("proc"),[],[],
                [Assign(Id("a"),BinaryOp(">",
                    BinaryOp("+",Id("a"),Id("b")),Id("c")))],
                VoidType())]))
        
        self.assertTrue(TestAST.test(input,expect,330))

    def test_simple_function31(self):
        """More complex program"""
        input = """var a:array[-1 .. -2] of integer;
                        a,b,c:integer;"""
        expect = str(Program([
            VarDecl(Id("a"),
                ArrayType(
                    "-1",
                    "-2",
                    IntType())),
            VarDecl(Id("a"),IntType()),
            VarDecl(Id("b"),IntType()),
            VarDecl(Id("c"),IntType())
            ]))
        
        self.assertTrue(TestAST.test(input,expect,331))

    def test_simple_function32(self):
        """More complex program"""
        input = """function foo(a:string): string;
        var b: string;
        begin
            putIntLn(-4);
        end
        """
        expect = str(Program(
            [FuncDecl(Id("foo"),
                [VarDecl(Id("a"),StringType())],
                [VarDecl(Id("b"),StringType())],
                [CallStmt(Id("putIntLn"),
                    [UnaryOp("-",IntLiteral(4))])],
                StringType())]))
        self.assertTrue(TestAST.test(input,expect,332))

    def test_simple_function33(self):
        """More complex program"""
        input = """function foo(a:string): string;
        var b: string;
        begin
            if (a > 4) and then (b < 4) then
            putIntLn(4);
        end
        """
        expect = str(Program(
            [FuncDecl(Id("foo"),
                [VarDecl(Id("a"),StringType())],
                [VarDecl(Id("b"),StringType())],
                [If(BinaryOp("andthen",
                        BinaryOp(">",Id("a"),IntLiteral(4)),
                        BinaryOp("<",Id("b"),IntLiteral(4))),
                    [CallStmt(Id("putIntLn"),[IntLiteral(4)])]
                )],
                StringType())]))
        self.assertTrue(TestAST.test(input,expect,333))

    def test_simple_function34(self):
        """More complex program"""
        input = """function foo(a:string): string;
        var b: string;
        begin
            if (a > 4) and (b < 4) then
            putIntLn(4);
        end
        """
        expect = str(Program(
            [FuncDecl(Id("foo"),
                [VarDecl(Id("a"),StringType())],
                [VarDecl(Id("b"),StringType())],
                [If(BinaryOp("and",
                        BinaryOp(">",Id("a"),IntLiteral(4)),
                        BinaryOp("<",Id("b"),IntLiteral(4))),
                    [CallStmt(Id("putIntLn"),[IntLiteral(4)])]
                )],
                StringType())]))
        self.assertTrue(TestAST.test(input,expect,334))

    def test_simple_function35(self):
        """More complex program"""
        input = """function foo(a:string): string;
        var b: string;
        begin
        end
        var a,b:boolean;
        procedure main();
        begin end
        """
        expect = str(Program(
            [FuncDecl(Id("foo"),
                [VarDecl(Id("a"),StringType())],
                [VarDecl(Id("b"),StringType())],
                [],
                StringType()),
            VarDecl(Id("a"),BoolType()),
            VarDecl(Id("b"),BoolType()),
            FuncDecl(Id("main"),[],[],[],VoidType())
            ]))
        self.assertTrue(TestAST.test(input,expect,335))

    def test_simple_function36(self):
        """More complex program"""
        input = """procedure main ();
        begin
            if 2 mod 3 then begin
            end
        end
        """
        expect = str(Program(
            [FuncDecl(Id("main"),
                [],
                [],
                [If(BinaryOp("mod",
                    IntLiteral(2),
                    IntLiteral(3)),[],[])],
                VoidType())
            ]))
        self.assertTrue(TestAST.test(input,expect,336))

    def test_simple_function37(self):
        """More complex program"""
        input = """Procedure main();
        begin
            a:=b:=c:= abc()+dfc();
        end
        """
        expect = str(Program(
            [FuncDecl(Id("main"),
                [],
                [],
                [Assign(Id("c"),
                    BinaryOp("+",
                        CallExpr(Id("abc"),[]),
                        CallExpr(Id("dfc"),[]))),
                Assign(Id("b"),Id("c")),
                Assign(Id("a"),Id("b"))],
                VoidType())
            ]))
        self.assertTrue(TestAST.test(input,expect,337))

    def test_simple_function38(self):
        """More complex program"""
        input = """Procedure main();
        begin
            a:=b:=c:= abc(a,b+(d+1) + 2,c)+dfc(a,c,d);
        end
        """
        expect = str(Program(
            [FuncDecl(Id("main"),
                [],
                [],
                [Assign(Id("c"),
                    BinaryOp("+",
                        CallExpr(Id("abc"),
                            [Id("a"),
                            BinaryOp("+",
                                BinaryOp("+",Id("b"),
                                    BinaryOp("+",Id("d"),IntLiteral(1))),
                                IntLiteral(2)),
                            Id("c")]),
                        CallExpr(Id("dfc"),
                            [Id("a"),Id("c"),Id("d")]))),
                Assign(Id("b"),Id("c")),
                Assign(Id("a"),Id("b"))],
                VoidType())
            ]))
        self.assertTrue(TestAST.test(input,expect,338))

    def test_simple_function39(self):
        """More complex program"""
        input = """Procedure main();
        begin
            b:= (a < a) > d;
            a:= n And 10 and b and 5;
        end"""
        expect = str(Program(
            [FuncDecl(Id("main"),
                [],
                [],
                [Assign(Id("b"),
                    BinaryOp(">",
                        BinaryOp("<",Id("a"),Id("a")),Id("d"))),
                Assign(Id("a"),
                    BinaryOp("and",
                        BinaryOp("and",
                            BinaryOp("And",Id("n"),IntLiteral(10)),
                            Id("b")),
                        IntLiteral(5)))],
                VoidType())
            ]))
        self.assertTrue(TestAST.test(input,expect,339))

    def test_simple_function40(self):
        """More complex program"""
        input = """Procedure main();
        var a,b:integer;
            a:real;
            b:string;
            c:boolean;
        begin
        end"""
        expect = str(Program(
            [FuncDecl(Id("main"),
                [],
                [VarDecl(Id("a"),IntType()),
                VarDecl(Id("b"),IntType()),
                VarDecl(Id("a"),FloatType()),
                VarDecl(Id("b"),StringType()),
                VarDecl(Id("c"),BoolType())],
                [],
                VoidType())
            ]))
        self.assertTrue(TestAST.test(input,expect,340))

    def test_simple_function41(self):
        """More complex program"""
        input = """Procedure main();
        var a,b:array [-1 .. -2] of Integer;
        begin
        end"""
        expect = str(Program(
            [FuncDecl(Id("main"),
                [],
                [VarDecl(Id("a"),
                    ArrayType(
                        "-1",
                        "-2",
                        IntType())),
                VarDecl(Id("b"),
                    ArrayType(
                        "-1",
                        "-2",
                        IntType()))],
                [],
                VoidType())
            ]))
        self.assertTrue(TestAST.test(input,expect,341))

    def test_simple_function42(self):
        """More complex program"""
        input = """Procedure main();
        begin
            a:= a[b[1]] + foo();
        end"""
        expect = str(Program(
            [FuncDecl(Id("main"),
                [],
                [],
                [Assign(Id("a"),
                    BinaryOp("+",
                        ArrayCell(Id("a"),
                            ArrayCell(Id("b"),IntLiteral(1))),
                        CallExpr(Id("foo"),[])))],
                VoidType())
            ]))
        self.assertTrue(TestAST.test(input,expect,342))

    def test_simple_function43(self):
        """More complex program"""
        input = """Procedure main();
        begin
            a:=b:=c:= (abc()+dfc())[1];
            if a>b then
             a:=5;
        end"""
        expect = str(Program(
            [FuncDecl(Id("main"),
                [],
                [],
                [Assign(Id("c"),
                    ArrayCell(
                        BinaryOp("+",
                            CallExpr(Id("abc"),[]),
                            CallExpr(Id("dfc"),[])),
                        IntLiteral(1))),
                Assign(Id("b"),Id("c")),
                Assign(Id("a"),Id("b")),
                If(
                    BinaryOp(">",Id("a"),Id("b")),
                    [Assign(Id("a"),IntLiteral(5))],
                    [])],
                VoidType())
            ]))
        self.assertTrue(TestAST.test(input,expect,343))

    def test_simple_function44(self):
        """More complex program"""
        input = """Procedure main();
        begin
            if a>b then
                if a>5 then
                    a:=b;
                else
                    if a>3 then
                        a:=3;
                    else
                        a:=3;
            else
            begin end
        end"""
        expect = str(Program(
            [FuncDecl(Id("main"),
                [],
                [],
                [If(
                    BinaryOp(">",Id("a"),Id("b")),
                    [If(
                        BinaryOp(">",Id("a"),IntLiteral(5)),
                        [Assign(Id("a"),Id("b"))],
                        [If(
                            BinaryOp(">",Id("a"),IntLiteral(3)),
                            [Assign(Id("a"),IntLiteral(3))],
                            [Assign(Id("a"),IntLiteral(3))])
                        ])],
                    [])
                ],
                VoidType())
            ]))
        self.assertTrue(TestAST.test(input,expect,344))

    def test_simple_function45(self):
        """More complex program"""
        input = """Procedure main();
        begin
            n:= 5>=a;
            m:= 6<=5;
            q:= 5<>2;
        end"""
        expect = str(Program(
            [FuncDecl(Id("main"),
                [],
                [],
                [Assign(Id("n"),
                    BinaryOp(">=",IntLiteral(5),Id("a"))),
                Assign(Id("m"),
                    BinaryOp("<=",IntLiteral(6),IntLiteral(5))),
                Assign(Id("q"),
                    BinaryOp("<>",IntLiteral(5),IntLiteral(2)))],
                VoidType())
            ]))
        self.assertTrue(TestAST.test(input,expect,345))

    def test_simple_function46(self):
        """More complex program"""
        input = """Procedure main();
        begin
            n:= not (not a);
            n:= not not a;
            m:= - (-c);
            m:= --c;
        end"""
        expect = str(Program(
            [FuncDecl(Id("main"),
                [],
                [],
                [Assign(Id("n"),
                    UnaryOp("not",
                        UnaryOp("not",Id("a")))),
                Assign(Id("n"),
                    UnaryOp("not",
                        UnaryOp("not",Id("a")))),
                Assign(Id("m"),
                    UnaryOp("-",
                        UnaryOp("-",Id("c")))),
                Assign(Id("m"),
                    UnaryOp("-",
                        UnaryOp("-",Id("c"))))],
                VoidType())
            ]))
        self.assertTrue(TestAST.test(input,expect,346))

    def test_simple_function47(self):
        """More complex program"""
        input = """function test() : Integer;
        begin
            n:= function1(function2(),aff[25],c+a);
            return n;
        end"""
        expect = str(Program(
            [FuncDecl(Id("test"),
                [],
                [],
                [Assign(Id("n"),
                    CallExpr(Id("function1"),
                        [CallExpr(Id("function2"),[]),
                        ArrayCell(Id("aff"),IntLiteral(25)),
                        BinaryOp("+",Id("c"),Id("a"))])),
                Return(Id("n"))],
                IntType())
            ]))
        self.assertTrue(TestAST.test(input,expect,347))

    def test_simple_function48(self):
        """More complex program"""
        input = """procedure main(m:integer);
        var y : array[1 .. 10] of string;
        begin
            putIntLn(sum(m,b,k));   
        end"""
        expect = str(Program(
            [FuncDecl(Id("main"),
                [VarDecl(Id("m"),IntType())],
                [VarDecl(Id("y"),
                    ArrayType("1","10",StringType()))],
                [CallStmt(Id("putIntLn"),
                    [CallExpr(Id("sum"),
                        [Id("m"),Id("b"),Id("k")])])],
                VoidType())
            ]))
        self.assertTrue(TestAST.test(input,expect,348))

    def test_simple_function49(self):
        """More complex program"""
        input = """procedure main(m:integer);
        begin
            foo()[4] := 5 +as/2;
        end"""
        expect = str(Program(
                [FuncDecl(Id("main"),
                    [VarDecl(Id("m"),IntType())],
                    [],
                    [Assign(
                        ArrayCell(
                            CallExpr(Id("foo"),[]),IntLiteral(4)),
                        BinaryOp("+",IntLiteral(5),
                            BinaryOp("/",Id("as"),IntLiteral(2))))],
                    VoidType())
                ]))
        self.assertTrue(TestAST.test(input,expect,349))

    def test_simple_function50(self):
        """More complex program"""
        input = """procedure main(m:integer);
        begin
            if a>b then
            begin
                if a>3 then
                    a:=3;
                else
                begin
                    a:=3;
                    with a,b:integer; do begin
                        if a < b then
                            while a < 4 do 
                            begin
                                if 3 < a then 
                                    a:=5;
                                else
                                    a:=6;
                            end
                    end
                end
            end
            else
                b:=a;
        end"""
        expect = str(Program(
            [FuncDecl(Id("main"),
                [VarDecl(Id("m"),IntType())],
                [],
                [If(
                    BinaryOp(">",Id("a"),Id("b")),
                    [If(
                        BinaryOp(">",Id("a"),IntLiteral(3)),
                        [Assign(Id("a"),IntLiteral(3))],
                        [Assign(Id("a"),IntLiteral(3)),
                        With(
                            [VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType())],
                            [If(BinaryOp("<",Id("a"),Id("b")),
                                [While(
                                    BinaryOp("<",Id("a"),IntLiteral(4)),
                                    [If(
                                        BinaryOp("<",IntLiteral(3),Id("a")),
                                        [Assign(Id("a"),IntLiteral(5))],
                                        [Assign(Id("a"),IntLiteral(6))])
                                    ])],
                                [])
                            ])
                        ])
                    ],
                    [Assign(Id("b"),Id("a"))])
                ],
                VoidType())
            ]))
        self.assertTrue(TestAST.test(input,expect,350))

    def test_simple_function51(self):
        """More complex program"""
        input = """function giaithua(n:integer):integer;
        var gt:integer;
        begin
            gt:=1;
            for i:=1 downto n do
            begin
                gt:= gt*i;
            end
            return gt;
        end
        Procedure main();
        begin
            putIntLn(giaithua(5));
        end"""
        expect = str(Program(
            [FuncDecl(Id("giaithua"),
                [VarDecl(Id("n"),IntType())],
                [VarDecl(Id("gt"),IntType())],
                [Assign(Id("gt"),IntLiteral(1)),
                For(Id("i"),IntLiteral(1),Id("n"),False,
                    [Assign(Id("gt"),
                        BinaryOp("*",Id("gt"),Id("i")))]),
                Return(Id("gt"))],
                IntType()),
            FuncDecl(Id("main"),
                [],
                [],
                [CallStmt(Id("putIntLn"),
                    [CallExpr(Id("giaithua"),[IntLiteral(5)])])
                ],
                VoidType())
            ]))
        self.assertTrue(TestAST.test(input,expect,351))

    def test_simple_function52(self):
        """More complex program"""
        input = """procedure main(m:integer);
        begin
            while a >0 do
            begin end
        end"""
        expect = str(Program(
            [FuncDecl(Id("main"),
                [VarDecl(Id("m"),IntType())],
                [],
                [While(
                    BinaryOp(">",Id("a"),IntLiteral(0)),[])
                ],
                VoidType())
            ]))
        self.assertTrue(TestAST.test(input,expect,352))

    def test_simple_function53(self):
        """More complex program"""
        input = """procedure main(m:integer);
        begin
            with a,b:real; do
            begin end
        end"""
        expect = str(Program(
            [FuncDecl(Id("main"),
                [VarDecl(Id("m"),IntType())],
                [],
                [With(
                    [VarDecl(Id("a"),FloatType()),
                    VarDecl(Id("b"),FloatType())],
                    [])
                ],
                VoidType())
            ]))
        self.assertTrue(TestAST.test(input,expect,353))

    def test_simple_function54(self):
        """More complex program"""
        input = """Procedure main();
        begin
            n:=2;
            while n<10 do
                n:=n*n;
        end"""
        expect = str(Program(
            [FuncDecl(Id("main"),
                [],
                [],
                [Assign(Id("n"),IntLiteral(2)),
                While(
                    BinaryOp("<",Id("n"),IntLiteral(10)),
                    [Assign(Id("n"),
                        BinaryOp("*",Id("n"),Id("n")))
                    ])
                ],
                VoidType())
            ]))
        self.assertTrue(TestAST.test(input,expect,354))

    def test_simple_function55(self):
        """More complex program"""
        input = """Procedure main();
        begin
            n:=2;
            for foo:= 6 To foo < 10 do 
                a := a*b+3+2*5-1;
            while n<10 do
                n:=n*n;
        end"""
        expect = str(Program(
            [FuncDecl(Id("main"),
                [],
                [],
                [Assign(Id("n"),IntLiteral(2)),
                For(Id("foo"),IntLiteral(6),
                    BinaryOp("<",Id("foo"),IntLiteral(10)),
                    True,
                    [Assign(Id("a"),
                        BinaryOp("-",
                            BinaryOp("+",
                                BinaryOp("+",
                                    BinaryOp("*",Id("a"),Id("b")),
                                    IntLiteral(3)),
                                BinaryOp("*",IntLiteral(2),IntLiteral(5))),
                            IntLiteral(1)))
                    ]),
                While(
                    BinaryOp("<",Id("n"),IntLiteral(10)),
                    [Assign(Id("n"),
                        BinaryOp("*",Id("n"),Id("n")))
                    ])
                ],
                VoidType())
            ]))
        self.assertTrue(TestAST.test(input,expect,355))

    def test_simple_function56(self):
        """More complex program"""
        input = """Procedure main();
        begin
            n:=2;
            while ((n<10) and (a>b)) do
                n:=n*n;
        end"""
        expect = str(Program(
            [FuncDecl(Id("main"),
                [],
                [],
                [Assign(Id("n"),IntLiteral(2)),
                While(
                    BinaryOp("and",
                        BinaryOp("<",Id("n"),IntLiteral(10)),
                        BinaryOp(">",Id("a"),Id("b"))),
                    [Assign(Id("n"),
                        BinaryOp("*",Id("n"),Id("n")))
                    ])
                ],
                VoidType())
            ]))
        self.assertTrue(TestAST.test(input,expect,356))

    def test_simple_function57(self):
        """More complex program"""
        input = """Procedure main();
        begin
            n:= not a;
            m:= a+-c;
        end"""
        expect = str(Program(
            [FuncDecl(Id("main"),
                [],
                [],
                [Assign(Id("n"),
                    UnaryOp("not",Id("a"))),
                Assign(Id("m"),
                    BinaryOp("+",Id("a"),
                        UnaryOp("-",Id("c"))))
                ],
                VoidType())
            ]))
        self.assertTrue(TestAST.test(input,expect,357))

    def test_simple_function58(self):
        """More complex program"""
        input = """Procedure main();
        begin
            a:=a+5;
            b:=a-5;
            c:=5/2;
            d:=6*5;
            e:=g mod 5;
            g:=h div 5;
        end"""
        expect = str(Program(
            [FuncDecl(Id("main"),
                [],
                [],
                [Assign(Id("a"),
                    BinaryOp("+",Id("a"),IntLiteral(5))),
                Assign(Id("b"),
                    BinaryOp("-",Id("a"),IntLiteral(5))),
                Assign(Id("c"),
                    BinaryOp("/",IntLiteral(5),IntLiteral(2))),
                Assign(Id("d"),
                    BinaryOp("*",IntLiteral(6),IntLiteral(5))),
                Assign(Id("e"),
                    BinaryOp("mod",Id("g"),IntLiteral(5))),
                Assign(Id("g"),
                    BinaryOp("div",Id("h"),IntLiteral(5)))
                ],
                VoidType())
            ]))
        self.assertTrue(TestAST.test(input,expect,358))

    def test_simple_function59(self):
        """More complex program"""
        input = """Procedure main();
        begin
            n:=1;
            S:=0;
            while n<10 do
            begin
                S:=S+n;
                n:=n+1;
            end
        end"""
        expect = str(Program(
            [FuncDecl(Id("main"),
                [],
                [],
                [Assign(Id("n"),IntLiteral(1)),
                Assign(Id("S"),IntLiteral(0)),
                While(
                    BinaryOp("<",Id("n"),IntLiteral(10)),
                    [Assign(Id("S"),
                        BinaryOp("+",Id("S"),Id("n"))),
                    Assign(Id("n"),
                        BinaryOp("+",Id("n"),IntLiteral(1)))
                    ])
                ],
                VoidType())
            ]))
        self.assertTrue(TestAST.test(input,expect,359))

    def test_simple_function60(self):
        """More complex program"""
        input = """Procedure main();
        begin
            for i:=n downto i do
            begin
                S:=S*i;
                if(S>20) then
                    break;
            end
        end"""
        expect = str(Program(
            [FuncDecl(Id("main"),
                [],
                [],
                [For(Id("i"),Id("n"),Id("i"),False,
                    [Assign(Id("S"),
                        BinaryOp("*",Id("S"),Id("i"))),
                    If(
                        BinaryOp(">",Id("S"),IntLiteral(20)),
                        [Break()],
                        [])
                    ])
                ],
                VoidType())
            ]))
        self.assertTrue(TestAST.test(input,expect,360))

    def test_simple_function61(self):
        """More complex program"""
        input = """function test() : Integer;
        begin
            for a := 0 to  10 do 
                begin
                    n := (fun() + 1 )[3];
                end
        end"""
        expect = str(
            Program(
                [FuncDecl(Id("test"),
                    [],
                    [],
                    [For(Id("a"),IntLiteral(0),IntLiteral(10),True,
                        [Assign(Id("n"),
                            ArrayCell(
                                BinaryOp("+",
                                    CallExpr(Id("fun"),[]),
                                    IntLiteral(1)),
                                IntLiteral(3)))
                        ])
                    ],
                    IntType())
                ]))
        self.assertTrue(TestAST.test(input,expect,361))

    def test_simple_function62(self):
        """More complex program"""
        input = """function test() : Integer;
        begin
            for a := 0 to  10 do 
                begin
                    fun()[4] := -5;
                    { PPL }
                end
        end"""
        expect = str(Program(
            [FuncDecl(Id("test"),
                [],
                [],
                [For(Id("a"),IntLiteral(0),IntLiteral(10),True,
                    [Assign(
                        ArrayCell(
                            CallExpr(Id("fun"),[]),IntLiteral(4)),
                        UnaryOp("-",IntLiteral(5)))
                    ])
                ],
                IntType())
            ]))
        self.assertTrue(TestAST.test(input,expect,362))

    def test_simple_function63(self):
        """More complex program"""
        input = """var a,b,c,d : boolean;
            a,b,c : integer;
        procedure main(); begin
            for f := 0 to 10 do begin
                if f > 5 then
                    k := f*f;
            end
        end"""
        expect = str(Program(
            [VarDecl(Id("a"),BoolType()),
            VarDecl(Id("b"),BoolType()),
            VarDecl(Id("c"),BoolType()),
            VarDecl(Id("d"),BoolType()),
            VarDecl(Id("a"),IntType()),
            VarDecl(Id("b"),IntType()),
            VarDecl(Id("c"),IntType()),
            FuncDecl(Id("main"),
                [],
                [],
                [For(Id("f"),IntLiteral(0),IntLiteral(10),True,
                    [If(
                        BinaryOp(">",Id("f"),IntLiteral(5)),
                        [Assign(Id("k"),
                            BinaryOp("*",Id("f"),Id("f")))
                        ],
                        [])
                    ])
                ],
                VoidType())
            ]))
        self.assertTrue(TestAST.test(input,expect,363))

    def test_simple_function64(self):
        """More complex program"""
        input = """var a,b,c,d : boolean;
        procedure main(); begin
            
        end
        function foo(): integer; begin
        end

        function a(): integer; begin
        end

        var a: integer;"""
        expect = str(Program(
            [VarDecl(Id("a"),BoolType()),
            VarDecl(Id("b"),BoolType()),
            VarDecl(Id("c"),BoolType()),
            VarDecl(Id("d"),BoolType()),
            FuncDecl(Id("main"),
                [],
                [],
                [],
                VoidType()),
            FuncDecl(Id("foo"),
                [],
                [],
                [],
                IntType()),
            FuncDecl(Id("a"),
                [],
                [],
                [],
                IntType()),
            VarDecl(Id("a"),IntType())
            ]))
        self.assertTrue(TestAST.test(input,expect,364))

    def test_simple_function65(self):
        """More complex program"""
        input = """procedure main(); begin
            if ((112> z[3]) and (123 > a[9])) then 
                a[5]:= f;
        end
        function foo(): integer; begin
        end"""
        expect = str(Program(
            [FuncDecl(Id("main"),
                [],
                [],
                [If(
                    BinaryOp("and",
                        BinaryOp(">",IntLiteral(112),
                            ArrayCell(Id("z"),IntLiteral(3))),
                        BinaryOp(">",IntLiteral(123),
                            ArrayCell(Id("a"),IntLiteral(9)))),
                    [Assign(
                        ArrayCell(Id("a"),IntLiteral(5)),Id("f"))],
                    [])
                ],
                VoidType()),
            FuncDecl(Id("foo"),[],[],[],IntType())
            ]))
        self.assertTrue(TestAST.test(input,expect,365))

    def test_simple_function66(self):
        """More complex program"""
        input = """procedure main(m:integer);
        var y : array[1 .. 32] of string;
        begin
            foo("ds","as")[3] := a[3] + -3;        
        end"""
        expect = str(Program(
            [FuncDecl(Id("main"),
                [VarDecl(Id("m"),IntType())],
                [VarDecl(Id("y"),
                    ArrayType(1,32,StringType()))],
                [Assign(
                    ArrayCell(
                        CallExpr(Id("foo"),
                            [StringLiteral("ds"),StringLiteral("as")]),
                        IntLiteral(3)),
                    BinaryOp("+",
                        ArrayCell(Id("a"),IntLiteral(3)),
                        UnaryOp("-",IntLiteral(3))))
                ],
                VoidType())
            ]))
        self.assertTrue(TestAST.test(input,expect,366))

    def test_simple_function67(self):
        """More complex program"""
        input = """procedure main(m:integer);
        var y : array[1 .. 49] of string;
        begin
            if(a>(b*m)) then
                if(a>(b*m)) then
                    begin
                    end
                                                        
            while s = a do
                m:=2;                     
         end"""
        expect = str(Program(
            [FuncDecl(Id("main"),
                [VarDecl(Id("m"),IntType())],
                [VarDecl(Id("y"),
                    ArrayType(1,49,StringType()))],
                [If(
                    BinaryOp(">",Id("a"),
                        BinaryOp("*",Id("b"),Id("m"))),
                    [If(
                        BinaryOp(">",Id("a"),
                            BinaryOp("*",Id("b"),Id("m"))),
                        [],
                        [])
                    ],
                    []),
                While(
                    BinaryOp("=",Id("s"),Id("a")),
                    [Assign(Id("m"),IntLiteral(2))
                    ])
                ],
                VoidType())
            ]))
        self.assertTrue(TestAST.test(input,expect,367))

    def test_simple_function68(self):
        """More complex program"""
        input = """Procedure main();
        begin

        end
        function abc():real;
        var a:integer;
        begin
            a:=5;
            c:=b--5;
        end"""
        expect = str(Program(
            [FuncDecl(Id("main"),[],[],[],VoidType()),
            FuncDecl(Id("abc"),
                [],
                [VarDecl(Id("a"),IntType())],
                [Assign(Id("a"),IntLiteral(5)),
                Assign(Id("c"),
                    BinaryOp("-",Id("b"),
                        UnaryOp("-",IntLiteral(5))))
                ],
                FloatType())
            ]))
        self.assertTrue(TestAST.test(input,expect,368))

    def test_simple_function69(self):
        """More complex program"""
        input = """function abc():real;
        var a:integer;
        begin
            a:=5;
            for a:= 0 to 3 do
                with a,c:integer; do
                    a:= b;
            return put();
            c:=b--5;
        end"""
        expect = str(Program(
            [FuncDecl(Id("abc"),
                [],
                [VarDecl(Id("a"),IntType())],
                [Assign(Id("a"),IntLiteral(5)),
                For(Id("a"),IntLiteral(0),IntLiteral(3),True,
                    [With(
                        [VarDecl(Id("a"),IntType()),
                        VarDecl(Id("c"),IntType())],
                        [Assign(Id("a"),Id("b"))])]),
                Return(CallExpr(Id("put"),[])),
                Assign(Id("c"),
                    BinaryOp("-",Id("b"),
                        UnaryOp("-",IntLiteral(5))))
                ],
                FloatType())
            ]))
        self.assertTrue(TestAST.test(input,expect,369))

    def test_simple_function70(self):
        """More complex program"""
        input = """function abc():real;
        var a:integer;
        begin
            a:=5;
                with a,c:integer; do
                    a:= b;
        end"""
        expect = str(Program(
            [FuncDecl(Id("abc"),
                [],
                [VarDecl(Id("a"),IntType())],
                [Assign(Id("a"),IntLiteral(5)),
                With([VarDecl(Id("a"),IntType()),
                        VarDecl(Id("c"),IntType())],
                        [Assign(Id("a"),Id("b"))])],
                FloatType())
            ]))
        self.assertTrue(TestAST.test(input,expect,370))

    def test_simple_function71(self):
        """More complex program"""
        input = """Procedure main();
        begin
            result:= func1(a,b,c);
        end"""
        expect = str(Program(
            [FuncDecl(Id("main"),[],[],
                [Assign(Id("result"),
                    CallExpr(Id("func1"),[Id("a"),Id("b"),Id("c")]))
                ],
                VoidType())
            ]))
        self.assertTrue(TestAST.test(input,expect,371))

    def test_simple_function72(self):
        """More complex program"""
        input = """
        function a():integer;
        begin
            return a mod b;
        end
        """
        expect = str(Program(
            [FuncDecl(Id("a"),[],[],
                [Return(
                    BinaryOp("mod",Id("a"),Id("b")))
                ],
                IntType())
            ]))
        self.assertTrue(TestAST.test(input,expect,372))    

    def test_simple_function73(self):
        """More complex program"""
        input = """function a():integer;
        begin
            return a - b;
        end
        """
        expect = str(Program(
            [FuncDecl(Id("a"),[],[],
                [Return(
                    BinaryOp("-",Id("a"),Id("b")))
                ],
                IntType())
            ]))
        self.assertTrue(TestAST.test(input,expect,373))  

    def test_simple_function74(self):
        """More complex program"""
        input = """function a():integer;
        begin
            return a div b;
        end
        """
        expect = str(Program(
            [FuncDecl(Id("a"),[],[],
                [Return(
                    BinaryOp("div",Id("a"),Id("b")))
            ],IntType())]))
        self.assertTrue(TestAST.test(input,expect,374))  

    def test_simple_function75(self):
        """More complex program"""
        input = """var i,d:integer;
        Procedure main();
        begin
            For i:=1 to n do
               if n mod i=0 then d := 0;
            if d=2 then kt:=true;
        end"""
        expect = str(Program(
            [VarDecl(Id("i"),IntType()),
            VarDecl(Id("d"),IntType()),
            FuncDecl(Id("main"),[],[],
                [For(Id("i"),IntLiteral(1),Id("n"),True,
                    [If(
                        BinaryOp("=",
                            BinaryOp("mod",Id("n"),Id("i")),IntLiteral(0)),
                        [Assign(Id("d"),IntLiteral(0))],[])]),
                If(
                    BinaryOp("=",Id("d"),IntLiteral(2)),
                    [Assign(Id("kt"),BooleanLiteral(True))],
                    [])
                ],
                VoidType())
            ]))
        self.assertTrue(TestAST.test(input,expect,375))  

    def test_simple_function76(self):
        """More complex program"""
        input = """procedure main();
        var x:real;
            y:integer;
        begin
            putIntLn("f : ");
        end
        """
        expect = str(Program(
            [FuncDecl(Id("main"),[],
                [VarDecl(Id("x"),FloatType()),
                VarDecl(Id("y"),IntType())],
                [CallStmt(Id("putIntLn"),[StringLiteral("f : ")])
                ],
                VoidType())
            ]))
        self.assertTrue(TestAST.test(input,expect,376))  

    def test_simple_function77(self):
        """More complex program"""
        input = """procedure main();
        var x:real;
            y:integer;
        begin
        return "abc";
        end
        """
        expect = str(Program(
            [FuncDecl(Id("main"),[],
                [VarDecl(Id("x"),FloatType()),
                VarDecl(Id("y"),IntType())],
                [Return(StringLiteral("abc"))
                ],
                VoidType())
            ]))
        self.assertTrue(TestAST.test(input,expect,377))  

    def test_simple_function78(self):
        """More complex program"""
        input = """procedure main();
        begin
            j:=i;
            while j mod 5 = 0 do
            begin
                j:=j div 5;
                count:=count+1;
            end
        end"""
        expect = str(Program(
            [FuncDecl(Id("main"),[],[],
                [Assign(Id("j"),Id("i")),
                While(
                    BinaryOp("=",
                        BinaryOp("mod",Id("j"),IntLiteral(5)),IntLiteral(0)),
                    [Assign(Id("j"),
                        BinaryOp("div",Id("j"),IntLiteral(5))),
                    Assign(Id("count"),
                        BinaryOp("+",Id("count"),IntLiteral(1)))
                    ])
                ],
                VoidType())
            ]))
        self.assertTrue(TestAST.test(input,expect,378))  

    def test_simple_function79(self):
        """More complex program"""
        input = """procedure main();
        Begin
            b := a - b;
            If b>c then
                a := a - b;
        End
        """
        expect = str(Program(
            [FuncDecl(Id("main"),[],[],
                [Assign(Id("b"),
                    BinaryOp("-",Id("a"),Id("b"))),
                If(
                    BinaryOp(">",Id("b"),Id("c")),
                    [Assign(Id("a"),
                        BinaryOp("-",Id("a"),Id("b")))
                    ],[])
                ],
                VoidType())
            ]))
        self.assertTrue(TestAST.test(input,expect,379))  

    def test_simple_function80(self):
        """More complex program"""
        input = """procedure main();
        var a : array[-1 .. 1] of string;
        begin
            while ((a<=10) and (b=true)) do
            begin
            end
        end
        """
        expect = str(Program(
            [FuncDecl(Id("main"),[],
                [VarDecl(Id("a"),
                    ArrayType("-1","1",StringType()))],
                [While(
                    BinaryOp("and",
                        BinaryOp("<=",Id("a"),IntLiteral(10)),
                        BinaryOp("=",Id("b"),BooleanLiteral(True))),
                    [])
                ],
                VoidType())
            ]))
        self.assertTrue(TestAST.test(input,expect,380))  

    def test_simple_function81(self):
        """More complex program"""
        input = """procedure main();
        begin
            with a : real; m: array[1 .. 4] of real; do
                While (A=10) Do Sum:=Sum+1;
        end
        """
        expect = str(Program(
            [FuncDecl(Id("main"),[],[],
                [With(
                    [VarDecl(Id("a"),FloatType()),
                    VarDecl(Id("m"),
                        ArrayType(1,4,FloatType()))],
                    [While(
                        BinaryOp("=",Id("A"),IntLiteral(10)),
                        [Assign(Id("Sum"),
                            BinaryOp("+",Id("Sum"),IntLiteral(1)))
                        ])
                    ])
                ],
                VoidType())
            ]))
        self.assertTrue(TestAST.test(input,expect,381))  

    def test_simple_function82(self):
        """More complex program"""
        input = """function main ():string;
        begin
            test := 6 and then 3;
        end
        """
        expect = str(Program(
            [FuncDecl(Id("main"),
                [],
                [],
                [Assign(Id("test"),
                    BinaryOp("andthen",IntLiteral(6),IntLiteral(3)))
                ],
                StringType())
            ]))
        self.assertTrue(TestAST.test(input,expect,382))  

    def test_simple_function83(self):
        """More complex program"""
        input = """procedure main();
        begin 
            if (a>10) then
                while (a<15) do
                    s := s+1;
        end
        """
        expect = str(Program(
            [FuncDecl(Id("main"),
                [],
                [],
                [If(
                    BinaryOp(">",Id("a"),IntLiteral(10)),
                    [While(
                        BinaryOp("<",Id("a"),IntLiteral(15)),
                        [Assign(Id("s"),
                            BinaryOp("+",Id("s"),IntLiteral(1)))
                        ])
                    ],[])
                ],
                VoidType())
            ]))
        self.assertTrue(TestAST.test(input,expect,383))

    def test_simple_function84(self):
        """More complex program"""
        input = """procedure main();
        begin 
            while(a = 10) do
                begin
                    if (a<20) then 
                        a := -func(pass);
                end
        end
        """
        expect = str(Program(
            [FuncDecl(Id("main"),[],
                [],
                [While(
                    BinaryOp("=",Id("a"),IntLiteral(10)),
                    [If(
                        BinaryOp("<",Id("a"),IntLiteral(20)),
                        [Assign(Id("a"),
                            UnaryOp("-",
                                CallExpr(Id("func"),[Id("pass")])))],
                        [])
                    ])
                ],
                VoidType())
            ]))
        self.assertTrue(TestAST.test(input,expect,384))  

    def test_simple_function85(self):
        """More complex program"""
        input = """procedure main();
        begin
            while (a>5) do
                begin
                    s:=s/s[i];
                end
        end 
        """
        expect = str(Program(
            [FuncDecl(Id("main"),[],[],
                [While(
                    BinaryOp(">",Id("a"),IntLiteral(5)),
                    [Assign(Id("s"),
                        BinaryOp("/",Id("s"),
                            ArrayCell(Id("s"),Id("i"))))
                    ])
                ],
                VoidType())
            ]))
        self.assertTrue(TestAST.test(input,expect,385))  

    def test_simple_function86(self):
        """More complex program"""
        input = """procedure main();
        begin
            if(x=true) then a[2]:=-a[3];
        end
        """
        expect = str(Program(
            [FuncDecl(Id("main"),[],
                [],
                [If(
                    BinaryOp("=",Id("x"),BooleanLiteral(True)),
                    [Assign(
                        ArrayCell(Id("a"),IntLiteral(2)),
                        UnaryOp("-",
                            ArrayCell(Id("a"),IntLiteral(3))))
                    ],[])
                ],
                VoidType())
            ]))
        self.assertTrue(TestAST.test(input,expect,386))  

    def test_simple_function87(self):
        """More complex program"""
        input = """procedure main();
        begin
            if(a>3) then 
                if(a<4) then
                    a := a+1;
        end
        """
        expect = str(Program(
            [FuncDecl(Id("main"),[],[],
                [If(
                    BinaryOp(">",Id("a"),IntLiteral(3)),
                    [If(BinaryOp("<",Id("a"),IntLiteral(4)),
                        [Assign(Id("a"),
                            BinaryOp("+",Id("a"),IntLiteral(1)))],
                        [])
                    ],[])
                ],
                VoidType())
            ]))
        self.assertTrue(TestAST.test(input,expect,387))  

    def test_simple_function88(self):
        """More complex program"""
        input = """procedure main();
        begin
            if(a>=3) then a:=3;
        end
        """
        expect = str(Program([FuncDecl(Id("main"),[],[],
            [If(
                BinaryOp(">=",Id("a"),IntLiteral(3)),
                [Assign(Id("a"),IntLiteral(3))],
                [])
            ],
            VoidType())
        ]))
        self.assertTrue(TestAST.test(input,expect,388))  

    def test_simple_function89(self):
        """More complex program"""
        input = """procedure main();
        var i:integer;
        begin
            s:=0;
            for i:=1 to 10 do s:=s8+i;
        end
        """
        expect = str(Program(
            [FuncDecl(Id("main"),[],
                [VarDecl(Id("i"),IntType())],
                [Assign(Id("s"),IntLiteral(0)),
                For(Id("i"),IntLiteral(1),IntLiteral(10),True,
                    [Assign(Id("s"),
                        BinaryOp("+",Id("s8"),Id("i")))
                    ])
                ],
                VoidType())
            ]))
        self.assertTrue(TestAST.test(input,expect,389))  

    def test_simple_function90(self):
        """More complex program"""
        input = """var p:real;
        i:integer;
        function power(x:real;y:integer):real;
        var p:real;
        i:integer;
        begin
        end    
        """
        expect = str(Program(
            [VarDecl(Id("p"),FloatType()),
            VarDecl(Id("i"),IntType()),
            FuncDecl(Id("power"),
                [VarDecl(Id("x"),FloatType()),
                VarDecl(Id("y"),IntType())],
                [VarDecl(Id("p"),FloatType()),
                VarDecl(Id("i"),IntType())],
                [],
                FloatType())
            ]))
        self.assertTrue(TestAST.test(input,expect,390))  

    def test_simple_function91(self):
        """More complex program"""
        input = """procedure main();
        begin
            p:=1;
            for i:=1 to y do p:=p*x;
            power:=p;
        end
        """
        expect = str(Program(
            [FuncDecl(Id("main"),[],[],
                [Assign(Id("p"),IntLiteral(1)),
                For(Id("i"),IntLiteral(1),Id("y"),True,
                    [Assign(Id("p"),
                        BinaryOp("*",Id("p"),Id("x")))]),
                Assign(Id("power"),Id("p"))
                ],
                VoidType())
            ]))
        self.assertTrue(TestAST.test(input,expect,391)) 

    def test_simple_function92(self):
        """More complex program"""
        input = """procedure foo();
        begin end

        """
        expect = str(Program([FuncDecl(Id("foo"),[],[],[],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,392)) 

    def test_simple_function93(self):
        """More complex program"""
        input = """Function r(n:integer):boolean;
        var i,d:integer;
        begin
            For i:=1 to n do
                if d=2 then kt:=true;
        end
        """
        expect = str(Program(
            [FuncDecl(Id("r"),
                [VarDecl(Id("n"),IntType())],
                [VarDecl(Id("i"),IntType()),
                VarDecl(Id("d"),IntType())],
                [For(Id("i"),IntLiteral(1),Id("n"),True,
                    [If(
                        BinaryOp("=",Id("d"),IntLiteral(2)),
                        [Assign(Id("kt"),BooleanLiteral(True))],
                        [])
                    ])
                ],
                BoolType())
            ]))
        self.assertTrue(TestAST.test(input,expect,393))  

    def test_simple_function94(self):
        """More complex program"""
        input = """function s(a,b:integer):integer;
        begin
            return a+b;
        end
        Procedure main();
        begin
            putIntLn(s(1,2));
        end
        """
        expect = str(Program(
            [FuncDecl(Id("s"),
                [VarDecl(Id("a"),IntType()),
                VarDecl(Id("b"),IntType())],
                [],
                [Return(BinaryOp("+",Id("a"),Id("b")))],
                IntType()),
            FuncDecl(Id("main"),[],[],
                [CallStmt(Id("putIntLn"),
                    [CallExpr(Id("s"),[IntLiteral(1),IntLiteral(2)])])
                ],
                VoidType())
            ]))
        self.assertTrue(TestAST.test(input,expect,394))  

    def test_simple_function95(self):
        """More complex program"""
        input = """Procedure main();
        begin
            foo("aa\\n");
        end
        """
        expect = str(Program(
            [FuncDecl(Id("main"),[],[],
                [CallStmt(Id("foo"),[StringLiteral("aa\\n")])
                ],
                VoidType())
            ]))
        self.assertTrue(TestAST.test(input,expect,395))  

    def test_simple_function96(self):
        """More complex program"""
        input = """Procedure main();
        var a,b,c:integer;
        begin
            if(y<5)and(z<10)then
            begin
            end
        end
        """
        expect = str(Program(
            [FuncDecl(Id("main"),[],
                [VarDecl(Id("a"),IntType()),
                VarDecl(Id("b"),IntType()),
                VarDecl(Id("c"),IntType()),],
                [If(
                    BinaryOp("and",
                        BinaryOp("<",Id("y"),IntLiteral(5)),
                        BinaryOp("<",Id("z"),IntLiteral(10))),
                    [],
                    [])
                ],
                VoidType())
            ]))
        self.assertTrue(TestAST.test(input,expect,396)) 

    def test_simple_function97(self):
        """More complex program"""
        input = """Procedure main();
        begin
            with a:integer;b: array [1 .. 2] of real;do
                begin
                    a:=2;
                    b:= func();
                end
        end
        """
        expect = str(Program(
            [FuncDecl(Id("main"),[],[],
                [With([VarDecl(Id("a"),IntType()),
                    VarDecl(Id("b"),ArrayType(1,2,FloatType()))],
                    [Assign(Id("a"),IntLiteral(2)),
                    Assign(Id("b"),
                        CallExpr(Id("func"),[]))
                    ])
                ],
                VoidType())
            ]))
        self.assertTrue(TestAST.test(input,expect,397)) 

    def test_simple_function98(self):
        """More complex program"""
        input = """Procedure main();
        begin
            n:= a(1,2)[b(5)[c(1)]];
        end
        """
        expect = str(Program(
            [FuncDecl(Id("main"),[],[],
                [Assign(Id("n"),
                    ArrayCell(
                        CallExpr(Id("a"),[IntLiteral(1),IntLiteral(2)]),
                        ArrayCell(
                            CallExpr(Id("b"),[IntLiteral(5)]),
                            CallExpr(Id("c"),[IntLiteral(1)]))))
                ],
                VoidType())
            ]))
        self.assertTrue(TestAST.test(input,expect,398)) 

    def test_simple_function99(self):
        """More complex program"""
        input = """Procedure main();
        begin
            a:= c/5/5-3+2--2*123+b;
        end
        """
        expect = str(Program(
            [FuncDecl(Id("main"),[],[],
                [Assign(Id("a"),
                    BinaryOp("+",
                        BinaryOp("-",
                            BinaryOp("+",
                                BinaryOp("-",
                                    BinaryOp("/",
                                        BinaryOp("/",Id("c"),IntLiteral(5)),
                                        IntLiteral(5)),
                                    IntLiteral(3)),
                                IntLiteral(2)),
                            BinaryOp("*",
                                UnaryOp("-",IntLiteral(2)),
                                IntLiteral(123))),
                        Id("b")))
                ],
                VoidType())
            ]))
        self.assertTrue(TestAST.test(input,expect,399)) 

