import copy
from component import *
import pygame
from personallib.camera import Camera

def component(base):
    return copy.deepcopy(base)

# Creating a NOT gate
map = {
    "inputs": [Input()],
    "components": [NAND()],     # 'map' created including all inputs, components, and outputs which would be on the screen  (each can be added by user)
    "outputs": [Output()]
}

map["inputs"][0].link(0, map["components"][0], 0)
map["inputs"][0].link(0, map["components"][0], 1)   # Inputs, components, and outputs can be linked together (by user dragging a wire between them)
map["components"][0].link(0, map["outputs"][0], 0)

map["inputs"][0].value = (map["inputs"][0].value + 1) % 2   # Input values can be toggled (by user clicking on them)
output = map["outputs"][0].evaluate()                       # Output values can be evaluated given the current inputs 
print(map["inputs"][0].value, output)                       # (each time an input or component or link is changed, this is evaluated)


not_gate = Component("NOT", (0, 0, 0), 1, 1, map)   # New component can be created from the current map (by user clicking to add the current map as a component)

# Creating an AND gate
map =   {
    "inputs": [Input(), Input()],
    "components": [NAND(), component(not_gate)],
    "outputs": [Output()]
}

map["inputs"][0].link(0, map["components"][0], 0)
map["inputs"][1].link(0, map["components"][0], 1)
map["components"][0].link(0, map["components"][1], 0)
map["components"][1].link(0, map["outputs"][0], 0)

and_gate = Component("AND", (0, 0, 0), 2, 1, map)

# Creating an OR gate
map = {
    "inputs": [Input(), Input()],
    "components": [component(not_gate), component(not_gate), NAND()],
    "outputs": [Output()]
}

map["inputs"][0].link(0, map["components"][0], 0)
map["inputs"][1].link(0, map["components"][1], 0)
map["components"][0].link(0, map["components"][2], 0)
map["components"][1].link(0, map["components"][2], 1)
map["components"][2].link(0, map["outputs"][0], 0)

or_gate = Component("OR", (0, 0, 0), 2, 1, map)

# Creating an XOR gate
map = {
    "inputs": [Input(), Input()],
    "components": [component(or_gate), NAND(), component(and_gate)],
    "outputs": [Output()]
}

map["inputs"][0].link(0, map["components"][0], 0)
map["inputs"][1].link(0, map["components"][0], 1)
map["inputs"][0].link(0, map["components"][1], 0)
map["inputs"][1].link(0, map["components"][1], 1)
map["components"][0].link(0, map["components"][2], 0)
map["components"][1].link(0, map["components"][2], 1)
map["components"][2].link(0, map["outputs"][0], 0)

xor_gate = Component("XOR", (0, 0, 0), 2, 1, map)

# Creatubg a half adder
map = {
    "inputs": [Input(), Input()],
    "components": [component(and_gate), component(xor_gate)],
    "outputs": [Output(), Output()]
}

map["inputs"][0].link(0, map["components"][0], 0)
map["inputs"][1].link(0, map["components"][0], 1)
map["inputs"][0].link(0, map["components"][1], 0)
map["inputs"][1].link(0, map["components"][1], 1)
map["components"][0].link(0, map["outputs"][0], 0)
map["components"][1].link(0, map["outputs"][1], 0)

half_adder = Component("HALF ADDER", (0, 0, 0), 2, 2, map)

# Creating a full adder
map = {
    "inputs": [Input(), Input(), Input()],
    "components": [component(half_adder), component(half_adder), component(or_gate)],
    "outputs": [Output(), Output()]
}

map["inputs"][0].link(0, map["components"][0], 0)
map["inputs"][1].link(0, map["components"][0], 1)
map["inputs"][2].link(0, map["components"][1], 1)
map["components"][0].link(0, map["components"][2], 1)
map["components"][0].link(1, map["components"][1], 0)
map["components"][1].link(0, map["components"][2], 0)
map["components"][1].link(1, map["outputs"][1], 0)
map["components"][2].link(0, map["outputs"][0], 0)

