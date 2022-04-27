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
  print("Ingrese el número de iteraciones: ")
  numero = int(input("(RECOMENDACIÓN: n <= 4): "))
  print()
  print()
  levels = numIte(0)(numero-1)

  t = ' ' * (len(' -> ') + max(map(construir(len)(str), levels)))
  print(formatoIm(__doc__ + ':')(lambda x: '\n' + str(x))(lambda xs: xs[0] + '\n' + (intercalar(map(lambda x: t + x, xs[1:]))))(impresion)(levels))
 
 
# GENERIC -------------------------------------------------
 
# secuencia (>>=) :: [a] -> (a -> [b]) -> [b]
def secuencia(xs):
  res = lambda f: list(chain.from_iterable(map(f, xs)))
  return res
 
# construir (<<<) :: (b -> c) -> (a -> b) -> a -> c
def construir(g):
    '''Right to left function composition.'''
    return lambda f: lambda x: g(f(x))
 
# numIte :: (Int, Int) -> [Int]
def numIte(m):
    '''Integer enumeration from m to n.'''
    return lambda n: list(range(m, 1 + n))
 
# reversa :: (a -> b -> c) -> b -> a -> c
def reversa(f):
    '''The (curried or uncurried) function f with its
       arguments reversed.'''
    if 1 < len(signature(f).parameters):
        return lambda a, b: f(b, a)
    else:
        return lambda a: lambda b: f(b)(a)
 
# valorN (!!) :: [a] -> Int -> a
def valorN(xs):
    '''Item at given (zero-based) valorN.'''
    return lambda n: None if 0 > n else (xs[n] if (hasattr(xs, "__getitem__")) else next(islice(xs, n, None)))
 
# iteracion :: (a -> a) -> a -> Gen [a]
def iteracion(f):
    '''An infinite list of repeated
       applications of f to x.
    '''
    def go(x):
        v = x
        while True:
            yield v
            v = f(v)
    return lambda x: go(x)
 
# intercalar :: [String] -> String
def intercalar(xs):
    '''A single string derived by the intercalation
       of a list of strings with the newline character.'''
    return '\n'.join(xs)
 
# unir :: (a -> b -> c) -> [a] -> [b] -> [c]
def unir(f):
    '''A list constructed by zipping with a
       custom function, rather than with the
       default tuple constructor.'''
    return lambda xs: lambda ys: (map(f, xs, ys))
 
# OUTPUT FORMATTING ---------------------------------------
 
# formatoIm :: String -> (a -> String) ->
#                     (b -> String) -> (a -> b) -> [a] -> String
def formatoIm(s):
    '''Heading -> x display function -> fx display function ->
                     f -> xs -> tabular string.
    '''
    def go(xShow, fxShow, f, xs):
        ys = [xShow(x) for x in xs]
        w = max(map(len, ys))
        return s + '\n' + '\n'.join(map(lambda x, y: y.rjust(w, ' ') + ' -> ' + fxShow(f(x)),xs, ys))
    return lambda xShow: lambda fxShow: lambda f: lambda xs: go(xShow, fxShow, f, xs)
  
main()