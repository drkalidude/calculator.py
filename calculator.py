
def main():
    while True:
        print("Выберите действие: ")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("5. Выйти")

        choice = input("Введите номер операции: ")

        if choice == '5':
            break

if __name__ == "__main__":
    main()