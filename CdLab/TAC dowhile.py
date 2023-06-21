def doWhileloop(code):
    fc = []
    idx = None
    doIdx = []
    tempIdx = 0
    for i in range(len(code)):
        just = code[i]
        if 'do' in just:
            idx = i
            doIdx.append(i + 1)
        elif 'while' in just:
            idx = i
            newid = just.index('(')
            end_idx = just.index(')')
            bool_condn = ''.join(just[newid:end_idx + 1])
            fc.append('if !{} goto({})'.format(bool_condn, doIdx.pop()))
            idx = i
        elif '}' in just:
            fc.append('goto({})'.format(idx + 1))
            fc[idx] = fc[idx].replace('None', str(i + 2))
            idx = None
        else:
            operands = just.split('=')

            if len(operands) == 2:
                left = operands[0].strip()
                right = operands[1].strip()
                if '+' in right:
                    op = '+'
                elif '-' in right:
                    op = '-'
                elif '*' in right:
                    op = '*'
                elif '/' in right:
                    op = '/'
                else:
                    op = None
                if op:
                    temp = 't{}'.format(tempIdx)
                    tempIdx += 1
                    fc.append('{} = {} {} {}'.format(temp,right.split(op)[0].strip(), op, right.split(op)[1].strip()))
                    fc.append('{} = {}'.format(left, temp))
                else:
                    fc.append(just)
            else:
                fc.append(just)
    return fc

with open('dowhile.txt') as f:
    code = f.readlines()
print('Given do-while-loop code is:')
print(''.join(code))
ans = []
for i in range(len(code)):
    if code[i] != '\n':
        if code[i][-1] == '\n':
            ans.append(code[i][:-1].strip())
        else:
            ans.append(code[i].strip())

fans = doWhileloop(ans)
fans.append('END')

print('Serial No \tThree address code')
for i in range(len(fans)):
    print(i + 1, "\t\t"+fans[i])