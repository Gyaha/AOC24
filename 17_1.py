pointer = 0
a = 25358015
b = 0
c = 0
output = []
program = [2,4,1,1,7,5,0,3,4,7,1,6,5,5,3,0]

def get_combo(value):
    if value < 4:
        return value
    elif value < 5:
        return a
    elif value < 6:
        return b
    elif value < 7:
        return c
    print('Invalid combo operand:', value)
    quit()

while pointer < len(program):
    opcode = program[pointer]
    print('opcode:', opcode)
    if opcode == 0:
        """The adv instruction (opcode 0) performs division. 
        The numerator is the value in the A register. 
        The denominator is found by raising 2 to the power of 
        the instruction's combo operand. (So, an operand of 2 
        would divide A by 4 (2^2); an operand of 5 would 
        divide A by 2^B.) The result of the division operation 
        is truncated to an integer and then written to the A register."""
        print('adv')
        operand = get_combo(program[pointer + 1])
        a = a // pow(2,operand)
        pointer += 2
        continue
    elif opcode == 1:
        """The bxl instruction (opcode 1) calculates the bitwise 
        XOR of register B and the instruction's literal operand, 
        then stores the result in register B."""
        print('bxl')
        operand = program[pointer + 1]
        b = b ^ operand
        pointer += 2
        continue
    elif opcode == 2:
        """The bst instruction (opcode 2) calculates the value of 
        its combo operand modulo 8 (thereby keeping only its 
        lowest 3 bits), then writes that value to the B register."""
        print('bst')
        operand = get_combo(program[pointer + 1])
        b = operand % 8
        pointer += 2
        continue
    elif opcode == 3:
        """The jnz instruction (opcode 3) does nothing if the A register is 0. 
        However, if the A register is not zero, it jumps by setting the 
        instruction pointer to the value of its literal operand; if this 
        instruction jumps, the instruction pointer is not increased by 2 
        after this instruction."""
        print('jnz')
        if a == 0:
            pointer += 2
            continue
        operand = program[pointer + 1]
        pointer = operand
        continue
    elif opcode == 4:
        """The bxc instruction (opcode 4) calculates the 
        bitwise XOR of register B and register C, then 
        stores the result in register B. (For legacy 
        reasons, this instruction reads an operand but ignores it.)"""
        print('bxc')
        b = b ^ c
        pointer += 2
        continue
    elif opcode == 5:
        """The out instruction (opcode 5) calculates the value of its 
        combo operand modulo 8, then outputs that value. (If a program 
        outputs multiple values, they are separated by commas.)"""
        print('out')
        operand = get_combo(program[pointer + 1])
        output.append((operand % 8))
        pointer += 2
        continue
    elif opcode == 6:
        """The bdv instruction (opcode 6) works exactly 
        like the adv instruction except that the result 
        is stored in the B register. (The numerator is 
        still read from the A register.)"""
        print('bdv')
        operand = get_combo(program[pointer + 1])
        b = a // pow(2,operand)
        pointer += 2
        continue
    elif opcode == 7:
        """The cdv instruction (opcode 7) works exactly 
        like the adv instruction except that the result 
        is stored in the C register. (The numerator is 
        still read from the A register.)"""
        print('cdv')
        operand = get_combo(program[pointer + 1])
        c = a // pow(2,operand)
        pointer += 2
        continue

    print('Unknown opcode')
    quit()

print('---')
print('A:', a)
print('B:', b)
print('C:', c)
print('Output:', output)

print(','.join([str(x) for x in output]))

# Had to leave the ',' in the output, otherwise the output was not accepted.