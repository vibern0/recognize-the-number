from nn import NeuralNetwork
import transform

print('1 - Train\n2 - Test')
x = int(raw_input('Option:'))

if x is 1:
    neural = NeuralNetwork()
elif x is 2:
    pass
