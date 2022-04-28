'''Implementacion de "Sierpinski Carpet"'''
from itertools import chain, islice
from inspect import signature
from operator import add

def impresion(n):

  f = unir(add)
  g = reversa(f)

  def patron(xs):
    return secuencia([xs,[' ' * len(s) for s in xs],xs])(construir(g(xs))(f(xs)))
    
  return valorN(iteracion(patron)(['▓▓']))(n)
 

def main():
  print()
  print("---------------------------------------")
  print("          Implementación extra")
  print("---------------------------------------")
  print()
  try:
    print("Ingrese el número de iteraciones: ")
    numero = int(input("(RECOMENDACIÓN: n <= 4): "))
    print()
    print()
    levels = numIte(0)(numero-1)
    t = ' ' * (len(' -> ') + max(map(construir(len)(str), levels)))
    print(formatoIm(__doc__ + ':')(lambda x: '\n' + str(x))(lambda xs: xs[0] + '\n' + (intercalar(map(lambda x: t + x, xs[1:]))))(impresion)(levels))
  except:
    print()
    print("Por favor ingrese un número, RECOMENDACIÓN: n <= 4")
    
def secuencia(xs):
  res = lambda f: list(chain.from_iterable(map(f, xs)))
  return res
 
def construir(g):
  return lambda f: lambda x: g(f(x))
 
def numIte(m):
  return lambda n: list(range(m, 1 + n))
 
def reversa(f):
  if 1 < len(signature(f).parameters):
      return lambda a, b: f(b, a)
  else:
      return lambda a: lambda b: f(b)(a)
 
def valorN(xs):
  val = lambda n: None if 0 > n else (xs[n] if (hasattr(xs, "__getitem__")) else next(islice(xs, n, None)))
  return val
 
def iteracion(f):
  def go(x):
      v = x
      while True:
          yield v
          v = f(v)
  return lambda x: go(x)
 
def intercalar(xs):
  return '\n'.join(xs)
 
def unir(f):
  lista = lambda xs: lambda ys: (map(f, xs, ys))
  return lista
 
def formatoIm(s):
  def go(xShow, fxShow, f, xs):
    ys = [xShow(x) for x in xs]
    w = max(map(len, ys))
    im = s + '\n' + '\n'.join(map(lambda x, y: y.rjust(w, ' ') + ' -> ' + fxShow(f(x)),xs, ys))
    return im
  imFin = lambda xShow: lambda fxShow: lambda f: lambda xs: go(xShow, fxShow, f, xs)  
  return imFin
  
main()