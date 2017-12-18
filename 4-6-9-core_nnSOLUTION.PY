#  core_nn SOLUTION
import numpy as n
inputs = n.array([[0, 0, 1],
                [1, 1, 1],
                [1, 0, 1],
                [0, 1, 0]])

training_set_outputs = n.array([[0, 1, 1, 0]]).T

synaptic_weights = 2 * n.random.random((3, 1)) - 1


def __sigmoid(self, x):
    return 1 / (1 + n.exp(-x))

def think(inputs):
    # Pass inputs through our neural network (our single neuron).
    return __sigmoid(n.dot(inputs, synaptic_weights))


print (think(inputs))
