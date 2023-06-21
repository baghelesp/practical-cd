def First(symbol):
  first=set([])
  #if symbol is terminal
  if symbol[0] in Terminals :
    first.add(symbol[0])
    return first
  
  #if symbol is epsilon
  if symbol[0] == "ε":
    first.add(symbol[0])
    return first
  
  if len(symbol)>1:
    for sym in symbol:
      first2=First(sym)
      if 'ε' in first2:
        first=first.union(first2-{'ε'})
      else:
        first=first.union(first2)

  else:
    for production_list in grammer[symbol[0]]:
      if(production_list[0] in Terminals):
        first.add(production_list[0])

      elif(production_list[0]=="ε"):
        first.add(production_list[0])

      elif(production_list[0] in Non_terminals):
          for Letter in production_list:
            first2=First(Letter)
            if("ε" in first2):
              first=first.union((first2-{"ε"} ))
            else:
              first=first.union(first2)
              break
  return first


def Follow(symbol):
  follow=set([])
  
  if(symbol=="S"):
    follow.add("$")

  keys=set([])
  for key,value in grammer.items():
    for string in value:
      for letter in string:
        if symbol == letter:
          keys.add(key)

  for k in keys:
    for production in grammer[k]: 
      for i in range(0,len(production)):
          if production[i]==symbol :       
            j=i                     
            if j!=len(production)-1:     
              for j in range(i,len(production)): 
                first=First(production[j+1:]) 
                if('ε' in  first):
                  follow=follow.union(Follow(k))
                  follow=follow.union((first-{'ε'}))
                else:
                  follow=follow.union(first)
                  break
            elif(i==len(production)-1):
                follow=follow.union(Follow(k))
            elif(symbol==k):
                return
            
  return follow    

def Create_table(): 
  table_dict=dict({})
  for nt in Non_terminals:
    table_dict[nt]=[First(nt),Follow(nt)]
  return table_dict

def LL1Table():
  S={}
  A={}
  B={}
  C={}
  ll={"S":S,"A":A,"B":B,"C":C}

  for k in ll.keys():
    for t in Terminals:
      ll[k][t]=list([])
  table=Create_table()
  for nt in Non_terminals:
    for production in grammer[nt]:
      first=First(production)
      for f in first:
        if f=='ε':
         for follow_temp in table[nt][1]:
          ll[nt][follow_temp].append(f'{nt}->ε')
        elif(f in table[nt][0]):  
          ll[nt][f].append(f'{nt}->{production}')
  for k in ll.keys():
    ll[k]=dict(sorted(ll[k].items()))
    print(f'{k}:=\t',end='')
    for s in ll[k]:
      print(f'{s}: {ll[k][s]}\t',end='')
    print("\n")

Non_terminals=["S","A","B","C"]
Terminals=["a","b","c","p","$"]
grammer={"S":["ABC","C"],"A":["a","bB","ε"],"B":["p","ε"],"C":["c"]}



print("Non-Terminals  \t   First  \t \t   Follow")
table=Create_table()
for k in table.keys():
  print(f'{k}  \t\t   {table[k][0]}  \t\t   {table[k][1]}')

print("LL(1) Parsing Table:\n")
print("Non-terminals")
LL1Table()