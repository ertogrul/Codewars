#  core_nn SOLUTION
import numpy as n
# define input data
input_data = n.array([[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 0]])
# define output data
output_data = n.array([[0, 1, 1, 0]]).T

# create NN
class NeuralNetwork():
    def __init__(self):
        # set first iteration weights
        n.random.seed(1)
        self.weights = 2 * n.random.random((3, 1)) - 1

    def sigmoid(self, x):
        # standardize inputs
        return 1 / ( 1 + n.exp(-x))

    def sig_derivative(self, x):
        # check direction in which weights will go
        return x * (1 - x)

    def train(self, input_data, output_data, nr_iterations):
        for i in iter(range(nr_iterations)):
            output = self.think(input_data)
            error = output_data - output
            adjustment = n.dot(input_data.T, error * self.sig_derivative(output))
            self.weights += adjustment
            if (i % 1000 == 0):
                print ("error after %s iteration: %s" % (i, str(n.mean(n.abs(error)))))

    def think(self, input_data):
        # pass inputs through NN (1 neuron)
        return self.sigmoid(n.dot(input_data, self.weights))


if __name__ == "__main__":
    # train nn
    nn = NeuralNetwork()
    print ("Initial weights: ")
    print (nn.weights)
    nn.train(input_data, output_data, 10000)
    print ("Trained weights: ", nn.weights)

    # test nn with new data
    test = [1, 0, 0]
    print ("Now we'll predict the output value for new data: ", test)
    print (nn.think(n.array(test)))
