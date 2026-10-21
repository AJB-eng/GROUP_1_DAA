import sys

print("\nPART 4 - Testing n=1000")
print("Current recursion limit:", sys.getrecursionlimit())

print("\nTrying original fib_B(1000)...")
try:
    reset_B()
    fib_B(1000)
except RecursionError:
    print("→ Crashed with RecursionError (this is normal)")

# Fix 1: Increase the recursion limit
print("\nFix 1: Increase recursion limit")
sys.setrecursionlimit(2000)
reset_B()
start = time.perf_counter()
print("fib_B(1000) =", fib_B(1000))
print("Time:", round(time.perf_counter() - start, 6), "seconds")
print("Calls:", calls_B)

# Fix 2: Iterative version (no recursion)
print("\nFix 2: Iterative version (no recursion)")
def fib_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for i in range(2, n+1):
        a, b = b, a + b
    return b

start = time.perf_counter()
print("fib_iterative(1000) =", fib_iterative(1000))
print("Time:", round(time.perf_counter() - start, 6), "seconds")

print("\nAll parts finished successfully!")# GROUP_1_DAA