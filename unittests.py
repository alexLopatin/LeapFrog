import time
import unittest
from leapfrog import LeapFrog
import numpy as np

class TestStringMethods(unittest.TestCase):
  def test_function1(self):
      eps=0.01
      z = lambda x,y : x**2+y**2
      actual_res=np.zeros(2)
      res = LeapFrog(z)
      b =np.all((actual_res+eps)>res) and np.all((actual_res-eps)<res)
      self.assertTrue(b)
      self.assertFalse(not b)
  def test_function2(self):
      eps=0.01
      z = lambda x,y : x**2+abs(y)**3
      actual_res=np.zeros(2)
      res = LeapFrog(z)
      b =np.all((actual_res+eps)>res) and np.all((actual_res-eps)<res)
      self.assertTrue(b)
      self.assertFalse(not b)
  def test_function3(self):
      eps=0.01
      z = lambda x,y : 0.5*(x**4-16*x**2+5*x)+0.5*(y**4-16*y**2+5*y)
      actual_res=np.array([-2.903534, -2.903534])
      res = LeapFrog(z)
      b =np.all((actual_res+eps)>res) and np.all((actual_res-eps)<res)
      self.assertTrue(b)
      self.assertFalse(not b)
  def test_function4(self):
      eps=0.01
      z = lambda x,y : (x+2*y-7)**2+(2*x+y-5)**2
      actual_res=np.array([1, 3])
      res = LeapFrog(z)
      b =np.all((actual_res+eps)>res) and np.all((actual_res-eps)<res)
      self.assertTrue(b)
      self.assertFalse(not b)

if __name__ == '__main__':
    unittest.main(TestStringMethods(),exit = False)
    time.sleep(5)