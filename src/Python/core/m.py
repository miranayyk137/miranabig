# 小numpy库
class array:
    def __init__(self, ndim):
        count =0
        if isinstance(ndim, list):
            count += 1
        self.ndim = count
