# Imports
from PIL import Image             # Reading and handling of images
import numpy as np                # Numeric funtions
import matplotlib.pyplot as plt   # Graphic representation funtions
from skimage import io

# Funciones
# Calculate the position of the array selected
def calcPos(value, data):
    return int((value%4)*(data.shape[1]/4)),int((value%16)/data.shape[0] * (data.shape[0]/4)) * (data.shape[0]//4)

# Exchange the couple of arrays with each other
def exchange(pos1, ref):
    # Position of the first array
    x1, y1 = calcPos(pos1, ref)
    
    print(calcPos(pos1, ref))
    ######Guardado de imagen
    # io.imsave("final.png", arreglo)

# Reading iamge
img = Image.open("./a.png")
img = img.convert('L')

# Draw image
plt.figure()
plt.subplot(122)
plt.imshow(img,cmap='gray',interpolation='nearest')
plt.show()

# Do image a array
data = np.asarray(img, dtype = np.int)

# Array reference of the new order for the new image
b = np.arange(16)
np.random.shuffle(b)


#### LLamado a función que cambia de posicón los cuadros de la imagen, con respecto
#### a lo indicadao en el arreglo b


# Input id of arrays
value1 = 4
while value1 != 55:
    value1=float(input("Input the first array: "))
    # Exchange operation
    exchange(value1, data)