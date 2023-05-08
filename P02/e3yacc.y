%{
#include<stdio.h>
#include<stdlib.h>
int answer=0;
%}
%token DO OB NUMBER EQUALTO ID RELOP CB WHILE OP CP SEMICOLON NL
%%
  
r : s SEMICOLON NL {printf("\nSequence Accepted\n\n"); exit(0);}
;
  
s : DO OB exp1 CB WHILE OP exp2 RELOP exp2 CP 
;

exp1 :  {printf("C");}
| ID EQUALTO b SEMICOLON 
;

b : b '+' b  	
| b '-' b		
| b '*' b	
| b '/' b		
| OP b CP
| ID 
;
exp2 : ID
| NUMBER
;
  
%%

int yyerror(char *msg)
{
printf("\nInvalid Expression \n");
exit(0);
}

main()
{
printf("\nEnter the expression : \n");
yyparse();
}
int yywrap(){return 1;}