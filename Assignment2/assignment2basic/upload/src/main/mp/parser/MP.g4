grammar MP;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

prog: stmt+;

stmt: ID '=' exp ';';
exp: term (ADDOP term)*;
term: term MULOP fact|fact;
fact: ID | INTLIT|FLOATLIT| '(' exp ')';
INTLIT: [0-9]+;
FLOATLIT: [0-9]+'.'[0-9]+;
ADDOP: '+'|'-';
MULOP: '*'|'/';
ID:[a-z]+;

fragment A : [aA];
fragment B : [bB];
fragment C : [cC];
fragment D : [dD];
fragment E : [eE];
fragment F : [fF];
fragment G : [gG];
fragment H : [hH];
fragment I : [iI];
fragment J : [jJ];
fragment K : [kK];
fragment L : [lL];
fragment M : [mM];
fragment N : [nN];
fragment O : [oO];
fragment P : [pP];
fragment Q : [qQ];
fragment R : [rR];
fragment S : [sS];
fragment T : [tT];
fragment U : [uU];
fragment V : [vV];
fragment W : [wW];
fragment X : [xX];
fragment Y : [yY];
fragment Z : [zZ];

ERROR_CHAR: .;
