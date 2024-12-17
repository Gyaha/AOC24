# This was hard
# Works by jumping back and forth
# If the distance is bigger than the target, it will move back
# If the distance is less than the target, it will move forward
# It will move by half the distance each time
# Then it will try and walk the rest of the way by 1 for a few times

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
prize_offset = 10000000000000

class Button:
    def __init__(self, data:str):
        _, xy = data.split(': ')
        x, y = xy.split(', ')
        _, x = x.split('+')
        _, y = y.split('+')
        self.x = int(x)
        self.y = int(y)
        self.vector = Vector2D(self.x, self.y)
        print(f'Button: x:{self.x}, y:{self.y}')

class Prize:
    def __init__(self, data:str):
        _, xy = data.split(': ')
        x, y = xy.split(', ')
        _, x = x.split('=')
        _, y = y.split('=')
        self.x = int(x) + prize_offset
        self.y = int(y) + prize_offset
        self.vector = Vector2D(self.x, self.y)
        print(f'Prize: x:{self.x}, y:{self.y}')
        
class Machine:
    def __init__(self, data:str):
        button_a, button_b, prize = data.split('\n')
        self.button_a = Button (button_a)
        self.button_b = Button(button_b)
        self.prize = Prize(prize)

class Vector2D:
    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y

    def distance(self, other:'Vector2D'):
        return abs(self.x - other.x) + abs(self.y - other.y)
    
    def magnitude(self):
        return abs(self.x) + abs(self.y)

    def __str__(self):
        return f'x:{self.x}, y:{self.y}'
    
    def __repr__(self):
        return self.__str__()

    def __add__(self, other:'Vector2D'):
        return Vector2D(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other:'Vector2D'):
        return Vector2D(self.x - other.x, self.y - other.y)
    
    def __mul__(self, other:int):
        return Vector2D(self.x * other, self.y * other)
    
    def __eq__(self, other:'Vector2D'):
        return self.x == other.x and self.y == other.y
  


def find_cheapest(machine:Machine):
    # region: Swap axis if needed
    a_x = machine.button_a.x
    a_y = machine.button_a.y

    b_x = machine.button_b.x
    b_y = machine.button_b.y

    p_x = machine.prize.x
    p_y = machine.prize.y

    if a_x > a_y:
        print('Swapping axis')
        a_x, a_y = a_y, a_x
        b_x, b_y = b_y, b_x
        p_x, p_y = p_y, p_x

    if a_x < a_y and b_x < b_y:
        print('Failed: They are on the same axis')
        return None
    # endregion

    button_a = Vector2D(a_x, a_y)
    button_b = Vector2D(b_x, b_y)
    target = Vector2D(p_x, p_y)

    print('A:', button_a)
    print('B:', button_b)
    print('T:', target)

    press_b = target.x // button_b.x
    press_a = 0
    #print('Press B:', press_b)
    #print('Press A:', press_a)
    move_by = press_b + 1
    walks = 100
    _try = 0
    while True:
        _try += 1 # Just for debugging
        #print('-------------------')

        position_b = button_b * press_b
        #print('Position B:', position_b)

        distance_b = target - position_b
        #print('Distance B:', distance_b)

        press_a = distance_b.x // button_a.x
        #print('Press A:', press_a)

        position_a = button_a * press_a
        #print('Position A:', position_a)

        combined = position_b + position_a
        #print('Combined:', combined)

        distance = target - combined
        print('Distance:', distance)

        if distance.x > target.x or distance.y > target.y:
            print('Failed: Distance is bigger than target')
            print('Press A:', press_a)
            print('Press B:', press_b)
            print('Distance:', distance)
            print('Try:', _try)
            return None

        # region Success
        if distance.x == 0 and distance.y == 0:
            print('Success')
            print('Press A:', press_a)
            print('Press B:', press_b)
            print('Distance:', distance)
            print('Try:', _try)
            return press_a * cost_a + press_b * cost_b
        # endregion

        if move_by > 2:
            move_by = move_by // 2
        else:
            if walks > 0:
                walks -= 1
                move_by = 1
            else:
                move_by = 0
        
        # Distance y bigger than 0
        if distance.y > 0:
            # Move B back
            press_b -= move_by
            print('Moved B back by:', move_by)
            if move_by > 0:
                continue

        # Distance x less than 0
        if distance.y < 0:
            # Move B forward
            press_b += move_by
            print('Moved B forward by:', move_by)
            if move_by > 0:
                continue

        print('Failed!')
        print('Press A:', press_a)
        print('Press B:', press_b)
        print('Distance:', distance)
        print('Try:', _try)
        return None
         
t = 0
for i, data_machine in enumerate(data_machines):
    print(f'Machine {i+1}')
    m = Machine(data_machine)
    p = find_cheapest(m)
    print()
    if p is not None:
        t += p
print('total:', t)
