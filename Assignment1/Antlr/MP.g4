/* Do The Hoang - 1611145 */

grammar MP; 

@lexer::header {
//from lexererr import *
}



options{
    //language=Python3;
}


// Parser

program: manydec EOF;
manydec: onedec*;
onedec: vardec | funcdec | procdec;

vardec: VAR varlist+;
varlist: ID (COMMA ID)* vartypelist SEMI;
vartypelist: COLON vartype;
vartype: vartypebasic | ARRAY paramarr OF vartypebasic ;
paramarr: LSB INTLIT DOUDOT INTLIT RSB;
vartypebasic: INTEGER | STRING | REAL | BOOLEAN;

funcdec: FUNCTION ID LB paramlist? RB COLON returntype SEMI vardec* compoundstmt?;
paramlist: (paramsingle + SEMI)* paramsingle;
paramsingle: ID (COMMA ID)* COLON vartype; 
returntype: vartype;



stmt: (assignstmt | funcstmt | vardec)*;

assignstmt: ID (ASSIOP assignlist)+ SEMI;
assignlist: exp ;
arrayvar: funcall LSB exp RSB | ID LSB exp RSB| LB exp RB LSB exp RSB;

funcstmt: ifstmt | whilestmt | forstmt | breakstmt | continuestmt | returnstmt | compoundstmt | withstmt | funcall;

ifstmt: IF ifexp THEN ifbody (ELSE ifbody)? ;
ifexp: exp;
ifbody: exp | stmt;

whilestmt: WHILE whileexp DO whilebody ;
whileexp: exp;
whilebody: exp | stmt;

forstmt: FOR ID ASSIOP exp (TO | DOWNTO) exp DO forbody ;
forbody: exp|stmt;

breakstmt: BREAK SEMI;

continuestmt: CONTINUE SEMI;

compoundstmt: BEGIN stmt END; 

returnstmt: RETURN returnbody SEMI;
returnbody: exp| funcall;

withstmt: WITH paramlist? DO stmt;

funcall: ID LB calllist? RB (LSB returnbody RSB)?;
calllist: exp (COMMA exp)*;


procdec: procmain | procbasic;
procmain: PROCEDURE MAIN LB RB SEMI compoundstmt;
procbasic: PROCEDURE ID LB paramlist? RB SEMI vardec* compoundstmt?; 




expstmt: exp SEMI;
exp: expr+;
expr: exp1 (EQUOP | NEOP | GTOP | GTEOP | LTOP | LTEOP) exp1| exp1;
exp1: exp1 (ADDOP | SUBOP | OROP) exp2 | exp2;
exp2: exp2 (MULOP | DIVOP | DIVINOP | MODOP | ANDOP) exp3 | exp3;
exp3: (SUBOP | NOTOP) exp3 | exp4;
exp4: exp4 LB exp RB | exp5 ;
exp5: LB exp RB|exp6;
exp6: literals | funcall | ID |  arrayvar | assignstmt ;
literals: INTLIT | BOOLLIT | REALLIT | STRINGLIT;


//expression


fragment Ca: 'a'|'A';
fragment Cb: 'b'|'B';
fragment Cc: 'c'|'C';
fragment Cd: 'd'|'D';
fragment Ce: 'e'|'E';
fragment Cf: 'f'|'F';
fragment Cg: 'g'|'G';
fragment Ch: 'h'|'H';
fragment Ci: 'i'|'I';
fragment Ck: 'k'|'K';
fragment Cl: 'l'|'L';
fragment Cm: 'm'|'M';
fragment Cn: 'n'|'N';
fragment Co: 'o'|'O';
fragment Cp: 'p'|'P';
fragment Cq: 'q'|'Q';
fragment Cr: 'r'|'R';
fragment Cs: 's'|'S';
fragment Ct: 't'|'T';
fragment Cu: 'u'|'U';
fragment Cv: 'v'|'V';
fragment Cw: 'w'|'W';
fragment Cx: 'x'|'X';
fragment Cy: 'y'|'Y';
fragment Cz: 'z'|'Z';

