# Imports
import numpy as np

# Funciones
# Calculate the position of the array selected
def calcPos(value):
    return int((value%4)*(data.shape[1]/4)), int((value%16)/data.shape[0] * (data.shape[0]/4))

# Exchange the couple of arrays with each other
def exchange(pos1, pos2):
    # Position of the first array
    x1, y1 = calcPos(pos1)
    print(calcPos(pos1))

# Definicion
data=np.full((673,840),5)

# Input id of arrays
value1=float(input("Input the first array: "))

# Exchange operation
exchange(value1, 0)