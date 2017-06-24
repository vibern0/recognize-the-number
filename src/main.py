from nn import NeuralNetwork
from transform import Transform
from generator import Dataset_Generator

print('1 - Train\n2 - Test\n3- Generate')
x = int(input('Option:'))

if x is 1:
    NeuralNetwork()
elif x is 2:
    Transform()
elif x is 3:
    Dataset_Generator()

