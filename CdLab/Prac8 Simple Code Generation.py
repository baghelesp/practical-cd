def generate_TAC(assignment):
    var, expression = assignment.split(" = ")
    operand1, operation, operand2 = expression.split(" ")
    tac = f"{var} = {operand1} {operation} {operand2}"
    return tac

def generate_assembly(tac):
    asm = []

    var, expression = tac.split(" = ")
    operand1, operation, operand2 = expression.split(" ")

    asm.append(f"MOV {operand1}, R0")  
    asm.append(f"MOV {operand2}, R1")  

    if operation == "+":
        asm.append("ADD R0, R1")  
    elif operation == "-":
        asm.append("SUB R0, R1")  
    elif operation == "*":
        asm.append("MUL R0, R1")  
    elif operation == "/":
        asm.append("DIV R0, R1")  

    asm.append(f"MOV R0, {var}")  

    return asm

def process_assignment_statements(assignments):
    tac_statements = []
    assembly_statements = []

    for assignment in assignments:
        tac = generate_TAC(assignment)
        tac_statements.append(tac)

        assembly = generate_assembly(tac)
        assembly_statements.extend(assembly)
        assembly_statements.append("")

    return tac_statements, assembly_statements

if __name__ == "__main__":
    assignments = [
        "z = x + y",
        "a = b * c",
        "d = e - f",
        "g = h / i",
    ]

    tac_statements, assembly_statements = process_assignment_statements(assignments)

    print("Three Address Code:")
    for tac in tac_statements:
        print(tac)
    print()

    print("Assembly Code:")
    for assembly in assembly_statements:
        print(assembly)