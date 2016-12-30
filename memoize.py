# Memoization
# from: https://jeremykun.com/2012/01/12/a-spoonful-of-python/
def memoize(f):
   cache = {}

   def memoizedFunction(*args):
      if args not in cache:
         cache[args] = f(*args)
      return cache[args]

   memoizedFunction.cache = cache
   return memoizedFunction

@memoize
def fib(n):
   if n <= 2:
      return 1
   else:
      return fib(n-1) + fib(n-2)


if __name__ == "__main__":
    fib(20)