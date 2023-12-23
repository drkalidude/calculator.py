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
        else:
            print("Неправильный ввод")
        

if __name__ == "__main__":
    main()