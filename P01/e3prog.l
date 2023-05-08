%{
#include<stdio.h>
#include<string.h>
int count=0;
int jpmorgan=0, infosys=0,wipro=0, accenture=0, informatica=0, male=0,female=0;
int cse=0,ece=0,it=0;
%}
%%
JPMorgan         {jpmorgan++;}
Infosys     {infosys++;}
Wipro       {wipro++;}
Accenture   {accenture++;}
Informatica {informatica++;}
Male         {male++;}
Female       {female++;}
" "[A-Z][a-z]*" "[A-Z][a-z]* {printf("%d]Name of Student is: %s\t",++count,yytext);}
[0-9]+"."?[0-9]*LPA    {printf("Package is: %s\t",yytext);}
[A-Za-z0-9_]*"@rknec.edu"  {printf("Mail is: %s\t",yytext);}
[0-9]+"."[0-9]+  {printf("CGPA is: %s\t",yytext);}
[0-9]+{10,10}  {printf("Mobile Number: %s\n",yytext);}
CSE             {cse++;}
IT              {it++;}
ECE             {ece++;}
. ;
%%
int yywrap()
{
return 1;
}


int main(void)
{
    extern FILE* yyin;
    yyin= fopen("e3input.txt","r");
    yylex();
    printf("Number of students placed in JPMorgan is %d\n",jpmorgan);
    printf("Number of students placed in Infosys is %d\n",infosys);
    printf("Number of students placed in Informatica is %d\n",informatica);
    printf("Number of students placed in Wipro is %d\n",wipro);
    printf("Number of students placed in Accenture is %d\n",accenture);
    printf("Number of male students placed is %d\n",male);
    printf("Number of female students placed is %d\n",female);
    printf("Number of CSE students placed is %d\n",cse);
    printf("Number of ECE students placed is %d\n",ece);
    printf("Number of IT students placed is %d",it);  

}

