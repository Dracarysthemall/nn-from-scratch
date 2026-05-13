class Layer:
    def __init__(self):
        self.input = None
        self.output = None
    
    def forward(self, input):
        # TODO: return the output of the layer for the given input
        pass
    
    def backward(self, output_gradient, learning_rate):
        # TODO: update parameters and return input gradient
        pass
    