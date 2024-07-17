class ExampleClass:
    _value_a = 0
    values = {}
    def __init__(self , **kwargs):
        for kw in kwargs:
            self.values[kw] = kwargs[kw]
            
    def sum(self):
        return sum(self.values.values())
    
    def sum2(self):
        return sum(map(lambda x: x+1, self.values.values()))

    def ops1(self):
        # return sorted(self.values.keys(), reverse=True)
        return sorted(self.values.values(), reverse=True)
    
example_obj = ExampleClass(a=10, b=20, c = 30)
print(example_obj.ops1()) 
#print(example_obj.sum2())
