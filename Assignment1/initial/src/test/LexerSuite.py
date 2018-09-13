import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_identifier101(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("\"a\\ktbc\"","Illegal Escape In String: a\\k",101))
    def test_identifier102(self):
    	self.assertTrue(TestLexer.test("\"test\\n\"","test\\n,<EOF>",102))
    def test_identifier103(self):
    	self.assertTrue(TestLexer.test("\"character\\n\"","character\\n,<EOF>",103))
    def test_identifier104(self):
    	self.assertTrue(TestLexer.test("\"char\\nart\\ber\"","char\\nart\\ber,<EOF>",104))
    def test_identifier105(self):
    	self.assertTrue(TestLexer.test("\"PPL\\\\PPL\"","PPL\\\\PPL,<EOF>",105))
    def test_identifier106(self):
    	self.assertTrue(TestLexer.test("\"PPL\\bPPL\"","PPL\\bPPL,<EOF>",106))
    def test_identifier107(self):
    	self.assertTrue(TestLexer.test("\"\\nPPL PPL\"","\\nPPL PPL,<EOF>",107))
    def test_identifier108(self):
    	self.assertTrue(TestLexer.test("\"PPL\\\\PPL\"","PPL\\\\PPL,<EOF>",108))
    def test_identifier109(self):
    	self.assertTrue(TestLexer.test("\"PPL\\tPPL\"","PPL\\tPPL,<EOF>",109))
    def test_identifier110(self):
    	self.assertTrue(TestLexer.test("\"PPL\\rPPL\"","PPL\\rPPL,<EOF>",110))
    def test_identifier111(self):
    	self.assertTrue(TestLexer.test("\"PPL\\\'PPL\"","PPL\\\'PPL,<EOF>",111))
    def test_identifier112(self):
    	self.assertTrue(TestLexer.test("\"PPL\\\"PPL\"","PPL\\\"PPL,<EOF>",112))
    def test_identifier113(self):
    	self.assertTrue(TestLexer.test("\"PPLPPL","Unclosed String: PPLPPL",113))
    def test_identifier114(self):
    	self.assertTrue(TestLexer.test("\"when the lexer detects an unterminated string","Unclosed String: when the lexer detects an unterminated string",114))
    def test_identifier115(self):
    	self.assertTrue(TestLexer.test("4e2","4e2,<EOF>",115))
    def test_identifier116(self):
    	self.assertTrue(TestLexer.test("\"sfsa \\b\"","sfsa \\b,<EOF>",116))
    def test_identifier117(self):
    	self.assertTrue(TestLexer.test("[1 .. 2]","[,1,..,2,],<EOF>",117))
    def test_identifier118(self):
    	self.assertTrue(TestLexer.test("a bc","a,bc,<EOF>",118))

   
    