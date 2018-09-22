import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_identifier101(self):
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
    def test_identifier119(self):
        self.assertTrue(TestLexer.test("begin end while","begin,end,while,<EOF>",119))
    def test_identifier120(self):
        self.assertTrue(TestLexer.test("for with 4e3 4e-3","for,with,4e3,4e-3,<EOF>",120))
    def test_identifier121(self):
        self.assertTrue(TestLexer.test("procedure main ();","procedure,main,(,),;,<EOF>",121))
    def test_identifier122(self):
        self.assertTrue(TestLexer.test("function foo(): real;","function,foo,(,),:,real,;,<EOF>",122))
    def test_identifier123(self):
        self.assertTrue(TestLexer.test("var a,b,c: real;","var,a,,,b,,,c,:,real,;,<EOF>",123))
    def test_identifier124(self):
        self.assertTrue(TestLexer.test("if n > 3 then","if,n,>,3,then,<EOF>",124))
    def test_identifier125(self):
        self.assertTrue(TestLexer.test("else a:= -5;","else,a,:=,-,5,;,<EOF>",125))
    def test_identifier126(self):
        self.assertTrue(TestLexer.test("with n <> 3;","with,n,<>,3,;,<EOF>",126))
    def test_identifier127(self):
        self.assertTrue(TestLexer.test("do begin n <= 4.5 ","do,begin,n,<=,4.5,<EOF>",127))
    def test_identifier128(self):
        self.assertTrue(TestLexer.test("FunctiON FOj();","FunctiON,FOj,(,),;,<EOF>",128))
    def test_identifier129(self):
        self.assertTrue(TestLexer.test("1346","1346,<EOF>",129))
    def test_identifier130(self):
        self.assertTrue(TestLexer.test("-51","-,51,<EOF>",130))
    def test_identifier131(self):
        self.assertTrue(TestLexer.test("_abcd","_abcd,<EOF>",131))
    def test_identifier132(self):
        self.assertTrue(TestLexer.test("afc_vasd","afc_vasd,<EOF>",132))
    def test_identifier133(self):
        self.assertTrue(TestLexer.test("141_account123","141,_account123,<EOF>",133))
    def test_identifier134(self):
        self.assertTrue(TestLexer.test("1.","1.,<EOF>",134))
    def test_identifier135(self):
        self.assertTrue(TestLexer.test(".1",".1,<EOF>",135))
    def test_identifier136(self):
        self.assertTrue(TestLexer.test("array[1+2 .. -3] %","array,[,1,+,2,..,-,3,],Error Token %",136))
    def test_identifier137(self):
        self.assertTrue(TestLexer.test("array[1+2 .. 3] ","array,[,1,+,2,..,3,],<EOF>",137))
    def test_identifier138(self):
        self.assertTrue(TestLexer.test("array[1*2 .. 4.]","array,[,1,*,2,..,4.,],<EOF>",138))
    def test_identifier139(self):
        self.assertTrue(TestLexer.test("array[1-2 .. .4]","array,[,1,-,2,..,.4,],<EOF>",139))
    def test_identifier140(self):
        self.assertTrue(TestLexer.test("array[1+2 .. 3] ","array,[,1,+,2,..,3,],<EOF>",140))
    def test_identifier140(self):
        self.assertTrue(TestLexer.test("array[1+2 .. 3] ","array,[,1,+,2,..,3,],<EOF>",140))
    def test_identifier141(self):
        self.assertTrue(TestLexer.test("div mod boolean","div,mod,boolean,<EOF>",141))
    def test_identifier142(self):
        self.assertTrue(TestLexer.test("divmod boolean","divmod,boolean,<EOF>",142))
    def test_identifier143(self):
        self.assertTrue(TestLexer.test("divmodboolean","divmodboolean,<EOF>",143))
    def test_identifier144(self):
        self.assertTrue(TestLexer.test("not with me","not,with,me,<EOF>",144))
    def test_identifier145(self):
        self.assertTrue(TestLexer.test("{,} ","<EOF>",145))
    def test_identifier146(self):
        self.assertTrue(TestLexer.test("0.25E123","0.25E123,<EOF>",146))
    def test_identifier147(self):
        self.assertTrue(TestLexer.test("1.2","1.2,<EOF>",147))
    def test_identifier148(self):
        self.assertTrue(TestLexer.test("1.","1.,<EOF>",148))
    def test_identifier149(self):
        self.assertTrue(TestLexer.test(".1",".1,<EOF>",149))
    def test_identifier150(self):
        self.assertTrue(TestLexer.test("1e2","1e2,<EOF>",150))
    def test_identifier151(self):
        self.assertTrue(TestLexer.test("1.2E-2","1.2E-2,<EOF>",151))
    def test_identifier152(self):
        self.assertTrue(TestLexer.test("1.2e-2","1.2e-2,<EOF>",152))
    def test_identifier153(self):
        self.assertTrue(TestLexer.test(".1E2",".1E2,<EOF>",153))
    def test_identifier154(self):
        self.assertTrue(TestLexer.test("9.0","9.0,<EOF>",154))
    def test_identifier155(self):
        self.assertTrue(TestLexer.test("12e8","12e8,<EOF>",155))
    def test_identifier156(self):
        self.assertTrue(TestLexer.test("0.33E-3","0.33E-3,<EOF>",156))
    def test_identifier157(self):
        self.assertTrue(TestLexer.test("128e-42","128e-42,<EOF>",157))
    def test_identifier158(self):
        self.assertTrue(TestLexer.test("true","true,<EOF>",158))
    def test_identifier159(self):
        self.assertTrue(TestLexer.test("false","false,<EOF>",159))
    def test_identifier160(self):
        self.assertTrue(TestLexer.test("12e8","12e8,<EOF>",160))
    def test_identifier161(self):
        self.assertTrue(TestLexer.test("[","[,<EOF>",161))
    def test_identifier162(self):
        self.assertTrue(TestLexer.test("]","],<EOF>",162))
    def test_identifier163(self):
        self.assertTrue(TestLexer.test("\\","Error Token \\",163))
    def test_identifier164(self):
        self.assertTrue(TestLexer.test("//","<EOF>",164))
    def test_identifier165(self):
        self.assertTrue(TestLexer.test("*","*,<EOF>",165))
    def test_identifier166(self):
        self.assertTrue(TestLexer.test("-","-,<EOF>",166))
    def test_identifier167(self):
        self.assertTrue(TestLexer.test("+","+,<EOF>",167))
    def test_identifier168(self):
        self.assertTrue(TestLexer.test("or","or,<EOF>",168))
    def test_identifier169(self):
        self.assertTrue(TestLexer.test("<>","<>,<EOF>",169))
    def test_identifier170(self):
        self.assertTrue(TestLexer.test(">",">,<EOF>",170))
    def test_identifier171(self):
        self.assertTrue(TestLexer.test("foo(2)[3+x]","foo,(,2,),[,3,+,x,],<EOF>",171))
    def test_identifier172(self):   
        self.assertTrue(TestLexer.test("a[b[2]] +3;","a,[,b,[,2,],],+,3,;,<EOF>",172))
    def test_identifier173(self):
        self.assertTrue(TestLexer.test("y: array","y,:,array,<EOF>",173))
    def test_identifier174(self):
        self.assertTrue(TestLexer.test("if () then return a;","if,(,),then,return,a,;,<EOF>",174))
    def test_identifier175(self):
        self.assertTrue(TestLexer.test("downto","downto,<EOF>",175))
    def test_identifier176(self):
        self.assertTrue(TestLexer.test("void","void,<EOF>",176))
    def test_identifier177(self):
        self.assertTrue(TestLexer.test("int main","int,main,<EOF>",177))
    def test_identifier178(self):
        self.assertTrue(TestLexer.test("123asd","123,asd,<EOF>",178))
    def test_identifier179(self):
        self.assertTrue(TestLexer.test("\"easd","Unclosed String: easd",179))
    def test_identifier180(self):
        self.assertTrue(TestLexer.test("\"PPL","Unclosed String: PPL",180))
    def test_identifier181(self):
        self.assertTrue(TestLexer.test("^","Error Token ^",181))
    def test_identifier182(self):
        self.assertTrue(TestLexer.test("!","Error Token !",182))
    def test_identifier183(self):
        self.assertTrue(TestLexer.test("!@#","Error Token !",183))
    def test_identifier184(self):
        self.assertTrue(TestLexer.test("\"PPL\\e asd","Illegal Escape In String: PPL\\e",184))
    def test_identifier185(self):
        self.assertTrue(TestLexer.test("<asd>","<,asd,>,<EOF>",185))
    def test_identifier186(self):
        self.assertTrue(TestLexer.test("with a:integerr;do","with,a,:,integerr,;,do,<EOF>",186))
    def test_identifier187(self):
        self.assertTrue(TestLexer.test(""""asdasd ""","""Unclosed String: asdasd""",187))
    def test_identifier188(self):
        self.assertTrue(TestLexer.test("\"asdasd\" ""","Unclosed String: asdasd",188))
    def test_identifier189(self):
        self.assertTrue(TestLexer.test("INT","INT,<EOF>",189))
    def test_identifier190(self):
        self.assertTrue(TestLexer.test("MaIn","MaIn,<EOF>",190))
    def test_identifier191(self):
        self.assertTrue(TestLexer.test("Var","Var,<EOF>",191))
    def test_identifier192(self):
        self.assertTrue(TestLexer.test("when while","when,while,<EOF>",192))
    def test_identifier193(self):
        self.assertTrue(TestLexer.test("BOolean","BOolean,<EOF>",193))
    def test_identifier194(self):
        self.assertTrue(TestLexer.test("STRing","STRing,<EOF>",194))
    def test_identifier195(self):
        self.assertTrue(TestLexer.test("String","String,<EOF>",195))
    def test_identifier196(self):
        self.assertTrue(TestLexer.test("1.2;","1.2,;,<EOF>",196))
    def test_identifier197(self):
        self.assertTrue(TestLexer.test("test97","test97,<EOF>",197))
    def test_identifier198(self):
        self.assertTrue(TestLexer.test("98test","98,test,<EOF>",198))
    def test_identifier199(self):
        self.assertTrue(TestLexer.test("9test9","9,test9,<EOF>",199))
    def test_identifier200(self):   
        self.assertTrue(TestLexer.test("fulltest","fulltest,<EOF>",200))