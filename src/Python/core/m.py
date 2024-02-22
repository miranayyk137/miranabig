# 小numpy库
class array:
    def __init__(self, ndim):
        global i
        global a
        i = 0
        a = []
        for a in ndim:
            # print(a)
            if isinstance(a, list): 
                if isinstance(a,list):
                    i += 1
            if isinstance(a, int):
                i = 1      
        self.ndim = i