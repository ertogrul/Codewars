#  core_nn SOLUTION
import numpy as n
# define input data
input_data = n.array([[0, 0, 1],
                    [1, 1, 1],
                    [1, 0, 1],
                    [0, 1, 0]])
# define output data
output_data = n.array([0, 1, 1, 0])


# set weights
n.random.seed(1)
weights = 2 * n.random.random((3, 1)) -1

# create NN
class NerualNertwork():
    def __init__(self):
        # set first iteration weights
        n.random.seed(1)
        self.weights = 2 * n.random.random((3, 1)) - 1

    def sigmoid(self, x):
        # standardize inputs
        return 1 / 1 + n.exp(-x)

    def sig_derivative(self, x):
        # check direction in which weights will go
        return 1 * (1 - x)
    def train(self, input_data, output_data, nr_iterations):
        for i in iter(range(nr_iterations)):
            output = self.think(input_data)
            error = output_data - output
            # adjustment = error * (sig_derivative(output))
            adjustment = n.dot(input_data.T, error * self.sig_derivative(output))
            self.weights += adjustment
            if (iteration % 100 == 0):
                print ("error after %s iteration: %s" % (iteration, str(n.mean(n.abs(error)))))