BOOLEAN:  Cb Co Co Cl Ce Ca Cn;

BREAK:  Cb Cr Ce Ca Ck;

CONTINUE: Cc Co Cn Ct Ci Cn Cu Ce;

ELSE: Ce Cl Cs Ce;

FOR: Cf Co Cr;

REAL:  Cr Ce Ca Cl;

IF: Ci Cf;

INTEGER: Ci Cn Ct Ce Cg Ce Cr;

RETURN: Cr Ce Ct Cu Cr Cn;

VOIDTYPE:  Cv Co Ci Cd;

DO: Cd Co;

WHILE: Cw Ch Ci Cl Ce;

MAIN: Cm Ca Ci Cn;

STRING:  Cs Ct Cr Ci Cn Cg;

WITH: Cw Ci Ct Ch;

TO: Ct Co;

DOWNTO: Cd Co Cw Cn Ct Co;

THEN: Ct Ch Ce Cn;

BEGIN: Cb Ce Cg Ci Cn;

END: Ce Cn Cd;

FUNCTION: Cf Cu Cn Cc Ct Ci Co Cn;

PROCEDURE: Cp Cr Co Cc Ce Cd Cu Cr Ce;

VAR: Cv Ca Cr;

ARRAY: Ca Cr Cr Ca Cy;

OF: Co Cf;


ID: [_a-zA-Z][_a-zA-Z0-9]* ;
    

//Comment
TRADBLOCK: '(*' .*? '*)' -> skip;

BLOCK: LP .*? RP -> skip;

LINE: '//' ~[\r\n]*-> skip;

//Operator
ASSIOP: ':=';

ADDOP: '+';

SUBOP: '-';

MULOP: '*';

DIVOP: '/';

DIVINOP: Cd Ci Cv;

MODOP: Cm Co Cd;

EQUOP: '=';

GTOP: '>';

GTEOP: '>=';

LTOP: '<';

LTEOP: '<=';

ANDOP: Ca Cn Cd;

OROP: Co Cr;

NEOP: '<>';

NOTOP: Cn Co Ct;

// Separators

COMMA: ',';

DOUDOT: '..';

COLON: ':';

SEMI: ';';

LSB: '[';

RSB: ']';

LB: '(' ;

RB: ')' ;

LP: '{';

RP: '}';

//Literals

fragment DIGIT: [0-9]+;

INTLIT: [0-9]+;

fragment EXPONENT: (('e')|('E')) ('-')? [0-9]+;

 
REALLIT: DIGIT '.' ~[.] 
        |  '.' DIGIT
        |  '.' DIGIT EXPONENT? 
        | DIGIT ~[.] '.' [0-9]* EXPONENT? 
        | DIGIT EXPONENT ;

BOOLLIT: Ct Cr Cu Ce | Cf Ca Cl Cs Ce;



WS : [ \t\r\n\f]+ -> skip ; // skip Cspaes, tabs, newlines



ERROR_CHAR
    : .
        /*{ 
            raise ErrorToken(self.text) 
        }*/
    ;


STRINGLIT
    :  '"' ( '\\' ~[bfrnt'"\\] | ~[\r\n\\"] )* '"'
       /* {
            s=self.text[1:-1]
            self.text=s
        }*/
    ;


ILLEGAL_ESCAPE
    : '"' ( ~[\r\n\\"] |'\\' [bfrnt'"\\]  )* '"'
        /*{
            i = 1;
            for k in self.text[1:]:
                if (k == '\\' ):
                    if self.text[i + 1] == 'b' or 't' or 'n' or 'f' or 'r' or '\"' or '\'' or '\\\\':
                        break;
                i = i + 1;
            raise IllegalEscape(self.text[1:i+2])
        }  */      
    ;

UNCLOSE_STRING
    :  '"' (~["\r\n])*
        /*{
            raise UncloseString(self.text[1:])
        }*/
    ;