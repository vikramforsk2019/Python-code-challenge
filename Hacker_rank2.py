
class Rectangle:
    def __init__(self, w, h):
      self.w = w
      self.h = h
    def area(self):
        return (self.w*self.h)
class Circle:
    def __init__(self, r):
      self.r = r
    def area(self):
      a = float(self.r**2 * math.pi)
      return a
if __name__ == "__main__":
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(raw_input())
    queries = []
    for _ in xrange(q):
        args = raw_input().split()
        shape_name, params = args[0], map(int, args[1:])
        if shape_name == "rectangle":
            a, b = params[0], params[1]
            shape = Rectangle(a, b)
        elif shape_name == "circle":
            r = params[0]
            shape = Circle(r)
        else:
            raise ValueError("invalid shape type")
        fptr.write("%.2f\n" % shape.area())
    fptr.close()

