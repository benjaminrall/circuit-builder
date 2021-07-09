import copy
from component import *

def component(base):
    return copy.deepcopy(base)

map = {
    "inputs": [Input()],
    "components": [NAND()],
    "outputs": [Output()]
}

map["inputs"][0].link(0, map["components"][0], 0)
map["inputs"][0].link(0, map["components"][0], 1)
map["components"][0].link(0, map["outputs"][0], 0)

not_gate = Component("NOT", (0, 0, 0), 1, 1, map)

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

map = {
    "inputs": [Input(), Input(), Input(), Input(), Input(), Input(), Input(), Input(), Input()],
    "components": [component(four_bit_adder)],
    "outputs": [Output(), Output(), Output(), Output(), Output()]
}

for i in range(9):
    map["inputs"][i].link(0, map["components"][0], i)
for i in range(5):
    map["components"][0].link(i, map["outputs"][i], 0)

number1 = format(int(input("Enter first number: ")), '04b')
number2 = format(int(input("Enter second number: ")), '04b')

# NUMBER 1
map["inputs"][0].value = int(number1[-4])
map["inputs"][1].value = int(number1[-3])
map["inputs"][2].value = int(number1[-2])
map["inputs"][3].value = int(number1[-1])
# NUMBER 2
map["inputs"][4].value = int(number2[-4])
map["inputs"][5].value = int(number2[-3])
map["inputs"][6].value = int(number2[-2])
map["inputs"][7].value = int(number2[-1])
# CARRY
map["inputs"][8].value = 0
out = ""
for output in map["outputs"]:
    out += f"{output.evaluate()}"
print(f"{int(out, 2)} ({out})")