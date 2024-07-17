class ABC():
    def print_help(self):
        print("Help from ABC")
        
class ChildABC(ABC):
    def print_help(self):
        print("Help from Child ABC")

class DEF():
    def print_help(self):
        print("Help from DEF")
        
class ChildDEF(DEF):
    def print_help(self):
        print("Help from Child DEF")
        
class TryPrint(DEF, ABC): #interchange the parameter like ABC, DEF
    def _print_help(self):
        print("Help from ABC and DEF")
        
if __name__ == "__main__":
    obj = TryPrint()
    obj.print_help()
