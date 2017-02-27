
def fib(n):
    """ one liner to get the fibonacci number of n """
    return n if n < 2 else (fib(n-1) + fib(n-2))
    
def print_fib(end_range=15):
    """ print all fibonacci numbers from 0 --> end_range. 
        default value is 0-->15 """
    for n in range(0, end_range):
        print(fib(n))
        

def main():
    print_fib()

if __name__ == "__main__":
    main()
