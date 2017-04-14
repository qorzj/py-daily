## 题目
实现一个向量类Vector，使它支持乘法运算符`*`，下标运算`[]`，且可以转为list和str，支持len(), sum(), max()等builtins函数。vector * vector的含义是向量内积(也称为点积)。vector * int表示向量按比例缩放。例如：
```
Vector(1,2,3) * Vector(1,2,3) --> Vector(1,4,9)
v = Vector(3,4,5,6)
v * 2 --> Vector(6,8,10,12)
v[0] --> 3; v[-1] --> 6; len(v) --> 4
list(v) --> [3,4,5,6]
str(v) --> 'Vector(3, 4, 5, 6)'
sum(v) --> 18
```
