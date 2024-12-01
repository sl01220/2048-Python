import time

def f(n):
    if n < 3:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
x=input('pick a number your memory might go to 100%'
        ' if you dont pick wisely.\n' )
n = int(x)

start_time = time.time()  # Record the start time
result = f(n)
end_time = time.time()    # Record the end time

print(f"Result: {result}")
print(f"Time taken: {end_time - start_time:.4f} seconds")
