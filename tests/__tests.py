import src.Python.core.ndim as np

def ass():
    a = np.array([[1,2,3,4],[2,3]])
    print(type(a))
    print(a.ndim)

    s = np.array([1,2,3])
    print(type(s))
    print(s.ndim)