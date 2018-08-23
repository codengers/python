#!/usr/bin/env python
class Points:

  def __init__(self, x=0, y=0):
  
    self.x = x
    self.y = y




p = Points(3,4)
q = Points()
print("(x={0}, y={1})".format(p.x, p.y))
#print(p.x,p.y, q.x, q.y)
