import time

def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def find_prime_numbers(start, end):
    prime_numbers = []
    if start <= 2 <= end:
        prime_numbers.append(2)
    if start % 2 == 0:
        start += 1
    for num in range(start, end + 1, 2):
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers

start_num = 1
end_num = int(input())

st = time.time()
prime_nums_in_range = find_prime_numbers(start_num, end_num)
print(*prime_nums_in_range)
print(time.time() - st)