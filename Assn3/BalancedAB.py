
import unittest

def BalancedAB(string):
   try:
      conA = string.rindex("A")
   except:
      return True
   try:
      conB = string.rindex("B")
   except:
      conB = -1
   if conB > conA:
      return True
   else:
      return False
