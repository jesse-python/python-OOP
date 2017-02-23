class MathDojo(object):
    def __init__(self):
        self.total = 0
    def add(self, *params):
        # print "Got " + str(params)

        for i in range(0, len(params)):
            if type(params[i]) is list or type(params[i]) is tuple:
                 for z in range(0, len(params[i])):
                    #  print params[i][z]
                     self.total += params[i][z]
            else:
                self.total += params[i]
        return self

    def subtract(self, *params):
        for i in range(0, len(params)):
            if type(params[i]) is list or type(params[i]) is tuple:
                 for z in range(0, len(params[i])):
                     self.total -= params[i][z]
            else:
                self.total -= params[i]
        return self
    def result(self):
        print "Result is " + str(self.total)

md = MathDojo()
md.add(2).add(2,5).subtract(3,2).result()

md2 = MathDojo()
md2.add([1],3,4).add((3, 5, 7, 8), [2, 4.3, 1.25]).subtract(2, [2,3], [1.1, 2.3]).result
