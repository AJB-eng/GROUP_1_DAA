import time

calls_A = 0

def fib_A(n):
    global calls_A
    calls_A += 1
    if n == 0 or n == 1:
        return n
    return fib_A(n-1) + fib_A(n-2)

def reset_A():
    global calls_A
    calls_A = 0

print("Algorithm A ready")
