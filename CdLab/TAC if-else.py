condition = "a < b"
true_block = ["x = a + b", "y = a - b"]
false_block = ["x = a - b", "y = a + b"]
code = []
start=1

print(len(true_block))
code.append(f"if {condition} goto {len(code)+100+2}")
code.append(f"goto {len(true_block)*2+100+3}")

for statement in true_block:
    code.append(f"t{start}  "+statement[1:])
    code.append(statement[0]+f" = t{start}  ")
    start+=1
code.append(f"goto {(len(true_block)+len(true_block))*2+100+3}")

for statement in false_block:
    code.append(f"t{start}  "+statement[1:])
    code.append(statement[0]+f" = t{start}  ")
    start+=1


for i, statement in enumerate(code):
    print(f"{i+100}: {statement}")