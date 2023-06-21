# Sample input code
input_code = "for (i=0; i<10; i++) { a = a*2; }"

def generate_3ac(input_code):
    # List that stores 3AC
    code = []
    # Line numbers for 3AC
    block_counter = 1
    # Used to generate unique names for variables 
    temp_counter = 1

    # Initial assignment
    init_assign = input_code.split("for (")[1].split(";")[0].strip() 
    code.append(f"{block_counter}) {init_assign}")
    block_counter += 1
    # i = 0 gets appended and block_counter gets incremented 

    # Conditional check
    cond_check = input_code.split(";")[1].strip()
    code.append(f"{block_counter}) if {cond_check} goto {block_counter+2}")
    block_counter += 1
    code.append(f"{block_counter}) goto {block_counter+6}")
    block_counter += 1
    # i < 10 gets appended and block counter gets inremented twice

    # Loop body
    loop_body = input_code.split("{")[1].split("}")[0].strip().split(";")
    # a = a + 1
    for statement in loop_body:
        if statement.strip():
            left, right = statement.strip().split("=")
            temp_var = f"t{temp_counter}"
            temp_counter += 1
            code.append(f"{block_counter}) {temp_var} = {right.strip()}")
            block_counter += 1
            code.append(f"{block_counter}) {left.strip()} = {temp_var}")
            block_counter += 1

    # Update iterator
    iterator_update = input_code.split(";")[2].split(")")[0].strip()
    iterator = iterator_update.split("++")[0].strip()
    temp_var = f"t{temp_counter}"
    code.append(f"{block_counter}) {temp_var} = {iterator} + 1")
    block_counter += 1
    code.append(f"{block_counter}) {iterator} = {temp_var}")
    block_counter += 1

    # Jump back to conditional check
    code.append(f"{block_counter}) goto {block_counter-6}")

    # End
    code.append(f"{block_counter+1}) END")

    return code

three_address_code = generate_3ac(input_code)
for line in three_address_code:
    print(line)
