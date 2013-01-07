##warning:
a.shape --> (N,) means 1-d
a.shape --> (N,1) means 2-d

a = np.array([1,2,3,4], dtype=np.float)
np.arange(0,1,0.1)
np.linspace(0, 1, 12)
np.logspace(0, 2, 20)
s = "abcdefg"
np.fromstring(s, dtype=np.int8)
np.fromstring(s, dtype=np.int16)
def func(i):
  return i%4+1
np.fromfunction(func, (10,))
>>> def func2(i, j):
...     return (i+1) * (j+1)
...
>>> a = np.fromfunction(func2, (9,9))
>>> a = np.arange(10)
persontype = np.dtype({
    'names':['name', 'age', 'weight'],
    'formats':['S32','i', 'f']})
a = np.array([("Zhang",32,75.5),("Wang",24,65.2)],
    dtype=persontype)
>>> x = np.linspace(0, 2*np.pi, 10)
# 对数组x中的每个元素进行正弦计算，返回一个同样大小的新数组
>>> y = np.sin(x)
t = np.sin(x,x)
import time
import math
import numpy as np

x = [i * 0.001 for i in xrange(1000000)]
start = time.clock()
for i, t in enumerate(x):
    x[i] = math.sin(t)
print "math.sin:", time.clock() - start

x = [i * 0.001 for i in xrange(1000000)]
x = np.array(x)
start = time.clock()
np.sin(x,x)
print "numpy.sin:", time.clock() - start
triangle_ufunc = np.frompyfunc( lambda x: triangle_wave(x, 0.6, 0.4, 1.0), 1, 1)
y2 = triangle_ufunc(x)
y2.astype(np.float64)
>>> x,y = np.ogrid[0:5,0:5]
>>> x
array([[0],
       [1],
       [2],
       [3],
       [4]])
>>> y
array([[0, 1, 2, 3, 4]])
>>> a = np.random.rand(10,10)
>>> b = np.random.rand(10)
>>> x = np.linalg.solve(a,b) ## a*x = b
>>> np.sum(np.abs(np.dot(a,x) - b))
>>> a1 = np.array([[1,1,1],[1,1,1],[1,1,1]])
>>> a2 = np.array([[2,2,2],[2,2,2],[2,2,2]])
>>> a3 = np.array([[3,3,3],[3,3,3],[3,3,3]])
>>> import scipy.linalg
>>> scipy.linalg.block_diag(a1, a2, a3)
