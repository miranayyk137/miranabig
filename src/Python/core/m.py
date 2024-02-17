# 小numpy库
class miranalist:
    def __init__(self, a):
        self.a = a
    def ndim(self):
        return 1

mx = input()
# input a number.请输入一个数。

m = miranalist(mx)
print(m.ndim())

