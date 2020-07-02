import sys

v=10

def add(x,a=10):
  return x+a

def add2(x):
  print('variable from module namespace = ',v)
  return x+v

def add3(x):
  b=input('variable to add ? = ')
  #print(x+b)
  return x+float(b)

if __name__=='__main__':
  y=float(sys.argv[1])
  z=float(sys.argv[2])
  print(add(y,z))
