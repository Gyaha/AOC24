class Computer():
    def __init__(self, a, b, c, program, test_output=False):
        self.reset(a, b, c, program)
        self.test_output = test_output

    def reset(self, a, b, c, program):
        self.a = a
        self.b = b
        self.c = c
        self.output = []
        self.program = program
        self.pointer = 0

    def get_combo(self, value):
        if value < 4:
            return value
        elif value < 5:
            return self.a
        elif value < 6:
            return self.b
        elif value < 7:
            return self.c
        print('Invalid combo operand:', value)
        quit()

    def run(self):
        while self.pointer < len(self.program):
            opcode = self.program[self.pointer]
            #print('opcode:', opcode)
            if opcode == 0:
                """The adv instruction (opcode 0) performs division. 
                The numerator is the value in the A register. 
                The denominator is found by raising 2 to the power of 
                the instruction's combo operand. (So, an operand of 2 
                would divide A by 4 (2^2); an operand of 5 would 
                divide A by 2^B.) The result of the division operation 
                is truncated to an integer and then written to the A register."""
                #print('adv')
                operand = self.get_combo(self.program[self.pointer + 1])
                self.a = self.a // pow(2,operand)
                self.pointer += 2
                continue
            elif opcode == 1:
                """The bxl instruction (opcode 1) calculates the bitwise 
                XOR of register B and the instruction's literal operand, 
                then stores the result in register B."""
                #print('bxl')
                operand = self.program[self.pointer + 1]
                self.b = self.b ^ operand
                self.pointer += 2
                continue
            elif opcode == 2:
                """The bst instruction (opcode 2) calculates the value of 
                its combo operand modulo 8 (thereby keeping only its 
                lowest 3 bits), then writes that value to the B register."""
                #print('bst')
                operand = self.get_combo(self.program[self.pointer + 1])
                self.b = operand % 8
                self.pointer += 2
                continue
            elif opcode == 3:
                """The jnz instruction (opcode 3) does nothing if the A register is 0. 
                However, if the A register is not zero, it jumps by setting the 
                instruction pointer to the value of its literal operand; if this 
                instruction jumps, the instruction pointer is not increased by 2 
                after this instruction."""
                #print('jnz')
                if self.a == 0:
                    self.pointer += 2
                    continue
                operand = self.program[self.pointer + 1]
                self.pointer = operand
                continue
            elif opcode == 4:
                """The bxc instruction (opcode 4) calculates the 
                bitwise XOR of register B and register C, then 
                stores the result in register B. (For legacy 
                reasons, this instruction reads an operand but ignores it.)"""
                #print('bxc')
                self.b = self.b ^ self.c
                self.pointer += 2
                continue
            elif opcode == 5:
                """The out instruction (opcode 5) calculates the value of its 
                combo operand modulo 8, then outputs that value. (If a program 
                outputs multiple values, they are separated by commas.)"""
                #print('out')
                operand = self.get_combo(self.program[self.pointer + 1])
                self.output.append((operand % 8))
                self.pointer += 2
                if self.test_output:
                    if self.output[len(self.output)-1] != self.program[len(self.output)-1]:
                        #print('Output does not match program')
                        #print(self.output)
                        #print(self.program)
                        break
                continue
            elif opcode == 6:
                """The bdv instruction (opcode 6) works exactly 
                like the adv instruction except that the result 
                is stored in the B register. (The numerator is 
                still read from the A register.)"""
                #print('bdv')
                operand = self.get_combo(self.program[self.pointer + 1])
                self.b = self.a // pow(2,operand)
                self.pointer += 2
                continue
            elif opcode == 7:
                """The cdv instruction (opcode 7) works exactly 
                like the adv instruction except that the result 
                is stored in the C register. (The numerator is 
                still read from the A register.)"""
                #print('cdv')
                operand = self.get_combo(self.program[self.pointer + 1])
                self.c = self.a // pow(2,operand)
                self.pointer += 2
                continue

            print('Unknown opcode')
            quit()

# Edge up close to length of program (16)

program = [2,4,1,1,7,5,0,3,4,7,1,6,5,5,3,0]
a = 35184371922204 # This is from previous testing
a = 35184387400000 # This is from previous testing
a = 35184396600000 # This is from previous testing
a = 35184551200000 # This is from previous testing
a = 35185887900000 # This is from previous testing
move_by = 1
computer = Computer(a,0,0,program)
while True:
    computer.reset(a,0,0,program)
    computer.run()
    print(len(computer.output))
    if len(computer.output) < len(program):
        move_by += 1
        a += pow(2, move_by)
        continue
    else:
        a -= pow(2, move_by)
        break
print(a)

# Edge up to length of program (16)
# Currently at (15) from previous function

move_by = 1
move_by_multiplier = 100000
program_length = len(program)
while True:
    computer.reset(a,0,0,program)
    computer.run()
    output_length = len(computer.output)

    if output_length < program_length:
        move_by += 1
        a += move_by * move_by_multiplier
    else: # output_length >= program_length
        a -= move_by * move_by_multiplier
        if move_by == 1:
            break
        move_by = 0
    print(a)
    
computer.reset(a,0,0,program)
computer.run()
print(a, len(computer.output), len(program))

# Now the program is outputting the same length as the program
# This will edge slowly towards the program output. Testing the output in the computer class
computer = Computer(a,0,0,program, True)
while computer.output != program:
    a += 1
    if a % 100000 == 0:
        print(a)
    computer.reset(a,0,0,program)
    computer.run()
print(a)