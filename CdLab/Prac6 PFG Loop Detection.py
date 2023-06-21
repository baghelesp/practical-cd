def find_leaders(statements):
    leaders = set()
    leaders.add(1)
    
    for i, statement in enumerate(statements):
        if "GOTO" in statement:
            target = int(statement.split()[-1])
            leaders.add(target)
            if i + 2 <= len(statements):
                leaders.add(i + 2)
    
    return leaders


def create_basic_blocks(statements, leaders):
    basic_blocks = {}
    current_block = None

    for i, statement in enumerate(statements, start=1):
        if i in leaders:
            current_block = i
            basic_blocks[current_block] = []

        basic_blocks[current_block].append(statement)
    
    return basic_blocks


def program_flow_graph(statements, basic_blocks):
    edges = set()

    for i, statement in enumerate(statements):
        if "GOTO" in statement:
            source = [k for k, v in basic_blocks.items() if statement in v][0]
            target = int(statement.split()[-1])
            edges.add((source, target))

            if i + 2 <= len(statements):
                edges.add((source, i + 2))
        
    return edges


def dominators(basic_blocks, pfg):
    dominators = {}

    for block in basic_blocks:
        if block == 1:
            dominators[block] = set()
        else:
            dominators[block] = set(basic_blocks.keys())

    while True:
        updated_dominators = dominators.copy()
        for block in basic_blocks:
            if block != 1:
                preds = {pred for pred, succ in pfg if succ == block}
                if preds:
                    updated_dominators[block] = {block} | set.intersection(*[dominators[pred] for pred in preds])

        if dominators == updated_dominators:
            break
        else:
            dominators = updated_dominators

    return dominators


def natural_loop(pfg):
    loops = set()

    for source, target in pfg:
        if target < source:
            loops.add((target, source))

    return loops


statements = [
    "count = 0",
    "Result = 0",
    "If count > 20 GOTO 8",
    "count = count + 1",
    "increment = 2 * count",
    "result = result + increment",
    "GOTO 3",
    "end"
]

leaders = find_leaders(statements)
basic_blocks = create_basic_blocks(statements, leaders)
pfg = program_flow_graph(statements, basic_blocks)
dominators_data = dominators(basic_blocks, pfg)
loops = natural_loop(pfg)

print("\nLeader statements:\n", leaders)
print("\nBasic blocks:\n", basic_blocks)
print("\nProgram Flow Graph:\n", pfg)
print("\nDominators of all basic blocks:\n", dominators_data)
print("\nNatural loop:\n", loops)