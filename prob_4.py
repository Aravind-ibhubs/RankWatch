class TestClass:
    x = 10
    @classmethod
    def get_test_again(cls):
        return cls.x
    
    @staticmethod
    def get_val(x):
        x += 2
        return x
    
t = TestClass()
t.x = 20
#print(t.get_test_again())
print(t.get_val(10))
