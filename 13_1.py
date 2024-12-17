data = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279"""

with open('Input/13.txt', 'r') as file:
    data = file.read()

data_machines = data.strip().split('\n\n')

cost_a = 3
cost_b = 1

class Button:
    def __init__(self, data:str):
        _, xy = data.split(': ')
        x, y = xy.split(', ')
        _, x = x.split('+')
        _, y = y.split('+')
        self.x = int(x)
        self.y = int(y)
        #print(f'Button: x:{self.x}, y:{self.y}')

class Prize:
    def __init__(self, data:str):
        _, xy = data.split(': ')
        x, y = xy.split(', ')
        _, x = x.split('=')
        _, y = y.split('=')
        self.x = int(x)
        self.y = int(y)
        #print(f'Prize: x:{self.x}, y:{self.y}')
        
class Machine:
    def __init__(self, data:str):
        button_a, button_b, prize = data.split('\n')
        self.button_a = Button (button_a)
        self.button_b = Button(button_b)
        self.prize = Prize(prize)

def find_cheapest(machine:Machine):
    a, ax, ay = 0, 0, 0
    while ax < machine.prize.x or ay < machine.prize.y:
        b, bx, by = 0,0,0
        ax = a * machine.button_a.x
        ay = a * machine.button_a.y
        while bx < machine.prize.x or by < machine.prize.y:
            bx = b * machine.button_b.x
            by = b * machine.button_b.y
            if ax + bx == machine.prize.x and ay + by == machine.prize.y:
                return a * cost_a + b * cost_b
            b += 1
        a += 1
    return None

t = 0
for data_machine in data_machines:
    m = Machine(data_machine)
    p = find_cheapest(m)
    if p is not None:
        t += p
print(t)