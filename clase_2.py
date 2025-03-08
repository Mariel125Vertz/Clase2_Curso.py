import numpy as np
array=np.array([[1,2,3],[4,5,6]])
print(array.ndim) #atributo devuelve un entero que indica el número de dimensiones del arreglo.
print(array.shape) #devuelve una tupla con el tamaño del arreglo en cada dimensión.
print(array.dtype)#describe el tipo de dato


z=np.array(3,dtype=np.uint8)
print(z)

double=np.array([1,2,3], dtype='d')
print(double)

z=z.astype(np.float64)
print(z)