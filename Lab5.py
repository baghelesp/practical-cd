f = open(r"C:\Users\DELL\Desktop\6th sem\Complier Design\Practical 05\code.txt", "rt")

#c=c*3;
# d=t-4;
# do
# {
#     a=a+2;
#     b=b+3;
#     d=d+63;
# }
while(a<99);
lines=f.readlines()
print("Three Address Code:")

addr=100
temp=0
count=1
flag=0

for i in range(len(lines)):
    if('=' in lines[i] and flag==0):
        stat=lines[i].split('=')
        print(f'({addr+temp})T{count}={stat[1][:-2]}')
        temp=1+temp
        print(f'({addr+temp}){stat[0].strip()}=T{count}')
        temp,count=temp+1,count+1
    elif "do" in lines[i]:
        flag=1
        i=i+2
        start=addr+temp
        while("}" not in lines[i]):
            stat=lines[i].split('=')
            print(f'({addr+temp})T{count}={stat[1][:-2]}')
            temp=1+temp
            print(f'({addr+temp}){stat[0].strip()}=T{count}')
            temp,count=temp+1,count+1
            i=i+1
    elif 'while' in lines[i]:
        j=0
        while(lines[i][j]!='('):
            j=j+1
        j=j+1
        str1=""
        while( lines[i][j]!=')'):
            str1+=lines[i][j]
            j=j+1
        print(f'({addr+temp}) if {str1} then goto {start}')
        temp=1+temp
        print(f'({addr+temp}) goto {addr+temp+1}')
        temp=temp+1
        print(f'({addr +temp}) exit')
    
f.close();