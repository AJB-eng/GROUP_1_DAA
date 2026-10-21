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

calls_B = 0
fibtable = {}

def fib_B(n):
    global calls_B
    calls_B += 1
    if n in fibtable:
        return fibtable[n]
    if n == 0 or n == 1:
        value = n
    else:
        value = fib_B(n-1) + fib_B(n-2)
    fibtable[n] = value
    return value

def reset_B():
    global calls_B, fibtable
    calls_B = 0
    fibtable = {}

print("Algorithm B ready")
