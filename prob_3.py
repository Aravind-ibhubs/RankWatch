import sys

class SampleClass:
    a = 0
    def __init__(self):
        self.a = 10
        
    def __del__(self):
        print("Last value of a is {}".format(self.a))
        try:
            sys.exit(2)
        except:
            pass 
        
sobj = SampleClass()
sobj.a = 50
del sobj
print("exiting")
