import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    pass
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """var a,b,c: array[1 .. 2] of integer;
                        a,b,c:integer;"""
        expect = str(Program([
            VarDecl(Id("a"),ArrayType(IntLiteral(1),IntLiteral(2),IntType())),
            VarDecl(Id("b"),ArrayType(IntLiteral(1),IntLiteral(2),IntType())),
            VarDecl(Id("c"),ArrayType(IntLiteral(1),IntLiteral(2),IntType())),
            VarDecl(Id("a"),IntType()),
            VarDecl(Id("b"),IntType()),
            VarDecl(Id("c"),IntType())
            ]))
        self.assertTrue(TestAST.test(input,expect,300))

    '''def test_simple_function(self):
        """More complex program"""
        input = """function foo ():INTEGER; begin
            putIntLn(4);
        end"""
        expect = str(Program([FuncDec(Id("foo"),[],[],[CallStmt(Id("putIntLn"),[IntLiteral(4)])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,301))
    
    def test_call_without_parameter(self):
        """More complex program"""
        input = """procedure main (); begin
            getIntLn();
        end
        function foo ():INTEGER; begin
            putIntLn(4);
        end"""
        expect = str(Program([
                FuncDec(Id("main"),[],[],[CallStmt(Id("getIntLn"),[])]),
                FuncDec(Id("foo"),[],[],[CallStmt(Id("putIntLn"),[IntLiteral(4)])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,302))'''
   