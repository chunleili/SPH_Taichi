import numpy as np
x= np.array([1,2,3,4,5])
y= np.array([6,7,8])


# 解释：meshgrid会将两个一维数组交织成网格。拓展的方式是重复。
# 它分为两种模式：ij模式和xy模式（默认）。例如x是5维数组(m=5)，y是3维数组(n=3)，则meshgrid之后变为5行3列数组。返回的值有两个。第一个是拓展x，第二个是拓展y。

# 如用一个值接收返回，就是两个都返回，组成一个list
print('-------如用一个值接收返回，就是两个都返回，组成一个list-----')
a = np.meshgrid(x,y,indexing='ij')
# print(a)
# res:
# [array([[1, 1, 1],
#        [2, 2, 2],
#        [3, 3, 3],
#        [4, 4, 4],
#        [5, 5, 5]]), 
#        array([[6, 7, 8],
#        [6, 7, 8],
#        [6, 7, 8],
#        [6, 7, 8],
#        [6, 7, 8]])]

# 如用两个值接收返回，那么分别就是两个数组拓展后的结果
print('-------如用两个值接收返回，那么分别就是两个数组拓展后的结果-----')
a,b = np.meshgrid(x,y,indexing='ij')
# print(a)
# res 
# [[1 1 1]
#  [2 2 2]
#  [3 3 3]
#  [4 4 4]
#  [5 5 5]]

# xy模式
print('-------xy模式拓展成n行m列-----')
a,b = np.meshgrid(x,y,indexing='xy')
# print(a)
# print(b)


# 拓展三维 ij
print('-------拓展三维 ij-----')
z = np.array([100,101])
res = np.meshgrid(x,y,z,indexing='ij')
# print(res)
# print('res[0]\n',res[0])
# print('res[1]\n',res[1])
# print('res[2]\n',res[2])
res = np.array(res)
print(res.shape)
print(res)
print(res[0].shape)
print(res[0])
print(res[1].shape)

# # 拓展三维xy
# print('-------拓展三维 xy-----')
# z = np.array([100,101])
# res = np.meshgrid(x,y,z,indexing='xy')
# print('-------拓展三维 xy-----')

# print('res[0]\n',res[0])
# print('res[1]\n',res[1])
# print('res[2]\n',res[2])