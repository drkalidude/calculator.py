def add(x,y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def main():
    while True:
        print("Выберите действие: ")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("5. Выйти")

        choice = input("Введите номер операции: ")

        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))

        if choice == '5':
            break

        if choice == '1':
            print("Результат:", add(num1, num2))
        elif choice == '2':
            print("Результат:", subtract(num1, num2))

        

if __name__ == "__main__":
    main()