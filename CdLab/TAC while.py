from prettytable import PrettyTable

def while_loop(cleaned_code):
    final_code = []
    while_idx = None
    for i in range(len(cleaned_code)):
        codeline = cleaned_code[i]

        if 'while' in codeline:
            while_idx = i

            start_idx = codeline.index('(')
            end_idx = codeline.index(')')
      
            bool_condn = ''.join(codeline[start_idx:end_idx+1])
            final_code.append('if !{} goto({})'.format(bool_condn,None))
            while_idx = i
        elif '}' in codeline:
            final_code.append('goto({})'.format(while_idx+1))
            final_code[while_idx] = final_code[while_idx].replace('None',str(i+2))
            while_idx = None
        else:
            final_code.append(codeline)
    return final_code


with open('code.txt') as f:
    code = f.readlines()

print('\n-----Statement-----')
print(''.join(code))

cleaned_code = []
for i in range(len(code)):
    if code[i] != '\n':
        if code[i][-1] == '\n':
         
            cleaned_code.append(code[i][:-1].strip())
        else:
            cleaned_code.append(code[i].strip())

final_code = while_loop(cleaned_code)

final_code.append('END')

print('\nThree Address Code-')
x1 = PrettyTable()
x1.field_names = ['Index','Code']
for i in range(len(final_code)):
	x1.add_row([i+1,final_code[i]])

print(x1)