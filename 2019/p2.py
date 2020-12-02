import unittest
from aocd.models import Puzzle

def print_frame(memory, pointer):
    print("...print_frame pointer=" + str(pointer) + ", memory=", end='')
    print(memory[pointer:pointer+4])
    pass

# Opcode 1 adds together numbers read from two positions and stores the result in a third position. The three integers immediately after the opcode tell you these three positions - the first two indicate the positions from which you should read the input values, and the third indicates the position at which the output should be stored.
def execute_opcode_1(memory, pointer):
    print("...executing opcode 1")
    memory[memory[pointer + 3]] = memory[memory[pointer + 1]] + memory[memory[pointer + 2]]
    return memory

# Opcode 2 works exactly like opcode 1, except it multiplies the two inputs instead of adding them. Again, the three integers after the opcode indicate where the inputs and outputs are, not their values.
def execute_opcode_2(memory, pointer):
    print("...executing opcode 2")
    memory[memory[pointer + 3]] = memory[memory[pointer + 1]] * memory[memory[pointer + 2]]
    return memory

def run_program(memory):
    print("Running Intcode program... ", end='')
    print(memory)
    program_counter = 0
    while memory[program_counter] != 99:
        print_frame(memory, program_counter)
        if memory[program_counter] == 1:
            memory = execute_opcode_1(memory, program_counter)
        elif memory[program_counter] == 2:
            memory = execute_opcode_2(memory, program_counter)
        else:
            print("ERROR! unknown opcode")
        program_counter += 4
    print("...HALT... dumping memory...", end='')
    print(memory)
    return memory

class TestClass(unittest.TestCase):

    def test_example_1(self):
        example_program = [1,0,0,0,99]
        example_output = [2,0,0,0,99]
        output = run_program(example_program)
        self.assertEqual(output, example_output)

    def test_example_long(self):
        example_program = [1,9,10,3,2,3,11,0,99,30,40,50]
        example_output = [3500,9,10,70,2,3,11,0,99,30,40,50]
        output = run_program(example_program)
        self.assertEqual(output, example_output)

    # Once you have a working computer, the first step is to restore the gravity assist program (your puzzle input) to the "1202 program alarm" state it had just before the last computer caught fire. To do this, before running the program, replace position 1 with the value 12 and replace position 2 with the value 2. What value is left at position 0 after the program halts?
    def test_part_a(self):
        puzzle = Puzzle(year=2019, day=2)
        input_program = [int(x) for x in puzzle.input_data.split(',')]
        input_program[1] = 12
        input_program[2] = 2
        run_program(input_program)

    def test_part_b(self):
        puzzle = Puzzle(year=2019, day=2)
        output = [0]
        for x in range(99):
            for y in range(99):
                input_program = [int(x) for x in puzzle.input_data.split(',')]
                input_program[1] = x
                input_program[2] = y
                output = run_program(input_program)
                if output[0] == 19690720:
                    print("!!! FOUND Y !!! y=" + str(y))
                    break
            if output[0] == 19690720:
                print("!!! FOUND X !!! x=" + str(x))
                break

if __name__ == '__main__':
    unittest.main()
