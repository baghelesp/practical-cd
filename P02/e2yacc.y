%{
#include<stdio.h>
#include<stdlib.h>
int answer=0;
%}
%token ZERO ONE NL 

%%
  
r : s NL {printf("\nSequence Accepted\n\n");}
;
  
s : ZERO a
;
  
a : n a
| ZERO
| ONE
;
 
n : ZERO
| ONE
;
  
%%

int yyerror(char *msg)
{
printf("\nInvalid Sequence \n");
exit(0);
}

main()
{
printf("\nEnter the expression : \n");
yyparse();
}
int yywrap(){return 1;}