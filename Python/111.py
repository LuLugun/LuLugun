import numpy as np
a = np.array([1,2,3])
print(a)
np3 = np.array([1, 2, 3, 4, 5, 6])
np3 = np3.reshape([2, 3])
print(np3.ndim, np3.shape, np3.dtype)
print(np3)
print(np3 > 3) # [False False False  True  True  True]
print(np3[np3 > 3]) # [4 5 6]
print(np3.sum(axis=1))
print(np3)
