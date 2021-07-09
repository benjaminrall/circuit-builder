import copy

class Component:
    def __init__(self, name, colour, inputs, outputs, map):
        self.name = name
        self.colour = colour
        self.inputs = [(None, 0) for i in range(inputs)]
        self.outputs = []
        self.map = map
    
    def evaluate(self, output):
        return self.map["outputs"][output].evaluate()

    def link(self, output, component, input):
        component.set_input(input, (self, output))

    def set_input(self, input, connection):
        self.inputs[input] = connection

    def get_input_values(self):
        self.inputValues = []
        for input in self.inputs:
            value = 0
            if isinstance(input[0], Input):
                value = input[0].get_value()
            elif isinstance(input[0], NAND):
                input[0].get_input_values()
                value = input[0].evaluate()
            elif isinstance(input[0], Component):
                input[0].get_input_values()
                for i in range(len(input[0].map["inputs"])):
                    input[0].map["inputs"][i].value = input[0].inputValues[i]
                value = input[0].evaluate(input[1])
            self.inputValues.append(value)
        return self.inputValues

class NAND(Component):
    def __init__(self):
        self.inputs = [None, None]
        self.inputValues = [0, 0]

    def evaluate(self):
        return {0 : 1, 1 : 1, 2 : 0}[sum(self.get_input_values())]
                
class Input(Component):
    def __init__(self):
        self.value = 0

    def get_value(self):
        return self.value

class Output(Component):
    def __init__(self):
        self.inputs = [(None, 0)]

    def evaluate(self):
        return self.get_input_values()[0]

'''
function(inputs):
    newInputs = []
    for input in inputs:
        if input connected to raw input : input = raw input
        else if output connected to component : input = Component.evaluate(function(Component inputs))
        else input = 0
        newInputs.append(input)
    return newInputs
'''

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
    "components": [component(xor_gate)],
    "outputs": [Output()]
}

map["inputs"][0].link(0, map["components"][0], 0)
map["inputs"][1].link(0, map["components"][0], 1)
map["components"][0].link(0, map["outputs"][0], 0)

map["inputs"][0].value = 0
map["inputs"][1].value = 0
print(map["outputs"][0].evaluate())

map["inputs"][0].value = 1
map["inputs"][1].value = 0
print(map["outputs"][0].evaluate())

map["inputs"][0].value = 0
map["inputs"][1].value = 1
print(map["outputs"][0].evaluate())

map["inputs"][0].value = 1
map["inputs"][1].value = 1
print(map["outputs"][0].evaluate())