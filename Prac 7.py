def optimize_TAC(tac):
    def copy_propagation(tac):
        var_map = {}
        optimized_tac = []

        for line in tac:
            tokens = line.split()

            if len(tokens) == 3 and tokens[1] == "=":
                var_map[tokens[0]] = tokens[2]
            else:
                new_line = " ".join([var_map.get(token, token) for token in tokens])
                optimized_tac.append(new_line)

        return optimized_tac

    def constant_propagation(tac):
        constants = {}
        optimized_tac = []

        for line in tac:
            tokens = line.split()

            if len(tokens) == 3 and tokens[1] == "=" and tokens[2].isdigit():
                constants[tokens[0]] = tokens[2]
            else:
                new_line = " ".join([constants.get(token, token) for token in tokens])
                optimized_tac.append(new_line)

        return optimized_tac

    def constant_folding(tac):
        optimized_tac = []

        for line in tac:
            tokens = line.split()

            if len(tokens) == 5:
                op1, operator, op2 = tokens[2], tokens[3], tokens[4]

                if op1.isdigit() and op2.isdigit():
                    result = eval(f"{op1} {operator} {op2}")
                    new_line = f"{tokens[0]} = {result}"
                else:
                    new_line = line

                optimized_tac.append(new_line)
            else:
                optimized_tac.append(line)

        return optimized_tac

    def common_subexpression_elimination(tac):
        subexpr_map = {}
        optimized_tac = []

        for line in tac:
            tokens = line.split()

            if len(tokens) == 5:
                subexpr = " ".join(tokens[2:])

                if subexpr in subexpr_map:
                    new_line = f"{tokens[0]} = {subexpr_map[subexpr]}"
                else:
                    subexpr_map[subexpr] = tokens[0]
                    new_line = line

                optimized_tac.append(new_line)
            else:
                optimized_tac.append(line)

        return optimized_tac

    optimized_tac = tac
    prev_tac = []

    while prev_tac != optimized_tac:
        prev_tac = optimized_tac
        optimized_tac = constant_propagation(optimized_tac)
        print(optimized_tac)
        optimized_tac = copy_propagation(optimized_tac)
        print(optimized_tac)
        optimized_tac = constant_folding(optimized_tac)
        print(optimized_tac)
        optimized_tac = common_subexpression_elimination(optimized_tac)
        print(optimized_tac)


    return optimized_tac


tac = [
    "a = 2",
    "b = x * x",
    "c = x",
    "d = a + 5",
    "e = b + c",
    "f = c * c",
    "g = d + e",
    "h = e * f"
]

optimized_tac = optimize_TAC(tac)

print("Original TAC:")
print("\n".join(tac))

print("\nOptimized TAC:")
print("\n".join(optimized_tac))