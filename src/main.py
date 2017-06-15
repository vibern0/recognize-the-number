from nn import NeuralNetwork
from transform import Transform

print('1 - Train\n2 - Test')
x = int(raw_input('Option:'))

if x is 1:
    NeuralNetwork()
elif x is 2:
    Transform()
    pass
