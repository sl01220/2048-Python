q1 = input('Hi who are you?\n')
if q1 == 'shawn':
    print('welcome back')
else:
    print('nice to meet you')
func = input('f1: press1\nf2: press2\nf3: press3\nf4: press4\n(1/2/3/4)\n ')
if func == '1':
    print('e')
if func == '2':
    fib_cache = {}


    def fib_memo(input_val):
        if input_val in fib_cache:
            return fib_cache[input_val]

        if input_val == 0:
            val = 0
        elif input_val < 2:
            val = 1
        else:
            val = fib_memo(input_val - 1) + fib_memo(input_val - 2)

        fib_cache[input_val] = val
        return val


    if __name__ == '__main__':
        print('======== Fibonacci Series ========')
        for i in range(1, 10000):
            print(f'Fibonacci ({i}) : {fib_memo(i)}')
if func == '3':
    password = input('type password:\n')
    if password == 'bruh':
        print('Password confirmed.')
    else:
        print('Password is wrong')
if func == '4':
    print('calculator\n')


    def add(x, y):
        return x + y


    def subtract(x, y):
        return x - y


    def multiply(x, y):
        return x * y


    def divide(x, y):
        return x / y


    print('calculations\n1.Add\n2.subtract\n3.multiply\n4.divide')
    while True:
        choice = input('calculations (1/2/3/4/)\n')
        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if choice == '1':
                print(num1, "+", num2, "=", add(num1, num2))

            elif choice == '2':
                print(num1, "-", num2, "=", subtract(num1, num2))

            elif choice == '3':
                print(num1, "*", num2, "=", multiply(num1, num2))

            elif choice == '4':
                print(num1, "/", num2, "=", divide(num1, num2))

            next_calculation = input("Let's do next calculation? (yes/no): ")
            if next_calculation == "no":
                break
            else:
                print("Invalid Input")
