import unittest

from math import sin
from math import cos
from math import tan


class Calculator(object):
     
       
    def add(self, values):        
            return reduce(lambda x,y:x+y, values)

    def divide(self, values):
#        number_types = (int, float, complex) 
#        if isinstance(x, number_types) and isinstance(y, number_types):
#            if y == 0:
#                return 'nan'
#            else:
#                return x / float(y)
#        else:
#            raise ValueError
        return reduce(lambda x, y: x/float(y), values)
            
    def multiply(self, values):
        return reduce(lambda x, y: x*y, values)

    def subtract(self,values):
        return reduce(lambda x, y: x-y, values)

    def exponent(self,values):
        return reduce(lambda x, y: x**y, values)
        
    def square(self,values):
        return map(lambda x: x**2, values)

    def squareroot(self,values):
        return map(lambda x: x**0.5, values)

    def sindegrees(self,values):
        return map(lambda x: sin(x*0.01745329252), values)

    def cosdegrees(self,values):
        return map(lambda x: cos(x*0.01745329252), values)
            
    def tandegrees(self,values):
        return map(lambda x: tan(x*0.01745329252), values)
     