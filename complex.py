from math import sqrt

class Complex:
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def add(self, z):
        real = self.re + z.re
        imag = self.im + z.im
        return Complex(real, imag)

    def times(self, z):
        real = self.re*z.re - self.im*z.im
        imag = self.re*z.im + self.im*z.re
        return Complex(real, imag)

    def norm(self):
        return sqrt(self.re**2 + self.im**2)

    def to_string(self):
        return str(self.re) + " + " + str(self.im) + "i"

def main():
    z1 = Complex(3, 4)
    z2 = Complex(-2, 3)
    print("z1 = ", z1.to_string())
    print("z2 = ", z2.to_string())
    s = z1.add(z2)
    print("z1 + z2 = ", s.to_string() )
    p = z1.times(z2)
    print("z1 x z2 = ", p.to_string() )
    a = z1.norm()
    print("|z1| = ", a)

if __name__ == "__main__":
    main()

