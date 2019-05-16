from __future__ import print_function
import torch as t

# 构建 5x3 矩阵，只是分配了空间，未初始化
# x = t.Tensor(5, 3)
# y = t.Tensor([[1,2],[3,4]])

# 使用[0,1]均匀分布随机初始化二维数组
x = t.rand(5, 3)
y = t.rand(5, 3)
print(x.size()) # 查看x的形状
x.size()[1], x.size(1) # 查看列的个数, 两种写法等价

t.add(x, y)

result = t.Tensor(5, 3) # 预先分配空间
t.add(x, y, out=result) # 输入到result
print(result)

print('最初y')
print(y)

print('第一种加法，y的结果')
y.add(x) # 普通加法，不改变y的内容
print(y)

print('第二种加法，y的结果')
y.add_(x) # inplace 加法，y变了
print(y)

# 注意，函数名后面带下划线_ 的函数会修改Tensor本身。例如，x.add_(y)和x.t_()会改变 x，
# 但x.add(y)和x.t()返回一个新的Tensor， 而x不变。

import numpy as np
a = np.ones(5)
b = t.from_numpy(a) # Numpy->Tensor
print(a)
print(b)
b.add_(1) # 以`_`结尾的函数会修改自身
print(a)
print(b) # Tensor和Numpy共享内存
scalar = b[0]
print(scalar)
print(scalar.size())#0-dim
print(scalar.item()) # 使用scalar.item()能从中取出python对象的数值
tensor = t.tensor([2]) # 注意和scalar的区别
print(tensor,scalar)
print(tensor.size(),scalar.size())
print(tensor.item(), scalar.item())
tensor = t.tensor([3,4]) # 新建一个包含 3，4 两个元素的tensor
scalar = t.tensor(3)
print(scalar)

old_tensor = tensor
new_tensor = t.tensor(old_tensor)
new_tensor[0] = 1111
print(old_tensor, new_tensor)

new_tensor = old_tensor.detach()
new_tensor[0] = 1111
print(old_tensor, new_tensor)
