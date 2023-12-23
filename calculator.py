import math

# Функция для решения квадратных уравнений
def solve_quadratic(a, b, c):
    d = b**2 - 4*a*c  # Вычисление дискриминанта
    # Проверка условий для дискриминанта
    if d > 0:
        root1 = (-b + math.sqrt(d)) / (2*a)
        root2 = (-b - math.sqrt(d)) / (2*a)
        return root1, root2
    elif d == 0:
        root = -b / (2*a)
        return root,
    else:
        return "Уравнение не имеет вещественных корней"

# Возведение числа x в степень n
def power(x, n):
    return x ** n

# Вычисление логарифма числа x по основанию base
def log(x, base):
    return math.log(x, base)

# Операции основной арифметики
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    # Проверка на деление на ноль
    if y == 0:
        return "Ошибка: Деление на ноль"
    return x / y

# Тригонометрические функции
def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))

# Обратные тригонометрические функции
def arcsin(x):
    return math.degrees(math.asin(x))

def arccos(x):
    return math.degrees(math.acos(x))

def arctan(x):
    return math.degrees(math.atan(x))


def main():
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))

    while True:
        # Вывод меню действий
        print("Выберите действие: ")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("5. Обновление чисел")
        print("6. Решение квадратного уравнения")
        print("7. Возведение в степень")
        print("8. Логарифм")
        print("9. Синус")
        print("10. Косинус")
        print("11. Тангенс")
        print("12. Арксинус")
        print("13. Арккосинус")
        print("14. Арктангенс")
        print("0. Выйти")

        # ... описание меню ...
        choice = input("Введите номер операции: ")

        if choice == '0':
            break

        # Обработка выбора пользователя
        # ... логика обработки ...
        
        if choice == '1':
            print("Результат:", add(num1, num2))
        elif choice == '2':
            print("Результат:", subtract(num1, num2))
        elif choice == '3':
            print("Результат:", multiply(num1, num2))
        elif choice == '4':
            print("Результат:", divide(num1, num2))
        elif choice == '5':
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
        elif choice == '6':
            a = float(input("Введите коэффициент a: "))
            b = float(input("Введите коэффициент b: "))
            c = float(input("Введите коэффициент c: "))
            print("Результат:", solve_quadratic(a, b, c))
        elif choice == '7':
            base = float(input("Введите основание (число, которое будет возведено в степень): "))
            exponent = float(input("Введите показатель степени: "))
            print("Результат:", power(base, exponent))
        elif choice == '8':
            number = float(input("Введите число для логарифмирования: "))
            base = float(input("Введите основание логарифма: "))
            print("Результат:", log(number, base))
        elif choice == '8':
            number = float(input("Введите число для логарифмирования: "))
            base = float(input("Введите основание логарифма: "))
            print("Результат:", log(number, base))

        elif choice == '9':
            angle = float(input("Введите угол в градусах для синуса: "))
            print("Результат:", sin(angle))

        elif choice == '10':
            angle = float(input("Введите угол в градусах для косинуса: "))
            print("Результат:", cos(angle))

        elif choice == '11':
            angle = float(input("Введите угол в градусах для тангенса: "))
            print("Результат:", tan(angle))

        elif choice == '12':
            value = float(input("Введите значение для арксинуса (от -1 до 1): "))
            print("Результат:", arcsin(value))

        elif choice == '13':
            value = float(input("Введите значение для арккосинуса (от -1 до 1): "))
            print("Результат:", arccos(value))

        elif choice == '14':
            value = float(input("Введите значение для арктангенса: "))
            print("Результат:", arctan(value))

        else:
            print("Неправильный ввод")
        

if __name__ == "__main__":
    main()