class Klass:

    def discriminant(self, a, b, c):
        D = b**2 - 4 * a * c
        print (D)
        return D
    
    def squareroot(self, a, b):
        x = -b / (2 * a)
        print (x)
        return x
    
    def squareroots(self, a, b, D):
        x1 = (-b + D ** 0.5) / (2 * a)
        x2 = (-b - D ** 0.5) / (2 * a)
        print(x1, x2)
        return sorted([x1, x2])