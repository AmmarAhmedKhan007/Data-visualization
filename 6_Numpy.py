
# 1 D array:

import numpy as np

x =np.array([2, 3, 44, 5])
print(x)
print(type(x))
print (len(x))

# types:

b = np.ones(4)                  # make array of [1 1 1 1]   and also make zeros or empty arrays
c = np.zeros(3)
d = np.empty(5)
e = np.arange(7)
f = np.arange(2, 21)            # for specific range
g = np.arange(2, 21, 2)         # for 2 gap
h = np.linspace (0, 10, num=5)        # print 5 numbers between 0 & 10
print (b)
print (c)
print (d)
print (e)
print (f)
print (g)
print (h)

# Specific data types in arrays

i = np.ones(5, dtype=np.int8)              
j = np.ones (5, dtype=np.float16)
print (i)
print (j)


# 2 D array :

y=np.array([[5, 5, 5, 5],[5, 5, 5, 5],[5, 5, 5, 5]])
print (y)
print (type(y))


# Types:

k = np.ones((4, 3))              
l = np.zeros((3, 3))
m = np.empty((5, 3))
print (k)
print (l)
print (m)


# 3 D array:

z = np.arange(24).reshape(2, 3, 4)          # 2 means 2 arrays. 3 means no of rows. 4 means no of cols.
print (z)