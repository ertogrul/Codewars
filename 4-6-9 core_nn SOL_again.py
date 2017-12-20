#again... writing single neuron network from the head....
import numpy as nu
# input
input_data = nu.array([[1, 1, 0], [0, 1, 0], [0, 0, 1], [1, 1, 1]])
output_data = nu.array([[1, 0, 0, 1]]).T
test = nu.array([1, 0, 0])
class NeuralNetwork():
    # weights
    def __init__(self):
        nu.random.seed(1)
        self.weights = 2 * nu.random.random((3, 1)) - 1

    def sigmoid(self, x):
        # multiplyi in one neuron plus normalize in sygmoid
        return 1 / (1 + nu.exp(-x))

    def derivative(self, x):
        # count derivative to make backpropagation
        return x * (1 - x)

    def train(self, input_data, output_data, nr_iterations):
        for i in iter(range(nr_iterations)):
            output = self.think(input_data)
            error = output_data - output
            adjustment = nu.dot(input_data.T, error * self.derivative(output))
            self.weights += adjustment
            if (i % 1000 == 0):
                print ("error after %s iteration: %s" % (i, str(nu.mean(nu.abs(error)))))

    def think(self, input_data):
        return self.sigmoid(nu.dot(input_data, self.weights))

nn = NeuralNetwork()
# print (nn.weights)
print ("NN's result without training:", nn.think(test))

print ("Initial weights: ")
print (nn.weights)
nn.train(input_data, output_data, 10000)
print ("Trained weights: ", nn.weights)

test = [1, 0, 0]
print ("Now we'll predict the output value for new data: ", test)
print (nn.think(nu.array(test)))
