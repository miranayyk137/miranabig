# 小numpy库
class Mirananumpy:
    def __init__(self, ndim):
        count = 0
        for item in ndim:
            if isinstance(item, list):
                count+=1
        self.ndim = count



print("mirananumpy")
print("请用mirananumpy创建一个数组: ")

#list1 = [[1,2,3,4],[2,3,4,5,6]]
#x = Mirananumpy(list1)

x = Mirananumpy([[1,2,3,4],[2,3,4,5,6]])
print(type(x))

print(x.ndim)
