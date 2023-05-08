%{
#include<stdio.h>
#include<string.h>
int i = 0;
int idt=0, opt=0, sc=0, kw=0;
%}

%%
int|float|printf|include|stdio.h {printf(" keyword=%s ",yytext); kw++;}
main {printf(" identifier=%s ",yytext); idt++;}
[a-zA-Z][a-zA-Z0-9]* {printf(" Identifier=%s ",yytext); idt++;}
[(|)|{|}|,|;|#|<|>|] {printf(" SpecialCharater=%s ",yytext); sc++;}
[*|+|-|=|/] {printf(" Operater=%s ",yytext); opt++;}

%%
int yywrap(void){}
int main()
{
// The function that starts the analysis
yyin=fopen("e1input.txt","r");
yylex();
printf("\n%d --> Identifier \t\t %d--> Operater \t\t \n%d--> SpecialCharater \t\t %d-->Keyword",idt,opt,sc,kw);
return 0;
}