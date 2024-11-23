import random
n = random.randint(3, 20)
def generate_password(n):
    password = ""
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            pair_sum = i + j
            if n % pair_sum == 0:
                password += f"{i}{j}"
    return password
if 3 <= n <= 20:
    result = generate_password(n)
    print(f"Пароль для числа {n}: {result}")
else:
    print("Введите корректное число от 3 до 20.")
