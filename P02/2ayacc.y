%{
#include<stdio.h>
#include<stdlib.h>
int answer=0;
%}
%token NUMBER ID NL 
%left '+' '-'
%left '*' '/'

%%
stmt : exp NL { printf("Valid expression & Answer: %d \n",$1); 
	exit(0);} 
|
exp1 NL { printf("Valid Expression \nBut, Calculation Can Be Performed On Variables \n"); 
	exit(0);}
; 

exp : exp '+' exp  	{$$=$1+$3; printf("+");}
| exp '-' exp		{$$=$1-$3; printf("-");}
| exp '*' exp		{$$=$1*$3; printf("*");}
| exp '/' exp		{$$=$1/$3; printf("/");}
| '(' exp ')'		{$$=$2;}
| NUMBER 		{$$=$1; printf("%d", yylval);}

;

exp1 : exp1 '+' exp1  	{$$=$1+$3; printf("+");}
| exp1 '-' exp1			{$$=$1-$3; printf("-");}
| exp1 '*' exp1			{$$=$1*$3; printf("*");}
| exp1 '/' exp1			{$$=$1/$3; printf("/");}
| '(' exp1 ')'			{$$=$2;}
| ID 					{$$=$1; printf("%d", yylval);}
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