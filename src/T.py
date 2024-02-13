class TTT:
    print("TTTTTTTTTTTTTTTTTTTTTTTTUYYYYYYYYYYYYYYYYYYYYUUUUUUUUU")

class TTTMyclass:
    i = 12345
    def f(self):
        return 'hello world.'


class Complex:
    def __init__(self,realpart, imagpart):
        self.r = realpart
        self.i = imagpart


x = TTTMyclass()
print(x.i)
print(x.f())

xa = Complex(3.0, -4.5)
print(xa.r, xa.i)
