%{
#include<stdio.h>
#include<string.h>
int ques_count=0;
int lines=0, words=0,s_letters=0,c_letters=0, num=0, spl_char=0,total=0;
%}
%%
[0-9]+"/"[0-9]+"/"[0-9]+{4,4}  printf("Date found %s",yytext);
I|II|III|IV|V|VI|VII|VIII {printf("\nSemester is: %s",yytext);}
\n { lines++; words++;}
[\t ' '] words++;
[A-Z] c_letters++;
[a-z] s_letters++;
[0-9] num++;
Question|question|Q {ques_count++;}

. ;
%%
int yywrap()
{
return 1;
}


int main(void)
{
    extern FILE* yyin;
    yyin= fopen("e2input.txt","r");
    yylex();
    printf("\nNumber of questions is: %d",ques_count);
    printf("\nThis File contains ...");
    printf("\n\t%d lines", lines+1);
    printf("\n\t%d words",words);
    printf("\n\t%d small letters", s_letters);
    printf("\n\t%d capital letters",c_letters);
    printf("\n\t%d digits", num);
    printf("\n\t%d special characters",spl_char);

}

