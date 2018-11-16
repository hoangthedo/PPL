import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """a = a + b - c * e;"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[])]))
        self.assertTrue(TestAST.test(input,expect,300))

    
   