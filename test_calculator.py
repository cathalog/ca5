import unittest
from calculator2 import Calculator # should find this file if in the same directory

class TestCalculator(unittest.TestCase):

    def test_calculator_multiply(self):
        result = Calculator().multiply([5,5])
        self.assertEqual(25, result)
        result = Calculator().multiply([5,0])
        self.assertEqual(0, result)
        result = Calculator().multiply([5,1])
        self.assertEqual(5, result) 
        result = Calculator().multiply([5,0.2])
        self.assertEqual(1, result)       

          
    def test_calculator_divide(self):
        result = Calculator().divide([5,5])
        self.assertEqual(1, result)
        result = Calculator().divide([5,1])
        self.assertEqual(5, result)
        result = Calculator().divide([5,0.2])
        self.assertEqual(25, result)     
        result = Calculator().divide([5,4])
        self.assertEqual(1.25, result) 

        
    def test_calculator_add(self):
        result = Calculator().add([5,5])
        self.assertEqual(10, result)
        result = Calculator().add([2,3])
        self.assertEqual(5, result)
        result = Calculator().add([2,5])
        self.assertEqual(7, result)
        

    def test_calculator_subtract(self):
        result = Calculator().subtract([5,5])
        self.assertEqual(0, result)
        result = Calculator().subtract([5,3])
        self.assertEqual(2, result)    
        result = Calculator().subtract([3,5])
        self.assertEqual(-2, result)  


    def test_calculator_exponent(self):
        result = Calculator().exponent([2,3])
        self.assertEqual(8, result)
        result = Calculator().exponent([5,0])
        self.assertEqual(1, result)    
        result = Calculator().exponent([-2,2])
        self.assertEqual(4, result)      
      
            
    def test_calculator_square(self):
        result = Calculator().square([2])
        self.assertEqual([4], result)
        result = Calculator().square([-2,2,10])
        self.assertEqual([4,4,100], result)    
        result = Calculator().square([40])
        self.assertEqual([1600], result)      

    def test_calculator_squareroot(self):
        result = Calculator().squareroot([16])
        self.assertEqual([4], result)
        result = Calculator().squareroot([4,256,144])
        self.assertEqual([2,16,12], result)    
        result = Calculator().squareroot([100])
        self.assertEqual([10], result) 

'''         
    def test_calculator_sin(self):
        result = round(Calculator().sindegrees([10]),10)
        self.assertEqual(0.1736481777, result)
        result = Calculator().sindegrees([90])
        self.assertEqual(1, result)    
        result = round(Calculator().sindegrees([135,50]),10)
        self.assertEqual([0.7071067812,0.7660444431], result)  
             
    def test_calculator_cos(self):
        result = round(Calculator().cosdegrees([0]),10)
        self.assertEqual(1, result)
        result = round(Calculator().cosdegrees([90]),10)
        self.assertEqual(0, result)    
        result = round(Calculator().cosdegrees([140]),10)
        self.assertEqual(-0.7660444431, result)    
          
        
    def test_calculator_tan(self):
        result = round(Calculator().tandegrees([0]),10)
        self.assertEqual(0, result)
        result = round(Calculator().tandegrees([45]),10)
        self.assertEqual(1, result) 
        result = round(Calculator().tandegrees([89]),7)
        self.assertEqual(57.2899616, result)    

'''       
                
if __name__ == '__main__':   # only runs from the command line, not other packages
    unittest.main()
   
