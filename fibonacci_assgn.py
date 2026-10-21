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

print(" Algorithm B ready")

print("\n- Checking answers for n = 0 to 20")
print("-" * 45)

for n in range(0, 21):
    reset_A()
    reset_B()
    a = fib_A(n)
    b = fib_B(n)
    print(f"n={n:2}  A={a}  B={b}  Match={a==b}")

print()


print("PART 2 - Algorithm A results")
print(f"{'n':>4} {'calls':>12} {'time(s)':>12}")
print("-" * 32)

for n in [5, 10, 15, 20, 25, 30, 35]:
    reset_A()
    start = time.perf_counter()
    fib_A(n)
    t = time.perf_counter() - start
    print(f"{n:4} {calls_A:12} {t:12.6f}")
    if t > 60:
        break

print()
print("PART 2 - Algorithm B results")
print(f"{'n':>4} {'calls':>12} {'time(s)':>12}")
print("-" * 32)

for n in [10, 50, 100, 200, 500, 1000]:
    reset_B()
    start = time.perf_counter()
    fib_B(n)
    t = time.perf_counter() - start
    print(f"{n:4} {calls_B:12} {t:12.6f}")
