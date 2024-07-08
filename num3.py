import numpy as np

arr1=np.array([1,2,3,4])
print(arr1)
print("SHAPE OF ARRAY=",arr1.shape)
print("NUMBER OF DIMENSIONAL=",arr1.ndim)
print("NUMBER OF ELEMENTS IN THE ARRAY=",arr1.size)
print("DATA TYPE OF THE ELEMENTS=",arr1.dtype)
print("--------------------------------------------------")
arr2=np.array([[1,2,3],[4,5,6]])
print(arr2)
print("SHAPE OF ARRAY=",arr2.shape)
print("NUMBER OF DIMENSIONAL=",arr2.ndim)
print("NUMBER OF ELEMENTS IN THE ARRAY=",arr2.size)
print("DATA TYPE OF THE ELEMENTS=",arr2.dtype)


print("--------------------------------------------------")
zeros=np.zeros((3,3))
print(zeros)
ones=np.ones((2,4))
print(ones)
identity=np.eye(3)
print(identity)
random=np.random.random((2,2))
range=np.arange(1,10)
print(range.reshape((3,3)))

l=np.linspace(0,1,5)