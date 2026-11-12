
class Vektor:
    def __init__(self, x, y):
      self.x = x
      self.y = y

    def __str__(self):
        return f"Vektor({self.x}, {self.y})"
    
    def secti(self, v):
        self.x += v.x
        self.y += v.y
        return Vektor(self.x, self.y)

    def nasob(self, i):
        self.x *= i
        self.y *= i
        return Vektor(self.x, self.y)
    

if __name__ == "__main__":
   
   v1 = Vektor(10, 5)
   print(v1)
   v2= Vektor(3, 8)
   print(v2)
   print(v1.secti(v2))

   print(v2.nasob(2))
