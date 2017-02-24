class Underscore(object):
    def map(self, function_to_apply, list_of_inputs):
        newlist = []
        for i in range(0, len(list_of_inputs)):
            newlist.append(function_to_apply(list_of_inputs[i]))
        return newlist
    def reduce(self, function_to_apply, list_of_inputs):
        total = list_of_inputs[0]
        for i in range(1, len(list_of_inputs)):
            total = function_to_apply(total, list_of_inputs[i])
        return total
    def find(self, function_to_apply, list_of_inputs):
        for i in range(0, len(list_of_inputs)):
            if function_to_apply(list_of_inputs[i]):
                return i
        return -1
    def filter(self, function_to_apply, list_of_inputs):
        newlist = []
        for i in range(0, len(list_of_inputs)):
            if function_to_apply(list_of_inputs[i]):
                newlist.append(list_of_inputs[i])
        return newlist
        # your code
    def reject(self, function_to_apply, list_of_inputs):
        newlist = []
        for i in range(0, len(list_of_inputs)):
            if not function_to_apply(list_of_inputs[i]):
                newlist.append(list_of_inputs[i])
        return newlist
        # your code


# you just created a library with 5 methods!
# let's create an instance of our class
_ = Underscore() # yes we are setting our instance to a variable that is an underscore
# evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
# should return [2, 4, 6] after you finish implementing the code above
rejects = list(_.reject(lambda x: x%2 == 0, [1,3,-2,1,-7]))
print rejects

maps = list(_.map(lambda x: x**2, [1,2,3,4,5]))
print maps

reduces = _.reduce((lambda x, y: x * y), [1,2,3,4])
print reduces

filters = list(_.filter(lambda x: x < 0, [1,2,34,-2,-2]))
print filters

finds = _.find(lambda x: x < 0, [1,2,3,-4,-4])
print finds
