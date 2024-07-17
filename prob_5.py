class TestVal():
    test_val = None
    @staticmethod
    def print_diff(self, val):
        print("Teest Val: {} and Difference is {}".format(
            self.test_val, abs(self.test_val - val)))
            
if __name__ == '__main__':
    val_test = TestVal()
    val_test.test_val = 10
    TestVal.print_diff(val_test, 50)
    