
import numpy as np

# Concatenate
# 1 d array                           
 
a = np.array ([2,4,5,8,22,99,100])
b = np.array ([12,9,7,6,44,87,222])
c =np.concatenate((a,b))
c.sort()
print (c)



# # 2 d array

x= np.array ([[2,4],[9,22]])
y= np.array ([[9,7],[1,44]])

z = np.concatenate((x,y),axis=0)
print (z)

# 3 d array

L= np.array ([[[2,4],[9,22]],
              [[2,4],[9,22]],
              [[2,4],[9,22]]])

print (L.size)         # to find size of array
                  
print (L.ndim)         # to find dimension

print (L.shape)        # to find shape of array

print (L)



# Reshape an array

o = np.arange(9)
# print (o)
print (o.reshape(3, 3))

# Other functions

e = np.array ([2,4,5,8,22,99,100])
print (e*2)                                # multiply array with 2
print (e.sum())
print (e.mean())
print (e+5)