import re


class Switch(object):
    operator_to_fn = {'AND': lambda a, b: (a & b) & 0xFFFF,
                      'OR': lambda a, b: (a | b) & 0xFFFF,
                      'NOT': lambda a: ~a & 0xFFFF,
                      'LSHIFT': lambda a, b: (a << b) & 0xFFFF,
                      'RSHIFT': lambda a, b: (a >> b) & 0xFFFF,
                      'IDENTITY': lambda a: a & 0xFFFF}

    def __init__(self, name, operator, inputs, circuit):
        self.name = name
        self.operator = operator
        self.value = None

        def make_input_fn(i):
            if re.match('[0-9]+', i):
                return lambda: int(i)
            else:
                return lambda: circuit[i].value

        self.inputs = map(make_input_fn, inputs)

    def reset(self):
        self.value = None

    def set_output(self):
        input_values = [i() for i in self.inputs]
        if all([i is not None for i in input_values]):
            self.value = self.operator_to_fn[self.operator](*input_values)


class Circuit(dict):
    def __init__(self, rules_file='input.txt'):
        self.load(rules_file)

    def load(self, rules_file='input.txt'):
        with open(rules_file, 'r') as fh:
            for line in fh:
                instruction, target = line.strip().split(' -> ')
                parts = instruction.split(' ')
                if len(parts) == 1:
                    operator = 'IDENTITY'
                    inputs = parts
                elif len(parts) == 2:
                    operator = parts[0]
                    inputs = [parts[1]]
                elif len(parts) == 3:
                    operator = parts[1]
                    inputs = [parts[0], parts[2]]

                switch = Switch(target, operator, inputs, self)
                self[target] = switch

    def energize(self):
        while not all(s.value is not None for s in self.values()):
            for switch in self.values():
                if switch.value is None:
                    switch.set_output()

    def reset(self):
        for switch in self.values():
            switch.reset()


circuit = Circuit('input.txt')
circuit.energize()
print 'part 1:', circuit['a'].value

tmp = circuit['a'].value
circuit.reset()
circuit['b'].value = tmp
circuit.energize()
print 'part 2:', circuit['a'].value