full_adder = Component("FULL ADDER", (0, 0, 0), 3, 2, map)

# Creating a 4 bit adder
map = {
    "inputs": [Input(), Input(), Input(), Input(), Input(), Input(), Input(), Input(), Input()],
    "components": [component(full_adder), component(full_adder), component(full_adder), component(full_adder)],
    "outputs": [Output(), Output(), Output(), Output(), Output()]
}

map["inputs"][8].link(0, map["components"][3], 2)
map["inputs"][7].link(0, map["components"][3], 1)
map["inputs"][3].link(0, map["components"][3], 0)
map["inputs"][6].link(0, map["components"][2], 1)
map["inputs"][2].link(0, map["components"][2], 0)
map["inputs"][5].link(0, map["components"][1], 1)
map["inputs"][1].link(0, map["components"][1], 0)
map["inputs"][4].link(0, map["components"][0], 1)
map["inputs"][0].link(0, map["components"][0], 0)
map["components"][3].link(0, map["components"][2], 2)
map["components"][2].link(0, map["components"][1], 2)
map["components"][1].link(0, map["components"][0], 2)
map["components"][0].link(0, map["outputs"][0], 0)
map["components"][3].link(1, map["outputs"][4], 0)
map["components"][2].link(1, map["outputs"][3], 0)
map["components"][1].link(1, map["outputs"][2], 0)
map["components"][0].link(1, map["outputs"][1], 0)

four_bit_adder = Component("FOUR BIT ADDER", (0, 0, 0), 9, 5, map)

# Creating an adder & subtracter
map = {
    "inputs": [Input(), Input(), Input(), Input(), Input(), Input(), Input(), Input(), Input()],
    "components": [component(xor_gate), component(xor_gate), component(xor_gate), component(xor_gate), component(four_bit_adder)],
    "outputs": [Output(), Output(), Output(), Output()]
}

for i in range(4):
    map["inputs"][i].link(0, map["components"][4], i)
for i in range(4):
    map["inputs"][i + 4].link(0, map["components"][i], 0)
for i in range(4):
    map["inputs"][8].link(0, map["components"][i], 1)
map["inputs"][8].link(0, map["components"][4], 8)
for i in range(4):
    map["components"][i].link(0, map["components"][4], i + 4)
for i in range(4):
    map["components"][4].link(i + 1, map["outputs"][i], 0)

alu = Component("ALU", (0, 0, 0), 9, 4, map)

# 4 BIT ADDER DEMONSTRATION
map = {
    "inputs": [Input(), Input(), Input(), Input(), Input(), Input(), Input(), Input(), Input()],
    "components": [component(alu)],
    "outputs": [Output(), Output(), Output(), Output()]
}

for i in range(9):
    map["inputs"][i].link(0, map["components"][0], i)
for i in range(4):
    map["components"][0].link(i, map["outputs"][i], 0)

d_number1 = int(input("Enter first number: "))
d_number2 = int(input("Enter second number: "))
b_number1 = format(d_number1, '04b')
b_number2 = format(d_number2, '04b')

neg = {0: 0, 1: -8}

# NUMBER 1
map["inputs"][0].value = int(b_number1[-4])
map["inputs"][1].value = int(b_number1[-3])
map["inputs"][2].value = int(b_number1[-2])
map["inputs"][3].value = int(b_number1[-1])
# NUMBER 2
map["inputs"][4].value = int(b_number2[-4])
map["inputs"][5].value = int(b_number2[-3])
map["inputs"][6].value = int(b_number2[-2])
map["inputs"][7].value = int(b_number2[-1])
# ADDITION
map["inputs"][8].value = 0
out = ""
for output in map["outputs"]:
    out += f"{output.evaluate()}"
print(f"{d_number1} + {d_number2} = {neg[int(out[0])] + int(out[1:], 2)} ({out})")
# SUBTRACTION
map["inputs"][8].value = 1
out = ""
for output in map["outputs"]:
    out += f"{output.evaluate()}"
print(f"{d_number1} - {d_number2} = {neg[int(out[0])] + int(out[1:], 2)} ({out})")