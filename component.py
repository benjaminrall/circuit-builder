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
