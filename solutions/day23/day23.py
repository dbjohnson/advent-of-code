import re


class Register(object):
    inst_to_func = {'inc': lambda x: x + 1,
                    'hlf': lambda x: x // 2,
                    'tpl': lambda x: x * 3}

    def __init__(self):
        self.value = 0

    def process(self, instruction):
        self.value = self.inst_to_func[instruction](self.value)


class Computer(object):
    def __init__(self):
        self.registers = {'a': Register(),
                          'b': Register()}

    def process_stack(self, filename='input.txt'):
        with open(filename, 'r') as fh:
            stack = [filter(None, re.split('[,\s]', line.strip())) for line in fh]

        position = 0
        while position >= 0 and position < len(stack):
            instruction = stack[position]
            if instruction[0] == 'jie':
                if self.registers[instruction[1]].value % 2 == 0:
                    position += int(instruction[2])
                else:
                    position += 1
            elif instruction[0] == 'jio':
                if self.registers[instruction[1]].value == 1:
                    position += int(instruction[2])
                else:
                    position += 1
            elif instruction[0] == 'jmp':
                position += int(instruction[1])
            else:
                instruction, register = instruction
                self.registers[register].process(instruction)
                position += 1


c = Computer()
c.process_stack('input.txt')
print 'part 1:', c.registers['b'].value

c = Computer()
c.registers['a'].value = 1
c.process_stack('input.txt')
print 'part 2:', c.registers['b'].value
