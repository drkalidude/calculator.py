import math

def solve_quadratic(a, b, c):
    d = b**2 - 4*a*c
    if d > 0:
        root1 = (-b + math.sqrt(d)) / (2*a)
        root2 = (-b - math.sqrt(d)) / (2*a)
        return root1, root2
    elif d == 0:
        root = -b / (2*a)
        return root,
    else:
        return "Уравнение не имеет вещественных корней"
    
def power(x, n):
    return x ** n

def log(x, base):
    return math.log(x, base)

def add(x,y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Ошибка: Деление на ноль"
    return x / y

def main():
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))

    while True:
        print("Выберите действие: ")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("5. Обновление чисел")
        print("6. Решение квадратного уравнения")
        print("0. Выйти")

        choice = input("Введите номер операции: ")

        if choice == '0':
            break

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
        else:
            print("Неправильный ввод")
        

if __name__ == "__main__":
    main()