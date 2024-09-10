def fibonacci_check(t):
    a, b = 0, 1
    while b <= t:
        if b == t:
            return True
        a, b = b, a + b
    return False

num = int(input("Informe um número: "))

if  fibonacci_check(num):
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} não pertence à sequência de Fibonacci.")