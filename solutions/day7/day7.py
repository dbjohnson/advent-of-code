import re
from collections import defaultdict

switch_to_state = defaultdict(int)
operator_to_fn = {'AND': lambda a, b: (a & b) & 0xFFFF,
                  'OR': lambda a, b: (a | b) & 0xFFFF,
                  'NOT': lambda a: ~a & 0xFFFF,
                  'LSHIFT': lambda a, b: (a << b) & 0xFFFF,
                  'RSHIFT': lambda a, b: (a >> b) & 0xFFFF}


def load_instructions(rules_file):
    instructions = []
    switch_to_state.clear()
    with open(rules_file, 'r') as fh:
        for line in fh:
            instruction, target = line.strip().split(' -> ')
            if re.match('^[0-9]+$', instruction):
                switch_to_state[target] = int(instruction)
            elif re.match('^[a-z]+$', instruction):
                instructions.append({'function': lambda a: a,
                                     'operands': [instruction],
                                     'target': target})
            else:
                for operator, fn in operator_to_fn.items():
                    if operator in instruction:
                        if instruction.startswith(operator):
                            operands = instruction.split('{} '.format(operator))[-1].split()
                        else:
                            operands = instruction.split(' {} '.format(operator))

                        def cast(x):
                            try:
                                return int(x)
                            except:
                                return x
                        operands = [cast(x) for x in operands]
                        instructions.append({'function': fn,
                                             'operands': operands,
                                             'target': target})
    return instructions


def solve(instructions):
    while instructions:
        for instruction in instructions:
            available_inputs = switch_to_state.keys()
            if all(isinstance(operand, int) or operand in available_inputs
                   for operand in instruction['operands']):
                instructions.remove(instruction)
                operands = []
                for operand in instruction['operands']:
                    if isinstance(operand, str):
                        operands.append(switch_to_state[operand])
                    else:
                        operands.append(operand)
                switch_to_state[instruction['target']] = instruction['function'](*operands)


instructions = load_instructions('day7.txt')
solve(instructions)
print 'part 1: ', switch_to_state['a']

instructions = load_instructions('day7.txt')
switch_to_state['b'] = 956   # for part two
solve(instructions)
print 'part 2: ', switch_to_state['a']
