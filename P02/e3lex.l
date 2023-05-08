%{
#include "y.tab.h"
%}
%%
do { return DO;}
\{  {return OB;}
\} {return CB;}
while {return WHILE;}
\( {return OP;}
\) {return CP;}
[=] {return EQUALTO;}
[<=|>=|==|!=|<|>] {return RELOP;}
[0-9]+ { return NUMBER;}
[a-zA-Z] {return ID;}
\; {return SEMICOLON;}
\n {return NL;}
[\t ' '] {};
. { return yytext[0];}

%%